from bs4 import BeautifulSoup
import cloudscraper, time

class AternosAPI():
    def __init__(self, headers, TOKEN, timeout = 10):

        #Timeout = number of retries to bypass cloudflare:
        
        self.timeout = timeout
        self.headers = {}
        self.TOKEN = TOKEN
        self.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
        self.headers['Cookie'] = headers
        self.SEC = self.getSEC()
        self.JavaSoftwares = ['Vanilla', 'Spigot', 'Forge', 'Magma','Snapshot', 'Bukkit', 'Paper', 'Modpacks', 'Glowstone']
        self.BedrockSoftwares = ['Bedrock', 'Pocketmine-MP']

    def getSEC(self):
        headers = self.headers['Cookie'].split(";")
        for sec in headers:
            if sec[:12] == "ATERNOS_SEC_":
                sec = sec.split("_")
                if len(sec) == 3:
                    sec = ":".join(sec[2].split("="))
                    return sec

        print("Invaild SEC")
        exit(1)

    def GetStatus(self):
        webserver = self.filterCloudflare(url='https://aternos.org/server/', headers=self.headers)
        webdata = BeautifulSoup(webserver.text, 'html.parser')
        status = webdata.find('span', class_='statuslabel-label').text
        status = status.strip()
        return status

    def StartServer(self):
        serverstatus = self.GetStatus()
        if serverstatus == "Online":
            return "Server Already Running"
        else:
            parameters = {}
            parameters['headstart'] = 0
            parameters['SEC'] = self.SEC
            parameters['TOKEN'] = self.TOKEN
            startserver = self.filterCloudflare(url=f"https://aternos.org/panel/ajax/start.php", params=parameters, headers=self.headers)

            #When pop up comes for confirmation:

            while("Preparing" not in  self.GetStatus() and self.GetStatus() != "Online"):
                time.sleep(10)
                startserver = self.filterCloudflare(url=f"https://aternos.org/panel/ajax/confirm.php", params=parameters, headers=self.headers)
            
            return "Server Started"
    
    #Added online player list:
    def GetPlayerInfo(self):
        players = []
        webserver = self.filterCloudflare(url='https://aternos.org/players/', headers=self.headers)
        webdata = BeautifulSoup(webserver.text, 'html.parser')
        status = webdata.findAll('div', class_='playername')
        for i in status:
            players.append(i.text.strip())
        return players

    def StopServer(self):
        serverstatus = self.GetStatus()
        if serverstatus == "Offline":
            return "Server Already Offline"
        else:
            parameters = {}
            parameters['SEC'] = self.SEC
            parameters['TOKEN'] = self.TOKEN
            stopserver = self.filterCloudflare(url=f"https://aternos.org/panel/ajax/stop.php", params=parameters, headers=self.headers)
            return "Server Stopped"

    def GetServerInfo(self):

        ServerInfo = self.filterCloudflare(url='https://aternos.org/server/', headers=self.headers)
        ServerInfo = BeautifulSoup(ServerInfo.text, 'html.parser')
        Software = ServerInfo.find('span', id='software')

        if(not Software): return
        
        Software = Software.text.strip()

        isJava = False; isBedrock = False
        
        if(self.arrayContains(self.JavaSoftwares, Software)):
            IP = ServerInfo.find('div', class_='server-ip mobile-full-width').get_text()
            IP = IP.strip()

            IP = IP.split(" ")
            IP = IP[0].strip()

            Port = "25565(Optional)"

            return f"{IP},{Port},{Software}"

        elif(self.arrayContains(self.BedrockSoftwares, Software)):

            IP = ServerInfo.find('span', id='ip').get_text()
            IP = IP.strip()

            Port = ServerInfo.find('span', id='port').get_text()
            Port = Port.strip()

            return f"{IP},{Port},{Software}"
    
    def filterCloudflare(self, url, params=None, headers=None):

        #Keeps sending request until we bypass Cloudflare:
        
        requests = cloudscraper.create_scraper()
        gotData = requests.get(url, params=params, headers=headers)
        counter = 0

        while "<title>Please Wait... | Cloudflare</title>" in gotData.text and counter < self.timeout:
            requests = cloudscraper.create_scraper()
            time.sleep(1)
            gotData = requests.get(url, params=params, headers=headers)
            counter += 1
        if("<title>Please Wait... | Cloudflare</title>" in gotData.text):
            print("Cloudfair error!!")
            exit(0)
        return gotData
    
    #Your paper wasn't working because it had PaperMC so changed a little bit:

    def arrayContains(self, array, string):
        for i in array:
            if string.lower() in i.lower() or i.lower() in string.lower() :
                return True
        return False
