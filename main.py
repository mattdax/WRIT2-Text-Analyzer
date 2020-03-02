import time
with open('sentiment.txt') as f:
  lineList = f.readlines()
listTwo = lineList.copy()

removed = 0
newL = [i for i in lineList if '1' in i]

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
# 1. Anger 2. Anticipation 3. Disgust 4. Fear 5. Joy 6. Negative 7. Positive 8. Sadness 9. Surprise 10. Trust
results = [0,0,0,0,0,0,0,0,0,0]

plus = 0 
for i in range(len(strone)):
	for x in range(len(words)):
		if words[x] in strone[i]:
			print("yes")
			if newEmotions[i] == 'anger':
				results[0] += 1
			if newEmotions[i] == 'anticipation':
				results[1] += 1
			if newEmotions[i] == 'disgust':
				results[2] += 1
			if newEmotions[i] == 'fear':
				results[3] += 1
			if newEmotions[i] == 'joy':
				results[4] += 1
			if newEmotions[i] == 'negative':
				results[5] += 1
			if newEmotions[i] == 'positive':
				results[6] += 1
			if newEmotions[i] == 'sadness':
				results[7] += 1
			if newEmotions[i] == 'surprise':
				results[8] += 1
			if newEmotions[i] == 'trust':
				results[9] += 1


print(results)
