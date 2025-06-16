import pyreadstat

def extract_datasets():
    demographics, _ = pyreadstat.read_xport("DEMO_J.XPT")
    nutrients, _ = pyreadstat.read_xport("DR1TOT_J.XPT")
    body, _ = pyreadstat.read_xport("BMX_J.XPT")
    return demographics, nutrients, body