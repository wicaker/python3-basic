# https://github.com/hacktiv8/phase-0-activities/blob/master/modules/anchor-basic-function.md

# 1 
def shoutOut():
  print('Hello world!')
shoutOut()

# 2
def calculateMultiply(num1, num2):
  return num1 * num2

num1 = 5
num2 = 6

hasilPerkalian = calculateMultiply(num1,num2)
print(hasilPerkalian)

# 3
def processSentence(name, age, address, hobby):
  return f'My Name is {name}, i was {age} year old, i live in {address}, and my hoby is {hobby}'
name = "Agus"
age = 30
address = "Jln. Malioboro, Yogjakarta"
hobby = "gaming"

fullSentence = processSentence(name,age,address,hobby)
print(fullSentence)