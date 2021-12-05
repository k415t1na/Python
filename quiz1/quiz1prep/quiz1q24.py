#Write a python program to ask the user to enter a sentence and write each letter on a new line

wq=input("Enter the sentence: ")
word= wq
for index,letter in enumerate(word,1):
    print(index,":",letter)
