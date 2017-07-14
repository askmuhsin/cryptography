##Substitution Cipher
##Input: string, key.
##Output: ciphered text.
##Create a method to Decipher by ; Input: cipher text, key

class SubCipher:

    def __init__(self, text, key):
        self.text = text
        self.key = key
        print("---------------------------------------------------------------")
        print("Original Text :", self.text)
        print("Key :", self.key)
        print("---------------------------------------------------------------")

    def cipher(self):
        k = ord(self.key) - 97
        if (k>=0 and k<27):
            cText = SubCipher.cipherCalc(SubCipher, self.text, k)
            print ("Cipher text :", cText)
        else:
            print("Invalid key!")
        print("---------------------------------------------------------------")

    def cipherCalc(self, text, key):
        k = key
        a = list(text)
        cipher_text = ""
        for i in range(len(a)):
            j = ord(a[i]) #check for non alphabets
            if (j>96 and j<123) or (j>64 and j<91): #check for non alphabets
                q = ord(a[i]) + k #ascii roll back check; z + 1 = a
                if ((q>122 and q<147) and (j>96 and j<123)) or ((q>90 and q<115) and (j>64 and j<91)):
                    cipher_text += chr( (ord(a[i]) + k)- 26)
                else:
                    cipher_text += chr( ord(a[i]) + k )
            else:
                cipher_text += a[i]
        return cipher_text

    def allCipher(self):
        cText = ""
        for i in range(0,26):
            cText = SubCipher.cipherCalc(SubCipher, self.text, i)
            print("Key :", chr(i+97),(format(i, '02d')) , "Cipher Text :", cText)
            cText=""
        print("---------------------------------------------------------------")

def main():
    ins = SubCipher("To be or not to be, That is the question", 'g')
    ins.cipher()
    ins.allCipher()

if __name__ == '__main__':
    main()
