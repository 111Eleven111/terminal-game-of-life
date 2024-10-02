from random import randint
from celle import Celle

class Spillebrett:
	def __init__(self, rader:int, kolonner:int):
		self._rader = rader
		self._kolonner = kolonner
		self._generasjon = 0
		
		self._rutenett = []
		
		teller = 0
		for rad in range(self._rader):
			self._rutenett.append([])
			
			for celle in range(self._kolonner):
				self._rutenett[teller].append(Celle())
			
			teller += 1
		self._generer()

	def tegn_brett(self):
		for ant in range(10):
			print("\n")
		
		for rad in self._rutenett:
			for celle in rad:
				print(celle.hent_status_tegn(), end = "")
				
			print("\n")

	def hent_celle(self, rad, kolonne):
		if (rad in range(self._rader) and 
		kolonne in range(self._kolonner)):
			return self._rutenett[rad][kolonne]
	
		else:
			return None

	def oppdatering(self):
		dod_til_liv = []
		liv_til_dod = []
		
		rad_teller = 0
		for rad in self._rutenett:
			kolonne = 0
			
			for celle in self._rutenett[rad_teller]:
				
				if celle.er_levende():
					liste = self.finn_nabo(rad_teller, kolonne)
					liste = self.finn_levende_naboer(liste)
					if len(liste) < 2:
						liv_til_dod.append(celle)
						
					elif len(liste) > 3:
						liv_til_dod.append(celle)
					
				else:
					liste = self.finn_nabo(rad_teller, kolonne)
					liste = self.finn_levende_naboer(liste)
					if len(liste) == 3:
						dod_til_liv.append(celle)
						
				kolonne += 1
				
			rad_teller += 1
		
		for celle in dod_til_liv:
			celle.sett_levende()
		
		for celle in liv_til_dod:
			celle.sett_dod()
			
		self._generasjon += 1
		self.tegn_brett()
		print(f"Generasjon: {self._generasjon}")

	def finn_levende_naboer(self, naboer:list):
		liste = []
		for celle in naboer:
			if celle and celle.er_levende():
				liste.append(celle)
				
		return liste
	
	def finn_antall_levende(self):
		teller = 0
		for rad in self._rutenett:
			for celle in rad:
				if celle.er_levende():
					teller += 1
					
		return teller

	def finn_nabo(self, rad, kolonne):
		#Nabo format:
		#1 2 3
		#4 c 5
		#6 7 8
		
		nabo1 = self.hent_celle(rad - 1, kolonne - 1)
		nabo2 = self.hent_celle(rad - 1, kolonne)
		nabo3 = self.hent_celle(rad - 1, kolonne + 1)
		nabo4 = self.hent_celle(rad, kolonne - 1)
		nabo5 = self.hent_celle(rad, kolonne + 1)
		nabo6 = self.hent_celle(rad + 1, kolonne - 1)
		nabo7 = self.hent_celle(rad + 1, kolonne)
		nabo8 = self.hent_celle(rad + 1, kolonne + 1)
		
		liste = []
		liste.append(nabo1)
		liste.append(nabo2)
		liste.append(nabo3)
		liste.append(nabo4)
		liste.append(nabo5)
		liste.append(nabo6)
		liste.append(nabo7)
		liste.append(nabo8)
		
		ny_liste = []
		for element in liste:
			if element is not None:
				ny_liste.append(element)
		
		
		return ny_liste

	def _generer(self):
		for rad in range(len(self._rutenett)):
			for celle in self._rutenett[rad]:
				if randint(0, 2) == 0:
					celle.sett_levende()

	def ui(self):
		while input("Skriv ENTER for neste gen\nq for å avslutte -> ").lower() != "q":
			self.oppdatering()
			print(self.finn_antall_levende())
				
brett = Spillebrett(8, 64)
brett.ui()


