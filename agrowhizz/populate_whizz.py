import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','agrowhizz.settings')

import django
# Import settings
django.setup()

import random
from blog.models import Post
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        id = random.randint(1,4)
        fake_author = User.objects.get(id=id)
        fake_title = fakegen.text(max_nb_chars=20, ext_word_list=None)
        fake_text= fakegen.text(max_nb_chars=2000, ext_word_list=None)
        created_date = timezone.now()
        published_date = timezone.now()

        # Create new Poat Entry
        post = Post.objects.get_or_create(author= fake_author,
                                          title =fake_title,
                                          text=fake_text,
                                          created_date=created_date,
                                          published_date =published_date)[0]




if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(10)
    print('Populating Complete')