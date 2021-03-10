import requests
import re, time

session = requests.Session()

def gas(kue):
	while True:
		try:
			headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
			resp = session.get("https://krypton.biz/dashboard.php", cookies=kue, headers=headers,allow_redirects=True)
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
		"PHPSESSID": "bb4a4d04ba11a934b50e65909933a715"
}

gas(cok)
