import random


def text_process(text):
    #making sure text can be split into 2 equal parts
    if (len(text)%2) != 0:
        text += ' '
    return text


#key generator taking seed derived from len(text)
def key_gen(seed, length): 
    key = "" 
    random.seed(seed)

    #generating key of length as data string/2; + 1 incase 1st no. is 0
    for i in range(int(length/2) +1): 
        temp = random.randint(0,9)  
        key = key + str(temp) 
          
    return(key) 


#xor_func function through 2 lists
#int(list2) to be able to index the key string and use as an integer mainly for when list2 is a key
def xor_func(list1, list2):
    lst = []
    for i in range(len(list1)):
        lst.append(list1[i] ^ int(list2[i]))
    return lst


def feistel_encrypt(data_string, k1, k2):
    #getting ascii list of data string
    data_string = [ord(x) for x in data_string]
    length = len(data_string)

    #dividing data into 2 equal parts
    l1 = data_string[:int(length/2)]
    r1 = data_string[int(length/2):]

    #round 1
    f1 = xor_func(r1, k1)
    l2 = r1
    r2 = xor_func(f1, l1)

    #round 2
    f2 = xor_func(r2, k2)
    l3 = r2
    r3 = xor_func(f2, l2)

    cipher_list = l3 + r3
    cipher_char = [chr(i) for i in cipher_list]
    cipher_text = ''.join(cipher_char)
    return cipher_text


def feistel_decrypt(cipher_text, k1, k2):
    #getting ascii list of data string
    data_string = [ord(x) for x in cipher_text]
    length = len(data_string)

    #dividing data into 2 equal parts
    l4 = data_string[:int(length/2)]
    r4 = data_string[int(length/2):]

    #round 1
    f3 = xor_func(l4, k2)
    l5 = xor_func(r4, f3)
    r5 = l4

    #round 2
    f4 = xor_func(l5, k1)
    l6 = xor_func(r5, f4)
    r6 = l5

    ans_list = l6 + r6
    ans_char = [chr(i) for i in ans_list]
    ans_text = ''.join(ans_char)
    return ans_text

