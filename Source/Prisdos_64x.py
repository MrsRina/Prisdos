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

import subprocess, os


class Launcher_Game:
	def __init__(self):
		try:
			startupinfo = subprocess.STARTUPINFO()
			startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			subprocess.check_call("python Data/Scripts/DAT_RAW.py", startupinfo=startupinfo)
		except:
			raise
		return None
	pass
pass

if __name__ == "__main__":
	Launcher_Game()
