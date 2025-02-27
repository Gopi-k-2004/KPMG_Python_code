count =0
max_attempt =5

pw = ''
secretWord = "swordFish"

while pw!=secretWord:
    count +=1
    if count > max_attempt:break
    if count ==3 : continue
    pw = input(f"{count} : what is your secret word?")
else:
    auth = True

print("Authorized" if auth else "Not Authorized...")

words = ('sky','tree','rain','water','road')

for word in words:
    if word == 'rain' : continue
    if word == 'mapper' : break
    print(word)
else:
    print("This is all the data we have")

