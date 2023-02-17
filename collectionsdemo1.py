#   LIST = mutable, ordered, heterogeneous

#my_fav_things = ["-111", 3.14159, False, "False", "Bill Evans"]
#my_fav_things.append("Raindrops on roses")
#print(my_fav_things, len(my_fav_things))

#mfs = ["-111", 3.14159, False, "False", "Bill Evans"]
#musician = "Bill Evans" # String is a Sequence of ordered elements
#print(mfs[1])
#print(musician[0])

#   Iterate over a collection of strings, til done.
authors = ["Thomas Mann", "James Joyce", "Jane Austin", "Toni Morrison", "Elizabeth Bishop"]
authors_initials = []

for author in authors:
    #print(author, len(author), type(author))
    print(author)

    name = author.split()   # The split (method) creates a LIST of space separated strings
    initials = name[0][0] + name[1][0]   # Concatenate the First & Last initial
    authors_initials.append(initials)   # Create a LIST of concatenated author initials
    print(initials)

print(authors_initials)
