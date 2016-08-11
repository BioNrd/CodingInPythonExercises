from skbio import DNA, read
with open("outfile.fasta", "w") as outfile:
    for seq in read('test_sequences.fasta', format='fasta'):
        new_seq = DNA(seq)
        for protein in new_seq.translate_six_frames():
            if not protein.has_stops():
                outfile.write(">" + str(new_seq.metadata['id']) + "\n" + str(protein) + "\n")