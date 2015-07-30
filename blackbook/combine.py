combined = ''

for i in range(77, 99):
	with open('text/p'+str(i)+'.txt') as page:
		print(page)
		for line in page.readlines():
			combined += line

print('writing combined text to combined.txt')
f = open('combined.txt', 'w+')
f.write(combined)
f.close()
