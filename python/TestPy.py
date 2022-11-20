from godot import exposed, export
from godot import *
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


@exposed
class TestPy(Control):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')


	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		print(wikiGoal)
		pass
