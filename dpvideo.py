# -*- coding: utf-8 -*-
import xBot
from xBot import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from akad.ttypes import LoginRequest
from akad import LineService
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from threading import Thread,Event
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize,pytz
from gtts import gTTS
from googletrans import Translator
from pytz import timezone
_session = requests.session()
botStart = time.time()
#WARNA
merah = "#FF2800"
kuning = "#FFFD00"
hijau = "#83FF00"
hijauMuda = "#00FF00"
unguTua = "#9900FF"
merahHati = "#660000"
biru = "#00DAFF"
biruTua = "#0000FF"
ungu = "#C323FF"
nila = "#4B0082"
pingTua = "#FF17CE"
ping = "#FF17CE"
hitam = "#000000"
putih = "#FFFFFF"
jambon = "#FF0066"
biruHitam = "#330033"
abuabu = "#000000cc"
sp_putih = {"type": "separator","color": putih}
sp_nila = {"type": "separator","color": nila}
sp_hitam = {"type": "separator","color": hitam}
sp_kuning = {"type": "separator","color": kuning}
sp_biru = {"type": "separator","color": biruTua}
sp_hijau = {"type": "separator","color": hijau}
sp_merah = {"type": "separator","color": merahHati}
sp_ungu = {"type": "separator","color": unguTua}
sp_ping = {"type": "separator","color": pingTua}
sp_abuabu = {"type": "separator","color": abuabu}
style_hijau={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":hijau}}
style_nila={"header":{"backgroundColor":nila},"body":{"backgroundColor":nila},"footer":{"backgroundColor":nila,"separator":True,"separatorColor":biruTua}}
style_edit={"header":{"backgroundColor":abuabu},"body": {"cornerRadius": "md","borderWidth": "5px","borderColor": unguTua},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":hijau}}
style_merah={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":merah}}
style_biru={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":biru}}
style_kuning={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":kuning}}
style_ungu={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":ungu}}
style_putih={"header":{"backgroundColor":putih},"body":{"backgroundColor":putih},"footer":{"backgroundColor":putih,"separator":True,"separatorColor":hitam}}
style_hitam={"header":{"backgroundColor":hitam},"body":{"backgroundColor":hitam},"footer":{"backgroundColor":hitam,"separator":True,"separatorColor":putih}}
Pabuabu = "https://bakarenders.com/renders/albums/userpics/11535/normal_hatsunemiku_-_loveiswar2.png"
Warna1 = (merah,hijau,biru,hijauMuda)
Warna2 = (biruTua,merahHati,unguTua,nila)
Warna3 = (putih,kuning,pingTua)
warnanya1 = random.choice(Warna1)
warnanya2 = random.choice(Warna2)
warnanya3 = random.choice(Warna3)
pict1 = "https://os.line.naver.jp/os/p/{}"
pict2 = "https://obs.line-scdn.net/{}"
#poto
logo = "https://1.bp.blogspot.com/-6T7oMDOIlKA/XVX_8-oO52I/AAAAAAAAGe0/W0MubSIIyUUzw3et2YifTWqxaNRRwWE-ACLcBGAs/s1600/20190816_075636.png"
image1 = "https://1.bp.blogspot.com/-zyUmsriCmGE/XVYAO-lsFLI/AAAAAAAAGe8/BsSUwtUfFc0mxRGxE_8fOz3peuxB3t9UwCLcBGAs/s1600/20190816_074821.jpg"
image2 = "https://1.bp.blogspot.com/-zK32-fvqcNw/XVYAUCQhrmI/AAAAAAAAGfA/hXKs0MS2OIMKi09tJ7yCjnjUbMiuV_TIACLcBGAs/s1600/20190816_074438.jpg"
image3 = "https://1.bp.blogspot.com/-OgPmr5eJpYg/XVYAVFAYcaI/AAAAAAAAGfE/Xwh0EqB_SrclP-NZ_DaDqxcYnWBZSa_FgCLcBGAs/s1600/20190816_074311.jpg"
a1 = "https://1.bp.blogspot.com/-pBMROlmPtdg/XXJF_q2cQCI/AAAAAAAAG1E/7TRgM49vMZAXvAEhtVbO--zPCqvdh8SBACLcBGAs/s1600/20190906_183218.jpg"
a2 = "https://1.bp.blogspot.com/-rTWcjzSC8uk/XXJF5YVuADI/AAAAAAAAG1A/noFsixwxTHoE9DDSoSbQHLs-OXnY5udCACLcBGAs/s1600/20190906_183534.jpg"
Gambar = (image1,image2,image3)
a3 = (a1,a2)
Hasile = random.choice(Gambar)
Aa1 = random.choice(a3)
logo = "https://1.bp.blogspot.com/-6T7oMDOIlKA/XVX_8-oO52I/AAAAAAAAGe0/W0MubSIIyUUzw3et2YifTWqxaNRRwWE-ACLcBGAs/s1600/20190816_075636.png"
Warna = (merah,kuning,hijau,biru,ping,ungu)
warnanya1 = random.choice(Warna)
warnanya2 = random.choice(Warna)
warnanya3 = random.choice(Warna)
print("\n____________________________[SELFBOT]____________________________")
me = LINE("EPCKGkxPfnhkgU5BIIId.u3Oosz4qA0t+5TyeTrb17q.xsHVM/bXCcqxwR+Yil7Fjj9RymOU0xb7OMsKLfkDyiw=")
me.log("Auth Token : " + str(me.authToken))
meM = me.getProfile().mid
me.log("MID : " + str(meM))
print("""
░▀░ █▀▀▄ █▀▀ █░█ █▀▀▄ █▀▀█ ▀▀█▀▀ █▀▀ 
▀█▀ █░░█ █▀▀ ▄▀▄ █▀▀▄ █░░█ ░░█░░ ▀▀█ 
▀▀▀ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀░ ▀▀▀▀ ░░▀░░ ▀▀▀ 
▄█░ ░█▀█░ ▄ █▀▀█ ▄▀▀▄ ▄ █▀█ █▀▀█ ▄█░ ▄▀▀▄ 
░█░ █▄▄█▄ ░ █▄▀█ █▄▄░ ░ ░▄▀ █▄▀█ ░█░ ▀▄▄█ 
▄█▄ ░░░█░ ▀ █▄▄█ ▀▄▄▀ ▀ █▄▄ █▄▄█ ▄█▄ ░▄▄▀ """)
Hallow = """
Bot @
Addblc @
Join
Banlist
Clearban
"""
oepoll = OEPoll(me)
St = "┣"
Zx = [me]
meProfile = me.getProfile()
meSettings = me.getSettings()
set = {
  "Picture": False,
  "bot": True,
  "Conection": "",
  "foto": {},
  "Ids":{},
  "keyCommand":"",
  "changeProfileVideo": {
    "picture": "",
    "stage": 2,
    "status": False,
    "video": ""
  },
  "PASUKAN": {},
  "setKey": False,
  "autoRead": False,
  "owner":{},
  "staff": {},
  "admin":{},
  "autoBlock": False,
  "detectMention": True,
  "detectMention2": False,
  "arespon":True,
  "blacklist":{},
  "checkSticker": False,
  "autoJoinTicket": True,
  "autoJoin": True,
  "autoAdd": True,
  "autoLeave": False,
  "limitkick": False,
  "contact": False,
  "autoJoinMessage": "ᴛᴇʀɪᴍᴀᴋᴀsɪʜ ᴋᴀᴋᴀ ᴀᴛᴀs ᴜɴᴅᴀɴɢᴀɴ ɢʀᴜᴘɴʏᴀ.",
  "comment": "ᴀᴜᴛᴏ ʟɪᴋᴇ ɴ ᴄᴏᴍᴍᴇɴᴛ ᴅᴏɴᴇ\nвʏ.ᴛᴇᴀᴍ ⊶ [B.O.G] ⊷",
  "comment2": "┏━━━━━━━━━•❅•°•❈•°•❅•━━━━━━━━┓\n┃┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓\n┃┃     ❀    [ BLACK_OF_GAMER ]    ❀\n┃┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓\n┃┃          LIKE N COMMENT DONE\n┃┃         IKUTAN CORET-CORET\n┃┃                     B.O.G_TEAM\n┃┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓\n┃┃  AciL :\n┃┃  http://line.me/ti/p/~adiputra.95\n┃┃  Denjaka :\n┃┃  https://bit.ly/38K8bbV\n┃┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛\n┗━━━━━━━━━•❅•°•❈•°•❅•━━━━━━━━┛",
  "mention":"ᴋᴀʟᴏ ɴɢɪɴᴛɪᴘ ᴛᴇʀᴜs ᴅᴀᴘᴇᴛ ɢᴇʟᴀs ᴘᴇᴄᴀʜ ᴅɪ ᴋᴇᴘᴀʟᴀ...",
  "Respontag":"https://youtube.com/channel/UCu5Aqj6zqJK59pXxNGw8HMg",
  "Respontag2":"ada apa tag saya d grup kak?",
  "tagpm":"subcrabe channelku donk kak\nhttps://youtube.com/channel/UCu5Aqj6zqJK59pXxNGw8HMg",
  "welcome":"ѕєĻαмαт đαтαηg,,,, вυđαуαкαη ¢єк ησтє кαк",
  "message":"тᴇяıмᴀ кᴀsıн suᴅᴀн ᴀᴅᴅ sᴀʏᴀ \nвʏ.ᴛᴇᴀᴍ \n⊶ вĻα¢к●σƒ●gαмєя ⊷",
  "baper":"ѕєĻαмαт тιηggαĻ тємαη,,, ѕємσgα єηgкαυ тєηαηg đι ѕαηα●",
  "userAgent": [
    "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
    "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
  ]
}
cctv = {
  "cyduk":{},
  "point":{},
  "sidermem":{}
}
Line_Apikey = "u951e70feab1a2b4f38fc1390f776a31b"
cont = me.getContact(meM)
Extr = me.getContact(Line_Apikey).displayName
for busht in Zx:
  for anding in Line_Apikey:
    try:
      busht.findAndAddContactsByMid(anding)
    except:pass
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
jamtgl = timeNow.strftime('|📆|%d/%B/%Y|⏰|%X|')
jam = timeNow.strftime('⏰ %X')
tgl = timeNow.strftime('📆 %d/%B/%Y')
def runtime(secs):
  mins, secs = divmod(secs,60)
  hours, mins = divmod(mins,60)
  days, hours = divmod(hours, 24)
  return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def Run_Xx():
  backupData()
  python = sys.executable
  os.execl(python, python, *sys.argv)
def logError(text):
  me.log("ERROR 404 !\n" + str(text))
  tz = pytz.timezone("Asia/Jakarta")
  timeNow = datetime.now(tz=tz)
  timeHours = datetime.strftime(timeNow,"(%H:%M)")
  day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
  hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
  bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
  inihari = datetime.now(tz=tz)
  hr = inihari.strftime('%A')
  bln = inihari.strftime('%m')
  for i in range(len(day)):
    if hr == day[i]: hasil = hari[i]
  for k in range(0, len(bulan)):
    if bln == str(k): bln = bulan[k-1]
  time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
  with open("errorLog.txt","a") as error:
    error.write("\n[%s] %s" % (str(time), text))
def mentionMembers(to, mid):
  try:
    arrData = ""
    textx = "╭━──────────────━╮\n│➢Total「{}」Members\n╰━──────────────━╯\n╭━──────────────━╮\n│➢ 1. ".format(str(len(mid)))
    arr = []
    no = 1
    num = 2
    for i in mid:
      mention = "@x\n"
      slen = str(len(textx))
      elen = str(len(textx) + len(mention) - 1)
      arrData = {'S':slen, 'E':elen, 'M':i}
      arr.append(arrData)
      textx += mention
      if no < len(mid):
        no += 1
        textx += "│➢ %i. " % (num)
        num=(num+1)
      else:
        try:
          no = "\n╰━─[ {} ]".format(str(me.getGroup(to).name))
        except:
          no = "\n╰━─[ Success ]"
    me.sendMessage(to, textx+"╰━──────────────━╯", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  except Exception as error:
    logError(error)
    me.sendMessage(to, "[ INFO ] Error :\n" + str(error))
Devert = "Thank you brothers\nMy name is "+cont.displayName+" use your bot script\nSubcrabe my chanel youtube\nhttps://youtube.com/channel/UCu5Aqj6zqJK59pXxNGw8HMg"
def changeProfileVideo(to):
  if set['changeProfileVideo']['picture'] == None:
    return me.sendMessage(to, "Foto tidak ditemukan")
  elif set['changeProfileVideo']['video'] == None:
    return me.sendMessage(to, "Video tidak ditemukan")
  else:
    path = set['changeProfileVideo']['video']
    files = {'file': open(path, 'rb')}
    obs_params = me.genOBSParams({'oid': me.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
    data = {'params': obs_params}
    r_vp = me.server.postContent('{}/talk/vp/upload.nhn'.format(str(me.server.LINE_OBS_DOMAIN)), data=data, files=files)
    if r_vp.status_code != 201:
      return me.sendMessage(to, "Gagal update profile")
    path_p = set['changeProfileVideo']['picture']
    set['changeProfileVideo']['status'] = False
    me.updateProfilePicture(path_p, 'vp')
extras = "  "+Extr+"\n"
def sendTemplate(to, text):
  data = { "type": "flex","altText": " Black Of Gamers","contents":
  {"type": "bubble","size": "micro",
  "styles":{"body":{"backgroundColor":"#000000"}},"type":"bubble",
  "body": {"cornerRadius": "md","borderWidth": "5px","borderColor": biruTua,
  "contents":[{"contents":[{"type":"separator","color":warnanya1},{"contents":[
  {"type":"separator","color":warnanya1},
  {"text": text ,"size":"xxs","align":"center","color": warnanya1,"wrap":True,"weight":"bold","type":"text"},
  {"type":"separator","color":warnanya1}
  ],"type":"box","spacing":"md","layout":"horizontal"},
  {"type":"separator","color":warnanya1}
  ],"type":"box","layout":"vertical"},
  ],"type":"box","layout":"vertical"}},}
  me.sendFlex(to, data)
def sendTemplate2 (to,text):
  data = { "type": "flex","altText": " Assalamu'alaikumm","contents":
  {"type": "bubble","styles": style_biru,"type":"bubble","size":"kilo","body":
  {"cornerRadius": "md","borderWidth": "5px","borderColor": biruTua,"contents":[{"contents":[{"type":"separator","color":"#ffffff"},
  {"contents":[sp_putih,
  {"text":"вĻα¢к●σƒ●gαмєя","size":"md","align":"center","color":"#BE1700","wrap":True,"weight":"bold","type":"text"},
  sp_putih
  ],"type":"box","spacing":"md","layout":"horizontal"},
  sp_putih],"type":"box","layout":"vertical"},
  {"contents":[sp_putih,
  {"contents":[sp_putih,
  {"type": "image","url": "https://1.bp.blogspot.com/-6T7oMDOIlKA/XVX_8-oO52I/AAAAAAAAGe0/W0MubSIIyUUzw3et2YifTWqxaNRRwWE-ACLcBGAs/s1600/20190816_075636.png","size": "full","aspectRatio": "3:1"},
  sp_putih
  ],"type":"box","spacing":"md","layout":"horizontal"},
  sp_putih],"type":"box","layout":"vertical"},
  {"contents": [sp_putih,
  {"contents":[sp_putih,
  {"text": text,"size":"xs","color":kuning,"wrap":True,"weight":"bold","type":"text"},
  sp_putih],"type":"box","spacing":"md","layout":"horizontal"},
  sp_putih],"type":"box","layout":"vertical"},
  ],"type":"box","spacing":"xs","layout":"vertical"}},}
  me.sendFlex(to, data)
def Fotter(to,text):
  data = {"type": "text","text": text,"sentBy": {"label": "вĻα¢к ● σƒ ● gαмєя","iconUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSi2LaC4ftZz21mtSDA3YkylLb6lgqncx_uxOp-wdyAlIqsVsJ1","linkUrl": "https://bit.ly/38K8bbV"}}
  me.sendFlex(to,data)
def RunTheRun(to, mid, firstmessage):
  try:
    arrData = ""
    text = "%s " %(str(firstmessage))
    arr = []
    mention = "@x \n"
    slen = str(len(text))
    elen = str(len(text) + len(mention) - 1)
    arrData = {'S':slen, 'E':elen, 'M':mid}
    arr.append(arrData)
    today = datetime.today()
    future = datetime(2018,7,25)
    hari = (str(future - today))
    comma = hari.find(",")
    hari = hari[:comma]
    teman = me.getAllContactIds()
    gid = me.getGroupIdsJoined()
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    eltime = time.time() - mulai
    bot = runtime(eltime)
    h = me.getContact(meM)
    me.reissueUserTicket()
    My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
    text += mention+"WAKTU :\n"+jamtgl+"\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND : "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nINEX_TEAM. ʟɪɴᴇ ᴠᴇʀ.8.14.2\nRUN : "+bot+"\n\nMY TOKEN :\n"+str(me.authToken)+"\n\nMY MID : \n"+h.mid+"\nMY ID LINE : "+My_Id+"\n\nCHANEL YOUTUBE\n"+set["Respontag"]
    me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  except Exception as error:
    print("Error :\n" + str(error))
def Comt(text):
  pesan = text.lower()
  if pesan.startswith(set["keyCommand"]):
    Pbot = pesan.replace(set["keyCommand"],"")
  else:
    Pbot = "command"
  return Pbot
def bot(op):
    global time
    global ast
    global groupParam
    opp1 = op.param1
    opp2 = op.param2
    opp3 = op.param3
    try:
        if op.type is None:
          pass
        else:
          if op.type == 0:
            pass
          else :
            print("[ {} ] {}".format(str(op.type), OpType._VALUES_TO_NAMES[op.type]))
        if op.type == 13:
          if meM in opp3:
            if set["autoJoin"] == True:
              me.acceptGroupInvitation(opp1)
              wr = me.getGroup(opp1)
              ban = [contact.mid for contact in wr.members]
              for x in ban:
                if x in set["blacklist"]:
                  try:
                    me.kickoutFromGroup(opp1,[x])
                  except:pass
                print("blacklist kick ok")
        if op.type in [19,32,17,13]:
          if opp3 in set["PASUKAN"]:
            if opp2 in meM and opp2 in set["PASUKAN"]:
              pass
            else:
              Nam = me.getContact(opp2).displayName
              set["blacklist"][opp2] = True
              try:
                sendTemplate(opp1,Nam+"\nBanlist true")
              except:
                try:
                  sendTemplate(opp1,Nam+"\nBanlist true")
                except:pass
        if op.type == 26:
         if set["bot"] == True:
           msg = op.message
           text = msg.text
           Id = msg.id
           To = msg.to
           Dari = msg._from
           to = msg.to
           if msg.contentType == 0:
             if text is None:
               return
           if msg.toType == 2:
             if msg.toType == 0:
                to = msg._from
             elif msg.toType == 2:
               to = msg.to
           if msg.contentType == 7:
             if set["checkSticker"] == True:
               msg.contentType = 0
               stk_id = msg.contentMetadata['STKID']
               stk_ver = msg.contentMetadata['STKVER']
               pkg_id = msg.contentMetadata['STKPKGID']
               ret_ = "╔══[ Sticker Info ]"
               ret_ += "\n╠ ID : {}".format(stk_id)
               ret_ += "\n╠ PACKAGES ID : {}".format(pkg_id)
               ret_ += "\n╠ VERSION : {}".format(stk_ver)
               ret_ += "\n╠ URL : line://shop/detail/{}".format(pkg_id)
               ret_ += "\n╚══[ Finish ]"
               patih = "http://dl.stickershop.line.naver.jp/products/0/0/{}/{}/android/stickers/{}.png".format(str(stk_ver),(pkg_id),(stk_id))
               path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
               data = { "type": "flex","altText": " Assalamu'alaikumm","contents":
               {"type": "bubble","size":"micro",
               "styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#800000"}},
               "type":"bubble","body":
               {"cornerRadius": "md","borderWidth": "5px","borderColor": biruTua,"contents":[
               {"contents":[
               sp_putih,
               sp_putih,
               {"contents":[
               sp_putih,
               {"text":"🆂🆃🅸🅲🅺🅴🆁 🅲🅷🅴🅲🅺","size":"xs","align":"center","color":"#ffff00","wrap":True,"weight":"bold","type":"text"},
               sp_putih
               ],"type":"box","spacing":"md","layout":"horizontal"},
               sp_putih,
               {"contents":[
               sp_putih,
               sp_putih,
               {"url": image1,"type":"image"},
               sp_putih,
               sp_putih,
               {"type":"image","url": logo,"size":"xl"},
               sp_putih,
               sp_putih
               ],"type":"box","spacing":"md","layout":"horizontal"},
               sp_putih,
               {"contents":[
               sp_putih,
               {"text": str(ret_),"size":"xxs","color":"#33ffff","wrap":True,"weight":"bold","type":"text"},
               sp_putih
               ],"type":"box","spacing":"md","layout":"horizontal"},
               sp_putih
               ],"type":"box","layout":"vertical"},
               ],"type":"box","spacing":"xs","layout":"vertical"}},}
               me.sendFlex(to, data)
               datanya = {
                "type": "template","altText": "Bagi tikel donk",
                "template":
                {"type": "image_carousel",
                "columns": [
                {"imageUrl": path,
                "layout": "horizontal",
                "action":
                {"type": "uri","label": "JAJAN TIKEL","uri": "line://shop/detail/{}".format(pkg_id),"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}}]}}
               me.sendFlex(to, datanya)
               set["checkSticker"] = False
           if msg.contentType == 0:
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if set["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                     if mention ['M'] in meM:
                       group = me.getGroup(To)
                       masuk = me.getContact(Dari)
                       nama = masuk.displayName
                       data = { "type": "flex","altText": " Assalamu'alaikumm","contents":
                            {"type": "bubble","size":"micro",
                            "styles":style_biru,
                            "type":"bubble","body":
                            {"cornerRadius": "xs","borderWidth": "5px","borderColor": hijau,"contents":[
                            {"contents":[
                            sp_putih,
                            {"contents":[
                            sp_putih,
                            {"text":"вĻα¢к●σƒ●gαмєя","size":"xs","align":"center","color": merah,"wrap":True,"weight":"bold","type":"text"},
                            sp_putih
                            ],"type":"box","spacing":"md","layout":"horizontal"},
                            sp_putih,
                            {"contents":[
                            sp_putih,
                            {"type": "image","url": "https://cdn.dribbble.com/users/293796/screenshots/3438995/fb-likes.gif","size": "xl","action": {"type": "uri","uri": "line://app/1609524990-mpvZ5xv5"}},
                            sp_putih,
                            {"url":"https://os.line.naver.jp/os/p/{}".format(masuk.pictureStatus),"type":"image","action": {"type": "uri","uri": "https://os.line.naver.jp/os/p/{}".format(masuk.pictureStatus)}},
                            sp_putih,
                            {"type":"image","url": "https://1.bp.blogspot.com/-zyUmsriCmGE/XVYAO-lsFLI/AAAAAAAAGe8/BsSUwtUfFc0mxRGxE_8fOz3peuxB3t9UwCLcBGAs/s1600/20190816_074821.jpg","size":"xl","action": {"type": "uri","uri": "https://bit.ly/38K8bbV"}},
                            sp_putih
                            ],"type":"box","spacing":"md","layout":"horizontal"},
                            sp_putih,
                            {"contents":[
                            sp_putih,
                            {"text": nama+" "+ set["Respontag2"],"size":"xs","color": hijau,"wrap":True,"weight":"bold","type":"text"},
                            sp_putih
                            ],"type":"box","spacing":"md","layout":"horizontal"},
                            sp_putih
                            ],"type":"box","layout":"vertical"},
                            ],"type":"box","spacing":"xs","layout":"vertical"}},}
                       me.sendFlex(to, data)
                       break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if set["arespon"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                     if mention ['M'] in meM:
                       h = me.getContact(Dari)
                       me.sendMessage(Dari, h.displayName+"\n"+set["tagpm"])
                       break
#===========================
        if op.type in [25, 26]:
          if set["bot"] == True:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            Id = msg.id
            To = msg.to
            Dari = msg._from
            if msg.contentType == 0:
              if text is None:
                return
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                 to = msg.to
               elif msg.toType == 2:
                 to = msg.to
               if msg.contentType == 1:
                 if Dari in meM:
                   if meM in set["foto"]:
                     path = me.downloadObjectMsg(Id)
                     del set["foto"][meM]
                     me.updateProfilePicture(path)
                     me.sendMessage(To, "Foto berhasil dirubah")
                 if set['changeProfileVideo']['status'] == True:
                   path = me.downloadObjectMsg(Id, saveAs="tmp/pict.bin")
                   if set['changeProfileVideo']['stage'] == 1:
                     set['changeProfileVideo']['picture'] = path
                     Fotter(To, "Silahkan kirimkan video yang ingin anda jadikan profile")
                     set['changeProfileVideo']['stage'] = 2
                   elif set['changeProfileVideo']['stage'] == 2:
                     set['changeProfileVideo']['picture'] = path
                     changeProfileVideo(To)
                     Fotter(To, "Type: Profile\n • Detail: Change Video Profile\n • Status: Succes..")
               elif msg.contentType == 2:
                 if set['changeProfileVideo']['status'] == True:
                   path = me.downloadObjectMsg(Id)
                   if set['changeProfileVideo']['stage'] == 1:
                     set['changeProfileVideo']['video'] = path
                     Fotter(To, "Type: Profile\n • Detail: Change Video Profile\n • Status: Send picture ~")
                     set['changeProfileVideo']['stage'] = 2
                   elif set['changeProfileVideo']['stage'] == 2:
                     set['changeProfileVideo']['video'] = path
                     changeProfileVideo(To)
               if msg.contentType == 0:
                    if set["autoRead"] == True:
                        me.sendChatChecked(To, Id)
                    if text is None:
                        print("[0] SEND COMMAND")
                        return
                    else:
                        Pbot = Comt(text)
                        Dari = msg._from
                        To = msg.to
                        Id = msg.id
                        if Pbot =="me":
                         if Dari in meM:
                          h = me.getContact(Dari)
                          dart = {
                      "type": "flex",
                      "altText": "{} mengirim kont".format(h.displayName),
                      "contents": {
                      "type": "carousel",
                      "type": "bubble",
                       "size": "nano",
                        "styles": style_biru,
                         "footer": {
                         "type": "box",
                         "layout": "horizontal","cornerRadius": "md","borderWidth": "5px","borderColor": biruTua,
                         "contents": [
                          sp_putih,
                           {
                           "type": "box",
                          "layout": "vertical",
                          "contents": [
                           sp_putih,
                           {
                           "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(h.pictureStatus),
                            "size": "full",
                            "aspectRatio": "20:13"
                              },
                             sp_putih,
                             {
                             "type": "text",
                             "text": h.displayName,
                             "color": putih,
                              "align": "start",
                               "size": "md",
                                "gravity": "center"
                                 },
                                  sp_putih,
                                 {
                                 "type": "box",
                                 "layout": "horizontal",
                                  "contents": [
                                  {
                                  "type": "text",
                                  "text": "Status",
                                   "color": putih,
                                    "size": "xxs",
                                     "align": "center"
                                     },
                                   sp_putih,
                                  {
                                 "type": "text",
                                 "text": "Aktif",
                                 "color": hijau,
                                 "align": "center",
                                  "size": "xxs"
                                   }
                                 ],
                               "flex": 1
                                },
                                sp_putih,
                                {
                                "flex": 3,
                                "type": "button",
                                "margin": "sm",
                                  "style": "secondary",
                                  "color": biru,
                                   "height": "sm",
                                    "action": {
                                    "type": "uri",
                                     "label": "👤 info",
                                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=checkmid%20{}".format(h.mid)
                                       }
                                       },
                                      sp_putih
                                      ]
                                    },
                                   sp_putih
                                  ]
                               }
                             }
                           }
                          me.sendFlex(To,dart)
               #           me.sendMessage(Line_Apikey, Devert)
                        if Pbot == "help":
                          if Dari in meM:
                            group = me.getGroup(To)
                            h = me.getContact(Dari)
                            data = {"type":"flex","altText":"{}".format(h.displayName),"contents":{"type":"carousel","contents":[
                            {"type": "bubble","size":"kilo",
                            "body": {
                              "type": "box",
                              "layout": "vertical","cornerRadius": "xs","borderWidth": "5px","borderColor": hijau,
                              "contents": [
                                {
                                  "type": "image",
                                  "url": "https://obs.line-scdn.net/{}".format(h.pictureStatus),
                                  "size": "full",
                                  "aspectMode": "cover",
                                  "aspectRatio": "4:6",
                                  "gravity": "top"
                                },
                                {
                          "type": "box",
                          "layout": "vertical","cornerRadius": "md","borderWidth": "2px","borderColor": biruTua,
                           "spacing": "md",
                            "action": {
                            "type": "uri",
                             "uri": "https://bit.ly/38K8bbV"
                              },
                            "contents": [
                           {"contents":[
                           sp_putih,
                            {"contents":[
                            sp_putih,
                            {"text":"вĻα¢к●σƒ●gαмєя","size":"md","align":"center","color": merah,"wrap":True,"weight":"bold","type":"text"},
                            sp_putih
                            ],"type":"box","spacing":"md","layout":"horizontal"},
                            sp_putih,
                            ],"type":"box","layout":"vertical"},
                            {"contents":[
                            sp_putih,
                            {"contents":[
                            sp_putih,
                            {"type": "image","url": "https://1.bp.blogspot.com/-6T7oMDOIlKA/XVX_8-oO52I/AAAAAAAAGe0/W0MubSIIyUUzw3et2YifTWqxaNRRwWE-ACLcBGAs/s1600/20190816_075636.png","size": "full","aspectRatio": "3:1"},
                            sp_putih
                            ],"type":"box","spacing":"md","layout":"horizontal"},
                            sp_putih
                            ],"type":"box","layout":"vertical"},
                              {
                              "type": "box",
                               "layout": "vertical",
                                "spacing": "xs",
                                "contents": [
                                {"contents":[
                                sp_putih,
                                {"contents":[
                                  sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Changedp",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=changedpvideo"
                                           }
                                       },sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Profile",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Profil"
                                           }
                                        },sp_putih
                                       ],"type":"box","spacing":"md","layout":"horizontal"},
                                      sp_putih
                                       ],"type":"box","layout":"vertical"},
                                       {"contents":[
                                       sp_putih,
                                       {"contents":[
                                       sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "R1 on",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=r1:on"
                                           }
                                       },sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "R1 off",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=r1:off"
                                           }
                                        },sp_putih
                                        ],"type":"box","spacing":"md","layout":"horizontal"},
                                        sp_putih
                                        ],"type":"box","layout":"vertical"},
                                        {"contents":[
                                        sp_putih,
                                        {"contents":[
                                       sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Pm on",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Pm:on"
                                           }
                                       },sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Pm off",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Pm:off"
                                           }
                                       },sp_putih
                                       ],"type":"box","spacing":"md","layout":"horizontal"},
                                       sp_putih
                                        ],"type":"box","layout":"vertical"},
                                       {"contents":[
                                       sp_putih,
                                       {"contents":[
                                       sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Mention",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Tag"
                                           }
                                       },sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Restart",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=#restart"
                                           }
                                       },sp_putih
                                       ],"type":"box","spacing":"md","layout":"horizontal"},
                                       sp_putih
                                        ],"type":"box","layout":"vertical"},
                                       {"contents":[
                                       sp_putih,
                                       {"contents":[
                                       sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Bot on",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Bot:on"
                                           }
                                       },sp_putih,
                                       {
                                           "type": "button",
                                           "style": "secondary",
                                           "color": ping,
                                           "height": "sm",
                                           "gravity": "center",
                                           "flex": 1,
                                           "action": {
                                               "type": "uri",
                                               "label": "Bot off",
                                               "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Bot:off"
                                           }
                                       },sp_putih
                                        ],"type":"box","spacing":"md","layout":"horizontal"},
                                        sp_putih
                                         ],"type":"box","layout":"vertical"},
                                         {"contents":[
                                       {"contents":[
                                       {"type":"image","url":"https://i.ibb.co/Rytts8y/com-kicklabz-sing-smule-downloader.png","size":"xxs"},
                                     {"type":"image","url":"https://i.ibb.co/xL3mVMK/Line-icon.png","size":"xxs"},{"type":"image","url":"https://i.ibb.co/26RvJVS/Pngtree-whatsapp-icon-logo-whatsapp-logo-3560533.png","size":"xxs"},
                                     {"type":"image","url":"https://i.ibb.co/b3JwtsP/Pngtree-youtube-logo-icon-3560542.png","size":"xxs"},{"type":"image","url":"https://i.ibb.co/QkJM8j7/20191101-134518.png","size":"xxs"}
                                        ],"type":"box","spacing":"md","layout":"horizontal"}
                                        ],"type":"box","layout":"vertical"},
                                          ]
                                   }
                            ],
                            "position": "absolute",
                               "cornerRadius": "3px",
                               "offsetTop": "2px",
                               "offsetStart": "2px",
                               "height": "371px",
                               "width": "246px"
                               }
                               ],
                              "paddingAll": "0px",
                              "paddingTop": "0px",
                              "cornerRadius": "3px"
                            }
                            }]}}
                            me.sendFlex(To, data)
                            sendTemplate2(To, Hallow)
                        elif Pbot == "mid":
                          if Dari in meM:
                              Fotter(To, Dari)
                        elif Pbot.startswith("getmid "):
                          if Dari in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            mi = me.getContact(key1)
                            data = {
                               "type": "text",
                               "text": "{}".format(key1),
                               "sentBy": {
                                  "label": "вĻα¢к●σƒ●gαмєя",
                                  "iconUrl": "https://scontent.fcgk9-2.fna.fbcdn.net/v/t1.0-9/cp0/e15/q65/p851x315/51691304_1868204569955031_2146220437988704256_o.jpg?_nc_cat=103&efg=eyJpIjoiYiJ9&_nc_eui2=AeH2ckLWYQHsnNZ_h-dxkaE6z8BLc-ped-MztW4ZIVdUV-ntVbUtpxp-yrIWasU0oZ8NiwTRmKSqr0DSF8HXmDE7MZQ7aCk7ff-H_i1Gzo8g7w&_nc_oc=AQn9OIKwJojXlHshN7igjGYPAx0PGSK3ICR-Vyp57YXxp1cGQulKVLgPBiaFkJfI2Iw&_nc_ht=scontent.fcgk9-2.fna&oh=bf88bf2a4f06709e8f5d18310f26865c&oe=5DB50A10",
                                  "linkUrl": "https://bit.ly/38K8bbV"
                                 }
                             }
                            me.sendFlex(To, data)
                        if Pbot == "removechat" or Pbot == "hapus chat":
                          if Dari in meM:
                            me.removeAllMessages(opp2)
                            sendTemplate(To, "Chat dibersihkan...")
                        if Pbot == "#reboot" or Pbot == "#restart":
                          if Dari in meM:
                            Fotter(To, "Loading…")
                            set["restartPoint"] = To
                            Run_Xx()
                            Fotter(To, "Silahkan gunakan seperti semula...")
                        if Pbot == "banlist":
                          if Dari in meM:
                            if set["blacklist"] == {}:
                              sendTemplate(To, " Nothing Blacklist ")
                            else:
                              pill = []
                              for i in set["blacklist"]:
                                ctk = me.getContact(i)
                                if len(pill) >= 400:
                                  pass
                                else:
                                  pill.append({"type": "bubble", "size": "nano",
                            "body": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "image",
                                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTjyGgn9g9AIbYJF6bFyRBQFPWAyMIrCBd_Jz-RIenlY-UbV8m",
                                  "size": "full",
                                  "aspectMode": "cover",
                                  "aspectRatio": "4:8",
                                  "gravity": "top"
                                },
                               {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                "type":"text",
                                "text": "{}".format(ctk.displayName),
                                "size": "xxs",
                                  "align":"center",
                                  "margin": "none",
                                  "color": biruHitam,
                                  "wrap": True,
                                  "weight": "regular"
                                }
                              ],
                             "position": "absolute",
                             "cornerRadius": "0px",
                             "offsetTop": "16px",
                               "offsetStart": "8px",
                               "backgroundColor": putih,
                               "height": "22px",
                               "width": "104px"
                              },
                               {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "image",
                                  "url": "https://obs.line-scdn.net/{}".format(ctk.pictureStatus),
                                  "size": "full",
                                  "aspectMode": "cover",
                                  "aspectRatio": "4:6",
                                  "gravity": "top"
                                }
                              ],
                             "position": "absolute",
                             "cornerRadius": "0px",
                             "offsetTop": "37px",
                               "offsetStart": "8px",
                               "height": "86px",
                               "width": "104px"
                              },
                              {
                              "type": "box",
                              "layout": "vertical","cornerRadius": "3px","borderWidth": "2px","borderColor": biruHitam,
                              "contents": [
                                {
                                  "type": "image",
                                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSjybug2NU0iSDmZG6iLiSUQljYgjnMr-PfT0gsXw3uE-ldVu9m",
                                  "size": "full",
                                  "aspectMode": "cover",
                                  "aspectRatio": "4:3",
                                  "gravity": "top"
                                }
                              ],
                             "position": "absolute",
                             "cornerRadius": "0px",
                             "offsetTop": "137px",
                               "offsetStart": "5px",
                               "height": "73px",
                               "width": "109px"
                              }
                              ],
                               "cornerRadius": "8px",
                              "paddingAll": "0px",
                              "paddingTop": "0px"
                            }
                           })
                              k = len(pill)//10
                              for aa in range(k+1):
                                data = {"type":"flex","altText":"Data blacklist","contents":{"type":"carousel","contents":pill[aa*10 : (aa+1)*10]}}
                                me.sendFlex(To, data)
                        if Pbot == "clearban":
                          if Dari in meM:
                            sendTemplate(To, "DAFTAR[%s] BAN\n[success deleted]" % (str(len(set["blacklist"]))))
                            set["blacklist"] = {}
                        if Pbot == "join":
                          if Dari in meM:
                            if set["PASUKAN"] == {}:
                              sendTemplate(To, " Nothing Bots ")
                            else:
                              me.inviteIntoGroup(To, set["PASUKAN"])
                        if Pbot.startswith("bot "):
                          if Dari in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                            for target in targets:
                              if target in set["PASUKAN"]:
                                sendTemplate(To, "Dia Sudah jadi pasukan")
                              else:
                                try:
                                  set["PASUKAN"][target] = True
                                  sendTemplate(To, "Berhasil add pasukan")
                                except:
                                  pass
                        if Pbot == "changedpvideo":
                          if Dari in meM:
                            set['changeProfileVideo']['status'] = True
                            set['changeProfileVideo']['stage'] = 1
                            sendTemplate(To, "Type: Profile\n • Detail: Change Video Profile\n • Status: Waiting for video\nPlease send a video...")
                        if Pbot == "tag" or Pbot == "tagall" or Pbot == "mention":
                          if Dari in meM:
                            group = me.getGroup(To)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                              txt = u''
                              s=0
                              b=[]
                              for i in group.members[a*20 : (a+1)*20]:
                                b.append(i.mid)
                              mentionMembers(msg.to, b)
                        if Pbot == "profil":
                          contact = me.getContact(Dari)
                          cover = me.getProfileCoverURL(Dari)
                          me.reissueUserTicket()
                          res = "╭━━━━━━━━━━━━━━━━━━━━╮\n├ ☠ Profile info\n├━━━━━━━━━━━━━━━━━━━━\n"
                          res += "├ ☠ Display Name :{}\n".format(contact.displayName)
                          res += "├ ☠ Mid: {}\n".format(contact.mid)
                          res += "├ ☠ Status Message\n├ ☠ {}\n".format(contact.statusMessage)
                          res += "╰━━━━━━━━━━━━━━━━━━━━╯"
                          sendTemplate2(To, res)
                          try:
                            poto = "https://os.line.naver.jp/os/p/{}".format(Dari)
                          except:
                            poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                          dax = {"type": "template","altText": "berak di celana","template": {"type": "image_carousel","columns": [{"imageUrl": poto,"layout": "horizontal","action": {"type": "uri","label": "PROFILE","uri": poto,"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}},{"imageUrl": cover,"layout": "horizontal","action": {"type": "uri","label": "COVER","uri": cover,"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}},{"imageUrl": "https://qr-official.line.me/L/"+me.getUserTicket().id+".png","layout": "horizontal","action": {"type": "uri","label": "CONTACT","uri": "https://line.me/ti/p/"+me.getUserTicket().id,"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}}]}}
                          me.sendFlex(To, dax)
                        if Pbot =="assalamualaikum":
                            me.sendMessage(To," وَالسَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُه...")
                        if Pbot == "joinqr on" or Pbot == 'jointicket on':
                          if Dari in meM:
                            set["autoJoinTicket"] = True
                            sendTemplate(To, "Join ticket diaktifkan")
                        if Pbot == "joinqr off" or Pbot == 'jointicket off':
                          if Dari in meM:
                            set["autoJoinTicket"] = False
                            sendTemplate(To,"Autojoin Tiket dinonaktifkan")
                        if Pbot == "join on" or Pbot == 'join:on':
                          if Dari in meM:
                            set["autoJoin"] = True
                            sendTemplate(To, "Join diaktifkan")
                        if Pbot == "join off" or Pbot == 'join:off':
                          if Dari in meM:
                            set["autoJoin"] = False
                            sendTemplate(To,"Autojoin dinonaktifkan")
                        if Pbot == "r1:on" or Pbot == 'r1 on':
                          if Dari in meM:
                            set["detectMention"] = True
                            sendTemplate(To, "Respon diaktifkan")
                        if Pbot == "r1:off" or Pbot == 'respon1 off':
                          if Dari in meM:
                            set["detectMention"] = False
                            sendTemplate(To,"Respon dinonaktifkan")
                        if Pbot == "pm:on" or Pbot == 'pm on':
                          if Dari in meM:
                            set["arespon"] = True
                            sendTemplate(To, "Respon pm diaktifkan")
                        if Pbot == "pm:off" or Pbot == 'responpm off':
                          if Dari in meM:
                            set["arespon"] = False
                            sendTemplate(To,"Respon pm dinonaktifkan")
                        if Pbot.startswith("addblc "):
                          if Dari in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                            for target in targets:
                              if target in set["blacklist"]:
                                Fotter(To, "Dia Sudah ada di blacklist")
                              else:
                                try:
                                  set["blacklist"][target] = True
                                  sendTemplate(To, "Berhasil tambah blacklist")
                                except:
                                  pass
                        if "/ti/g/" in Pbot:
                          if set["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                              if l not in n_links:
                                n_links.append(l)
                            for ticket_id in n_links:
                              group = me.findGroupByTicket(ticket_id)
                            me.acceptGroupInvitationByTicket(group.id,ticket_id)
                            sendTemplate2(To, "Succes masuk group : %s" % str(group.name))
        if op.type in [25, 26]:
            msg = op.message
            text = msg.text
            Id = msg.id
            To = msg.to
            Dari = msg._from
            if msg.contentType == 0:
              if text is None:
                return
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                 to = msg.to
               elif msg.toType == 2:
                 to = msg.to
               if msg.contentType == 0:
                    if text is None:
                        print("[0] SEND COMMAND")
                        return
                    else:
                        msg = op.message
                        text = msg.text
                        Pbot = Comt(text)
                        Dari = msg._from
                        To = msg.to
                        Id = msg.id
                        if Pbot == "bot:off" or Pbot == "matikan":
                          print ("NOTIF BOT NON ACTIVE")
                          if Dari in meM:
                            RunTheRun(To,Dari, "RESULT\n")
                            print("""
                            BOT TEMPLATE
                            VERSION : INEXBOTS
                            REVISION : VPS-TERMUX
                            {}
                            """.format(jamtgl))
                            Fotter(To, "Ok I'am Turn down "+me.getContact(Dari).displayName)
                            set["bot"] = False
                        if Pbot == "bot:on" or Pbot == "aktifkan":
                          print ("NOTIF BOT ACTIVE")
                          if Dari in meM:
                            Fotter(To, "Already Ok "+me.getContact(Dari).displayName)
                            RunTheRun(To,Dari, "RESULT\n")
                            print("""
                            BOT TEMPLATE
                            VERSION : INEXBOTS
                            REVISION : VPS-TERMUX
                            {}
                            """.format(jamtgl))
                            set["bot"] = True
                            set["Conection"] = To

    except Exception as error:
      logError(error)
      print (error)


while True:
  try:
    ops = oepoll.singleTrace(count=50)
    if ops is not None:
      for op in ops:
        oepoll.setRevision(op.revision)
        thread = threading.Thread(target=bot, args=(op,))
        thread.start()
  except Exception as error:
    logError(error)
    print(error)
