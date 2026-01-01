a = """Hi,
This is a multi-line string."""
b = '''Hello,
This is another multi-line string.'''
print(a)
print(b)

a="welcome to mashup stack"
print (len(a))


paragraph = "This is a sample paragraph for string indexing and slicing." \
" It contains multiple sentences to demonstrate various string operations."\
"the python course is very simple"\
" Let's explore indexing and slicing in Python strings"
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])


print("slicing:",paragraph[:50])

text = "python"
print(text.upper())

text="WELCOME TO MASHUP STACK"
print(text.lower())


text = "   Hello, World!   "
print(text.strip())



a = "Mashup, Stack!"
b = a.split(",")
print(b)

print("checking:","course" in paragraph)


course_description = "Learn Python programming from scratch."
length = len(course_description)
word_count = len(course_description.split())
result = "The course description is {} characters long and has {} words.".format(length, word_count)
print(result)