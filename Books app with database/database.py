# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:43:21 2021

@author: paolo
É possibile considerare questo database come una vera e propria interfaccia in
quanto fa da tramite per la scrittura di dati su un file.
"""

books = []

'''
Saving elements in to RAM. The following instructions only works in short terms 
period because here, the elements we are gonna save, are gonna be destroyed 
after we stop the exectuion
'''

def add_book(name, author):
    books.append({'name' : name, 'author' : author, 'read' : False})

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]
    

# Avrei potuto rimuovere un libro nel seguente modo ma non è 'sicuro' 
# rimuuovere elementi durante l'iterazione.     
# def delete_book(name): 
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)


''' 
CSV file read and writing with format: name, author, read\n
This method can allow us to save for long time period, our info
'''
books_file='books.txt'
def add_book_file(name, author):
    with open(books_file , 'a') as file:
        file.write(f'{name}, {author}, False\n')

def get_all_books_from_file():
    with open(books_file, 'r') as file:
        content = [line.strip().split(',') for line in file.readlines()]
        return [{'name':line[0], 'author':line[1], 'read':line[2]}
                  for line in content
            ]
    
    
def mark_book_as_read_in_file(name): #il seguente non è assolutamente il modo migliore per modificare un file
                                     #sto letteralmente copiado tutti gli elementi e li riscrivo dentro lo stesso file
    books = get_all_books_from_file()
    for book in books:
        if book['name'] == name:
            book['read'] = 'True'
    _save_all_books(books)

def _save_all_books(books): # NOTA: TUTTE LE FUNZIONI CON UN _ DAVANTI, SONO 
                            # PRIVATE FUNCTION, funzioni che non deve esser richiamata 
                            # MAI in altri file
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']}, {book['author']}, {book['read']}\n") 

def delete_book_in_file(name):
    books = get_all_books_from_file()
    books = [book for book in books if book['name']!=name]
    _save_all_books(books)
    
''' 
JSON (Java Script Object Notation) file read and writing with format: {name, 
author, read}\n. We are going to create something similar to a py dictionary.
This method can allow us to save for long time period, our info and use it in
web apps.
Thats what a json file looks like:
    [
     { 'name':'Name f the book'
       'author' : 'Author of the book'
       'read' : True
     }
    ]
'''    
import json

books_json = 'books.json'

def create_book_table():
    with open(books_json, 'w') as file:
        json.dump([], file)  

def add_book_file_json(name, author):
    books = get_all_books_from_file_json()
    books.append({'name' : name, 'author':author, 'read' : False})
    _save_all_books_json(books)
    
def get_all_books_from_file_json():
    with open(books_json, 'r') as file:
        return json.load(file)
    
def _save_all_books_json(books): #private function
    with open(books_json, 'w') as file:
        json.dump(books, file)
    
def mark_book_as_read_in_file_json(name): #il seguente non è assolutamente il modo migliore per modificare un file
                                     #sto letteralmente copiado tutti gli elementi e li riscrivo dentro lo stesso file
    books = get_all_books_from_file_json()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books_json(books)

def delete_book_in_file_json(name):
    books = get_all_books_from_file_json()
    books = [book for book in books if book['name']!=name]
    _save_all_books_json(books)

'''
USING SQLite3 AS DATABASE
'''
import sqlite3

def create_book_table_sq():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read text)')
    
    connection.commit()
    connection.close()

def add_book_sq(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    #cursor.execute(f'INSERT INTO books VALUES("{name}","{author}", "No")')
    cursor.execute('INSERT INTO books VALUES(?,?,"No")',(name, author))
    
    connection.commit()
    connection.close()

def get_all_books_sq():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author':row[1], 'read':row[2]} for row in cursor.fetchall()] #restituisce una lista di tuple [(name, author, read), (name, author, read)]
    
    connection.close()
    return books 

def delete_book_sql(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM books WHERE name=?',(name,))
    
    connection.commit()
    connection.close()

def mark_book_as_read_sql(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('UPDATE books SET read = "Yes" WHERE name=?',(name,))
    
    connection.commit()
    connection.close()

    
    
    