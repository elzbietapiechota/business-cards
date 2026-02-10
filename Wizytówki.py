from faker import Faker
fake = Faker('pl_PL')

class BaseContact:
    
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
       
    def __str__(self):
       return f"{self.first_name} {self.last_name}, {self.email}, {self.phone_number}"
    
    @property
    def length(self):
       return len((f"{self.first_name} {self.last_name}"))
    
    def contact(self):
        return f"Wybieram numer +48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}." 
    
  
class BusinessContact(BaseContact):
   
   def __init__(self, company, job, work_phone_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.company = company
       self.job = job
       self.work_phone_number = work_phone_number
    
   def __str__(self):
       return f"{self.first_name} {self.last_name}, {self.email}, {self.work_phone_number}, {self.company}, {self.job}"
   
   def contact(self):
       return f"Wybieram numer służbowy +48 {self.work_phone_number} i dzwonię do {self.first_name} {self.last_name}."


def create_contacts(card_type, cards_quantity):
    random_contacts = []
    
    for i in range(cards_quantity):
       
        if card_type == BaseContact:
            contact = BaseContact(
                first_name=fake.first_name(), 
                last_name=fake.last_name(), 
                phone_number=fake.phone_number(), 
                email=fake.email())
        
        elif card_type == BusinessContact:
            contact = BusinessContact(
                first_name=fake.first_name(), 
                last_name=fake.last_name(), 
                phone_number=fake.phone_number(), 
                email=fake.email(), 
                company=fake.company(), 
                job=fake.job(), 
                work_phone_number=fake.phone_number())
       
        random_contacts.append(contact)
    return random_contacts

if __name__ == '__main__':
    print("Wizytówki:")
    print()
    generated_cards = create_contacts(BusinessContact, 3)

    for card in generated_cards:
        print(card)
        print(card.contact())
        print(f"Długość znaków imienia i nazwiska wraz ze spacją: {card.length}")
        print()
    




