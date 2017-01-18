#import sys
#print "Write Symptoms:"
#t=sys.stdin.read()

#t=raw_input("Insert Symptoms: ")
print "Insert Symptoms: "
#t=" ".join(iter(raw_input, ""))
def input(t):

    clean=[]
    for n in t.split():
        clean.append(n.replace("\n"," "))


    t=clean



    wr=[]
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    w =[]
    for o in t:
        print "o : ",o.encode('ascii','ignore')
        w.append(stemmer.stem(o))
    

    t=w

    import string
     
    w=[]
    for o in t:
        w.append(o.encode('ascii','ignore').translate(None, string.punctuation))

    t=w


    t=" ".join(t)


	#print "input: ",t



#test file writing
    with open("input2.txt", "w") as myfile:
         for o in t:
             myfile.write(o)
           

    myfile.close()

    #return t



