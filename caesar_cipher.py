'''
    KEY + 1

    A == B
    B == C
    C == D
    ...

    Z = A

    Algorithm definition :

        plaintext  = ATTACKATDAWN
        alpha      = ABCDEFGHIJKLMNOPQRSTUVWXYZ
        key        = BCDEFGHIJKLMNOPQRSTUVWXYZA
        ciphertext = BUUBDLBUEBXO

        x : index key ( T = 17 , A = 0)
        n : rotation (3 or 5 )
        Encrypt(x) = (x + n) % 26
        Decrypt(x) = (x - n) % 26

        example :
            Plaintext: the grass is always greener
            Encrytped: ymj lwfxx nx fqbfdx lwjjsjw
            Decrytped: the grass is always greener
'''



key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

def show_result(plaintext, n):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(n, plaintext)
    decrypted = decrypt(n, encrypted)

    print 'Rotation: %s' % n
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted


show_result("Ramin", 3)
