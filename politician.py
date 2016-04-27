__author__ = 'Felix'
class Politician:

    politicianCount = 0
    def __init__(self,firstname,lastname,country,mandat):
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.mandat = mandat
        Politician.politicianCount += 1

    def displayPolitician(self):
        print("The Head of State of " + self.country+", " + self.firstname.capitalize()+" "+self.lastname +
        " has been elected for " + str(self.mandat) + " years.")



Obama = Politician("Barack","Obama","USA",4)
Merkel = Politician("Angela","Merkel","Germany",6)
Hollande = Politician("Francois","Hollande","France",5)

Obama.displayPolitician()
Merkel.displayPolitician()

print("Total number of politicians %d" % Politician.politicianCount)