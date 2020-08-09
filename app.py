#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import os
import sys
from os import system
from sys import platform

con = None

def load_office(con, cur, file_name):
    with open(file_name, 'r') as office:
        counter = 0
        for row in office:
            cur.execute("INSERT OR IGNORE INTO office values (?,?,?)", row.split(","))
            con.commit()
            counter += 1
    print('*** {} Records transferred to office! ***'.format(counter))

def load_managed(con, cur, file_name):
    with open(file_name, 'r') as managed:
        counter = 0
        for row in managed:
            cur.execute("INSERT OR IGNORE INTO managed values (?,?)", row.split(","))
            con.commit()
            counter += 1
    print('*** {} Records transferred to managed! ***'.format(counter))

def load_rental_agreement(con, cur, file_name):
    with open(file_name, 'r') as rental_agreement:
        counter = 0
        for row in rental_agreement:
            cur.execute("INSERT OR IGNORE INTO rental_agreement values (?,?,?)", row.split(","))
            con.commit()
            counter += 1
    print('*** {} Records transferred to rental_agreement! ***'.format(counter))

def load_party(con, cur, file_name):
    with open(file_name, 'r') as party:
        counter = 0
        for row in party:
            cur.execute("INSERT OR IGNORE INTO party values (?,?)", row.split(","))
            con.commit()
            counter += 1
    print('*** {} Records transferred to party! ***'.format(counter))

def load_customer_agency(con, cur, file_name):
    with open(file_name, 'r') as customer_agency:
        counter = 0
        for row in customer_agency:
            cur.execute("INSERT OR IGNORE INTO customer_agency values (?,?,?,?,?)", row.split(","))
            con.commit()
            counter += 1
    print('*** {} Records transferred to customer_agency! ***'.format(counter))

def erase_tables():
    print("erasing tables")

    #connect to the database
    con = lite.connect("soap.db")
    cur = con.cursor()
    cur.execute("DELETE FROM office")
    cur.execute("DELETE FROM managed")
    cur.execute("DELETE FROM rental_agreement")
    cur.execute("DELETE FROM party")
    cur.execute("DELETE FROM customer_agency")
    con.commit()
    con.close()

def main():
    continue_to_run = True
    user_input = 0
    while continue_to_run:
        print("Menu")
        print("1. Run a command")
        print("2. Load a csv file into tables")
        print("3. Erase the tables")
        print("4. Quit")
        user_input = input("What do you wish to do? ")
        while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4':
            print("Menu")
            print("1. Run a command")
            print("2. Load a csv file into tables")
            print("3. Erase the tables")
            print("4. Quit")
            user_input = input("What do you wish to do? ")
        
        if(user_input == '1'):
            try:
                #connect to the database
                con = lite.connect("soap.db")
                cur = con.cursor()
                myStmt = "go"
                #test code
                if platform == "linux" or platform == "darwin":
                    system("clear")
                elif platform == "win32":
                    system("cls")
                #end test code

                while (myStmt != "quit" and myStmt != "q" and myStmt != "exit"):
                    #ask for usr input
                    myStmt = input(">>")
                    if (myStmt != "q" and myStmt != "q" and myStmt != "exit"):
                        cur.execute(myStmt)
                        data = cur.fetchall()
                        print("The results are: ")
                        for rec in data:
                            for field in rec:
                                print(field,"\t",end='')
                            print()
                    print()
                con.commit()
                con.close()

                if platform == "linux" or platform == "darwin":
                    system("clear")
                elif platform == "win32":
                    system("cls")
                #end test code

            except lite.Error as e:
                print("Error %s:" % e.args[0])
                sys.exit(1)

        if(user_input == '2'):
            csv_choice = input("Which csv file would youlike to load?")
            while(os.path.exists(csv_choice) == False):
                csv_choice = input("Invalid input, please try another filename.")

            print("Menu")
            print("1. office")
            print("2. managed")
            print("3. rental_agreement")
            print("4. party")
            print("5. customer_agency")
            table_choice = input("Pick a table for insertion.")
            
            while table_choice != '1' and table_choice != '2' and table_choice != '3' and table_choice != '4' and table_choice != '5':
                print("Menu")
                print("1. office")
                print("2. managed")
                print("3. rental_agreement")
                print("4. party")
                print("5. customer_agency")
                table_choice = input("Invalid input, please try another table.")

            #connect to the database
            con = lite.connect("soap.db")
            cur = con.cursor()

            if(table_choice == '1'):
                load_office(con, cur, csv_choice)
            if(table_choice == '2'):
                load_managed(con, cur, csv_choice)
            if(table_choice == '3'):
                load_rental_agreement(con, cur, csv_choice)
            if(table_choice == '4'):
                load_party(con, cur, csv_choice)
            if(table_choice == '5'):
                load_customer_agency(con, cur, csv_choice)
                
            con.commit()
            con.close()

        if(user_input == '3'):
            erase_tables()

        if(user_input == '4'):
            print("Quitting from the application")
            continue_to_run = False
            sys.exit(0)
if __name__ == "__main__":
    main()