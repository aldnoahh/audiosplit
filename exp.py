from pydub import AudioSegment as aseg
import os
mylist= os.listdir('/home/akshay/Desktop/audio/')

type(mylist)

for index, y in enumerate(mylist):
	nAud = aseg.from_wav("/home/akshay/Desktop/audio/"+y)
	k=int(len(nAud)/1000)
	y1= (k//5)+1
	for j in range(y1+1):
		a1,a2=0,5
		t1 = a1 * 1000 #Works in milliseconds
		t2 = a2 * 1000
		a1+=5
		a2+=5
		nAud = nAud[t1:t2]
		nAud.export('/home/akshay/Desktop/audi2/'+y+str(j)+'.WAV')
		#nAud.export('/home/akshay/Desktop/audi/'+y+str(j), format="wav")





"""
t1 = 0 * 1000 #Works in milliseconds
t2 = 10 * 1000
nAud = aseg.from_wav("/home/akshay/Desktop/audio/1An.WAV")
nAud = newAudio[t1:t2]
nAud.export('/home/akshay/Desktop/s_half.WAV', format="wav") """
		
	

