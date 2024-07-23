#My first practice with strings
text = "Hello I'm: Santiago"
#finding the colon
index = text.find(":")
#Creating a list to know where I can find my name
data = text[index + 1:].strip()
#To print the data
print(data)
# print(text.find(":"))