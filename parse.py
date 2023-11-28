
# Online Python - IDE, Editor, Compiler, Interpreter

import csv

with open('necStandardDisneyCodes.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        print('\t- platform: template')
        print('\t\tname: "' + row[0] + '"')
        print('\t\ton_press:')
        print('\t\t\t- remote_transmitter.transmit_nec:')
        print('\t\t\t\taddress: ' + row[1])
        print('\t\t\t\tcommand: ' + row[2])
