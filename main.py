import config
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
import cv2
import numpy
import cv2.aruco as aruco

bot = TeleBot(config.token)
keyboard = ReplyKeyboardMarkup(True)
keyboard.row('/start', '/info')
keyboard.row('Привки :3', 'Поки :D')
sticker1 = 'CAACAgQAAxkBAAO4YEJg0yjXTm0lcQ1-Z004VQS-PpYAAiMBAAKoISEGEQLLnvFEuxIeBA'

@bot.message_handler(commands = ['start'])
def start(message):
    print(message.chat.id, message.text)
    bot.send_sticker(message.chat.id, sticker1)
    bot.send_message(message.chat.id, 'Бот принял ислам', reply_markup = keyboard)

@bot.message_handler(commands = ['info'])
def info(message):
    print(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Ета мой бот', reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def lalala(message):
    print(message.chat.id, message.text)
    bot.send_message(message.chat.id, message.text, reply_markup = keyboard)
    #bot.send_message(message.chat.id, 'Принял!')

@bot.message_handler(content_types = ['photo'])
def reseive_photo(message_photo):
    photo_id = message_photo.photo[-1].file_id
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('image5.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)
    new_file.close()
    image = cv2.imread('image5.jpg')

    dictionary = aruco.Dictionary_get(aruco.DICT_4X4_50)
    image = cv2.imread('image5.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    marker_grounds, ids, service = aruco.detectMarkers(image_gray, dictionary)
    aruco.drawDetectedMarkers(image, marker_grounds)
    number= ids[0][0]
    print(number)
    bot.send_message(config.my_chat_id, 'Вы отправили aruco метку под номером: ', number)
    #image_new = image[100:200, 200:300]
    #image_resize = cv2.resize(image, (300, 300))
    cv2.imshow('window', image)
    cv2.waitKey()
    photo = open('image5.jpg', 'rb')
    bot.send_photo(message_photo.chat.id, 'image5.jpg')
    
bot.send_message(config.my_chat_id, 'Я вас Котегорически Приветствую')
bot.polling(none_stop = True)
print(config.token)
