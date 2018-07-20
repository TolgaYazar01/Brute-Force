alphabet = "abcdefghijklmnopqrstuvwxyz"
secretmessage = ""

def decode (secretmessage) :
    for key in range(0, len(alphabet)):
        newAlphabet = alphabet[key:] + alphabet[:key]
        attempt = ""

        for i in range(len(secretmessage)):
            index = alphabet.find(secretmessage[i])
            
            if index < 0:
                attempt += secretmessage[i]
            else:
                attempt += newAlphabet[index]
        print("key: " + str(key) + " - " + attempt)

        
        
msg = input("enter msg: ")
decode(msg)
