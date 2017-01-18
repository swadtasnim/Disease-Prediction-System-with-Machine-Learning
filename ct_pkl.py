#basic thing
#import nltk
from lxml import html
import requests
#from collections import defaultdict
ur=["http://www.mayoclinic.org/diseases-conditions/heart-attack/basics/symptoms/con-20019520","http://www.mayoclinic.org/diseases-conditions/heart-failure/basics/symptoms/con-20029801","http://www.mayoclinic.org/diseases-conditions/high-blood-pressure/basics/symptoms/con-20019580","http://www.mayoclinic.org/diseases-conditions/lung-cancer/basics/symptoms/con-20025531","http://www.mayoclinic.org/diseases-conditions/dengue-fever/basics/symptoms/con-20032868","http://www.mayoclinic.org/diseases-conditions/asthma/basics/symptoms/con-20026992","http://www.mayoclinic.org/diseases-conditions/kidney-failure/basics/symptoms/con-20024029","http://www.mayoclinic.org/diseases-conditions/bronchitis/basics/symptoms/con-20014956","http://www.mayoclinic.org/diseases-conditions/cystitis/basics/symptoms/con-20024076","http://www.mayoclinic.org/diseases-conditions/diabetes/basics/symptoms/con-20033091","http://www.mayoclinic.org/diseases-conditions/dyslexia/basics/symptoms/con-20021904","http://www.mayoclinic.org/diseases-conditions/fever/basics/symptoms/con-20019229","http://www.mayoclinic.org/diseases-conditions/gallbladder-cancer/basics/symptoms/con-20023909","http://www.mayoclinic.org/diseases-conditions/gangrene/basics/symptoms/con-20031120","http://www.mayoclinic.org/diseases-conditions/gastritis/basics/symptoms/con-20021032","http://www.mayoclinic.org/diseases-conditions/hepatitis-a/basics/symptoms/con-20022163","http://www.mayoclinic.org/diseases-conditions/hepatitis-b/basics/symptoms/con-20022210","http://www.mayoclinic.org/diseases-conditions/kidney-stones/basics/symptoms/con-20024829","http://www.mayoclinic.org/diseases-conditions/hiv-aids/basics/symptoms/con-20013732","http://www.mayoclinic.org/diseases-conditions/acute-lymphocytic-leukemia/basics/symptoms/con-20042915","http://www.mayoclinic.org/diseases-conditions/milk-allergy/basics/symptoms/con-20032147","http://www.mayoclinic.org/diseases-conditions/brain-aneurysm/basics/symptoms/con-20028457","http://www.mayoclinic.org/diseases-conditions/anthrax/basics/symptoms/con-20022705","http://www.mayoclinic.org/diseases-conditions/back-pain/basics/symptoms/con-20020797","http://www.mayoclinic.org/diseases-conditions/breast-cysts/basics/symptoms/con-20032264","http://www.mayoclinic.org/diseases-conditions/bladder-cancer/basics/symptoms/con-20027606","http://www.mayoclinic.org/diseases-conditions/eye-melanoma/basics/symptoms/con-20027875","http://www.mayoclinic.org/diseases-conditions/inflammatory-breast-cancer/basics/symptoms/con-20035052","http://www.mayoclinic.org/diseases-conditions/oral-and-throat-cancer/basics/symptoms/con-20042850","http://www.mayoclinic.org/diseases-conditions/ovarian-cancer/basics/symptoms/con-20028096","http://www.mayoclinic.org/diseases-conditions/thyroid-cancer/basics/symptoms/con-20043551","http://www.mayoclinic.org/diseases-conditions/cardiomyopathy/basics/symptoms/con-20026819","http://www.mayoclinic.org/diseases-conditions/cellulitis/basics/symptoms/con-20023471","http://www.mayoclinic.org/diseases-conditions/cervicitis/basics/symptoms/con-20026738","http://www.mayoclinic.org/diseases-conditions/cholera/basics/symptoms/con-20031469","http://www.mayoclinic.org/diseases-conditions/primary-cough-headaches/basics/symptoms/con-20024827","http://www.mayoclinic.org/diseases-conditions/cyclospora/basics/symptoms/con-20032789","http://www.mayoclinic.org/diseases-conditions/dysarthria/basics/symptoms/con-20035008","http://www.mayoclinic.org/diseases-conditions/folliculitis/basics/symptoms/con-20025909","http://www.mayoclinic.org/diseases-conditions/frostbite/basics/symptoms/con-20034608","http://www.mayoclinic.org/diseases-conditions/liver-failure/basics/symptoms/con-20030966","http://www.mayoclinic.org/diseases-conditions/fuchs-dystrophy/basics/symptoms/con-20023893","http://www.mayoclinic.org/diseases-conditions/giant-cell-arteritis/basics/symptoms/con-20023109","http://www.mayoclinic.org/diseases-conditions/glaucoma/basics/symptoms/con-20024042","http://www.mayoclinic.org/diseases-conditions/glomerulonephritis/basics/symptoms/con-20024691","http://www.mayoclinic.org/diseases-conditions/h-pylori/basics/symptoms/con-20030903","http://www.mayoclinic.org/diseases-conditions/sinus-headaches/basics/symptoms/con-20025426","http://www.mayoclinic.org/diseases-conditions/heat-stroke/basics/symptoms/con-20032814","http://www.mayoclinic.org/diseases-conditions/juvenile-rheumatoid-arthritis/basics/symptoms/con-20014378","http://www.mayoclinic.org/diseases-conditions/keratitis/basics/symptoms/con-20035288","http://www.mayoclinic.org/diseases-conditions/lactose-intolerance/basics/symptoms/con-20027906","http://www.mayoclinic.org/diseases-conditions/lyme-disease/basics/symptoms/con-20019701","http://www.mayoclinic.org/diseases-conditions/mesothelioma/basics/symptoms/con-20026157","http://www.mayoclinic.org/diseases-conditions/mumps/basics/symptoms/con-20019914","http://www.mayoclinic.org/diseases-conditions/overactive-bladder/basics/symptoms/con-20027632","http://www.mayoclinic.org/diseases-conditions/parkinsons-disease/basics/symptoms/con-20028488","http://www.mayoclinic.org/diseases-conditions/pericarditis/basics/symptoms/con-20035562","http://www.mayoclinic.org/diseases-conditions/pneumonitis/basics/symptoms/con-20031011","http://www.mayoclinic.org/diseases-conditions/polio/basics/symptoms/con-20030957","http://www.mayoclinic.org/diseases-conditions/pulmonary-edema/basics/symptoms/con-20022485","http://www.mayoclinic.org/diseases-conditions/pulmonary-valve-stenosis/basics/symptoms/con-20013659","http://www.mayoclinic.org/diseases-conditions/q-fever/basics/symptoms/con-20030930","http://www.mayoclinic.org/diseases-conditions/spinal-cord-injury/basics/symptoms/con-20023837","http://www.mayoclinic.org/diseases-conditions/renal-artery-stenosis/basics/symptoms/con-20036702"]
#print ur
#t = open("Diseases.txt","r")
#lines = t.readlines()
#c=[]
#for s in lines:
    #c.append(s.replace("\n",""))
    
#m=len(c)-2 
#i=0 
x={}
i=0

for s in ur:
    print i
    i=i+1
    
    
    page = requests.get(s)
    tree = html.fromstring(page.content)
    u=[]
    
    u=tree.xpath('//meta[@name="Subject"]/@content')
    #print u[0]
    with open("Disease.txt", "a") as myfile:
         
         myfile.write(u[0])
         myfile.write("\n")  

    myfile.close()
#symptom
    buyers = tree.xpath('//div[@id="main-content"]/ul/li/text()')
#print buyers
#description
    t=tree.xpath('//div[@id="main-content"]/p/text()')
    t=buyers+t




    #t=unicode(t)

        
    
    #print t

    #stemming
    wr=[]
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    w =[]
    for o in t:
        wr="  "
        for v in o.split():
            #print "v : ",v.encode('ascii','ignore')
            w.append(stemmer.stem(v.encode('ascii','ignore')))
            #print "w: ",w
            wr=" ".join(w)

    t=wr

#file=open("temp.txt","w")
#for n in t:
        #file.write(n)

    #file.close()
    #t = open("temp.txt","r")

    #lines = t.readlines()
    #t.close()

    
    
    #clean = ''.join(l.replace('\n','') for l in open('temp.txt')) 
    #print 'clean: ',clean
    #clean=unicode(clean)
    #t=clean
    t=",".join(t)

#removing puctuation
    import string
     
    w=[]
    for o in t:
        w.append(o.encode('ascii','ignore').translate(None, string.punctuation))
    t=w

#removing newlines
    clean=[]
    for n in t:
        clean.append(n.replace("\n"," "))


    t=clean

#test file writing
    with open("test.txt", "a") as myfile:
         for o in t:
             myfile.write(o.encode('ascii','ignore'))
         myfile.write("\n")  

    myfile.close()

#Pkl File

    t = open("test.txt","r")

    lines = t.readlines()
    t.close()

    import pickle
    output = open('myfile.pkl', 'wb')
    pickle.dump(lines, output)
    output.close()
    
    #q=[]
    #for link in tree.xpath('//div[@id="main_0_left1_0_tertiarynav"]/ol/li/a/@href'):
    #    q.append(link)
    
    x[u[0]]={}
    
    x[u[0]]["dia"]=s.replace("/symptoms","/tests-diagnosis")
    print "dia= ",x[u[0]]["dia"]
    x[u[0]]["med"]=s.replace("/symptoms","/treatment")
    print "med=",x[u[0]]["med"]
    #i=i+1
 
 
    
#for j in range(0,18):
 #   print x[c[j]]['med'],x[c[j]]['dia'] 

f = open ('mydict.txt', 'w')
f.write(str(x))
f.close()

#g = open('mydict.txt', 'r')
#g.read()


 
#g.close()
#h = open('mydict.txt', 'r')
#newdict = eval(h.read())
#newdict

t = open("Disease.txt","r")

lines = t.readlines()
t.close()
lines

#for j in lines:
#    print "Med: ",newdict[['med'],"\nDia: ",newdict[c[j]]['dia']
                          
l=[]
for d in lines:
    l.append(d.replace("\n",""))
import pickle
output = open('myfile2.pkl', 'wb')
pickle.dump(l, output)
output.close()


