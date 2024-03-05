import os
from grobid_client_python.grobid_client.grobid_client import GrobidClient

if not os.path.isdir('pdfsOut'):
    os.makedirs("pdfsOut")
else:
    for f in os.scandir('pdfsOut'):
        os.remove(f.path)
        
client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "pdfs",output="pdfsOut", n=20)