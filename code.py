import os
from os import path


liste=[]
#this is the text file path where you see the ultimate result.
z="C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\test.txt"

d="C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\txt2"
for root, dirs, files in os.walk("C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\txt2"): #this is the target text file to divide into sentences.
    for file in files:
        f=open(z,'a')
        if file.endswith('.txt'):
         #print(os.path(file))
         text=""
         text = open(path.join(d, file)).read()
         text=text.replace("İ", "i")
         text=text.replace("Ğ", "ğ")
         text=text.replace (chr(34)," ")
         text=text.replace (chr(8212)," ")
         text=text.replace (chr(8226)," ")
         text=text.replace (chr(8217)," ")
         text=text.replace (chr(8216)," ")
         ekle=text.split()
         a=0
         numaralar=[]
         for x in ekle:
          if x.endswith(".") or x.endswith("!") or x.endswith(":") or x.endswith(chr(8221)) or x.endswith("?") :
           a=ekle.index(x,a)
           numaralar.append(a) #make a list to see where the each sentence ends
numaralar.insert(0,0) 
print(numaralar)
son=len(numaralar)
cumle=[]
ind=0
for i in range(0,son):
 if i==son-1:
  quit()
 else:
 #using numaralar list divide text into sentences.
  no1=numaralar[i]
  no2=numaralar [i+1]
  cumle=[]
  for i in range(no1,no2+1):
   cumle.append(ekle[i])
  if no1!=0:
   cumle.pop(0)  
 #print(cumle)  
 yazo=" ".join(cumle)
 #save each sentences to the text file. 
 f.write(yazo + '\n')
  
f.close()
 
'''s=" "
yazo=s.join(liste)
f.write(yazo)
f.close()'''
