import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','agrowhizz.settings')

import django
# Import settings
django.setup()

import random
from blog.models import Post
from boards.models import Board, Topic
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone

fakegen = Faker()

def populateBlog(N):
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

        # Create new Post Entry
        post = Post.objects.get_or_create(author= fake_author,
                                          title =fake_title,
                                          text=fake_text,
                                          created_date=created_date,
                                          published_date =published_date)[0]


def populateBoard(N):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.text(max_nb_chars=20, ext_word_list=None)
        fake_description= fakegen.text(max_nb_chars=40, ext_word_list=None)
        

        # Create new Post Entry
        board = Board.objects.get_or_create(name= fake_name,
                                          description =fake_description)[0]



def populateBoardTopic(N):
    '''
    Create N Entries of Dates Accessed
    '''
    board = Board.objects.all()
    for entry in range(N):

        def add_board():
            t = Board.objects.get_or_create(name=random.choice(board))[0]
            t.save()
            return t

        # Create Fake Data for Topic entry
        id = random.randint(1,4)
        fake_starter = User.objects.get(id=id)
        fake_board = add_board()
        fake_subject= fakegen.text(max_nb_chars=20, ext_word_list=None)
        last_updated = timezone.now()

        # Create new Topic for Entry
        topic = Topic.objects.get_or_create(subject= fake_subject,
                                          last_updated = last_updated,
                                          board = fake_board,
                                          starter = fake_starter)[0]

if __name__ == '__main__':
    
    print("Populating the Blog...Please Wait")
    populateBlog(int(input("How many Blog you want to create? ")))
    print('Populating Blog Complete')
    print('')
    print('*************************************')
    print("Populating the Board...Please Wait")
    populateBoard(int(input("How many Board you want to create? ")))
    print('Populating Board Complete')
    print('')
    print('*************************************')
    print("Populating the Board Topics...Please Wait")
    populateBoardTopic(int(input("How many Board Topics you want to create? ")))
    print('Populating Board Topics Complete')
    print('')
    print('*************************************')
    print('Populating Complete')