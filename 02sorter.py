# Logan Krohn
# Sample sorter

input = open("output01.txt","r")  # open file, read-only
output = open("sorted.txt", "w") # open file, write

lines = input.readlines()
lines.sort()

for line in lines:
	output.write(line)

input.close()
output.close()
