from random import randint


def fileLength(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i+1

def getQuestion(fname, line):
	#print line
	with open(fname) as f:
		reading = ''
		for i in range(0,line):
			reading = f.readline()
		question = ''
		for q in reading:
			if q == ',':
				break
			else:
				question = question + q
	return question

def getAnswer(fname, line):
	with open(fname) as f:
		reading = ''
		for i in range(0,line):
			reading = f.readline()
		answer = ''
		for a in reading:
			if a == ',':
				answer = ''
				continue
			if a == '\n':
				break
			else:
				answer = answer + a
	return answer


filename = 'capitals.txt' #raw_input("Please enter the name of the file with flashcard:")

length = fileLength(filename)

linenumber = randint(1, int(length))

question = getQuestion(filename, linenumber)
answer = getAnswer(filename, linenumber)

print question
print answer





