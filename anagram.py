s1 = 'apple'
s2  = 'pleap'
c1 = [0] * 26
c2 = [0] * 26

for i in range(len(s1)):
	pos = ord(s1[i])-ord('a')
	c1[pos] = c1[pos] + 1

print(c1)

for i in range(len(s2)):
	pos = ord(s2[i])-ord('a')
	c2[pos] = c2[pos] + 1

print(c2)

print(c1 == c2)