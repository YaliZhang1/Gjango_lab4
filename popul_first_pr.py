import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Lab4_project.settings')

import django
django.setup()

from User.models import User
from faker import Faker

fakegen=Faker()
def add_user(N=5):
    fake_firstname = fakegen.unique.first_name()
    fake_lastname = fakegen.unique.last_name()
    fake_email = fakegen.email()
    u = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)

if __name__ == '__main__':
    print("populating script!")
    for _ in range(20):
        add_user(20)
    print("populating complete!")