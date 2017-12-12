#!/usr/bin/python
#Author : Ramin Farajpour Cami

'''

Affine Cipher


    Formula to encrypt : ax + b % 26
    Formual to decrypt : IN * (x - b) mod 26

    There are 2 key:
    for example : 17 , 20

    Text = RAMIN

    A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
    -------------------------------------------------------------------
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

    To encrypt :



        R  A  M  I N
        ------------
        17 0  12 8 13


        By using formula encryption ax+b % 26.
        a = first key
        b = second key
        x = is the each letter


        ------------
        R  A  M  I N
        ------------
        17 0  12 8 13
        23 20 16 0 7  <== ax+b % 26
        ------------
        X  U  Q  A H
        ------------

    To decrypt :

        X  U  Q  A  H
        23 20 16 0  7

        By using formula decryption.
        a = first key
        b = second key
        x = 0 - infiniti

        by using first key, find the inverse modular which firstkey * x mod 26 must equal to 1.

        17 * 0 mod 26 != 1
        17 * 1 mod 26 != 1
        .
        .
        .
        17 * 23 mod 26 == 1  <--- 23 is the modular inverse

        by using 23,
        b = second key
        x = is the each letter encrypted letter

        23 *(x-b) mod 26
        --------------------------------------
        X  U  Q  A H
        --------------------------------------
        23 20 16 0 7
        17 0  12 8 13  <== 23 *(x-b) mod 26
        --------------------------------------
        R  A  M  I  N
        --------------------------------------


'''

lst = ["A", "B" ,"C" ,"D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y","Z"]

def helper(cipher_msg):
    cipher_text = ""
    for i in cipher_msg:
        for j in range(len(lst)):
            if i == j:
                char = lst[j].lower()
                cipher_text += char
    return cipher_text

def encrypt(message,key1, key2):

    cipher = []
    for i in message:
        for j in range(len(lst)):
           if i.lower() == lst[j].lower():
                ciph = (key1*j+key2) % 26
                cipher.append(ciph)

    return helper(cipher)

def decrypt(cipher_msg, key1, key2):

    cipher_lst = []
    x = 0
    inverse = 0
    while(True):
        inverse =  key1 * x  % 26
        if (inverse == 1):
            break
        x = x + 1

    for i in cipher_msg:
        for j in range(len(lst)):
            if i.lower() == lst[j].lower():
                cipher_int = x * (j - key2) % 26
                cipher_lst.append(cipher_int)

    return helper(cipher_lst)

def main():

    key1 = 17
    key2 = 20

    msg = "RAMIN"
    encode_msg = encrypt(msg, key1, key2)
    print "Your message encode : %s" % encode_msg

    print "Your message decode : %s" % decrypt(encode_msg, key1, key2)

if __name__ == "__main__":
    main()

