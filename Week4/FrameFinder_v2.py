import csv

def check_this_sequence(sequence, start):
    protein=[]
    reading_frame = start + 1
    print("Frame = "+str(reading_frame),end="\t")
    for i in range(start, len(sequence), 3):
        codon = sequence[i:i+3]
        #print(codon, end=",")
        #Traveses the length of the sequence 3 spaces at a time.
        #Codon is a slice of 3 bases of the sequence starting at position i
        #Code from http://stackoverflow.com/questions/13496790/python-iterating-over-a-string-by-2-characters

        aa = get_this_aa(codon)
        #query the codon dictionary using a function

        protein.append(aa)
        #buld up that protien sequence!! We will check for stop codons below. 

    return(protein)

def get_this_aa(codon):
    if len(codon) < 3:
        return('')
    else:
        #print(codon_codes['TTT'])
        return(codon_codes[codon])

##
#Open code file and populate the dictionary
codon_codes = {}
with open('standard_code.tsv', 'r') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    for row in reader:
        codon_codes[row['Codon']] = row['Amino Acid']


##
#open the sequence file, and check the reading frames
with open('test_sequences.txt', 'r') as infile:
    reader = infile

    for sequence in reader:
        sequence = sequence.strip("\n")
        print("\nSequence:\t"+sequence)
        
        for start in [0,1,2]:

            aa_list = check_this_sequence(sequence, start)
            
            if ('*' in aa_list[-1]):
                #check is * is at the end of the list. If so, this is still a potential valid translation.
                aa_string = ''.join(map(str,aa_list))
                #get ready to print items of a list without the extra '[]' and ',' stuff.
                print(aa_string)

            elif any("*" in s for s in aa_list):
                #else if * is anywhere else in the list, it is not the correct frame.
                print("Stop codon found mid-translation")

            else:
                #else, there are no stops, so it is a potential correct frame. 
                aa_string = ''.join(map(str,aa_list))
                print(aa_string)
                #print(" :protein: " + aa_string)
