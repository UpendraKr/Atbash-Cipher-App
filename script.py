import sys

def atbash_cipher_convert(string):
    reverse_alpha = "zyxwvutsrqponmlkjihgfedcba"
    upper_reverse_alpha = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    l = len(string)
    ans = ""
    for i in range(l):
        if string[i] == ' ':
    	    ans = ans + ' '
    	    continue
	if string[i] == '\n':
    	    ans = ans + '\n'
    	    continue
	if not string[i].isalpha():
    	    ans = ans + string[i]
    	    continue
    	if string[i].isupper():
    	    ans = ans + upper_reverse_alpha[ord(string[i])-ord('A')]
    	else:
            ans = ans + reverse_alpha[ord(string[i])-ord('a')]
    return ans
    
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as file1:
    data = file1.read()

data = data.strip(' ')
ans_data = atbash_cipher_convert(data)

with open(output_file, 'w') as file2:
    file2.write(ans_data)
