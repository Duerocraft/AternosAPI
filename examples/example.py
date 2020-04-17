from aternosapi import AternosAPI

headers_cookie = "ATERNOS_SEC_65u4dtlb18c00000=nvve5a3plwm00000; ATERNOS_SEC_o0813b2r4p000000=lghd2h9q51000000; GED_PLAYLIST_ACTIVITY=W3sidSI6IjhYbWoiLCJ0c2wiOjE1ODM1NTgzNzYsIm52IjoxLCJ1cHQiOjE1ODM1NTgzNzUsImx0IjoxNTgzNTU4Mzc1fV0.; __cfduid=d2896cc4e883d66976dc5dae378a576821587116246; ATERNOS_LANGUAGE=en; _ga=GA1.2.1681177297.1587116253; _gid=GA1.2.1493791183.1587116253; ATERNOS_SESSION=udpBAQS9ft13yXRMAQNc5rPFn9Tge5gQTLhqKimd5l2lfMH1am31UcSUY66AIDp9KOdacihXfzTEh0NuF1NuVEOf3npMyhwQNZPg; DigiTrust.v1.identity=eyJpZCI6IldwUDFzV1FQNWI1a003cEE0RVhiOUtDRnJSa0pBOHBiekNDK2FPMTIvQmxhbWhyNXZYVkFwNlluNmpQV09yOUdLVDFsS1p0LzhmWG5XZlpkZDZVWkdLSWh2dVB0SGwrQlhCd3JWQ1VYQWZDQ0VCazk2a2hYMTJNS25DekV2RTNBNEs2RWplTFg2UWlpSHpoOGdhWm01TFpQWERBdmRsWlkzeUVaRlVQRFhobDd5bktNQWduU2tJQlJ5c2g4RFVZOTMzT01hYWpzYnZ3ai9oNDZmOVRJRStGVkxweUNHdXB2cGlsOFM5dmt0THU3eVJ4UVpBbTJIOGNLdTJRT1psVzlNQk9qV1NsR1dKdlM5Q1J6dDF0NExhN1ZCQzE4L2p5UXFuL2JlZ1dHWTRwQmdGMmJzQ2F4TGhDSS95SUdhUmYxeUI5RlN3S0U1clRqRys3d1ZIRmZUZz09IiwidmVyc2lvbiI6MiwicHJvZHVjZXIiOiIxQ3JzZFVOQW82IiwicHJpdmFjeSI6eyJvcHRvdXQiOmZhbHNlfSwia2V5diI6NH0%3D; __gads=ID=29d604c8bdf47988:T=1587116285:S=ALNI_MYlGmx2O5wOks1tiMInu4kd1241qA; cto_bundle=plzbjF8zdWduS1V4OW9JR0ZMMW1KJTJGZ21CdTZnSmFrUlVoMiUyRnhRSkY3Sk02RVZoNjV2M3paRXY2MXhINGx3diUyRmtUa3llcVNuMzlQQ3pmbkdMNSUyQm1uMWpwb3hmcTg4WTRHdVpUZ2h3dTBCYWFiQzZvamFtd251SG5NYnJLZW9iMDBwSnVv; cuid=df1ebb829036b51e35301587116308184_1589708308184"
cookie = "udpBAQS9ft13yXRMAQNc5rPFn9Tge5gQTLhqKimd5l2lfMH1am31UcSUY66AIDp9KOdacihXfzTEh0NuF1NuVEOf3npMyhwQNZPg"
ASEC = "65u4dtlb18c00000:nvve5a3plwm00000"

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
