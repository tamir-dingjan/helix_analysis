# sequence.py - Class and methods for holding a sequence object

import requests
from collections import Counter
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

class Sequence:
    def __init__(self, label=None, id=None, seq=None):
        self.id = {}
        self.sequence = None
        self.composition = None
        self.seq_length = None

        if not (label is None) and not (id is None):
            self.set_id(label, id)

        if not (seq is None):
            self.set_sequence(seq)

    def set_id(self, label, id):
        self.id[label] = id

    def set_sequence(self, seq):
        self.sequence = seq
        self.seq_length = len(seq)

    def fetch_sequence(self):
        if self.id.get("uniprot", None) is None:
            raise Exception("ERROR: No Uniprot ID set! Cannot fetch sequence.")

        uniprot_site_prefix = "https://www.uniprot.org/uniprot/"

        fasta = requests.get(uniprot_site_prefix + self.id["uniprot"] + ".fasta").text.split("\n")
        self.record = requests.get(uniprot_site_prefix + self.id["uniprot"] + ".xml")

        self.set_sequence("".join(fasta[1:]))
        self.id["uniprot_header"] = fasta[0]

        # self.data = ET.fromstring(self.record.text)

        self.data = BeautifulSoup(self.record.text, 'xml')
        self.id["scientific_name"] = self.data.find('organism').find('name', {'type':"scientific"}).text

    def analyse_aa_composition(self):
        if self.sequence is None:
            raise Exception("ERROR: No sequence set! Cannot analyse amino acid composition")

        raw_counts = Counter(self.sequence)

        # Convert raw counts into a percentage
        self.composition = {res: raw_counts[res] / self.seq_length * 100.0 for res in raw_counts}




