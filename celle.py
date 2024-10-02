class Celle:
	# Konstruktør
	def __init__(self):
		self._status = "dod"

	def sett_dod(self):
		self._status = "dod"

	def sett_levende(self):
		self._status = "levende"

	def er_levende(self):
		if self._status == "levende":
			return True
		return False
	
	def hent_status_tegn(self):
		if self._status == "levende":
			return "O"
		return "."
