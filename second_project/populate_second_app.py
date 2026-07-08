import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "second_project.settings")


import django
django.setup()


import random
from second_app.models import Topic,webpage,AccessRecord,user
from faker import Faker




fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        fake_first_name=fakegen.first_name()
        fake_last_name=fakegen.last_name()
        fake_email=fakegen.email()


        webpg=webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        usr=user.objects.get_or_create(First_Name=fake_first_name,Last_Name=fake_last_name,Email=fake_email)[0]




        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print("Populating Complete")