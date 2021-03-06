__author__ = 'tim'

import fileinput
from optparse import OptionParser
import random


def obfuscate(data,lossrate):
    s=''
    for i,c in enumerate(data):
        if random.randint(0,100) < lossrate:
            s=s+' '
        else:
            s=s+c
    return(s)

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file to read", type=str, default='-')
parser.add_option("-d", "--data", type=str, dest="fields", help="data fields to extract i.e. 2,3,4")
parser.add_option("-l", "--loss", type=str, dest="loss",
                  help="percentage of data to loose per output field, i.e. 50,20,90")
parser.add_option("-s", "--split", type=str, dest="split",default=",",
                  help="split data using what field i.e ,(, is the default) - \t etc")
parser.add_option("-t", "--type", type=str, dest="loss_type",default="All",
                  help="Type of loss All(default) or Partial")
(options, args) = parser.parse_args()
loss = [int(a) for a in options.loss.split(',')]
fields = [int(a) for a in options.fields.split(',')]
first_line = True
if options.loss_type.upper().startswith('A'):
   FullLoss=True
else:
   FullLoss=False

try:
    for line in fileinput.input(options.filename):
        data_line = line.split(options.split)
        pos = 0
        new_line = ''
#        print ("line is "+line)
#        print(str(fields))
#        print(str(data_line))
        for wanted in fields:
            data = data_line[wanted -1]
            rnd = random.randint(0,100)
            if pos > 0:
                new_line += options.split
            if first_line:
                new_line += data.rstrip()
            else:
                if rnd > loss[pos]:
                        new_line += data.rstrip()
                else:
                        if FullLoss==False:
                           new_line += obfuscate(data.rstrip(),loss[pos])
		
            pos += 1
        print(""+new_line)
        first_line = False
#    ifp.close()
except FileNotFoundError:
    print("File %s not found", options.filename)
    pass
