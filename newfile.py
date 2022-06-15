import vk_api
import json
import requests
import random
import traceback
import os
import subprocess
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from array import *
from random import randint
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
keyboard = VkKeyboard(one_time=True)



vk_session = vk_api.VkApi(token='token')
longpoll = VkBotLongPoll(vk_session, group_id="202796234")
vk = vk_session
num = int
msg_art = str
avk=vk_session.get_api()
##Далее описывается функционал отправки всякой хуйни и выгрузки фото (для последующей отправки)
def sender(id, text):
    avk.messages.send(user_id = id, message = text, random_id = 0, keyboard = keyboard.get_keyboard())
def send_attach(id, url):
    avk.messages.send(user_id = id, attachment = url, random_id = 0, keyboard = keyboard.get_keyboard())
def send_stick(id, number):
    avk.messages.send(user_id = id, sticker_id = number, random_id = 0)
def sender_chat(chat_id, text):
    avk.messages.send(chat_id = chat_id, message = text, random_id = random.randint(0,100))
def send_attach_chat(chat_id, url):
    avk.messages.send(chat_id = chat_id, attachment = url, random_id = 0)

def upload_photo(chat_id, filename):
    link = vk.method('photos.getMessagesUploadServer', {'peer_id': chat_id})['upload_url']
    print(link)
    cookies = vk.http.cookies
    up = json.loads(requests.post(link, files={'photo': open(filename, 'rb')}).text)
    photos = vk.method('photos.saveMessagesPhoto', up)
    print(photos)
    ownerId = photos[0]['owner_id']
    photoId = photos[0]['id']
    vk.method('messages.send', {'peer_id': chat_id, 'random_id': random.randint(0,2048), 'attachment': "photo{}_{}".format(ownerId, photoId)})
while True: ##цикл для лонгпола, без этой хуеты иногда вылетает ошиб_очка, а так на похуй
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print(event)
                peer_id = event.message['peer_id']
                if peer_id >= 2000000000: ##Если пир айди - это айди беседы, значит бот работает в режиме беседы с одним функционалом
                    if 'action' in event.message:
                        if (event.message['action']['type'] == 'chat_invite_user') and (event.message['action']['member_id'] == -202796234):
                            chat_id = int(event.chat_id)
                            sender_chat(chat_id, 'Вас приветствует бот-идиот. Разрешите боту просматривать всю переписку чтобы команды срабатывали')
                    else:
                        msg = event.message['text'].lower()
                        chat_id = int(event.chat_id)
                        random_id = random.randint(0, 100)
                        attachments = []
                        id = event.message['from_id']
                        ##if msg in ["/art", "/арт", "[club152451931|@random_anime_official], арт", "[club152451931|@random_anime_official], art", "[club152451931|@random_anime_official], /art", "[club152451931|@random_anime_official], /арт", "[club152451931|@random_anime_official] /art", "[club152451931|@random_anime_official] арт", "[club152451931|@random_anime_official] art", "[club152451931|@random_anime_official] /арт"]:
                           ## files = os.listdir("/home/qph7/Yuri pack")
                            ##upload_photo(peer_id, "/home/qph7/Yuri pack/"+files[random.randint(0, len(files)-1)])
                            ##В этих строчках я пытался описать хуйню для добавления сразу нескольких картиночек в одно сообщение, но мне стало похуй
                        if msg in ["пчел"]:
                            send_attach_chat(chat_id, "photo-202796234_457239018") ##На основе вот этой команды предлагаю сделать команду на блок стикеров. Картинка выгружена в альбом паблика и отправляется просто url этой картинки, что даёт почти моментальный респонс
                        if msg in ["нацист"]:
                            send_attach_chat(chat_id, "video-29544671_171117427")
                        if msg in ["совок"]:
                            send_attach_chat(chat_id, "photo-202796234_457239017")
                        if msg in ["навальный", "/navalny", "овальный"]:
                            files = os.listdir("/home/qph7/овальный")
                            upload_photo(peer_id, "/home/qph7/овальный/"+files[random.randint(0, len(files)-1)])
                        if msg in ["/укр", "/ukr", "укр"]:
                            files = os.listdir("/home/qph7/Укр")
                            upload_photo(peer_id, "/home/qph7/Укр/"+files[random.randint(0, len(files)-1)])
                        if msg in ["/консерва", "консерва"]:
                            files = os.listdir("/home/qph7/Консерва")
                            upload_photo(peer_id, "/home/qph7/Консерва/"+files[random.randint(0, len(files)-1)])
                        if msg in ["/gosl"]:
                            files = os.listdir("/home/qph7/Гуслинг")
                            upload_photo(peer_id, "/home/qph7/Гуслинг/"+files[random.randint(0, len(files)-1)])
                else:     ##Если мы не находимся в беседе - функционал другой
                    msg = event.message['text'].lower()
                    id = event.message['from_id']
                    attachments = []
                    if msg in ["привет", "начать", "здравствуйте", "здравствуй", "ку", "хай", "прив", "дарова", "дороу", "привет.", "здравствуйте.", "здравствуй.", "ку.", "хай.", "прив.", "дарова.", "дороу.", "привет!", "здравствуйте!", "здравствуй!", "ку!", "хай!", "прив!", "дарова!", "дороу!"]:
                        sender(id, "Вас приветствует бот")
                        send_stick(id, 21)
                    elif msg in ["арт", "art", "/art", "/арт", "/юри", "юри"]:
                        files = os.listdir("/home/qph7/Yuri pack")
                        upload_photo(peer_id, "/home/qph7/Yuri pack/"+files[random.randint(0, len(files)-1)])
                    if msg in ["/укр", "/ukr", "укр"]:
                        files = os.listdir("/home/qph7/Укр")
                        upload_photo(peer_id, "/home/qph7/Укр/"+files[random.randint(0, len(files)-1)])
                        ##send_attach(id, 'photo-152451931_'+str(randint(457248038, 457251894))) ##photo-152451931_457248038 - photo-152451931_457251894
                    #elif msg[0] == "/art":
                        #msg_art == msg.split()
                        #print(msg_art)
                        #for word in msg_art:
                            #if word.isnumeric():
                                #num == word
                        #if num == num.empty:
                            #send_attach(id, 'photo-152451931_'+str(randint(457248038, 457251894)))
                        #else:
                            #while num > 0:
                                #send_attach(id, 'photo-152451931_'+str(randint(457248038, 457251894)))
                                #num = num - 1
                    ##О, здесь я тоже пытался описать отправку нескольких картинок, можно поржать
                    elif msg in ["включить пк"] and ((id == 428225339) or (id == 245663694)): ##Wake on LAN удобная штука
                        os.system("wakeonlan B4:2E:99:1B:EE:72")
                        sender(id, "Пк включен")
                    elif msg in ["ip"] and ((id == 428225339) or (id == 245663694)): ##А это мне лень было конфижить на роутере DHCP и поэтому я просто каждый раз обращался к боту чтобы он мне писал айпи локальный
                        result = subprocess.check_output("hostname -I", shell=True)
                        b = result[0:11]
                        print(b)
                        sender(id, b)
                    elif msg in ["пак"]:
                        sender(id, "Пак всех артов за всё время:\nyadi.sk/d/RxmjBQkxMeo1tw?w=1")
                    else:
                        sender(id, 'Я тебя не понимаю')
    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
