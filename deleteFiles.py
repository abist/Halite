import os

fileList = [f for f in os.listdir(".") if f.endswith(".hlt") or f.endswith(".log") or f.endswith(".py~") or f.endswith(".md~")]
for f in fileList:
    os.remove(f)
