import csv

#Open code file and populate the dictionary
def codon_coder_definer():
    codon_codes = {}
    with open('standard_code.tsv', 'r') as infile:
        reader = csv.DictReader(infile, delimiter='\t')
        for row in reader:
            codon_codes[row['Codon']] = row['Amino Acid']
    return codon_codes

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))
#http://stackoverflow.com/questions/7654971/parsing-a-fasta-file-using-a-generator-python

def is_dna(sequence):
    for base in sequence:
        if base.upper() not in ['A', 'T', 'C', 'G']:
            return False
    return True

def check_this_sequence(sequence, start):
    protein=[]
    reading_frame = start + 1
    #print("Frame = "+str(reading_frame),end="\t")
    for i in range(start, len(sequence), 3):
        #Code from http://stackoverflow.com/questions/13496790/python-iterating-over-a-string-by-2-characters
        #walks from starting postion to the end of the sequence 3 postions at a time. [e.g., 0, 3, 6, 9]
        #however 'i' is just the starting index. To get the 3 postions after the index:
        codon = sequence[i:i+3]
        #print(codon, end=",")

        aa = get_this_aa(codon)
        #query the codon dictionary using a function

        protein.append(aa)
        #buld up that protien sequence!! We will check for stop codons below. 

    return(protein)

def get_this_aa(codon):
    if len(codon) < 3:
        return('')
    else:
        return(codon_codes[codon])
        #print(codon_codes['TTT'])

def printer(name,aa_list):
    aa_string = ''.join(map(str,aa_list))
    #get ready to print items of a list without the extra '[]' and ',' stuff.
    f.write(name+'\n'+aa_string+'\n')


#############

codon_codes = codon_coder_definer()

f = open('translation.fasta', 'w')

with open('test_sequences.txt') as fp:
    for name, seq in read_fasta(fp):
        #print(name, seq)
        print("Working on "+name[1:])
        stop_counter=0
        if is_dna(seq):
            for start in [0,1,2]:

                aa_list = check_this_sequence(seq, start)

                if ('*' in aa_list[-1]):
                    #check is * is at the end of the list. If so, this is still a potential valid translation.
                    printer(name,aa_list)
                    
                elif any("*" in s for s in aa_list):
                    #else if * is anywhere else in the list, it is not the correct frame.
                    stop_counter += 1
                    next

                else:
                    #else, there are no stops, so it is a potential correct frame. 
                    printer(name,aa_list)
                    
            if stop_counter >= 3:
                print("Stop codon found mid-translation in all frames of "+name[1:])

        else: 
            print('Bad Input in '+name[1:])        