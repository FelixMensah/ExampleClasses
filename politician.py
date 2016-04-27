__author__ = 'Felix'


class Politician:
    politicianCount = 0

    def __init__(self, firstname, lastname, country, mandate):
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.mandate = mandate
        Politician.politicianCount += 1

    def displayPolitician(self):
        print("The Head of State of %s, %s %s has been elected for %d years." % (
            self.country, self.firstname, self.lastname, self.mandate))


Obama = Politician("Barack", "Obama", "USA", 4)
Merkel = Politician("Angela", "Merkel", "Germany", 6)
Hollande = Politician("Francois", "Hollande", "France", 5)

Obama.displayPolitician()
Merkel.displayPolitician()

print("Total number of politicians %d" % Politician.politicianCount)
