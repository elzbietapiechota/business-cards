from faker import Faker
fake = Faker('pl_PL')

class BusinessCard:
    
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email     
    
    @property
    def length(self):
       return len((f"{self.first_name} {self.last_name}"))

class BaseContact(BusinessCard):
   
   def __init__(self, private_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.private_phone = fake.phone_number()
    
   def contact(self):
       print(f"Wybieram numer +48 {self.private_phone} i dzwonię do {self.first_name} {self.last_name}.")

base_cards = [] 
for card in range(5):
    base_cards.append(BaseContact(
        first_name=fake.first_name(), 
        last_name=fake.last_name(),
        company=fake.company(),
        job=fake.job(), 
        private_phone=fake.phone_number(),
        email=fake.email()))
    
class BusinessContact(BusinessCard):
   
   def __init__(self, work_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.work_phone = fake.phone_number()
    
   def contact(self):
       print(f"Wybieram numer +48 {self.work_phone} i dzwonię do {self.first_name} {self.last_name}.")

business_cards = [] 
for card in range(5):
    business_cards.append(BusinessContact(
        first_name=fake.first_name(), 
        last_name=fake.last_name(), 
        company=fake.company(),
        job=fake.job(),
        email=fake.email(),
        work_phone=fake.phone_number()))

def create_contacts(card_type, cards_quantity):
    random_contacts = []
    
    for i in range(cards_quantity):
       
        if card_type == BaseContact:
            random_contacts.append(BaseContact(        
                first_name=fake.first_name(), 
                last_name=fake.last_name(),
                company=fake.company(),
                job=fake.job(), 
                private_phone=fake.phone_number(),
                email=fake.email()))
        
        elif card_type == BusinessContact:
            random_contacts.append(BusinessContact(
                first_name=fake.first_name(), 
                last_name=fake.last_name(), 
                company=fake.company(),
                job=fake.job(),
                email=fake.email(),
                work_phone=fake.phone_number()))
       
    return random_contacts
            
print("Wizytówki prywatne:")
for card in base_cards:
    card.contact()
    print(f"Długość: {card.length}")
print()

print("Wizytówki służbowe:")
for card in business_cards:
    card.contact()
    print(f"Długość: {card.length}")
print()

print("Wizytówki losowe:")
generated_cards = create_contacts(BaseContact, 2)
for card in generated_cards:
    card.contact()
    print(f"Długość: {card.length}")

