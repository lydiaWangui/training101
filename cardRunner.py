# from classesAndObjects2 import Card
#
# card1 = Card(4500)
# myCard = Card(6000)
# print(card1.balance)
#
# print(card1.withdraw(23000))
# print(card1.balance)


from classes import Library

techCampLib = Library(bks=1000, gen=['Drama','Comedy','Fiction'],mems=['Jed','Sly','paul'])
print(techCampLib.books)
print(techCampLib.genre)
print(techCampLib.members)

techCampLib.lend()

print(techCampLib.books)