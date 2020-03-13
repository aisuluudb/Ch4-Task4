# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.

class ContactList():

    def __init__(self, names, contacts):
        self.names = names
        self.contacts = contacts

class List(ContactList):

    def __init__(self):
        self.all_contacts = []

    def search_by_name(self, *name):
        for i in name:
            self.all_contacts.append(i)
        matches_ = set([i for i in self.all_contacts if self.all_contacts.count(i) > 1])
        for match in matches_:
            print("list of matches: ", match)
        

class ContactList(List):
    def __init__(self):
        super().__init__()

my_contacts = ContactList()
my_contacts.search_by_name('lisa', 'kara', 'sarah', 'lisa', 'lyuda', 'sarah', 'larisa')