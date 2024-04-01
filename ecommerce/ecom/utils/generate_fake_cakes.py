import random
import faker

from cakes.models import Cake


fake = faker.Faker()

CAKE_NAMES = (
    "Napaleon",
    "Amandine",
    "Banana bread",
    "Banana cake",
    "Basbousa",
    "Battenberg cake",
    "Chiffon cake"
)

def _generate_fake_name():
    return random.choice(CAKE_NAMES)

def _generate_fake_description():
    return fake.text(max_nb_chars=200)

def _generate_fake_weight():
    return random.randint(500, 4500)

def _generate_fake_price():
    return random.randint(10, 100)

def _generate_fake_datetime():
    return fake.date_time()


def _create_cake_objects(amount):
    for x in range(amount):
        cake = Cake.objects.create(
            name=_generate_fake_name(),
            description=_generate_fake_description(),
            weight=_generate_fake_weight(),
            price=_generate_fake_price(),
            baked_at=_generate_fake_datetime()
        )


