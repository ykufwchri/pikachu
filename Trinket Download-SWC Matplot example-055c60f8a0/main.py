import os as myos   # module with alias

# read a text file
with open("story.txt", "r") as f:
    story = f.read()

print(story)

files = ["story.txt", "story1.txt", "story3.txt"]

for filename in files:
    with open(filename, "r") as f:
        print(f"--- {filename} ---")
        print(f.read(), "\n")