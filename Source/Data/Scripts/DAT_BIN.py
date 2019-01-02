"""
Direitos do autor, (GoT)Sr_Rina.

// Sem Empresa //

Criado e desenvolvido por (GoT)Sr_Rina, utilizando a JanJa2D, que
por sinal o mesmo esta desenvolvendo, caso queira modificar o jogo,
fique livre, porem nao responsabilizo por "bugs" ou "crash" em geral.

// Condicoes //

Usado OpenGL, em seu nucleo, com total diretos da OpenGL e em juncao da Pygame, e JanJa.

// Observacoes //

Basicamente, isso e pygame com OpenGL, porem e complexo demais usar pygame e OpenGL bruto.

// Citacoes //

- None -

"""

import math, sys

try:
	from janja2d.core import *
	from janja2d.JanRect import task
except:
	raise
pass

class LOAD_BIN_CONFIG(object):
	F=None

	BIN_RESOLUTION_WIDTH=0
	BIN_RESOLUTION_HEIGHT=0

	BIN_DISPLAY_FREQUENCY=0
	BIN_DISPLAY_FULLSCREEN=None

	BIN_INDEX_WIDTH=None
	BIN_INDEX_HEIGHT=None

	BIN_INDEX_FREQUENCY=None
	BIN_INDEX_FULLSCREEN=None

	BIN_ERROR_WIDTH=True
	BIN_ERROR_HEIGHT=True

	BIN_ERROR_FREQUENCY=True
	BIN_ERROR_FULLSCREEN=True

	def __init__(self):
		try:
			#self.F=open("%s/Bin/BIN_CONFIG.bin" % JanSys.getFilePath())
			self.F=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath())

			for Linhas in self.F:
				if Linhas[:1] == "w":
					self.BIN_INDEX_WIDTH=Linhas.replace("w", "")
					self.BIN_RESOLUTION_WIDTH=int(self.BIN_INDEX_WIDTH)
					self.BIN_ERROR_WIDTH=False

				elif Linhas[:1] == "h":
					self.BIN_INDEX_HEIGHT=Linhas.replace("h", "")
					self.BIN_RESOLUTION_HEIGHT=int(self.BIN_INDEX_HEIGHT)
					self.BIN_ERROR_HEIGHT=False
				
				elif Linhas[:1] == "d":
					self.BIN_INDEX_FREQUENCY=Linhas.replace("d", "")
					self.BIN_DISPLAY_FREQUENCY=int(self.BIN_INDEX_FREQUENCY)
					if self.BIN_DISPLAY_FREQUENCY == 60:
						self.BIN_ERROR_FREQUENCY=False

					elif self.BIN_DISPLAY_FREQUENCY == 30:
						self.BIN_ERROR_FREQUENCY=False

				elif Linhas[:1] == "f":
					self.BIN_INDEX_FULLSCREEN=Linhas.replace("f", "")
					self.BIN_DISPLAY_FULLSCREEN=int(self.BIN_INDEX_FULLSCREEN)
					self.BIN_ERROR_FULLSCREEN=False

			self.backup()
			self.F.close()
		except:
			self.backup()
		return None

	def getW(self):
		try:
			return self.BIN_RESOLUTION_WIDTH
		except:
			raise
		return None

	def getH(self):
		try:
			return self.BIN_RESOLUTION_HEIGHT
		except:
			raise
		return None

	def getD(self):
		try:
			return self.BIN_DISPLAY_FREQUENCY
		except:
			raise
		return None

	def getF(self):
		try:
			return self.BIN_DISPLAY_FULLSCREEN
		except:
			raise
		return None

	def setW(self, w):
		try:
			#cache_w=open("%s/Bin/BIN_CONFIG.bin" % JanSys.getFilePath()).read()

			cache_w=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath()).read()
			
			pack_w=cache_w.replace("w%d" % self.getW(), "w{}".format(str(w)))

			repack_w=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "r+")

			#repack_w=open("%s/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "r+")

			repack_w.write(pack_w)

			repack_w.close()
		except:
			raise
		return None

	def setH(self, h):
		try:
			#cache_h=open("%s/Bin/BIN_CONFIG.bin" % JanSys.getFilePath()).read()

			cache_h=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath()).read()

			pack_h=cache_h.replace("h%d" % self.getH(), "h{}".format(str(h)))

			repack_h=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "r+")

			#repack_h=open("%s/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "r+")

			repack_h.write(pack_h)

			repack_h.close()
		except:
			raise
		return None

	def setD(self, d):
		try:
			cache_d=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath()).read()

			pack_d=cache_d.replace("d%d" % self.getD(), d)

			repack_d=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "r+")

			repack_d.write(pack_d)

			repack_d.close()
		except:
			raise
		return None

	def setF(self, f):
		try:
			cache_f=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath()).read()

			pack_f=cache_f.replace("f%d" % self.getF(), "f{}".format(str(f)))

			repack_f=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "r+")

			repack_f.write(pack_f)

			repack_f.close()
		except:
			raise
		return None

	def backup(self):
		try:
			"""
			Se caso alguem mexer nesse arquivo, e mudar algo como frequencia ou tamanho da janela, devera deixar, d, w, h...
			Pois assim, nao ira reiniciar toda a config deixando como a de orriginal.
			"""
			if (self.BIN_ERROR_WIDTH, self.BIN_ERROR_HEIGHT, self.BIN_ERROR_FREQUENCY, self.BIN_ERROR_FULLSCREEN) == (False, False, False, False):
				pass
			else:
				print(self.BIN_ERROR_WIDTH, self.BIN_ERROR_HEIGHT, self.BIN_ERROR_FREQUENCY, self.BIN_ERROR_FULLSCREEN)
				repack=open("%s/Prisdos/Data/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "w")
				#repack=open("%s/Bin/BIN_CONFIG.bin" % JanSys.getFilePath(), "w")
				repack.write(
"""
Sistema de salvamento da configuracão de video dentro do jogo.

- Resolução do jogo.
w1280
h720

- Frequencia do ecrã (30, 60).
d60

- Tela cheia. 
f0

- Creditos:
Sr_Rina.
""")
				repack.close()

		except:
			raise
		return None
