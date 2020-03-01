import time
with open('sentiment.txt') as f:
  lineList = f.readlines()
listTwo = lineList.copy()
print(len(lineList))
removed = 0
newL = [i for i in lineList if '1' in i]
print(newL)
words = []
emotions = []

for i in range(len(newL)):
	for x in range(len(newL[i])):
		
		if newL[i][x] == '\t':
			words.append(newL[i][0:x])
			emotions.append(newL[i][x:])
			break
newEmotions = []
for i in range(len(emotions)):
	for x in range(len(emotions[i])):
		newEmotions.append(emotions[i][1:len(emotions[i])-3])


strone = 'I have my secrets. I take my time, stare at my face until I’m a stranger, a she who is not me. A she who helps herself to whatever will buff the sharp edges of the world. Yesterday a yellow pill pinned the sun to the center of the sky where it remained unstained by clouds. Waiting for the bus, she danced to the thunder of drums from a car idling at a red light. A glass door gave her back herself, a whirling dervish in sneakers. If you drove by just then you’d think, now there’s a happy gal.'
strone = strone.split()

plus = 0 
for i in range(len(strone)):
	for x in range(len(newL)):

		if  strone[i] in newL[x]:
			plus +=1
