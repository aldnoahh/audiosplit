#Program for spliting multiple audio files into sub-file of each with a defined time



from pydub import AudioSegment as aseg
import os
mylist= os.listdir('/home/akshay/Desktop/audio/')  #input directory

type(mylist)
t=5   #define the time you need each file to be
for index, y in enumerate(mylist):
	nAud = aseg.from_wav("/home/akshay/Desktop/audio/"+y)
	k=int(len(nAud)/1000)
	y1= (k//t)+1
	a1,a2=0,t
	for j in range(y1+1):
		t1 = a1 * 1000 #Works in milliseconds
		t2 = a2 * 1000
		a1+=t
		a2+=t
		nAud = nAud[t1:t2]
		nAud.export('/home/akshay/Desktop/audi2/'+y+str(j)+'.WAV')  #output directory
