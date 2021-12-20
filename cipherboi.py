def cipher(a,b):
    
    ascii=[]
    for character in a:
        ascii.append(ord(character))
    print(ascii)
        
   
    for i in range(0,len(ascii)):
        ascii[i]=ascii[i]+b
        if(ascii[i]>90 and ascii[i]<97):
            ascii[i]=65
        if(ascii[i]>122):
            ascii[i]=97
    print(ascii)
        
    string=[]
    for numbers in ascii:
        string.append(chr(numbers))
    print(string)
    
    print(" ".join(string))
    
    
    


cipher("DEFENDTHEFORT",7)




def decrypt(a,b):
    
    ascii=[]
    for character in a:
        ascii.append(ord(character))
    print(ascii)
        
   
    for i in range(0,len(ascii)):
        ascii[i]=ascii[i]-b
        if(ascii[i]<65):
            ascii[i]=84
    print(ascii)
        
    string=[]
    for numbers in ascii:
        string.append(chr(numbers))
    print(string)
    
    print(" ".join(string))


decrypt("KLMLUKAOLMVYA",7)

print("small code")
