# -*- coding: utf8 -*-
import telebot
import random
import requests
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
token='802401444:AAFT2tlcNH-0ns58weFEjVqBi7LfRJS9E40'
bot=telebot.TeleBot(token)
imglib=['Gru1.png','Gru2.png','Gru3.png','Gru4.png','Gru5.png','Gru6.png','Gru7.png','Gru8.png','Gru9.png','Gru10.png','Gru11.png','Gru12.png']



@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'freunde halo. Вас приветствует постироничный грю. Пиши сюда любые слова и я буду переводить их в несмешную постиронию')
	bot.send_photo(message.chat.id,'https://i.pinimg.com/originals/d5/18/80/d518802fbfe0180d5c818f388e5979a8.png')
@bot.message_handler(content_types=['text'])
def main_script(message):
	def text_on_pic(input_image_path,output_image_path,text, pos):
		photo = Image.open(input_image_path)
		drawing = ImageDraw.Draw(photo)
		
		white=(255,255,255)
		font = ImageFont.truetype("compact.ttf", 100)
		try:

			drawing.text(pos, text,fill=(255,255,255,255), font=font)
		except:
			drawing.text(pos, text, font=font)
		photo.save(output_image_path)
		with open(output_image_path, 'rb') as f:
  			contents = f.read()
		bot.send_photo(message.chat.id,contents)
		
		os.remove(output_image_path)
		
		
	if message.text:
		img=random.choice(imglib)
	if img=='Gru1.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(250,250))
	elif img=='Gru2.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(200,200))
	elif img=='Gru3.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(750,800))
	elif img=='Gru4.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(150,200))
	elif img=='Gru5.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(500,800))
	elif img=='Gru6.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(200,200))
	elif img=='Gru7.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(500,700))
	elif img=='Gru8.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(380,900))
	elif img=='Gru9.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(500,900))
	elif img=='Gru10.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(500,800))
	elif img=='Gru11.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(500,800))
	elif img=='Gru12.png':
		text_on_pic(img, 'Watermarkered_Gru.png',
                   text=message.text,
                   pos=(500,900))
bot.polling()

	
