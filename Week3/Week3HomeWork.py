seq_file = open("seqs.fasta")
max_content = 0
for line in seq_file.readlines():
    gc_content = 0

    if line[0] != ">":
        #print(line)
        sequence_length = len(line)
        for nucleotide in line:
            if nucleotide.lower() in ['g', 'c']:
                gc_content+=1
        gc_content_figure = round(gc_content / sequence_length, 3)

        if max_content > gc_content_figure:
            next
        else:    
            max_content = gc_content_figure
            max_name = name
        #print(name, gc_content)
    else:
        name = line[1:]

print("The maximum GC content is in the sequence named: " + max_name, end="")
print("The GC content of this sequence is: %a" % max_content)

seq_file.close()

#If multiple sequences have the same GC content, the last sequence found will print to the screen.
#To do this properly script, it needs a hash. We have not covered those yet. 