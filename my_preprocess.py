#!/usr/bin/python

import pickle
import cPickle
import numpy

from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from lxml import html
import requests
import ctypes

def process(words_file = "I:/Python 2.7/project/myfile.pkl",diseases_file="I:/Python 2.7/project/myfile2.pkl"):
#words_file = "I:/Python 2.7/mywork/myfile.pkl"

    mc=[]

    ### the words (features) and authors (labels), already largely preprocessed
    ### this preprocessing will be repeated in the text learning mini-project
    diseases_file_handler = open(diseases_file, "r")
    diseases = pickle.load(diseases_file_handler)
   
    diseases_file_handler.close()

    words_file_handler = open(words_file, "r")
    word_data = cPickle.load(words_file_handler)
   
    words_file_handler.close()

    ### test_size is the percentage of events assigned to the test set
    ### (remainder go into training)
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, diseases, test_size=0.0, random_state=42)

#print "features_train",features_train



    t = open("input2.txt","r")

    lines = t.readlines()
    t.close()
    features_test=lines
    print "features_test: ",features_test



    ### text vectorization--go from strings to lists of numbers
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
    features_train_transformed = vectorizer.fit_transform(features_train).toarray()
    features_test_transformed  = vectorizer.transform(features_test).toarray()

    flattened_feature = features_train_transformed.ravel()
    z_f = [f for f in flattened_feature if f == 0]
    print "Zero feat, ", len(z_f)
    print "features, ", len(flattened_feature)
    
    

    print "Number of features: ", len(flattened_feature) - len(z_f)
    print  features_train_transformed[15]
    print features_test_transformed

    from sklearn.decomposition import PCA



    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    clf1 = GaussianNB()

    clf1.fit(features_train_transformed,labels_train)
    pre = clf1.predict(features_test_transformed)
    pre2=clf1.predict_proba(features_test_transformed)
    mc.append(pre[0])

    print "NB Predictive Disease is : ",pre[0]
    print pre
    print pre2
    
    bl=0
    j=0
    for i in labels_train:
        print i
        if i==pre[0]:
           print i,j
           bl=j
        j=j+1

    #import matplotlib.pyplot as plt
    pca = PCA(n_components=64).fit(features_train_transformed)
    data2D = pca.transform(features_train_transformed)
    centers2D = pca.transform(features_test_transformed)

    

#colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(features_test_transformed)))

#cs = [colors[i//len(features_train_transformed)] for i in range(len(features_test_transformed)*len(features_train_transformed))]
   # s = [20*2**n for n in range(len(features_train_transformed))]
    import numpy as np     
    t = np.arange(64)
    
    print t  
   
        
    #plt.legend()
    #plt.grid(True)    
    
    #lines
    print "labes",labels_train
    print data2D[:,0]
    print "\n",data2D[:,1]
    import matplotlib

    l=[]
    for name in matplotlib.colors.cnames:
        l.append(name)
        

    
    #j=[]
    #for i in t:
       # j.append(plt.scatter(data2D[i][0], data2D[i][1],s=100,c=l[i]))
      #  print j[i],"\n"
    #plt.legend(j,labels_train,scatterpoints=1,loc='lower center',bbox_to_anchor=(0.5, -0.12),ncol=6,fontsize=8)
    
    #label = [0,1,2,3,0,1,2,3]
    #colors = ['red','green','blue','purple']

     #fig = plt.figure(figsize=(8,8))
     #plt.scatter(x, y, c=label, cmap=matplotlib.colors.ListedColormap(colors))

    #i=0
    #for xy in zip(data2D[:,0], data2D[:,1]):
                                          # <--
      #  plt.annotate(labels_train[i], xy=xy, textcoords='data')
        #i=i+1
    #plt.grid(True)
    #plt.show()
    #plt.hold(True)


    #print centers2D.ravel()

    #plt.scatter(centers2D[:,0], centers2D[:,1],
     #       marker='x',s=100, linewidths=3, c='r',label="Cross-validation score")
    
    
    #plt.legend()
    #plt.grid(True)
    
   # plt.show()
    #sh(plt)
    
    #plt.plot(t, centers2D.ravel(),
       #      c='r')
    #plt.show()
    from mpl_toolkits.mplot3d import Axes3D,proj3d
    import pylab
    from matplotlib import pyplot
    from mpldatacursor import datacursor


    fig_size = pyplot.rcParams["figure.figsize"]
    fig_size[0] = 15
    fig_size[1] = 10
    pyplot.rcParams["figure.figsize"] = fig_size

    fig=pylab.figure()
    ax = Axes3D(fig)
    j=[]
    #for i in t:
    print t,"\n"
    print data2D[:,0].ravel(),"\n"
    p=data2D[:,0].ravel()
    print p[0],"\n",len(p),"\n"
    print data2D[:,1].ravel()
    q=data2D[:,1].ravel()
    print len(q),"\n"
    print "labels", labels_train[bl]
    
    #plt.plot(p,q,s=100)
    #plt.show()
    k=[]
    for i in t:
        k.append(ax.scatter(i,p[i], q[i],'o',s=100,c=l[i],label='{}'.format(labels_train[i])))


    pyplot.hold(True)
    ax.scatter(bl,centers2D[:,0].ravel(), centers2D[:,1].ravel(),
            marker='x',s=100, linewidths=3, c='r',label="Your Disease")
    ax.text(bl,centers2D[:,0].ravel(),centers2D[:,1].ravel(),  'Your Disease', size=15, zorder=1,
           color='k')
    ax.text(bl,p[bl],q[bl],  '%s' % labels_train[bl], size=15, zorder=1,
           color='k')
    datacursor(formatter='{label}'.format,hover=True)
    
#    ax.scatter(bl,data2D[bl][0],data2D[bl][1], 
      #      marker='D',s=100, linewidths=3, c='black',label="Cross-validation score")
    #print j[i],"\n"
    pyplot.legend(k,labels_train,scatterpoints=1,loc='centerleft',bbox_to_anchor=(0.27, 0.9),ncol=2,fontsize=8)
    
    #i=0
    #for xyz in zip(t,p,q):
       # print xyz[0]                                  # <--
     #   ax.text(xyz[0],xyz[1],xyz[2],labels_train[xyz[0]], textcoords='data')
     #   i=i+1
     
    
        
       
#import matplotlib.pyplot as plt
#fig = plt.figure()
#plt.xlabel("Features")
#plt.ylabel("Labels")
#plt.ylim(-4, 14)
#plt.scatter(features_train_transformed.ravel(), labels_train, color = 'green')
#plt.plot(features_test_transformed.ravel(), pre, color = 'blue')
#plt.show()


    from sklearn.naive_bayes import MultinomialNB
    clf2 = MultinomialNB()
    clf2.fit(features_train_transformed,labels_train)
    pre1 = clf2.predict(features_test_transformed)

    print "Multinomial NB Predictive Disease is : ",pre1[0]
    print pre1

    mc.append(pre1[0])

    bl=0
    j=0
    for i in labels_train:
        print i
        if i==pre1[0]:
           print i,j
           bl=j
        j=j+1
        
    ax.text(bl,p[bl],q[bl],  '%s' % labels_train[bl], size=15, zorder=1,  
           color='k')    

    from sklearn.linear_model import LogisticRegression
    clf3 = LogisticRegression()
    clf3.fit(features_train_transformed,labels_train)
    pre2 = clf3.predict(features_test_transformed)

    mc.append(pre2[0])

    print "LogisticRegression Predictive Disease is : ",pre2[0]
    print pre2
    
    bl=0
    j=0
    for i in labels_train:
        print i
        if i==pre2[0]:
           print i,j
           bl=j
        j=j+1
        
    ax.text(bl,p[bl],q[bl],  '%s' % labels_train[bl], size=15, zorder=1,  
           color='k')

    from sklearn.multiclass import OneVsRestClassifier
    from sklearn.svm import LinearSVC
    cl4=OneVsRestClassifier(LinearSVC())
    pre3=OneVsRestClassifier(LinearSVC()).fit(features_train_transformed,labels_train).predict(features_test_transformed)
    print "OneVsRestClassifiere Predictive Disease is : ",pre3[0]
    print pre3

    mc.append(pre3[0])
    
    bl=0
    j=0
    for i in labels_train:
        print i
        if i==pre3[0]:
           print i,j
           bl=j
        j=j+1
        
    ax.text(bl,p[bl],q[bl],  '%s' % labels_train[bl], size=15, zorder=1,  
           color='k')

    #pyplot.show()

#print dict_names


    

    #print"\n\nTests and Diagnosis: "
   # print dict_names[pre[0]]['dia']

    x=[]
    x = list(set(mc))
    print x


    return x,pyplot

     #feature selection, because text is super high dimensional and 
    # can be really computationally chewy as a result
#selector = SelectPercentile(f_classif, percentile=5)
#selector.fit(features_train_transformed, labels_train)
#features_train_transformed = selector.transform(features_train_transformed).toarray()
#features_test_transformed  = selector.transform(features_test_transformed).toarray()

    ### info on the data
    
    
    
#print "features_train_transformed",features_train_transformed
#print "features_test_transformed",features_test_transformed
#print "labels_train",labels_train
def med(p):
    dict_names = {'Heart attack' : {'dia':'Electrocardiogram (ECG) \nBlood tests \nChest X-ray \nEchocardiogram \nCoronary catheterization (angiogram) \nCardiac computerized tomography (CT) or magnetic resonance imaging (MRI) ',
                                 'med': 'Aspirin\nThrombolytics\nAntiplatelet agents\nOther blood-thinning medications\nPain relievers\nNitroglycerin\nBeta blockers\nACE inhibitors'},
              'Heart failure' : {'dia':'Blood tests.\nElectrocardiogram (ECG).\nEchocardiogram.\nStress test.\nCardiac computerized tomography (CT) scan or magnetic resonance imaging (MRI).\nCoronary angiogram.',
                                 'med': 'Angiotensin-converting enzyme (ACE) inhibitors.\nAngiotensin II receptor blockers.\nInotropes.\nDigoxin (Lanoxin).\nCoronary bypass surgery.'},
              'High blood pressure' : {'dia':'Measurement of:\nNormal blood pressure.\nPrehypertension.\nStage 1 hypertension.\nStage 2 hypertension.',
                                 'med': 'Thiazide diuretics\nBeta blockers\nAngiotensin-converting enzyme (ACE) inhibitors\nAngiotensin II receptor blockers (ARBs)\nCalcium channel blockers\nRenin inhibitors\nAlpha blockers\nAlpha-beta blockers\nCentral-acting agents\nVasodilators\nAldosterone antagonists'},
              'Lung cancer' : {'dia':'Imaging tests.\nSputum cytology.\nTissue sample (Biopsy)',
                                 'med': 'Erlotinib (Tarceva and others)\nAfatinib (Gilotrif)\nGefitinib (Iressa)\nBevacizumab (Avastin)\nCrizotinib (Xalkori)\nCeritinib (Zykadia)'},
              'Dengue fever' : {'dia': 'Blood tests\nTissue or Fluid culture',
                                 'med': 'Supportive care in a hospital\nIntravenous (IV) fluid and electrolyte replacement\nBlood pressure monitoring\nTransfusion to replace blood loss'},
              'Adult asthma' : {'dia':'Spirometry.\nPeak flow.\nMethacholine challenge.\nNitric oxide test.\nImaging tests.\nAllergy testing.\nSputum eosinophils.\nProvocative testing for exercise and cold-induced asthma.',
                                 'med': 'Inhaled corticosteroids\nLeukotriene modifiers\nLong-acting beta agonists\nCombination inhalers\nTheophylline'},
              'Acute kidney failure' : {'dia':'Urine output measurements.\nUrine tests.\nBlood tests.\nImaging tests.\nRemoving a sample of kidney tissue for testing.',
                                 'med': 'Treatments to balance the amount of fluids in your blood\nMedications to control blood potassium\nMedications to restore blood calcium levels\nDialysis to remove toxins from your blood'},
              'Bronchitis' : {'dia':'Chest X-ray.\nSputum tests.\nPulmonary function test.',
                                 'med': 'Antibiotics.\nCough medicine.\nOther medications.'},
              'Cystitis' : {'dia':'Cystoscopy\nUrine analysis.\nImaging.',
                                 'med': 'Medications that are taken orally or inserted directly into your bladder\nProcedures that manipulate your bladder to improve symptoms, such as stretching the bladder with water or gas (bladder distention) or surgery\nNerve stimulation, which uses mild electrical pulses to relieve pelvic pain and, in some cases, reduce urinary frequency'},
              'Diabetes mellitus' : {'dia':'Glycated hemoglobin (A1C) test.\nRandom blood sugar test.\nFasting blood sugar test.\nOral glucose tolerance test.\nIf your at high risk of gestational diabetes\nIf your at average risk of gestational diabetes,\nInitial glucose challenge test.\nFollow-up glucose tolerance testing.',
                                 'med': 'Healthy eating. Monitoring your blood sugar. Insulin.'},
              'Dyslexia' : {'dia':'Your child development, educational issues and medical history.\nYour child home life.\nQuestionnaires.\nVision, hearing and brain (neurological) tests.\nPsychological testing.\nTesting reading and other academic skills.',
                                 'med': 'Address the problem early\nRead aloud to your child\nWork with school of your child\nSet an example for reading'},
              'Fever NOS' : {'dia':'Ask questions about your symptoms and medical history\nPerform a physical exam\nOrder tests, such as blood tests or a chest X-ray, as needed, based on your medical history and physical exam',
                                 'med': 'Acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others)\nAspirin, for adults only.'},
              'Gallbladder cancer' : {'dia':'Blood tests.\nProcedures to create images of the gallbladder.\nAdditional imaging tests',
                                 'med': 'Surgery to remove the gallbladder\nSurgery to remove the gallbladder and a portion of the liver\nChemotherapy\nRadiation therapy\nClinical trials.' },
              'Gangrene' : {'dia':'Blood tests.\nSurgery.\nFluid or tissue culture.\nImaging test',
                                 'med': 'Surgery.\nHyperbaric oxygen therapy.'},
              'Gastritis' : {'dia':'Tests for H. pylori.\nUsing a scope to examine your upper digestive system (endoscopy).\nX-ray of your upper digestive system.',
                                 'med': ' clarithromycin (Biaxin)\namoxicillin or metronidazole (Flagyl)\nomeprazole (Prilosec)\nlansoprazole (Prevacid)\nrabeprazole (Aciphex)\nesomeprazole (Nexium)\ndexlansoprazole (Dexilant) and pantoprazole (Protonix)'},
              'Hepatitis A' : {'dia':'Blood tests',
                                 'med': 'Rest.\nCope with nausea.\nRest your liver.'},
              'Hepatitis B' : {'dia': 'Blood tests\nliver biopsy',
                                 'med': 'Antiviral medications.\nInterferon alfa-2b (Intron A).\nLiver transplant.'},
              'Kidney stone' : {'dia':'Blood testing.\nUrine testing.\nAnalysis of passed stones.',
                                 'med': 'Drinking water.\nPain relievers.\nMedical therapy.\nUsing sound waves to break up stones.\nSurgery to remove very large stones in the kidney\nUsing a scope to remove stones\nParathyroid gland surgery'}
              }
              
    return dict_names[p]['med']   


def dia(p):
    dict_names = {'Heart attack' : {'dia':'Electrocardiogram (ECG) \nBlood tests \nChest X-ray \nEchocardiogram \nCoronary catheterization (angiogram) \nCardiac computerized tomography (CT) or magnetic resonance imaging (MRI) ',
                                 'med': 'Aspirin\nThrombolytics\nAntiplatelet agents\nOther blood-thinning medications\nPain relievers\nNitroglycerin\nBeta blockers\nACE inhibitors'},
              'Heart failure' : {'dia':'Blood tests.\nElectrocardiogram (ECG).\nEchocardiogram.\nStress test.\nCardiac computerized tomography (CT) scan or magnetic resonance imaging (MRI).\nCoronary angiogram.',
                                 'med': 'Angiotensin-converting enzyme (ACE) inhibitors.\nAngiotensin II receptor blockers.\nInotropes.\nDigoxin (Lanoxin).\nCoronary bypass surgery.'},
              'High blood pressure' : {'dia':'Measurement of:\nNormal blood pressure.\nPrehypertension.\nStage 1 hypertension.\nStage 2 hypertension.',
                                 'med': 'Thiazide diuretics\nBeta blockers\nAngiotensin-converting enzyme (ACE) inhibitors\nAngiotensin II receptor blockers (ARBs)\nCalcium channel blockers\nRenin inhibitors\nAlpha blockers\nAlpha-beta blockers\nCentral-acting agents\nVasodilators\nAldosterone antagonists'},
              'Lung cancer' : {'dia':'Imaging tests.\nSputum cytology.\nTissue sample (Biopsy)',
                                 'med': 'Erlotinib (Tarceva and others)\nAfatinib (Gilotrif)\nGefitinib (Iressa)\nBevacizumab (Avastin)\nCrizotinib (Xalkori)\nCeritinib (Zykadia)'},
              'Dengue fever' : {'dia': 'Blood tests\nTissue or Fluid culture',
                                 'med': 'Supportive care in a hospital\nIntravenous (IV) fluid and electrolyte replacement\nBlood pressure monitoring\nTransfusion to replace blood loss'},
              'Adult asthma' : {'dia':'Spirometry.\nPeak flow.\nMethacholine challenge.\nNitric oxide test.\nImaging tests.\nAllergy testing.\nSputum eosinophils.\nProvocative testing for exercise and cold-induced asthma.',
                                 'med': 'Inhaled corticosteroids\nLeukotriene modifiers\nLong-acting beta agonists\nCombination inhalers\nTheophylline'},
              'Acute kidney failure' : {'dia':'Urine output measurements.\nUrine tests.\nBlood tests.\nImaging tests.\nRemoving a sample of kidney tissue for testing.',
                                 'med': 'Treatments to balance the amount of fluids in your blood\nMedications to control blood potassium\nMedications to restore blood calcium levels\nDialysis to remove toxins from your blood'},
              'Bronchitis' : {'dia':'Chest X-ray.\nSputum tests.\nPulmonary function test.',
                                 'med': 'Antibiotics.\nCough medicine.\nOther medications.'},
              'Cystitis' : {'dia':'Cystoscopy\nUrine analysis.\nImaging.',
                                 'med': 'Medications that are taken orally or inserted directly into your bladder\nProcedures that manipulate your bladder to improve symptoms, such as stretching the bladder with water or gas (bladder distention) or surgery\nNerve stimulation, which uses mild electrical pulses to relieve pelvic pain and, in some cases, reduce urinary frequency'},
              'Diabetes mellitus' : {'dia':'Glycated hemoglobin (A1C) test.\nRandom blood sugar test.\nFasting blood sugar test.\nOral glucose tolerance test.\nIf your at high risk of gestational diabetes\nIf your at average risk of gestational diabetes,\nInitial glucose challenge test.\nFollow-up glucose tolerance testing.',
                                 'med': 'Healthy eating. Monitoring your blood sugar. Insulin.'},
              'Dyslexia' : {'dia':'Your child development, educational issues and medical history.\nYour child home life.\nQuestionnaires.\nVision, hearing and brain (neurological) tests.\nPsychological testing.\nTesting reading and other academic skills.',
                                 'med': 'Address the problem early\nRead aloud to your child\nWork with school of your child\nSet an example for reading'},
              'Fever NOS' : {'dia':'Ask questions about your symptoms and medical history\nPerform a physical exam\nOrder tests, such as blood tests or a chest X-ray, as needed, based on your medical history and physical exam',
                                 'med': 'Acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others)\nAspirin, for adults only.'},
              'Gallbladder cancer' : {'dia':'Blood tests.\nProcedures to create images of the gallbladder.\nAdditional imaging tests',
                                 'med': 'Surgery to remove the gallbladder\nSurgery to remove the gallbladder and a portion of the liver\nChemotherapy\nRadiation therapy\nClinical trials.' },
              'Gangrene' : {'dia':'Blood tests.\nSurgery.\nFluid or tissue culture.\nImaging test',
                                 'med': 'Surgery.\nHyperbaric oxygen therapy.'},
              'Gastritis' : {'dia':'Tests for H. pylori.\nUsing a scope to examine your upper digestive system (endoscopy).\nX-ray of your upper digestive system.',
                                 'med': ' clarithromycin (Biaxin)\namoxicillin or metronidazole (Flagyl)\nomeprazole (Prilosec)\nlansoprazole (Prevacid)\nrabeprazole (Aciphex)\nesomeprazole (Nexium)\ndexlansoprazole (Dexilant) and pantoprazole (Protonix)'},
              'Hepatitis A' : {'dia':'Blood tests',
                                 'med': 'Rest.\nCope with nausea.\nRest your liver.'},
              'Hepatitis B' : {'dia': 'Blood tests\nliver biopsy',
                                 'med': 'Antiviral medications.\nInterferon alfa-2b (Intron A).\nLiver transplant.'},
              'Kidney stone' : {'dia':'Blood testing.\nUrine testing.\nAnalysis of passed stones.',
                                 'med': 'Drinking water.\nPain relievers.\nMedical therapy.\nUsing sound waves to break up stones.\nSurgery to remove very large stones in the kidney\nUsing a scope to remove stones\nParathyroid gland surgery'}
              }
              
    return dict_names[p]['dia'] 


def medlink(p):
    print "in medlink\n",p
    h = open('mydict.txt', 'r')
    newdict = eval(h.read())
    #newdict
    t="http://www.mayoclinic.org"
    t=newdict[p]["med"]
    print t
    page = requests.get(t)
    tree = html.fromstring(page.content)
    s=[]
    s=tree.xpath('//div[@id="main-content"]/p/text()')
    s= s + tree.xpath('//ul/li/text()')
    x=' '
    while x in s: s.remove(x)
    x='\r\n                    '
    while x in s: s.remove(x)
    x='\n    '
    while x in s: s.remove(x)
    
    #for v in s:
        #print v
    print "returning s" 
    s="\n".join(s)
    return s
    
def dialink(p):
    print "in dialink\n"
    h = open('mydict.txt', 'r')
    newdict = eval(h.read())
    #newdict
    t="http://www.mayoclinic.org"
    t=newdict[p]["dia"]
    print t
    page = requests.get(t)
    tree = html.fromstring(page.content)
    s=[]
    s=tree.xpath('//div[@id="main-content"]/p/text()')
    s= s + tree.xpath('//ul/li/text()')
    x=' '
    while x in s: s.remove(x)
    x='\r\n                    '
    while x in s: s.remove(x)
    x='\n    '
    while x in s: s.remove(x)
    
    #for v in s:
      #  print v
    print "returning s" 
    s="\n".join(s)
    return s    
    

         
    