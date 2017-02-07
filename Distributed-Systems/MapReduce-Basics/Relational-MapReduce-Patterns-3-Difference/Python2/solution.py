# Enter your code here. Read input from STDIN. Print output to STDOUT
# This template is based on the framework supplied for a similar challenge, in a Coursera Data Science course: https://www.coursera.org/course/datasci
# And the code supplied here: https://github.com/uwescience/datasci_course_materials/blob/master/assignment3/wordcount.py
# The map-reduce emulator is provided
# You need to fill out the mapper and reducer functions

import json
import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        jenc = json.JSONEncoder()
        for item in self.result:
            print str(item[1]).strip()

mapReducer = MapReduce()

r = 0
s = 0

def mapper(record):
    key = record["key"]
    value = record["value"]
    # ADD THE REQUIRED LOGIC BELOW
    # You may need to add some lines for the mapper logic to work
    # At the end, you need to complete the emit intermediate step
    global r
    global s
    key = value
    if ' ' not in value:
        if r > 0:
            value = "R"
            r -= 1
        else:
            value = "S"
        mapReducer.emitIntermediate(key, value)
    else:
        [r, s] = map(int, value.split())

def reducer(key, list_of_values):
    # ADD THE REQUIRED LOGIC BELOW
    # You may need to add some lines for the reducer logic to work
    # At the end, you need to complete the emit step
    if ("R" in list_of_values) and ("S" not in list_of_values): 
        mapReducer.emit((key, key))

if __name__ == '__main__':
    inputData = []
    counter = 0
    for line in sys.stdin:
        counter += 1
        inputData.append(json.dumps({"key":counter,"value":line}))
    mapReducer.execute(inputData, mapper, reducer)

