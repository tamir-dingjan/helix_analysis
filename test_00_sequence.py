import sequence

s = sequence.Sequence("uniprot", "P12345")
s.fetch_sequence()
s.analyse_aa_composition()