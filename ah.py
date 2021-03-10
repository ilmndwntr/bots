import requests
import re, time

session = requests.Session()

def gas(kue):
	while True:
		try:
			headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
			resp = session.get("https://coinez.biz/dashboard.php", cookies=kue, headers=headers,allow_redirects=True)
			tok = re.findall(r'<font id="bal">(.*?)</font>', resp.text)[0]
			print('\033[1;31;40m•\033[0m \033[1;33;40mMining Has Been Started\033[0m')
			print('\033[1;31;40m•\033[0m Please Wait...')
			time.sleep(100)
			if "getBalance" in resp.text:
				print("\033[1;31;40m•\033[0m \033[1;32;40mSUCCESS\033[0m ")
				time.sleep(2)
				print("\033[1;31;40m•\033[0m \033[1;34;40mYour Balance Now\033[0m: \033[1;32;40m"+tok+"\033[0m")
				continue
			else:
				print("ERROR")
				continue
		except:
			continue

cok = {
		"PHPSESSID": "lg0a0ila7b1m073t1n0blsrj40",
		"__tawkuuid": "e::coinez.biz::QV3JqmOxTIcSrE27V+QbALlLlhg9VhwZiFYyYkLoffV5Y3ogiBwIlUI5EU0eoEgK::2",
		"_ga": "GA1.2.1243436230.1615114043",
		"_gid": "GA1.2.1876514742.1615293494",
		"TawkConnectionTime": "0"
}

gas(cok)