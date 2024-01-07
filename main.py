# https://github.com/connor33341/BambuBoard

# Imports
import time
from jsonRW import JsonReader
from log import log
from update import UpdateSystem
import os

# Data & Cfg
ReaderClass = JsonReader("config.json")
ReaderData = ReaderClass.Read()

HttpPort = ReaderData["HttpPort"]
PrinterUrl = ReaderData["PrinterUrl"]
PrinterPort = ReaderData["PrinterPort"]
PrinterSN = ReaderData["PrinterSN"]
PrinterAccessCode = ReaderData["PrinterAccessCode"]
AutoUpdate = ReaderData["AutoUpdate"]
NodeStartCMD = ReaderData["NodeStartCMD"]

# Main
if __name__ == "__main__":
    log("[INFO]: Server Starting")
    UpdateClass = UpdateSystem(AutoUpdate)
    try:
        UpdateClass.CFU()
        UpdateClass.BWD()
    except (Exception) as Error:
        print("[ERROR]: "+Error)
    os.chdir("web")
    os.system(NodeStartCMD)
