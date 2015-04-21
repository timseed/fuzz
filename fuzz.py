__author__ = 'tim'

from optparse import OptionParser
import random

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file to read", metavar="FILE")
parser.add_option("-d", "--data", type=str, dest="fields", help="data fields to extract i.e. 2,3,4")
parser.add_option("-l", "--loss", type=str, dest="loss",
                  help="percentage of data to loose per output field, i.e. 50,20,90")
(options, args) = parser.parse_args()
loss = [int(a) for a in options.loss.split(',')]
fields = [int(a) for a in options.fields.split(',')]
first_line = True

try:
    ifp = open(options.filename)
    for line in ifp:
        data_line = line.split(',')
        pos = 0
        new_line = ''
        for wanted in fields:
            data = data_line[wanted -1]
            rnd = random.random()
            if pos > 0:
                new_line += ","
            if rnd*100 < loss[pos] or first_line:
                new_line += data
            pos += 1
        print(""+new_line)
        first_line = False
    ifp.close()
except FileNotFoundError:
    print("File %s not found", options.filename)
    pass