# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:43:42 2021

@author: paolo
"""
from database import *

user_choice = '''
Press one of the following commands:
a - to add a book
r - to sign a book as read
l - to list all books
d - to delete a book
q - to quit
Your choice: '''

def menu():
    user_input = input(user_choice)
    while (user_input != 'q'):
        
        if(user_input == 'a'):
            prompt_add_book()
            
        elif(user_input == 'l'):
            list_books()
            
        elif(user_input == 'r'):
            prompt_read_book()
        
        elif(user_input == 'd'):
            prompt_delete_book()
        
        else:
            print('please enter a valid input')
            
        user_input = input(user_choice +"\n")
        print("")
        
        
#ask for book name and author to add to our list
def prompt_add_book(): 
    name = input('enter book name: ')
    author = input('enter author name: ')
    #add_book(name, author) # Only RAM
    #add_book_file(name, author) # Only CSV File
    #add_book_file_json(name, author) #Only JSON File
    add_book_sq(name,author)
    
#show all books in the list saved inside the database
def list_books():
    #books = get_all_books() # Only RAM
    #books = get_all_books_from_file() #Only CSV File
    #books = get_all_books_from_file_json() #Only JSON File
    books = get_all_books_sq()
    for book in books:
        #read = 'Yes' if book['read'] == 'Yes' else 'No' # metodo valido per un csv File
        read = 'Yes' if book['read'] else 'No' # metodo valido per JSON File
        print(f"{book['name']} by {book['author']}, read: {book['read']}")

#ask for the book name and change it to read inside our database
def prompt_read_book():    
    name = input('enter book name: ')
    #mark_book_as_read(name) # Only RAM
    #mark_book_as_read_in_file(name) # Only CSV File
    #mark_book_as_read_in_file_json(name) # Only JSON File
    mark_book_as_read_sql(name)

#ask for book name and remove it from the list inside our database
def prompt_delete_book():
    name = input('enter book name: ')
    #delete_book(name) # ONLY RAM
    #delete_book_in_file(name) # Only CSV File
    #delete_book_in_file_json(name) # Only JSON File
    delete_book_sql(name)
    
#create_book_table() #just for the first running
create_book_table_sq()
menu()

#vedere se il libro è già stato inserito    
