from aternosapi import AternosAPI

headers_cookie = "ATERNOS_SEC_znt392ckka000000=iqxu3o27bjl00000; __cfduid=d733afe73174bb68643350c30f38a82c11581746695; ATERNOS_LANGUAGE=en; ATERNOS_SESSION=ov3TtocHUeQGkngU1XmWuXnAl31juHTjGDyoLzmL5uvJSU0ZSl2Vz6eLCIPx67KhmWNToHVkK39GqFksVLDxYTzUsnJb0YRpiwY1"
cookie = "ov3TtocHUeQGkngU1XmWuXnAl31juHTjGDyoLzmL5uvJSU0ZSl2Vz6eLCIPx67KhmWNToHVkK39GqFksVLDxYTzUsnJb0YRpiwY1"
ASEC = "znt392ckka000000:iqxu3o27bjl00000"

server = AternosAPI(headers_cookie, cookie, ASEC)

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