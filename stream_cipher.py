#!/usr/bin/python

```             --------------------------
                |      Key Stream        |
                |      Generetor         |
                |                        |
                --------------------------
                              |  
                             XOR    
       Xi------------------->(+)---------------->Yi

    :
        Xi , Yi , Si ∈ {0, 1}.
        Encryption: y i = (Xi) ≡ Xi + Si mod 2.
        Decryption: x i = (Yi) ≡ Yi + Si mod 2.

>>> 
>>> x = 0
>>> s = 1
>>> (x + s) % 2
1
>>> x = 1
>>> (x + s) % 2 <==== X=1 , S=1 XOR ==> Y is 0
0
>>> y = (x + s) % 2 <==== S=1 , Y=0 XOR ==> X is 1 
>>> s = 1 
>>> (y + s) % 2
1
>>> 
```
