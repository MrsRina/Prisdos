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

import sys, math, DAT_BIN, DAT_1, DAT_2

try:
	from janja2d.core import *
	from janja2d.JanRect.janwin import JanWin
	from janja2d.JanRect import task
except:
	raise

class RAW:
	RAW_WINDOW_GAME=None
	RAW_EVENT_WINDOW=None
	RAW_RANDOM_INFO_VER=None
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	RAW_GAME_INIT=False

	RAW_GAME_LOG_INIT=True
	RAW_GAME_LOG_1_INIT=True
	RAW_GAME_LOG_2_INIT=False
	RAW_GAME_PRESS_INIT=False

	RAW_GAME_LOG_1=None
	RAW_GAME_LOG_2=None
	RAW_GAME_PRESS=None

	RAW_GAME_MAIN_MENU_INIT=False

	RAW_GAME_MENU_INIT=False
	RAW_GAME_MENU=None

	RAW_START_GAME_MENU_INIT=False
	RAW_START_MENU=None

	RAW_LOAD_GAME_MENU_INIT=False
	RAW_LOAD_GAME_MENU=None

	RAW_CONFIGURACOES_GAME_MENU_INIT=False
	RAW_CONFIGURACOES_GAME_MENU=None

	RAW_CONFIGURACOES_VIDEO_GAME_MENU_INIT=False
	RAW_CONFIGURACOES_VIDEO_GAME_MENU=None

	RAW_EXIT_GAME=False

	RAW_LEVEL_1_INIT=False
	RAW_LEVEL_1=None

	def __init__(self):
		os.environ["SDL_VIDEO_CENTERED"]="1"
		
		self.RAW_WINDOW_GAME=JanWin("Prisdos", (self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH()), self.MAIN_BIN_CONFIG.getF(), None)
		self.RAW_WINDOW_GAME.setWindowIcone("Data/Scripts/Texturas/icone.ico")
		self.RAW_WINDOW_GAME.setWhile(self.GameEvents)

	def GameEvents(self):
		self.RAW_GAME_INIT=True

		# Index:
		self.RAW_RANDOM_INFO_VER=DAT_1.INFO_VER(self.RAW_WINDOW_GAME, "1.7")

		self.RAW_GAME_LOG_1=DAT_1.LOG_1()
		self.RAW_GAME_LOG_2=DAT_1.LOG_2()

		self.RAW_GAME_PRESS=DAT_1.GAME_PRESS(self.RAW_WINDOW_GAME)
		self.RAW_GAME_MENU=DAT_1.MAIN_MENU()
		self.RAW_START_MENU=DAT_1.COMECAR_GAME_MENU(self.RAW_WINDOW_GAME)
		self.RAW_LOAD_GAME_MENU=DAT_1.CARREGAR_GAME_MENU(self.RAW_WINDOW_GAME)
		self.RAW_CONFIGURACOES_GAME_MENU=DAT_1.CONFIG_GAME_MENU(self.RAW_WINDOW_GAME)
		self.RAW_CONFIGURACOES_VIDEO_GAME_MENU=DAT_1.CONFIG_VIDEO_GAME_MENU(self.RAW_WINDOW_GAME)

		while self.RAW_GAME_INIT:
			# Clear Buffers:			
			loader.loadBuffers()

			# Definir FPS:
			self.RAW_WINDOW_GAME.setFps(self.MAIN_BIN_CONFIG.getD())

			if self.RAW_GAME_LOG_INIT:
				if self.RAW_GAME_LOG_1_INIT:
					# Desativar o mouse:
					self.RAW_WINDOW_GAME.disableMouse()
					self.RAW_WINDOW_GAME.setGrabWindow(1)
					self.Log1()

				if self.RAW_GAME_LOG_2_INIT:
					# Desativar o mouse:
					self.RAW_WINDOW_GAME.disableMouse()
					self.RAW_WINDOW_GAME.setGrabWindow(1)
					self.Log2()

			if self.RAW_GAME_MAIN_MENU_INIT:
				# Reativar o mouse:
				self.RAW_WINDOW_GAME.enableMouse()
				self.RAW_WINDOW_GAME.setGrabWindow(1)

				self.RAW_THEME_MUSIC=loader.loadSound("%s/Prisdos/Data/Scripts/Sons/Musicas/theme_menu_bass_1.mp3" % JanSys.getFilePath())
				self.RAW_THEME_MUSIC.play("repeat")

				while self.RAW_THEME_MUSIC.whilePlay():					
					"""	Enquanto a musica passa."""

					if self.RAW_GAME_PRESS_INIT:
						self.GamePress()

					if self.RAW_GAME_MENU_INIT:
						self.MainMenu() 

					if self.RAW_START_GAME_MENU_INIT:
						self.StartGameMenu()
		
					if self.RAW_LOAD_GAME_MENU_INIT:
						self.LoadGameMenu()

					if self.RAW_CONFIGURACOES_GAME_MENU_INIT:
						self.ConfigGameMenu()

					if self.RAW_CONFIGURACOES_VIDEO_GAME_MENU_INIT:
						self.ConfigVideoMenu()
				
					if self.RAW_EXIT_GAME:
						sys.exit()

		pass

	def Log1(self):
		try:
			"""
			Por (GoT)Sr_Rina #8637 - Discord.

			- Em si, esse metodo e diferente dos outros demais, ou seja
			o loop, fica fora dos eventos, Isso e para conseguir esperar
			usando wait(setWaitFor).
			"""

			def next_log(): self.RAW_GAME_LOG_1_INIT=False; self.RAW_GAME_LOG_2_INIT=True

			# Carregar buffers:
			loader.loadBuffers()

			self.RAW_GAME_LOG_1.render()

			# Entrada:
			if self.RAW_WINDOW_GAME.getTicks() > 6500:
				next_log()

			# Eventos:
			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				self.RAW_WINDOW_GAME.accept("KEYUP", "Keys definidas em UP", self.RAW_EVENT_WINDOW, next_log)

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

			# Loop:
			self.RAW_WINDOW_GAME.Loop()
		except:
			raise
		return None

	def Log2(self):
		try:
			"""
			Por (GoT)Sr_Rina #8637 - Discord.

			- Em si, esse metodo e diferente dos outros demais, ou seja
			o loop, fica fora dos eventos, Isso e para conseguir esperar
			usando wait(setWaitFor).
			"""

			def next_press(): self.RAW_GAME_LOG_2_INIT=False; self.RAW_GAME_LOG_INIT=False; self.RAW_GAME_MAIN_MENU_INIT=True; self.RAW_GAME_PRESS_INIT=True

			# Carregar buffers:
			loader.loadBuffers()

			self.RAW_GAME_LOG_2.render()

			# Entrada:
			if self.RAW_WINDOW_GAME.getTicks() > 10000:
				next_press()

			# Eventos:
			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				self.RAW_WINDOW_GAME.accept("KEYUP", "Keys definidas em UP", self.RAW_EVENT_WINDOW, next_press)

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

			# Loop:
			self.RAW_WINDOW_GAME.Loop()
		except:
			raise
		return None

	def GamePress(self):
		try:
			def next_menu(): self.RAW_GAME_PRESS_INIT=False; self.RAW_GAME_MENU_INIT=True

			# Carregar buffers:
			loader.loadBuffers()

			self.RAW_GAME_PRESS.render()

			# Eventos:
			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				self.RAW_WINDOW_GAME.accept("KEYUP", "Keys definidas em UP", self.RAW_EVENT_WINDOW, next_menu)

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

			# Loop:
			self.RAW_WINDOW_GAME.Loop()
		except:
			raise
		return None

	def MainMenu(self):
		try:
			"""
			Por (GoT)Sr_Rina #8637 - Discord.

			- Em si, esse metodo e diferente dos outros acima, ou seja
			o loop, fica dentro dos eventos, isso e para conseguir alinhar
			os efeitos dentro dos eventos.
			"""

			def start(): self.RAW_GAME_MENU_INIT=False; self.RAW_START_GAME_MENU_INIT=True
			def load(): self.RAW_GAME_MENU_INIT=False; self.RAW_LOAD_GAME_MENU_INIT=True
			def settings(): self.RAW_GAME_MENU_INIT=False; self.RAW_CONFIGURACOES_GAME_MENU_INIT=True
			def bye(): self.RAW_GAME_MENU_INIT=False; self.RAW_EXIT_GAME=True

			# Clear Buffers:			
			loader.loadBuffers()

			self.RAW_GAME_MENU.render()
			self.RAW_RANDOM_INFO_VER.render()
			
			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				# Menu CLick:
				self.RAW_GAME_MENU.reparentTo(self.RAW_EVENT_WINDOW, start, load, settings, bye)
	
				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

				# Loop:
				self.RAW_WINDOW_GAME.Loop()
			pass
		except:
			raise
		return None

	def StartGameMenu(self):
		try:
			def game():	self.RAW_START_GAME_MENU_INIT=False; self.RAW_LEVEL_1_INIT=True
			def back():	self.RAW_START_GAME_MENU_INIT=False; self.RAW_GAME_MENU_INIT=True

			# Clear Buffers:			
			loader.loadBuffers()
		
			self.RAW_START_MENU.render()

			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				try:
					self.RAW_START_MENU.reparentTo(self.RAW_EVENT_WINDOW, game, game, game, back)
				except:
					raise

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

				# Loop:
				self.RAW_WINDOW_GAME.Loop()
			pass
		except:
			raise
		return None

	def LoadGameMenu(self):
		try:
			def load_game(): self.RAW_LOAD_GAME_MENU_INIT=False; self.RAW_GAME_MENU_INIT=True
			def back(): self.RAW_LOAD_GAME_MENU_INIT=False; self.RAW_GAME_MENU_INIT=True

			# Carregar buffers:
			loader.loadBuffers()

			self.RAW_LOAD_GAME_MENU.render()

			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				self.RAW_LOAD_GAME_MENU.reparentTo(self.RAW_EVENT_WINDOW, load_game, load_game, load_game, back)

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

				# Loop:
				self.RAW_WINDOW_GAME.Loop()
		except:
			raise
		return None

	def ConfigGameMenu(self):
		try:
			def video(): self.RAW_CONFIGURACOES_GAME_MENU_INIT=False; self.RAW_CONFIGURACOES_VIDEO_GAME_MENU_INIT=True
			def back():  self.RAW_CONFIGURACOES_GAME_MENU_INIT=False; self.RAW_GAME_MENU_INIT=True

			# Carregar buffers:
			loader.loadBuffers()

			self.RAW_CONFIGURACOES_GAME_MENU.render()

			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				self.RAW_CONFIGURACOES_GAME_MENU.reparentTo(self.RAW_EVENT_WINDOW, None, video, None, back)

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

				# Loop:
				self.RAW_WINDOW_GAME.Loop()
		except:
			raise
		return None

	def ConfigVideoMenu(self):
		try:
			def back(): self.RAW_CONFIGURACOES_VIDEO_GAME_MENU_INIT=False; self.RAW_CONFIGURACOES_GAME_MENU_INIT=True

			# Carregar buffers:
			loader.loadBuffers()

			self.RAW_CONFIGURACOES_VIDEO_GAME_MENU.render()

			for self.RAW_EVENT_WINDOW in self.RAW_WINDOW_GAME.event():
				self.RAW_CONFIGURACOES_VIDEO_GAME_MENU.reparentTo(self.RAW_EVENT_WINDOW, back)

				# Debug:
				self.RAW_WINDOW_GAME.debug(self.RAW_EVENT_WINDOW)

				# Loop:
				self.RAW_WINDOW_GAME.Loop()
		except:
			raise
		return None

if __name__ == '__main__':
	RAW()
