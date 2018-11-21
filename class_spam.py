#-*-coding:utf8-*-

from pynput.keyboard import Key, Controller
import string
from time import sleep

class Spam():
	def __init__(self):
		self.keyboard = Controller()
	
	def cambiar_de_ventana(self):
		with self.keyboard.pressed(Key.cmd):
			self.keyboard.press(Key.tab)
			self.keyboard.release(Key.tab)
		
		sleep(0.5)

	def enviar_mensajes(self, texto, cantidad_de_veces):
		for n in range(cantidad_de_veces):
			for j in range(len(texto)):
				caracter = texto[j]
				if caracter == ' ':
					self.keyboard.press(Key.space)
					self.keyboard.release(Key.space)
				elif caracter in string.ascii_uppercase:
					with self.keyboard.pressed(Key.shift):
						caracter = caracter.lower()
						self.keyboard.press(caracter)
						self.keyboard.release(caracter)
				else:
					self.keyboard.press(caracter)
					self.keyboard.release(caracter)

			self.keyboard.press(Key.enter)
			self.keyboard.release(Key.enter)

# para descomentar borre las lineas 38 y 49 -------------
'''
whatsapp = Spam()
# para cambiar a la ventana anterior
whatsapp.cambiar_de_ventana()
# para congelar el programa dos segundos
#sleep(2)

texto = 'ingrese aca su texto'
N = #cantidad de veces a enviar

whatsapp.cantidad_de_veces(texto, N)
'''