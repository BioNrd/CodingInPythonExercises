seq_file = open("seqs.fasta")
max_content = 0
maximum_hash = {}
for line in seq_file.readlines():
    #read in line by line a FASTA file.

    new_line = line.strip("\n")
    #clean off newline endings

    gc_content = 0
    #counter to 0

    if new_line[0] != ">":
        #if the newline is not a >

        sequence_length = len(new_line)
        #get the sequence length

        for nucleotide in new_line:
            if nucleotide.lower() in ['g', 'c']:
                gc_content+=1
        gc_content_figure = round(gc_content / sequence_length, 3)
        maximum_hash.update({name: gc_content_figure})
        #work across each base of the sequence, if it is a g or a c count it else dont
        #sequence is converted to lower case.
        #calculate the g/c content of each sequence and add it to a dictionary

    else:
        name = new_line[1:]
        #if the line has a >, remove the first charecter and keep the rest as the name of the sequence. 
seq_file.close()

#print(maximum_hash)

z = [0]
while maximum_hash:
    key, value = maximum_hash.popitem()
    if value > z[0]:
        z = [value,[key]]
    elif value == z[0]:
        z[1].append(key)
print("Maximum GC content: ", end="")
print(z)
#Iterate over the dictionary to find the max values, and check if there are duplicated max values.
#Code taken from: http://stackoverflow.com/questions/9853302/using-pythons-max-to-return-two-equally-large-values


#Alternative method:
#highest = max(maximum_hash.values())
#print([k for k,v in maximum_hash.items() if v == highest])
