import os

os.system("cls || clear")

description = """
Many people in this game are looking for the easiest way
to pass the notes to the game keyboard, this is a tool to 
help you with that.
"""

print("")
print("Avalonia music converter for pc - Tool")
print(description)
print("")


target = input("Put letters of the music: ").lower()

print("")

if target.__contains__("do*") or target.__contains__("do") or target.__contains__("re") or target.__contains__("mi") or target.__contains__("fa") or target.__contains__("sol") or target.__contains__("la") or target.__contains__("si"):
	print("Result: " + target.replace("do*", "k").replace("do", "a").replace("re", "s").replace("mi", "d").replace("fa", "f").replace("sol", "g").replace("la", "h").replace("si", "j"))
else:
	print("It appears that nothing was found to replace")
