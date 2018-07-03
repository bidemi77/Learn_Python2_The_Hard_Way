class Song(object):

    def __init__(self,lyrics):
	    self.lyrics=lyrics


    def sing_me_a_song(self):
		for line in self.lyrics:
			print line 

happy_bday = Song(["Happy birthday to you",
	              "I don't want to get sued",
	              "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
	                   "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class Car(object):

	def __init__(self, models):
		self.models = models

	def make_an_electric_car(self):
		for line in self.models:
			print line 

tesla = Car(["This is the very first electric car made in United States."])

ford  = Car(["This is not an electric car but it was made in Detroit."])

tesla.make_an_electric_car()
ford.make_an_electric_car()



