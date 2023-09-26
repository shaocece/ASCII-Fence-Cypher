import numpy as np

def get_digit(text):
#If ascii code of any letter is not 2 digits, the error will occur and print out information
	text=list(text)
	for i in text:
		if len(str(ord(i)))==2:
			pass
		else:
			print("Invalid Code")
			return InvalidSyntax
	return text

def reverse_array(num,remainder=''):
	'''
	If the length of code is odd, the last digit will become remainder.
	'''
	x=num
	if x and type(x)=="list":
		pass
	else:
		x=get_digit(num)
	n_array=[]
	x1=[]
	#print(x)
	if len(x)%2==0:
		for i in x:
			x1.append(str(ord(i)))
		for j in range(0,len(x1),2):
			n_array.append(list(x1[j]+x1[j+1]))
			#print(n_array)
		b_list=np.zeros(shape=(4,len(n_array)))
		for k in range(4):
			for  w in range(len(n_array)):
				a_list=n_array[w][k]
				b_list[k][w]=int(a_list)
		n_array=b_list.tolist()
		#print(remainder)
		return n_array,remainder
		'''
		'''
	elif len(x)%2==1:
		remainder=[]
		remainder.append(list(str(ord(x[-1]))+"r"))
		x.pop()
		return reverse_array(x,remainder)
	
def encrypt(n):
	p,remainder=reverse_array(n)
	#print(remainder)
	cypher=""
	key=""
	for i in range(2):
		for j in range(len(p[0])):
			cypher+=str(int(p[i][j]))
			key+=str(str(int(p[i+2][j])))
	if len(remainder)!=0:
		cypher+=str(remainder[0][0])
		key+=(remainder[0][1])
	return cypher, key

def decrypt(cypher, key):
	cypher=list(str(cypher))
	key=list(str(key))
	if len(cypher)%2!= 1:
		length=int(len(list(cypher))/2)
		c=[]
		code=""
		for i in range(length):
			c.append(cypher[i]+cypher[i+length])
			c.append(key[i]+key[i+length])
		for j in range(len(cypher)):
			code+=chr(int(c[j]))
		return code
	else:
		remainder=[]
		remainder.append(cypher[-1]+key[-1])
		#print(remainder)
		cypher.pop()
		key.pop()
		try:
			cypher=int(''.join(cypher))
			key=int(''.join(key))
		except:
			code=''
			code+=chr(int(remainder[0]))
			return code
		code=decrypt(cypher,key)
		code+=chr(int(remainder[0]))
		return code
if __name__=="__main__":
	test_code="ASCII"
	c,k=encrypt(test_code)
	print(c,k)
	print(decrypt(c,k))