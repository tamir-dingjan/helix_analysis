import multiseq

proteins = ["P12345", "P67804"]
m = multiseq.Multiseq(ids=proteins)
m.build_dataset()