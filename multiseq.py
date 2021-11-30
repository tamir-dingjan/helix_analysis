# multiseq.py - Class and methods for handling a set of sequences

import pandas as pd
import sequence


class Multiseq:
    def __init__(self, ids=None):
        self.dataset = []
        self.table = None
        self.ids = None
        self.amino_acids = ['A',
                            'R',
                            'N',
                            'D',
                            'B',
                            'C',
                            'E',
                            'Q',
                            'Z',
                            'G',
                            'H',
                            'I',
                            'L',
                            'K',
                            'M',
                            'F',
                            'P',
                            'S',
                            'T',
                            'W',
                            'Y',
                            'V']

        if not (ids is None):
            self.ids = ids

    def build_dataset(self):
        if self.ids is None:
            raise Exception("ERROR: No IDs present in Multiseq! Cannot build sequences.")

        for i in self.ids:
            s = sequence.Sequence("uniprot", i)
            s.fetch_sequence()
            s.analyse_aa_composition()
            self.dataset.append(s)

        # Populate the results table
        scientific_names = [x.id.get('scientific_name', None) for x in self.dataset]
        protein_names = [x.id.get('protein_name', None) for x in self.dataset]
        seq_lengths = [x.seq_length for x in self.dataset]
        sequences = [x.sequence for x in self.dataset]

        self.table = pd.DataFrame(list(zip(scientific_names,
                                           protein_names,
                                           seq_lengths,
                                           sequences)),
                                  columns=['scientific_name',
                                           'protein_name',
                                           'sequence_length',
                                           'sequence'])

        for aa in self.amino_acids:
            self.table[aa] = [s.composition.get(aa, None) for s in self.dataset]
