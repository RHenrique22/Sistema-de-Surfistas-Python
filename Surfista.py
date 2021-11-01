from Prancha import *
from Campeonato import *

class Surfista:
	def __init__(self, nome, idade, campeonatos = [], pranchas = []):
		self._nome = str(nome)
		self._idade = int(idade)
		self._campeonatos = campeonatos
		self._pranchas = pranchas

	@property
	def nome_surfista(self):
		return self._nome

	@nome_surfista.setter
	def nome_surfista(self, nome_surfista):
		self._nome = nome_surfista

	@property
	def idade_surfista(self):
		return self._idade

	@idade_surfista.setter
	def idade_surfista(self, idade_surfista):
		self._idade = idade_surfista

	def surfista_camps(self):
		return self._campeonatos

	def prancha_surfista(self):
		return self._pranchas

	def __str__(self):
		return (f'Nome do Surfista: {self._nome}\nIdade do Surfista: {self._idade}'
		f'\nLista de Campeonatos que já participou: {self._campeonatos}'
		f'Listas de Pranchas que possui: {self._pranchas}')