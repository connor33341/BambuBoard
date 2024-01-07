# https://github.com/connor33341/BambuBoard

# Imports
import time
from jsonRW import JsonReader
from log import log

# Data & Cfg
ReaderClass = JsonReader("config.json")
ReaderData = ReaderClass.Read()

HttpPort = ReaderData["HttpPort"]
PrinterUrl = ReaderData["PrinterUrl"]
PrinterPort = ReaderData["PrinterPort"]
PrinterSN = ReaderData["PrinterSN"]
PrinterAccessCode = ReaderData["PrinterAccessCode"]

# Main
if __name__ == "__main__":
    log("[INFO]: Server Starting")