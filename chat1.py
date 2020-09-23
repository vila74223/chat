def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig' ) as f:
		for line in f:
			data.append(line.strip())
	return data

def conversion(content):
	new = []
	person = None
	for line in content:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #at fist persone is a null, when it has valus exacute the program
			new.append(person + ':' + line)
	return new

def write_file(filename, content):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in content:
			f.write(line + '\n')

def main():
	data = read_file('input.txt')
	data = conversion(data)
	write_file('output.txt', data)

main()