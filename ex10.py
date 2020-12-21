tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t\t* Grass
"""

slim_cat = '''
I'm a slim cat
\t* I want to be a fat cat
\t\t Maybe I need more food
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print slim_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
