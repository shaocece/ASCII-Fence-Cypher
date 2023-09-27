import numpy as np

def reverse_array(num,remainder=''):
	'''
	If the length of code is odd, the last digit will become remainder.
	'''
	x=num
	if x and type(x)=="list":
		pass
	else:
		x=list(num)
	n_array=[]
	x1=[]
	#print(x)
	if len(x)%2==0:
		for i in x:
			if len(str(ord(i)))==2:
				x1.append("0"+str(ord(i)))
			elif len(str(ord(i)))==3:
				x1.append(str(ord(i)))
		for j in range(0,len(x1),2):
			n_array.append(list(x1[j]+x1[j+1]))
			#print(n_array)
		b_list=np.zeros(shape=(6,len(n_array)))
		for k in range(6):
			for  w in range(len(n_array)):
				a_list=n_array[w][k]
				b_list[k][w]=int(a_list)
		n_array=b_list.tolist()
		return n_array,remainder

	elif len(x)%2==1:
		remainder=[]
		if len(str(ord(x[-1])))==2:
			remainder.append(list("0"+str(ord(x[-1]))))
		elif len(str(ord(x[-1])))==3:
			remainder.append(list(str(ord(x[-1]))))
		x.pop()
		return reverse_array(x,remainder)
	
def encrypt(n):
	p,remainder=reverse_array(n)
	#print(remainder)
	cypher=""
	key=""
	for i in range(3):
		for j in range(len(p[0])):
			cypher+=str(int(p[i][j]))
			key+=str(str(int(p[i+3][j])))
	if len(remainder)!=0:
		cypher+=str(remainder[0][0])
		key+=(remainder[0][1]+remainder[0][2])
	return cypher, key

def decrypt(cypher, key):
	cypher=list(str(cypher))
	key=list(str(key))
	if len(cypher)%3!= 1:
		length=int(len(list(cypher))/3)
		c=[]
		code=""
		for i in range(length):
			c.append(cypher[i]+cypher[i+length]+cypher[i+length*2])
			c.append(key[i]+key[i+length]+key[i+length*2])
		for j in range(length*2):
			code+=chr(int(c[j]))
		return code
	else:
		remainder=[]
		remainder.append(cypher[-1]+key[-2]+key[-1])
		print(remainder)
		cypher.pop()
		key.pop()
		key.pop()
		try:
			cypher=''.join(cypher)
			key=''.join(key)
		except:
			code=''
			code+=chr(int(remainder[0]))
			return code
		code=decrypt(cypher,key)
		print(remainder)
		code+=chr(int(remainder[0]))
		return code
if __name__=="__main__":
	test_code="ASCII-Fence_Cypher"
	c,k=encrypt(test_code)
	print(c,k)
	print(decrypt(c,k))