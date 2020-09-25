def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig' ) as f:
		for line in f:
			data.append(line.strip())
	return data


def conversion(content):
	person = None
	allenword = 0
	vikiword = 0
	allenstick = 0
	vikistick = 0
	allenpicture = 0
	vikipicture = 0
	for line in content:
		d = line.split(' ')
		time = d[0]
		name = d[1]
		if name == 'Allen':
			if d[2] ==  "貼圖":
				allenstick += 1
			elif d[2] == "圖片":
				allenpicture += 1
			else:	
				for content in d[2:]:
					allenword += len(content)	
		elif name == 'Viki':
			if d[2] ==  "貼圖":
				vikinstick += 1
			elif d[2] == "圖片":
				vikipicture += 1
			else:	
				for content in d[2:]:
					vikiword += len(content)	
	print('allen said', allenword, 'words.') 
	print('allen sent', allenstick, 'stickers.')	
	print('allen sent', allenpicture, 'pictures.')
	
	print('viki said', allenword, 'words.') 
	print('viki sent', allenstick, 'stickers.')	
	print('viki sent', allenpicture, 'pictures.')



def write_file(filename, content):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in content:
			f.write(line + '\n')


def main():
	data = read_file('LINE-Viki.txt') #myth 1 'data = ' can be omitted
	data = conversion(data)  #myth 2 here 'data' replaced 'new'


main()