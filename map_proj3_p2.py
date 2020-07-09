#!/usr/bin/env python

import csv
import sys

SEP = "\t"

class Mapper(object):

	def __init__(self, stream, sep=SEP):
		self.stream = stream
		self.sep    = sep

	def emit(self, key, value):
		sys.stdout.write("%s%s%s\n" % (key, self.sep, value))

    def map(self):
        #Bunch of counters
        a=1
        a2 =1
        b=1
        b2=1
        
        node = [] #List pulled from the text file
        temp = []
        temp2=[]
        links = [] #List of unique source nodes by name
        con = [] #List of links per souce nodes
        fnode = [] #List of total amount of unique nodes
        #reader = csv.reader(self.stream)
        for line in self.stream:
            l = line.strip()
            node.append(l.split("\t"))
          
            #just a test for working code.
            #print(a)
          
            #counting the number of links going out of the first node
            if a != 1:
                if l.split("\t")[0] == temp:
                    b = b + 1
                    a = a + 1
                else:
                  links.append(temp)
                  con.append(b)
                  b = 1
                  a = a + 1
                  temp = l.split("\t")[0]
                  #self.counter("num of nodes")
            else:
                temp = l.split("\t")[0]
                a = a + 1
          
            #counting the number of nodes
            if a2 != 1:
                temp2 = l.split("\t")[1]
                q = 0
                r = 0
                for m in fnode:
                  if m == temp2: #Nodes in destination
                    q = q + 1
                  if m == temp: #nodes in source
                    r = r + 1
                #end For m
                if q == 0: #adding node to total if unique from destination
                    fnode.append(temp2)
                    a2 = a2 + 1
                if r == 0: #adding node to total if unique from source
                    fnode.append(temp)
            else: #Add the very first node
                temp2 = l.split("\t")[1]
                fnode.append(temp2)
                a2 = a2 + 1     
                
        #end For loop line
        
        #For the last line (node-link) in the text file for souce
        links.append(temp)
        con.append(b)

        #Checking Stuff
        print("Total Number of nodes ",len(fnode))
        print("Total Number of source nodes ",len(links))
        print("Number of source nodes with links ",len(con))


        d = len(con) # number of links per source node
        p = 0 #To collect probabilities

        #print(con) #Test to see how may nodes and the number of links
        
        #For calculating probabilities taking into account dead ends and spider traps [NOT COMPLETE]
        #beta = .9
        #n=4        
        
                
        #Last thing before the Program ends
        for i in node: #to find the probability of destination link
            c = 0
            for j in links:
                if i[0] == j:
                p = con[c]
            else:
                c = c+1
            self.emit(i[1],float(1)/float(p))

if __name__ == '__main__':
 	mapper = Mapper(sys.stdin)
 	mapper.map()
