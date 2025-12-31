a = """Hi,
This is a multi-line string."""
b = '''Hello,
This is another multi-line string.'''
print(a)
print(b)

a="welcome to mashup stack"
print (len(a))


paragraph = "This is a sample paragraph for string indexing"
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])


print("Preview (first 50 characters):", paragraph[:50])
print("From index 10 to 30:", paragraph[10:31])
print("From start to index 20:", paragraph[:21])
print("From index 15 to end:", paragraph[15:])


text = "python"
print(text.upper())

text="WELCOME TO MASHUP STACK"
print(text.lower())


text = "   Hello, World!   "
print(text.strip())



a = "Mashup, Stack!"
b = a.split(",")
print(b)


course_description = "Learn Python programming from scratch."
length = len(course_description)
word_count = len(course_description.split())
result = "The course description is {} characters long and has {} words.".format(length, word_count)
print(result)