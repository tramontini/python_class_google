import sys

def repeat(s, exclaim):
	result = s * 3 # The same as s + s + s
	if exclaim:
		result = result + '!!!'
	return result 

def main():
	print repeat('Yay', False)
	print repeat('Woo', True)

if __name__ == '__main__':
	main()