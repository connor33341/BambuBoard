from jsonRW import JsonReader

ReaderClass = JsonReader("config.json")
ReaderData = ReaderClass.Read()

ConsoleLogging = ReaderData["ConsoleLogging"]

def log(Text):
    if ConsoleLogging:
        print(Text)
