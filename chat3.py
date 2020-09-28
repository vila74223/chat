content = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		content.append(line.strip())

for line in content:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)

