import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','agrowhizz.settings')

import django
# Import settings
django.setup()

import random
from blog.models import Post
from boards.models import Board, Topic, Post
from agrodata.models import Database, Company, CompanyAddress, CompanyLogo
from agrodata.models import IngredientsCategories, Ingredients, IngredientDetail, ProductPhysicalProperty, ProductPicture
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone

fakegen = Faker()

# Create Fake Data for the blog App
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


# Create Fake Data for the board App
# *************************************************
def populateBoard(N):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.text(max_nb_chars=20, ext_word_list=None)
        fake_description= fakegen.text(max_nb_chars=40, ext_word_list=None)
        

        # Create new board Entry
        board = Board.objects.get_or_create(name= fake_name,
                                          description =fake_description)[0]


# Create Fake Data for the board App of The Board topic
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

# Create Fake Data for the board App of The Board post
def populateBoardPost(N):
    '''
    Create N Entries of Dates Accessed
    '''

    topic = Topic.objects.all()
    for entry in range(N):

        def add_topic():
            t = Topic.objects.get_or_create(subject=random.choice(topic))[0]
            t.save()
            return t

        # Create Fake Data for Post entry
        id = random.randint(1,4)
        fake_topic = add_topic()
        fake_message= fakegen.text(max_nb_chars=200, ext_word_list=None)
        created_at = timezone.now()
        updated_at = timezone.now()
        created_by = User.objects.get(id=id)
        updated_by = User.objects.get(id=id)

        # Create new Post for Entry
        post = Post.objects.get_or_create(message= fake_message,
                                          topic = fake_topic,
                                          created_at = created_at,
                                          updated_at = updated_at,
                                          created_by = created_by,
                                          updated_by = updated_by)[0]


# Populating Databas model in Agrodata App
# *************************************************

def populateAgrodataDatabase(N):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.text(max_nb_chars=20, ext_word_list=None)
        fake_description= fakegen.text(max_nb_chars=40, ext_word_list=None)
        

        # Create new Post Entry
        database = Database.objects.get_or_create(name= fake_name,
                                                  description =fake_description)[0]


# Populating Company model in Agrodat App for company

def populateAgrodataCompany(N):
    '''
    Create N Entries of Data Accessed
    '''

    database = Database.objects.all()
    for entry in range(N):

        def add_database():
            t = Database.objects.get_or_create(name=random.choice(database))[0]
            t.save()
            return t

        # Create Fake Data for Company entry
        
        fake_database = add_database()
        fake_company_name= fakegen.company()
        fake_profile_description= fakegen.text(max_nb_chars=90, ext_word_list=None)
        fake_full_description= fakegen.text(max_nb_chars=1500, ext_word_list=None)
        last_updated = timezone.now()

        # Create Fake Data for Company Address entry
        fake_location = fakegen.street_address()
        fake_city = fakegen.city()
        fake_state = fakegen.state()
        fake_country = fakegen.country()
        fake_postal_code = fakegen.postcode()
        fake_fax = fakegen.phone_number()
        fake_telephone = fakegen.phone_number()
        fake_website = fakegen.url()
        fake_twitter = fakegen.url()
        fake_facebook  = fakegen.url()
        fake_linkedin = fakegen.url()
        fake_email = fakegen.ascii_free_email()

        # Create Fake Data for Company Logo entry
        fake_picture = '/media/uploads/CompanyLogos/noimage_AhFphmJ.png'

        # Create new Company for Entry
        company = Company.objects.get_or_create(company_name = fake_company_name,
                                                profile_description = fake_profile_description,
                                                full_description = fake_full_description,
                                                database = fake_database,
                                                last_updated = last_updated)[0]

        # Create new Company Address for Entry
        companyAddress = CompanyAddress.objects.get_or_create(  company_name = company,
                                                                location = fake_location,
                                                                city = fake_city,
                                                                state = fake_state,
                                                                country = fake_country,
                                                                postal_code = fake_postal_code,
                                                                fax = fake_fax,
                                                                telephone = fake_telephone,
                                                                website = fake_website,
                                                                twitter = fake_twitter,
                                                                facebook  = fake_facebook,
                                                                linkedin = fake_linkedin,
                                                                email = fake_email,
                                                                last_updated = last_updated)[0]
        # Create new Company Logo for Entry
        companyLogo = CompanyLogo.objects.get_or_create(company_name = company,
                                                picture = fake_picture,
                                                uploaded_at = last_updated)[0]

# Populating IngredientsCategories model in Agrodat App

def populateAgrodataIngredientsCategories(N):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_category = fakegen.text(max_nb_chars=15, ext_word_list=None)
        
        
        # Create new IngredientsCategories Entry
        ingredientsCategories = IngredientsCategories.objects.get_or_create(category= fake_category)[0]


# Populating Ingredients model in Agrodat App

def populateAgrodataIngredients(N):
    '''
    Create N Entries of Data Accessed
    '''
    company = Company.objects.all()
    ingredientsCategories = IngredientsCategories.objects.all()
    for entry in range(N):

        def add_ingredients():
            t = IngredientsCategories.objects.get_or_create(category=random.choice(ingredientsCategories))[0]
            t.save()
            return t
        
        def add_company():
            t = Company.objects.get_or_create(company_name=random.choice(company))[0]
            t.save()
            return t

        # Create Fake Data for Ingredients entry
        fake_name = fakegen.text(max_nb_chars=15, ext_word_list=None)
        fake_category = add_ingredients()
        fake_company_name = add_company()
        fake_product_code = fakegen.hexify(text="^^^^", upper=False)
        last_updated = timezone.now()

        # Create Fake Data for IngredientDetail entry
        fake_declaration = fakegen.text(max_nb_chars=150, ext_word_list=None)
        fake_usage = fakegen.text(max_nb_chars=150, ext_word_list=None)
        fake_full_description = fakegen.text(max_nb_chars=1500, ext_word_list=None)

        # Create Fake Data for ProductPhysicalProperty entry
        fake_appearance = fakegen.text(max_nb_chars=150, ext_word_list=None)
        fake_Colour = fakegen.text(max_nb_chars=150, ext_word_list=None)
        fake_Taste = fakegen.text(max_nb_chars=150, ext_word_list=None)
        fake_Flavour = fakegen.text(max_nb_chars=150, ext_word_list=None)

        # Create Fake Data for ProductPicture entry
        fake_picture = '/media/uploads/CompanyLogos/noimage_AhFphmJ.png'

        # Create new Ingredients for Entry
        ingredient = Ingredients.objects.get_or_create( name = fake_name,
                                                        category = fake_category,
                                                        company_name = fake_company_name,
                                                        product_code= fake_product_code,
                                                        last_updated = last_updated)[0]
        
        # Create new IngredientDetail for Entry
        ingredientDetail = IngredientDetail.objects.get_or_create(  ingredient_name = ingredient,
                                                                    declaration= fake_declaration,
                                                                    usage= fake_usage,
                                                                    full_description = fake_full_description)[0]


        # Create new ProductPhysicalProperty for Entry
        productPhysicalProperty = ProductPhysicalProperty.objects.get_or_create(ingredient_name = ingredient,
                                                                                appearance = fake_appearance,
                                                                                Colour = fake_Colour,
                                                                                Taste = fake_Taste,
                                                                                Flavour = fake_Flavour)[0]

        
        # Create new ProductPicture for Entry
        productPicture = ProductPicture.objects.get_or_create(ingredient_name = ingredient,
                                                              picture = fake_picture,
                                                              uploaded_at = last_updated)[0]



if __name__ == '__main__':
    
    print("The Blog contains {} data".format(len(Post.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateBlog(int(input("How many Blog you want to create? ")))
        print('Populating Blog Complete')
        print('')
        print('*************************************')
    
    print("The Board contains {} data".format(len(Board.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateBoard(int(input("How many Board you want to create? ")))
        print('Populating Board Complete')
        print('')
        print('*************************************')

    print("The Board Topic contains {} data".format(len(Topic.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateBoardTopic(int(input("How many Board Topic you want to create? ")))
        print('Populating Board Topic Complete')
        print('')
        print('*************************************')
    
    print("The Board Posts contains {} data".format(len(Post.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateBoardPost(int(input("How many Board Posts you want to create? ")))
        print('Populating Board Posts Complete')
        print('')
        print('*************************************')

    print("The Agrodata Database contains {} data".format(len(Database.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateAgrodataDatabase(int(input("How many Agrodata Database you want to create? ")))
        print('Populating Agrodata Database Complete')
        print('')
        print('*************************************')
    
    print("The Agrodata Company contains {} data".format(len(Company.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateAgrodataCompany(int(input("How many Agrodata Company you want to create? ")))
        print('Populating Agrodata Company Complete')
        print('')
        print('*************************************')
    
    print("The Agrodata ingredientsCategories contains {} data".format(len(IngredientsCategories.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateAgrodataIngredientsCategories(int(input("How many Agrodata IngredientsCategories you want to create? ")))
        print('Populating Agrodata IngredientsCategories Complete')
        print('')
        print('*************************************')
    
    print("The Agrodata ingredients contains {} data".format(len(Ingredients.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateAgrodataIngredients(int(input("How many Agrodata Ingredients you want to create? ")))
        print('Populating Agrodata Ingredients Complete')
        print('')
        print('*************************************')

    print('All Populating process is Completed')