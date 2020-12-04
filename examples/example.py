from aternosapi import AternosAPI

headers_cookie = "xxxxx"
TOKEN = "xxxxx"
server = AternosAPI(headers_cookie, TOKEN)

def cmd(cmd):
	if cmd == "start":
		print(server.StartServer())
	if cmd == "stop":
		print(server.StopServer())
	if cmd == "status":
		print(server.GetStatus())
	if cmd == "info":
		print(server.GetServerInfo())

while True:
	icmd = input("[*] > ")
	cmd(icmd)
