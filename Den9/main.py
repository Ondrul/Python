programing_dictonary = {"Bug": "An error that prevent the program from running expected.",
                        "Function": "A piece of code that you can easily call over and over again."}
print(programing_dictonary["Bug"])
programing_dictonary["Loop"] = "The action of doing something over and over again"
print(programing_dictonary)

#programing_dictonary = {}
#print(programing_dictonary)
for thing in programing_dictonary:
    print(thing)
    print(programing_dictonary[thing])