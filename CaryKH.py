from random import *
import array as arr
import numpy
import os

#import files and separate them into array
with open('txts\DONT_TOUCH\words_k.txt') as f:
    words_k = [line.rstrip('\n') for line in f]
with open('txts\DONT_TOUCH\words_h.txt') as f:
    words_h = [line.rstrip('\n') for line in f]
#generate random numbers 4 first run
randwordk = randint(0, 3952);
randwordh = randint(0, 13743);
#set shutdown var
end = 0;
#choice
choice = 0;
#use those numbers to grab a random word from vocalubrary !ONLY! starting with K/H and write them into separate vars
k_word = words_k[randwordk];
h_word = words_h[randwordh];
#print Cary and two words
print("Cary ");
print(k_word);
print(h_word);
print();
#open output txt and write Cary K* H*
output = open('txts\output.txt', "a");
output.write(f"Cary {k_word} {h_word} \n");
#while shutdown is not called
while end == 0:
#give user choice: 
    print ("again/quit/quitopen/cleanfile (REGISTER SENSETIVE!!! type answer in lowercase. also after cleanfile the program shuts down): ");
    choice = input();
#generate again
    if choice == "again":
#choose random number
        randwordk = randint(0, 3952);
        randwordh = randint(0, 13743);
#using them assign random words to vars
        k_word = words_k[randwordk];
        h_word = words_h[randwordh];
#and print dat
        print("Cary ");
        print(k_word);
        print(h_word);
        print();
        #open output txt and write Cary K* H*
        output = open('txts\output.txt', "a");
        output.write(f"Cary {k_word} {h_word} \n");
#or quit
    elif choice == "quit":
#set shutdown to one
        end = 1;
#everything that not work
    elif choice == "debug":
        print("IT'S TIME TO STOP! OK!?");
        #_1debug = input("K Word Number: ");
        #_2debug = input("H Word Number: ");
        #print("Cary");
        #print(words_k[_1debug]);
        #print(words_h[_2debug]);
#also recreate output.txt
    elif choice == "cleanfile":
#close the file
        output.close();
#remove the file
        os.remove("txts\output.txt");
#open the file for writing and the same way create it
        output = open("txts\output.txt", "w");
        print("done!");
#pause
        pause = input("Press any key to terminate the program...");
        end = 1;
#and print out all outputs & quit
    elif choice == "quitopen":
        print("Showing all name abbriviations");
#open file for reading
        output = open("txts/output.txt");
#print its content out
        print(output.read());
#pause
        pause = input("Press any key to terminate the program...");
        end = 1;
