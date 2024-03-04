from grobid_client.grobid_client import GrobidClient

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "pdfs",output="pdfsOut", n=20)