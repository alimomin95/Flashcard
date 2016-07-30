from random import randint


def fileLength(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i+1

def getQuestion(fname, line):
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

def printStats(correct, incorrect, total):
	print 'You got ' + str(correct) + ' correct answers.'
	print 'You got ' + str(incorrect) + ' incorrect answers'
	print 'Your accuracy was ' + str((float(correct)/float(total))*100.00) + '%.'

correct = 0
incorrect = 0
total = 0

while 1:
	filename = 'capitals.txt' #raw_input("Please enter the name of the file with flashcard:")

	length = fileLength(filename)
	total = correct + incorrect

	linenumber = randint(1, int(length))

	question = getQuestion(filename, linenumber)
	answer = getAnswer(filename, linenumber)

	user_input = raw_input('What is the capital of ' + question + ': ')

	if user_input == 'exit':
		printStats(correct, incorrect, total)
		print 'Goodbye!'
		break

	if user_input == answer:
		correct += 1
		print 'Correct!'
	else:
		incorrect += 1
		print 'Incorrect! The capital of ' + question + ' is ' + answer + '.'







