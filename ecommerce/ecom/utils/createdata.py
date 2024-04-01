import random
from cakes.models import Cake
from django.core.management.base import BaseCommand
from faker import Faker


fake = Faker()

def populate(value):
    for i in range(value):
        weight = random.randint(100, 1000)
        name = fake.name()
        description = fake.text(max_nb_chars=200)
        price = fake.price(default=0)
        baked_at = fake.date_time().strftime('%H:%M:%S')

        
def main():
    num = int(input("How many records do you want to send: "))
    populate(num)

if __name__ == "__main__":
    main()
