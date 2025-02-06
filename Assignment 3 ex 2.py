#def repeat(thing, n):
#    return (thing * n)

#def repeat(thing, n):
#    result = ""
#    for i in range(n):
#        result += thing
#    return result

#thing = input("SPAM BOT \n type something you want spammed!: ")
#n = int(input("how many times do you want to SPAM IT:(number)"))

#print(repeat(thing, n))

def print_right(text):
    print(" " * (40 - len(text)) + text)


print_right("hello")