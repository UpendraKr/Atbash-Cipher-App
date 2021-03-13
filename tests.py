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

def test_atbash_cipher_convert():
    string = "abc"
    s = atbash_cipher_convert(string)
    assert s == 'zyx'

def test_check_capitalization():
    string = "AbC"
    s = atbash_cipher_convert(string)
    assert s == 'ZyX'

def test_check_non_alphabets():
    string = "AbC123!!"
    s = atbash_cipher_convert(string)
    assert s == 'ZyX123!!'