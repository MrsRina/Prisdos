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

import math, sys, random, DAT_BIN, re

try:
	from janja2d.core import *
	from janja2d.JanRect import task
except:
	raise
pass

class MAIN_MENU(object):
	MAIN_BUTTON_COMECAR_DOWN=None
	MAIN_BUTTON_CARREGAR_DOWN=None
	MAIN_BUTTON_CONFIGURACOES_DOWN=None
	MAIN_BUTTON_SAIR_DOWN=None

	MAIN_BUTTON_COMECAR_PASS=None
	MAIN_BUTTON_CARREGAR_PASS=None
	MAIN_BUTTON_CONFIGURACOES_PASS=None
	MAIN_BUTTON_SAIR_PASS=None

	MAIN_FONT=None
	MAIN_BACKGROUND_IMAGE_BORDE=None

	MAIN_PACK=None

	MAIN_BUTTON_COMECAR_CLICK=None
	MAIN_BUTTON_CARREGAR_CLICK=None
	MAIN_BUTTON_CONFIGURACOES_CLICK=None
	MAIN_BUTTON_SAIR_CLICK=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self):
		try:
			# Carregar Caminhos:
			self.MAIN_BACKGROUND_IMAGE_BORDE=loader.loadImage("Data/Scripts/Texturas/Gui/janela_nua.png")
			self.MAIN_BUTTON_COMECAR_DOWN=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_começar_down.png")
			self.MAIN_BUTTON_CARREGAR_DOWN=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_carregar_down.png")
			self.MAIN_BUTTON_CONFIGURACOES_DOWN=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_configurações_down.png")
			self.MAIN_BUTTON_SAIR_DOWN=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_sair_down.png")

			self.MAIN_BUTTON_COMECAR_PASS=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_começar_down.png")
			self.MAIN_BUTTON_CARREGAR_PASS=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_carregar_down.png")
			self.MAIN_BUTTON_CONFIGURACOES_PASS=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_configurações_down.png")
			self.MAIN_BUTTON_SAIR_PASS=loader.loadImage("Data/Scripts/Texturas/Gui/MenuPrincipal/botão_sair_down.png")

			# Posicao:	
			self.MAIN_BUTTON_COMECAR_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_COMECAR_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 520))
			self.MAIN_BUTTON_CARREGAR_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_CARREGAR_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 395))
			self.MAIN_BUTTON_CONFIGURACOES_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_CONFIGURACOES_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 270))
			self.MAIN_BUTTON_SAIR_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_SAIR_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 145))

			self.MAIN_BUTTON_COMECAR_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_COMECAR_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 520))
			self.MAIN_BUTTON_CARREGAR_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_CARREGAR_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 395))
			self.MAIN_BUTTON_CONFIGURACOES_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_CONFIGURACOES_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 270))
			self.MAIN_BUTTON_SAIR_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.MAIN_BUTTON_SAIR_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH() - 145))

			# Cor:
			self.MAIN_BUTTON_COMECAR_PASS.setColor(155, 0, 155, 255)
			self.MAIN_BUTTON_CARREGAR_PASS.setColor(155, 0, 155, 255)
			self.MAIN_BUTTON_CONFIGURACOES_PASS.setColor(155, 0, 155, 255)
			self.MAIN_BUTTON_SAIR_PASS.setColor(155, 0, 155, 255)

			# Tamanho:
			self.MAIN_BACKGROUND_IMAGE_BORDE.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())
		except:
			raise
		return None

	def reparentTo(self, event, comecar, carregar, configuracoes, sair):
		try:
			# Comecar:
			self.MAIN_BUTTON_COMECAR_CLICK.makeTask("mouse1", event, comecar)
			self.MAIN_BUTTON_COMECAR_CLICK.makeTask("mouse-motion", event, self.comecar_pass)

			# Carregar:
			self.MAIN_BUTTON_CARREGAR_CLICK.makeTask("mouse1", event, carregar)
			self.MAIN_BUTTON_CARREGAR_CLICK.makeTask("mouse-motion", event, self.carregar_pass)

			# Configuracoes:
			self.MAIN_BUTTON_CONFIGURACOES_CLICK.makeTask("mouse1", event, configuracoes)
			self.MAIN_BUTTON_CONFIGURACOES_CLICK.makeTask("mouse-motion", event, self.configuracoes_pass)

			# Sair:
			self.MAIN_BUTTON_SAIR_CLICK.makeTask("mouse1", event, sair)
			self.MAIN_BUTTON_SAIR_CLICK.makeTask("mouse-motion", event, self.sair_pass)
		except:
			raise
		return None

	def comecar_pass(self):
		try:
			self.MAIN_BUTTON_COMECAR_PASS.renderImage()
		except:
			raise
		return None

	def carregar_pass(self):
		try:
			self.MAIN_BUTTON_CARREGAR_PASS.renderImage()
		except:
			raise
		return None

	def configuracoes_pass(self):
		try:
			self.MAIN_BUTTON_CONFIGURACOES_PASS.renderImage()
		except:
			raise
		return None

	def sair_pass(self):
		try:
			self.MAIN_BUTTON_SAIR_PASS.renderImage()
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.MAIN_BACKGROUND_IMAGE_BORDE.renderImage()
			self.MAIN_BUTTON_COMECAR_DOWN.renderImage()
			self.MAIN_BUTTON_CARREGAR_DOWN.renderImage()
			self.MAIN_BUTTON_CONFIGURACOES_DOWN.renderImage()
			self.MAIN_BUTTON_SAIR_DOWN.renderImage()

			# Adicionar evento click:
			self.MAIN_BUTTON_COMECAR_CLICK=task.taskClick(self.MAIN_BUTTON_COMECAR_DOWN)
			self.MAIN_BUTTON_CARREGAR_CLICK=task.taskClick(self.MAIN_BUTTON_CARREGAR_DOWN)
			self.MAIN_BUTTON_CONFIGURACOES_CLICK=task.taskClick(self.MAIN_BUTTON_CONFIGURACOES_DOWN)
			self.MAIN_BUTTON_SAIR_CLICK=task.taskClick(self.MAIN_BUTTON_SAIR_DOWN)
		except:
			raise
		return None

class COMECAR_GAME_MENU(object):
	JANJA_SURFACE=None

	COMECAR_BACKGROUND_IMAGE=None

	COMECAR_JOGO_1_DOWN=None
	COMECAR_JOGO_2_DOWN=None
	COMECAR_JOGO_3_DOWN=None
	COMECAR_JOGO_VOLTAR_DOWN=None

	COMECAR_JOGO_1_PASS=None
	COMECAR_JOGO_2_PASS=None
	COMECAR_JOGO_3_PASS=None
	COMECAR_JOGO_VOLTAR_PASS=None

	COMECAR_JOGO_1_CLICK_PASS=None
	COMECAR_JOGO_2_CLICK_PASS=None
	COMECAR_JOGO_3_CLICK_PASS=None
	COMECAR_JOGO_VOLTAR_CLICK_PASS=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self, surface):
		try:
			self.JANJA_SURFACE=surface

			# Paths:
			self.COMECAR_BACKGROUND_IMAGE=loader.loadImage("Data/Scripts/Texturas/Gui/janela_nua.png")

			self.COMECAR_JOGO_1_DOWN=loader.loadText(surface, "Jogo1", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.COMECAR_JOGO_2_DOWN=loader.loadText(surface, "Jogo2", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.COMECAR_JOGO_3_DOWN=loader.loadText(surface, "Jogo3", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.COMECAR_JOGO_VOLTAR_DOWN=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=46, color=(155, 0, 155, 0))

			self.COMECAR_JOGO_1_PASS=loader.loadText(surface, "Jogo1", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.COMECAR_JOGO_2_PASS=loader.loadText(surface, "Jogo2", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.COMECAR_JOGO_3_PASS=loader.loadText(surface, "Jogo3", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.COMECAR_JOGO_VOLTAR_PASS=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=46, color=(255, 0, 255, 0))

			# Size:
			self.COMECAR_BACKGROUND_IMAGE.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())

			# Pos:
			self.COMECAR_BACKGROUND_IMAGE.setPos((0, 0))

			self.COMECAR_JOGO_1_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-410+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.COMECAR_JOGO_2_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-150+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.COMECAR_JOGO_3_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2+110+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.COMECAR_JOGO_VOLTAR_DOWN.setPos((10, 10))

			self.COMECAR_JOGO_1_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-410+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.COMECAR_JOGO_2_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-150+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.COMECAR_JOGO_3_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2+110+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.COMECAR_JOGO_VOLTAR_PASS.setPos((10, 10))
		except:
			raise
		return None

	def reparentTo(self, event, cmd_1, cmd_2, cmd_3 ,cmd_4):
		try:
			# pass:
			self.COMECAR_JOGO_1_CLICK_PASS.makeTask("mouse-motion", event, self.effect_jogo_1)
			self.COMECAR_JOGO_2_CLICK_PASS.makeTask("mouse-motion", event, self.effect_jogo_2)
			self.COMECAR_JOGO_3_CLICK_PASS.makeTask("mouse-motion", event, self.effect_jogo_3)
			self.COMECAR_JOGO_VOLTAR_CLICK_PASS.makeTask("mouse-motion", event, self.effect_voltar)

			# Comandos:
			self.COMECAR_JOGO_1_CLICK_PASS.makeTask("mouse1", event, cmd_1)
			self.COMECAR_JOGO_2_CLICK_PASS.makeTask("mouse1", event, cmd_2)
			self.COMECAR_JOGO_3_CLICK_PASS.makeTask("mouse1", event, cmd_3)
			self.COMECAR_JOGO_VOLTAR_CLICK_PASS.makeTask("mouse1", event, cmd_4)
		except:
			raise
		return None

	def effect_jogo_1(self):
		try:
			self.COMECAR_JOGO_1_PASS.renderText()
		except:
			raise
		return None

	def effect_jogo_2(self):
		try:
			self.COMECAR_JOGO_2_PASS.renderText()
		except:
			raise
		return None

	def effect_jogo_3(self):
		try:
			self.COMECAR_JOGO_3_PASS.renderText()
		except:
			raise
		return None

	def effect_voltar(self):
		try:
			self.COMECAR_JOGO_VOLTAR_PASS.renderText()
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.COMECAR_BACKGROUND_IMAGE.renderImage()

			self.COMECAR_JOGO_1_DOWN.renderText()
			self.COMECAR_JOGO_2_DOWN.renderText()
			self.COMECAR_JOGO_3_DOWN.renderText()
			self.COMECAR_JOGO_VOLTAR_DOWN.renderText()

			# Add Clicks:
			self.COMECAR_JOGO_1_CLICK_PASS=task.taskClick(self.COMECAR_JOGO_1_DOWN)
			self.COMECAR_JOGO_2_CLICK_PASS=task.taskClick(self.COMECAR_JOGO_2_DOWN)
			self.COMECAR_JOGO_3_CLICK_PASS=task.taskClick(self.COMECAR_JOGO_3_DOWN)
			self.COMECAR_JOGO_VOLTAR_CLICK_PASS=task.taskClick(self.COMECAR_JOGO_VOLTAR_DOWN)
		except:
			raise
		return None

class CARREGAR_GAME_MENU(object):
	CARREGAR_BACKGROUND_IMAGE=None

	CARREGAR_JOGO_1_DOWN=None
	CARREGAR_JOGO_2_DOWN=None
	CARREGAR_JOGO_3_DOWN=None
	CARREGAR_VOLTAR_DOWN=None

	CARREGAR_JOGO_1_PASS=None
	CARREGAR_JOGO_2_PASS=None
	CARREGAR_JOGO_3_PASS=None
	CARREGAR_VOLTAR_PASS=None

	CARREGAR_JOGO_1_CLICK=None
	CARREGAR_JOGO_2_CLICK=None
	CARREGAR_JOGO_3_CLICK=None

	JANJA_SURFACE=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self, surface):
		try:
			self.JANJA_SURFACE=surface

			# Paths:
			self.CARREGAR_BACKGROUND_IMAGE=loader.loadImage("Data/Scripts/Texturas/Gui/janela_nua.png")

			self.CARREGAR_JOGO_1_DOWN=loader.loadText(surface, "Jogo1", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.CARREGAR_JOGO_2_DOWN=loader.loadText(surface, "Jogo2", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.CARREGAR_JOGO_3_DOWN=loader.loadText(surface, "Jogo3", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.CARREGAR_VOLTAR_DOWN=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=46, color=(155, 0, 155, 0))
		
			self.CARREGAR_JOGO_1_PASS=loader.loadText(surface, "Jogo1", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.CARREGAR_JOGO_2_PASS=loader.loadText(surface, "Jogo2", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.CARREGAR_JOGO_3_PASS=loader.loadText(surface, "Jogo3", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.CARREGAR_VOLTAR_PASS=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=46, color=(255, 0, 255, 0))

			# Size:
			self.CARREGAR_BACKGROUND_IMAGE.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())

			# Pos:
			self.CARREGAR_BACKGROUND_IMAGE.setPos((0, 0))

			self.CARREGAR_JOGO_1_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-410+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.CARREGAR_JOGO_2_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-150+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.CARREGAR_JOGO_3_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2+110+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.CARREGAR_VOLTAR_DOWN.setPos((10, 10))

			self.CARREGAR_JOGO_1_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-410+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.CARREGAR_JOGO_2_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-150+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.CARREGAR_JOGO_3_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2+110+25, self.MAIN_BIN_CONFIG.getH()/2+100))
			self.CARREGAR_VOLTAR_PASS.setPos((10, 10))
		except: 
			raise
		return None

	def reparentTo(self, event, LOAD_1, LOAD_2, LOAD_3, back):
		try:
			# Pass:
			self.CARREGAR_JOGO_1_CLICK.makeTask("mouse-motion", event, self.effect_jogo_1)
			self.CARREGAR_JOGO_2_CLICK.makeTask("mouse-motion", event, self.effect_jogo_2)
			self.CARREGAR_JOGO_3_CLICK.makeTask("mouse-motion", event, self.effect_jogo_3)
			self.CARREGAR_VOLTAR_CLICK.makeTask("mouse-motion", event, self.effect_voltar)

			# Click:
			self.CARREGAR_JOGO_1_CLICK.makeTask("mouse1", event, LOAD_1)
			self.CARREGAR_JOGO_2_CLICK.makeTask("mouse1", event, LOAD_2)
			self.CARREGAR_JOGO_3_CLICK.makeTask("mouse1", event, LOAD_3)
			self.CARREGAR_VOLTAR_CLICK.makeTask("mouse1", event, back)
		except:
			raise
		return None

	def effect_jogo_1(self):
		try:
			self.CARREGAR_JOGO_1_PASS.renderText()
		except:
			raise
		return None

	def effect_jogo_2(self):
		try:
			self.CARREGAR_JOGO_2_PASS.renderText()
		except:
			raise
		return None

	def effect_jogo_3(self):
		try:
			self.CARREGAR_JOGO_3_PASS.renderText()
		except:
			raise
		return None

	def effect_voltar(self):
		try:
			self.CARREGAR_VOLTAR_PASS.renderText()
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.CARREGAR_BACKGROUND_IMAGE.renderImage()

			self.CARREGAR_JOGO_1_DOWN.renderText()
			self.CARREGAR_JOGO_2_DOWN.renderText()
			self.CARREGAR_JOGO_3_DOWN.renderText()
			self.CARREGAR_VOLTAR_DOWN.renderText()

			# Add Clicks:
			self.CARREGAR_JOGO_1_CLICK=task.taskClick(self.CARREGAR_JOGO_1_DOWN)
			self.CARREGAR_JOGO_2_CLICK=task.taskClick(self.CARREGAR_JOGO_2_DOWN)
			self.CARREGAR_JOGO_3_CLICK=task.taskClick(self.CARREGAR_JOGO_3_DOWN)
			self.CARREGAR_VOLTAR_CLICK=task.taskClick(self.CARREGAR_VOLTAR_DOWN)
		except:
			raise
		return None

class CONFIG_GAME_MENU(object):
	CONFIG_BACKGROUND_IMAGE=None

	CONFIG_GAME_DOWN=None
	CONFIG_VIDEO_DOWN=None
	CONFIG_SOM_DOWN=None

	CONFIG_VOLTAR_DOWN=None

	CONFIG_GAME_PASS=None
	CONFIG_VIDEO_PASS=None
	CONFIG_SOM_PASS=None

	CONFIG_VOLTAR_PASS=None

	CONFIG_GAME_CLICK=None
	CONFIG_VIDEO_CLICK=None
	CONFIG_SOM_CLICK=None

	CONFIG_VOLTAR_CLICK=None

	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self, surface):
		try:
			# Paths:
			self.CONFIG_BACKGROUND_IMAGE=loader.loadImage("Data/Scripts/Texturas/Gui/janela_nua.png")

			# Textos:
			self.CONFIG_GAME_DOWN=loader.loadText(surface, "Jogo", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.CONFIG_VIDEO_DOWN=loader.loadText(surface, "Video", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.CONFIG_SOM_DOWN=loader.loadText(surface, "Som", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(155, 0, 155, 0))
			self.CONFIG_VOLTAR_DOWN=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=56, color=(155, 0, 155, 0))

			self.CONFIG_GAME_PASS=loader.loadText(surface, "Jogo", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.CONFIG_VIDEO_PASS=loader.loadText(surface, "Video", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.CONFIG_SOM_PASS=loader.loadText(surface, "Som", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=78, color=(255, 0, 255, 0))
			self.CONFIG_VOLTAR_PASS=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=56, color=(255, 0, 255, 0))
			
			# Size:
			self.CONFIG_BACKGROUND_IMAGE.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())

			# Pos:
			self.CONFIG_GAME_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.CONFIG_GAME_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2-125))
			self.CONFIG_VIDEO_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.CONFIG_VIDEO_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2-25))
			self.CONFIG_SOM_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.CONFIG_SOM_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2+75))
			self.CONFIG_VOLTAR_DOWN.setPos((10, 10))

			self.CONFIG_GAME_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.CONFIG_GAME_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2-125))
			self.CONFIG_VIDEO_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.CONFIG_VIDEO_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2-25))
			self.CONFIG_SOM_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.CONFIG_SOM_PASS.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2+75))
			self.CONFIG_VOLTAR_PASS.setPos((10, 10))

		except:
			raise
		return None

	def reparentTo(self, event, game, video, som, back):
		try:
			# Pass:
			self.CONFIG_GAME_CLICK.makeTask("mouse-motion", event, self.effect_game)
			self.CONFIG_VIDEO_CLICK.makeTask("mouse-motion", event, self.effect_video)
			self.CONFIG_SOM_CLICK.makeTask("mouse-motion", event, self.effect_som)
			self.CONFIG_VOLTAR_CLICK.makeTask("mouse-motion", event, self.effect_voltar)

			# Cmd:
			self.CONFIG_GAME_CLICK.makeTask("mouse1", event, game)
			self.CONFIG_VIDEO_CLICK.makeTask("mouse1", event, video)
			self.CONFIG_SOM_CLICK.makeTask("mouse1", event, som)
			self.CONFIG_VOLTAR_CLICK.makeTask("mouse1", event, back)
		except:
			raise
		return None

	def effect_game(self):
		try:
			self.CONFIG_GAME_PASS.renderText()
		except:
			raise
		return None

	def effect_video(self):
		try:
			self.CONFIG_VIDEO_PASS.renderText()
		except:
			raise
		return None

	def effect_som(self):
		try:
			self.CONFIG_SOM_PASS.renderText()
		except:
			raise
		return None

	def effect_voltar(self):
		try:
			self.CONFIG_VOLTAR_PASS.renderText()
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.CONFIG_BACKGROUND_IMAGE.renderImage()

			self.CONFIG_GAME_DOWN.renderText()
			self.CONFIG_VIDEO_DOWN.renderText()
			self.CONFIG_SOM_DOWN.renderText()
			self.CONFIG_VOLTAR_DOWN.renderText()

			# Clicks:
			self.CONFIG_GAME_CLICK=task.taskClick(self.CONFIG_GAME_DOWN)
			self.CONFIG_VIDEO_CLICK=task.taskClick(self.CONFIG_VIDEO_DOWN)
			self.CONFIG_SOM_CLICK=task.taskClick(self.CONFIG_SOM_DOWN)
			self.CONFIG_VOLTAR_CLICK=task.taskClick(self.CONFIG_VOLTAR_DOWN)
		except:
			raise
		return None

class CONFIG_VIDEO_GAME_MENU(object):
	VIDEO_BACKGROUND_IMAGE=None

	VIDEO_RESOLUTION_TEXT=None
	VIDEO_FULLSCREEN_TEXT=None

	VIDEO_VSYNC_TEXT=None
	
	VIDEO_RESOLUTION_DOWN=None
	VIDEO_FULLSCREEN_DOWN=None

	VIDEO_VSYNC_DOWN=None
	VIDEO_SALVAR_DOWN=None

	VIDEO_CANCELAR_DOWN=None
	VIDEO_OK_DOWN=None

	VIDEO_VOLTAR_DOWN=None

	VIDEO_RESOLUTION_PASS=None
	VIDEO_FULLSCREEN_PASS=None

	VIDEO_VSYNC_PASS=None
	VIDEO_SALVAR_PASS=None

	VIDEO_CANCELAR_PASS=None
	VIDEO_OK_PASS=None

	VIDEO_VOLTAR_PASS=None

	VIDEO_RESOLUTION_CLICK=None
	VIDEO_FULLSCREEN_CLICK=None

	VIDEO_VSYNC_CLICK=None
	VIDEO_SALVAR_CLICK=None

	VIDEO_CANCELAR_CLICK=None
	VIDEO_OK_CLICK=None
	VIDEO_VOLTAR_CLICK=None

	VIDEO_RESOLUTION_SAVED_LIST=None
	VIDEO_RESOLUTION_CONVERTED_LIST=None

	VIDEO_LOADED_SOME_CHANGE_CANCELAR=False

	VIDEO_LOADED_SOME_CHANGE_OK=False

	VIDEO_RSOLUTION_SAVED=None

	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	W, H=MAIN_BIN_CONFIG.getW(), MAIN_BIN_CONFIG.getH()

	def __init__(self, surface):
		try:
			# Cache:
			self.surface_cache=surface

			# Paths:
			self.VIDEO_BACKGROUND_IMAGE=loader.loadImage("Data/Scripts/Texturas/Gui/janela_nua.png")

			# Text:
			self.VIDEO_RESOLUTION_TEXT=loader.loadText(surface, "Resolução", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
			self.VIDEO_FULLSCREEN_TEXT=loader.loadText(surface, "Tela cheia", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
			self.VIDEO_VSYNC_TEXT=loader.loadText(surface, "V-Sync", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
		
			self.VIDEO_RESOLUTION_DOWN=loader.loadText(surface, "%d x %d" % (self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH()), font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
			self.VIDEO_FULLSCREEN_DOWN=loader.loadText(surface, "Ligado" if self.MAIN_BIN_CONFIG.getF() else "Desligado", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
			self.VIDEO_VSYNC_DOWN=loader.loadText(surface, "60" if self.MAIN_BIN_CONFIG.getD() == 60 else "30", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
			
			self.VIDEO_CANCELAR_DOWN=loader.loadText(surface, "Cancelar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))
			self.VIDEO_OK_DOWN=loader.loadText(surface, "Ok", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(155, 0, 155, 0))

			self.VIDEO_VOLTAR_DOWN=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=56, color=(155, 0, 155, 0))

			self.VIDEO_RESOLUTION_PASS=loader.loadText(surface, self.VIDEO_RESOLUTION_DOWN.getText(), font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(255, 0, 255, 0))
			self.VIDEO_FULLSCREEN_PASS=loader.loadText(surface, self.VIDEO_FULLSCREEN_DOWN.getText(), font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(255, 0, 255, 0))
			self.VIDEO_VSYNC_PASS=loader.loadText(surface, self.VIDEO_VSYNC_DOWN.getText(), font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(255, 0, 255, 0))

			self.VIDEO_CANCELAR_PASS=loader.loadText(surface, "Cancelar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(255, 0, 255, 0))
			self.VIDEO_OK_PASS=loader.loadText(surface, self.VIDEO_OK_DOWN.getText(), font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=58, color=(255, 0, 255, 0))	

			self.VIDEO_VOLTAR_PASS=loader.loadText(surface, "Voltar", font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=56, color=(255, 0, 255, 0))

			# Size:
			self.VIDEO_BACKGROUND_IMAGE.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())

			# pos:
			self.VIDEO_VOLTAR_DOWN.setPos((10, 10))

			self.VIDEO_RESOLUTION_TEXT.setPos((self.VIDEO_VOLTAR_DOWN.getX()+self.VIDEO_VOLTAR_DOWN.getWidth()+10, 100))

			self.VIDEO_RESOLUTION_DOWN.setPos((self.VIDEO_RESOLUTION_TEXT.getX(), self.VIDEO_RESOLUTION_TEXT.getY()+self.VIDEO_RESOLUTION_DOWN.getHeight()+50))
			
			self.VIDEO_RESOLUTION_PASS.setPos((self.VIDEO_RESOLUTION_TEXT.getX(), self.VIDEO_RESOLUTION_TEXT.getY()+self.VIDEO_RESOLUTION_DOWN.getHeight()+50))
		
			self.VIDEO_FULLSCREEN_TEXT.setPos((self.VIDEO_RESOLUTION_TEXT.getX()+self.VIDEO_FULLSCREEN_TEXT.getWidth()+100, self.VIDEO_RESOLUTION_TEXT.getY()))

			self.VIDEO_FULLSCREEN_DOWN.setPos((self.VIDEO_FULLSCREEN_TEXT.getX(), self.VIDEO_FULLSCREEN_TEXT.getY()+self.VIDEO_FULLSCREEN_DOWN.getHeight()+50))

			self.VIDEO_FULLSCREEN_PASS.setPos((self.VIDEO_FULLSCREEN_TEXT.getX(), self.VIDEO_FULLSCREEN_TEXT.getY()+self.VIDEO_FULLSCREEN_DOWN.getHeight()+50))

			self.VIDEO_OK_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()-self.VIDEO_OK_DOWN.getWidth()-50, self.MAIN_BIN_CONFIG.getH()-self.VIDEO_OK_DOWN.getHeight()-50))
			self.VIDEO_CANCELAR_DOWN.setPos((self.VIDEO_OK_DOWN.getX()-self.VIDEO_CANCELAR_DOWN.getWidth()-50, self.VIDEO_OK_DOWN.getY()))

			self.VIDEO_VSYNC_TEXT.setPos((self.VIDEO_FULLSCREEN_TEXT.getX()+self.VIDEO_VSYNC_TEXT.getWidth()+150, self.VIDEO_FULLSCREEN_TEXT.getY()))

			self.VIDEO_VSYNC_DOWN.setPos((self.VIDEO_VSYNC_TEXT.getX(), self.VIDEO_VSYNC_TEXT.getY()+self.VIDEO_VSYNC_DOWN.getHeight()+50))

			self.VIDEO_VOLTAR_PASS.setPos((10, 10))

			self.VIDEO_VSYNC_PASS.setPos((self.VIDEO_VSYNC_TEXT.getX(), self.VIDEO_VSYNC_TEXT.getY()+self.VIDEO_VSYNC_DOWN.getHeight()+50))

			self.VIDEO_OK_PASS.setPos((self.MAIN_BIN_CONFIG.getW()-self.VIDEO_OK_DOWN.getWidth()-50, self.MAIN_BIN_CONFIG.getH()-self.VIDEO_OK_DOWN.getHeight()-50))
			self.VIDEO_CANCELAR_PASS.setPos((self.VIDEO_OK_DOWN.getX()-self.VIDEO_CANCELAR_DOWN.getWidth()-50, self.VIDEO_OK_DOWN.getY()))
		except:
			raise
		return None

	def reparentTo(self, event, back):
		try:
			# Pass:
			self.VIDEO_RESOLUTION_CLICK.makeTask("mouse-motion", event, self.effect_resolution)
			self.VIDEO_FULLSCREEN_CLICK.makeTask("mouse-motion", event, self.effect_fullscreen)
			self.VIDEO_VSYNC_CLICK.makeTask("mouse-motion", event, self.effect_vysinc)

			self.VIDEO_VOLTAR_CLICK.makeTask("mouse-motion", event, self.effect_voltar)

			# Click:
			self.VIDEO_RESOLUTION_CLICK.makeTask("mouse1", event, self.change_resolution)
			self.VIDEO_FULLSCREEN_CLICK.makeTask("mouse1", event, self.change_fullscreen)
			self.VIDEO_VSYNC_CLICK.makeTask("mouse1", event, self.change_vsync)

			self.VIDEO_VOLTAR_CLICK.makeTask("mouse1", event, back)

			if self.VIDEO_LOADED_SOME_CHANGE_OK:
				# Clicks:
				self.VIDEO_OK_CLICK=task.taskClick(self.VIDEO_OK_DOWN)
	
				self.VIDEO_OK_CLICK.makeTask("mouse-motion", event, self.effect_ok)

				self.VIDEO_OK_CLICK.makeTask("mouse1", event, self.ok)

			if self.VIDEO_LOADED_SOME_CHANGE_CANCELAR:
				# Clicks:
				self.VIDEO_CANCELAR_CLICK=task.taskClick(self.VIDEO_CANCELAR_DOWN)
				
				self.VIDEO_CANCELAR_CLICK.makeTask("mouse-motion", event, self.effect_cancelar)

				self.VIDEO_CANCELAR_CLICK.makeTask("mouse1", event, self.cancelar)
		except:
			raise
		return None

	def change_resolution(self):
		try:
			self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=True
			self.VIDEO_LOADED_SOME_CHANGE_OK=True

			self.VIDEO_RESOLUTION_LIST=self.surface_cache.getListResolutions() # Obter comando com o cache da surface <0.001b>
			self.VIDEO_RESOLUTION_SAVED_LIST=str(self.VIDEO_RESOLUTION_LIST[random.randint(0, 22)])
			self.VIDEO_RESOLUTION_CONVERTED_LIST=self.VIDEO_RESOLUTION_SAVED_LIST.replace("(", "").replace(",", "").replace(")", "")

			self.VIDEO_RESOLUTION_DOWN.setText(self.VIDEO_RESOLUTION_CONVERTED_LIST)
			self.VIDEO_RESOLUTION_PASS.setText(self.VIDEO_RESOLUTION_DOWN.getText())

			# W, H:
			self.W, self.H=re.findall('\d+', self.VIDEO_RESOLUTION_DOWN.getText())
		except:
			raise
		return None

	def change_fullscreen(self):
		try:
			if self.VIDEO_FULLSCREEN_DOWN.getText() == "Ligado":
				self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=True
				self.VIDEO_LOADED_SOME_CHANGE_OK=True
				self.VIDEO_FULLSCREEN_DOWN.setText("Desligado")
				return self.VIDEO_FULLSCREEN_PASS.setText(self.VIDEO_FULLSCREEN_DOWN.getText())

			elif self.VIDEO_FULLSCREEN_DOWN.getText() == "Desligado":
				self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=True
				self.VIDEO_LOADED_SOME_CHANGE_OK=True
				self.VIDEO_FULLSCREEN_DOWN.setText("Ligado")
				return self.VIDEO_FULLSCREEN_PASS.setText(self.VIDEO_FULLSCREEN_DOWN.getText())
		except:
			raise
		return None

	def change_vsync(self):
		try:
			if self.VIDEO_VSYNC_DOWN.getText() == "60":
				self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=True
				self.VIDEO_LOADED_SOME_CHANGE_OK=True
				self.VIDEO_VSYNC_DOWN.setText("30")
				return self.VIDEO_VSYNC_PASS.setText(self.VIDEO_VSYNC_DOWN.getText())

			elif self.VIDEO_VSYNC_DOWN.getText() == "30":
				self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=True
				self.VIDEO_LOADED_SOME_CHANGE_OK=True
				self.VIDEO_VSYNC_DOWN.setText("60")
				return self.VIDEO_VSYNC_PASS.setText(self.VIDEO_VSYNC_DOWN.getText())
		except:
			raise
		return None

	def ok(self):
		try:
			if self.VIDEO_LOADED_SOME_CHANGE_OK == True:
				self.VIDEO_LOADED_SOME_CHANGE_OK=False
				self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=False

				self.MAIN_BIN_CONFIG.setF(1 if self.VIDEO_FULLSCREEN_DOWN.getText() == "Ligado" else 0)

				self.MAIN_BIN_CONFIG.setD("d"+self.VIDEO_VSYNC_DOWN.getText())
				
				self.VIDEO_RESOLUTION_SAVED_LIST=re.findall('\d+', self.VIDEO_RESOLUTION_DOWN.getText())

				# W, H:
				self.W, self.H=self.VIDEO_RESOLUTION_SAVED_LIST

				self.MAIN_BIN_CONFIG.setW(self.W)
				self.MAIN_BIN_CONFIG.setH(self.H)

				self.VIDEO_LOADED_SOME_CHANGE=False
			pass

		except:
			raise
		return None

	def cancelar(self):
		try:
			"""
			Retorna a tudo denovo.
			"""
			if self.VIDEO_LOADED_SOME_CHANGE_CANCELAR == True:
				self.VIDEO_LOADED_SOME_CHANGE_CANCELAR=False

				self.VIDEO_RESOLUTION_DOWN.setText("%d %d" % (self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH()))
				self.VIDEO_RESOLUTION_PASS.setText(self.VIDEO_RESOLUTION_DOWN.getText())
	
				self.VIDEO_FULLSCREEN_DOWN.setText("Ligado" if self.MAIN_BIN_CONFIG.getF() else "Desligado")
				self.VIDEO_FULLSCREEN_PASS.setText(self.VIDEO_FULLSCREEN_DOWN.getText())
	
				self.VIDEO_VSYNC_DOWN.setText("60" if self.MAIN_BIN_CONFIG.getD() == 60 else "30")
				self.VIDEO_VSYNC_PASS.setText(self.VIDEO_VSYNC_DOWN.getText())
			pass
		except:
			raise
		return None

	def effect_resolution(self):
		try:
			return self.VIDEO_RESOLUTION_PASS.renderText()
		except:
			raise
		return None

	def effect_fullscreen(self):
		try:
			return self.VIDEO_FULLSCREEN_PASS.renderText()
		except:
			raise
		return None

	def effect_vysinc(self):
		try:
			return self.VIDEO_VSYNC_PASS.renderText()
		except:
			raise
		return None

	def effect_ok(self):
		try:
			return self.VIDEO_OK_PASS.renderText()
		except:
			raise
		return None

	def effect_cancelar(self):
		try:
			return self.VIDEO_CANCELAR_PASS.renderText()
		except:
			raise
		return None

	def effect_voltar(self):
		try:
			return self.VIDEO_VOLTAR_PASS.renderText()
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.VIDEO_BACKGROUND_IMAGE.renderImage()

			self.VIDEO_RESOLUTION_TEXT.renderText() # > Texto resolucao.
			self.VIDEO_RESOLUTION_DOWN.renderText() # > Botao resolucao.
			self.VIDEO_FULLSCREEN_TEXT.renderText() # > Texto fullscreen.
			self.VIDEO_FULLSCREEN_DOWN.renderText() # > Botao fullscreen.
			self.VIDEO_VSYNC_TEXT.renderText() # > Texto vsync.
			self.VIDEO_VSYNC_DOWN.renderText() # > Botao vsync

			self.VIDEO_VOLTAR_DOWN.renderText() # > Botao voltar.

			# Clicks:
			self.VIDEO_RESOLUTION_CLICK=task.taskClick(self.VIDEO_RESOLUTION_DOWN)
			self.VIDEO_FULLSCREEN_CLICK=task.taskClick(self.VIDEO_FULLSCREEN_DOWN)
			self.VIDEO_VSYNC_CLICK=task.taskClick(self.VIDEO_VSYNC_DOWN)

			self.VIDEO_VOLTAR_CLICK=task.taskClick(self.VIDEO_VOLTAR_DOWN)

			if self.VIDEO_LOADED_SOME_CHANGE_OK:
				# Render:
				self.VIDEO_OK_DOWN.renderText()

			if self.VIDEO_LOADED_SOME_CHANGE_CANCELAR:				
				# Render:
				self.VIDEO_CANCELAR_DOWN.renderText()

		except:
			raise
		return None

class LOG_1(object):
	LOG_1=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self):
		try:
			# Path:
			self.LOG_1=loader.loadImage("Data/Scripts/Texturas/Logos/CoposLogo.png")

			# Size:
			self.LOG_1.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.LOG_1.renderImage()
		except:
			raise
		return None

class LOG_2(object):
	LOG_2=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self):
		try:
			# Path:
			self.LOG_2=loader.loadImage("Data/Scripts/Texturas/Logos/WksLogo.png")

			# Size:
			self.LOG_2.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.LOG_2.renderImage()
		except:
			raise
		return None

class GAME_PRESS(object):
	PRESS_BACKGROUND_IMAGE=None

	PRESS_TEXT_DOWN=None

	PRESS_TEXT_PASS=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self, surface):
		try:
			# Paths:
			self.PRESS_BACKGROUND_IMAGE=loader.loadImage("Data/Scripts/Texturas/Gui/janela_nua.png")

			self.PRESS_TEXT_DOWN=loader.loadText(surface, "Aperte duas vezes qualquer tecla para continuar",
												 font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", 
												 size=46, color=(155, 0, 155, 0))

			self.PRESS_TEXT_PASS=loader.loadText(surface, "Aperte duas vezes qualquer tecla para continuar",
												 font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", 
												 size=46, color=(255, 0, 255, 0))

			# Size:
			self.PRESS_BACKGROUND_IMAGE.setSize(self.MAIN_BIN_CONFIG.getW(), self.MAIN_BIN_CONFIG.getH())

			# Pos:
			self.PRESS_TEXT_DOWN.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.PRESS_TEXT_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2+200))

			self.PRESS_TEXT_PASS.setPos((self.MAIN_BIN_CONFIG.getW()/2-self.PRESS_TEXT_DOWN.getWidth()/2, self.MAIN_BIN_CONFIG.getH()/2+200))
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.PRESS_BACKGROUND_IMAGE.renderImage()

			self.PRESS_TEXT_DOWN.renderText()
		except:
			raise
		return None

class INFO_VER(object):
	VER_TEXT=None

	# Carregar configuracao:
	MAIN_BIN_CONFIG=DAT_BIN.LOAD_BIN_CONFIG()

	def __init__(self, surface, version):
		try:
			# Paths:
			self.VER_TEXT=loader.loadText(surface, version, font="Data/Scripts/Texturas/Gui/Fontes/Bad_Signal.otf", size=26, color=(155, 0, 155, 0))

			# Pos:
			self.VER_TEXT.setPos((self.MAIN_BIN_CONFIG.getW()-self.VER_TEXT.getWidth()-20, self.MAIN_BIN_CONFIG.getH()-self.VER_TEXT.getHeight()-10))
		except:
			raise
		return None

	def render(self):
		try:
			# Render:
			self.VER_TEXT.renderText()
		except:
			raise
		return None
