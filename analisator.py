"""
TODO:
	док-строки, аннотация типов аргументов методов (переменная:str)
	в normalize_words ограничить аргументы, сделать метод top-n (где  n - не больше кол-ва слов)
	в порядке убывания
"""

import re
from collections import Counter
import docx
from docx import Document
import pymorphy2

file_path = "Test_file.txt"
file_d = "Test_docx.docx"


class App:
	def __init__(self, file_path:str):
		self.file_path = file_path

	def make_string_from_file(self):  # Достаём слова из файла
		if self.file_path.endswith(".txt"):
			with open(self.file_path, "r", encoding="utf8") as file:
				self.content = file.read()

		elif self.file_path.endswith(".docx"):
			self.content = docx.Document(self.file_path)

		else:
			self.content = ""

	def make_words_from_text(self): # достаем все русские слова
		self.words = re.findall("[а-яё]+", self.content.lower())
		return self.words

	def normalize_words(self, part_of_speech): # отбирает слова
		morph = pymorphy2.MorphAnalyzer()
		self.normalized_words = list()
		for word in self.words:
			parse = morph.parse(word)[0]
			for part in part_of_speech:
				if part in parse.tag:
					self.normalized_words.append(parse.normal_form)

	def top_n(self, num:int): # находит топ самых популярных слов
		counter = Counter(x for x in self.normalized_words)
		print(counter.most_common(num))


app = App("Test_file.txt")
app.make_string_from_file()
words = app.make_words_from_text()
app.normalize_words(("NOUN", "VERB")
app.top_n(5)
