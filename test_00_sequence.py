import sequence

s = sequence.Sequence("uniprot", "P67804")
s.fetch_sequence()
s.analyse_aa_composition()