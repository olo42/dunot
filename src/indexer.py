"""Create index.html for Zetelkasten"""
from pathlib import Path

MD_DIR = '../md/'
HT_DIR = '../html/'

class Entry:
    def __init__(self, url):
        self.url = url

entries = []

for p in Path(MD_DIR).glob('**/*.md'):
    with p.open() as f:
        lines = f.readlines()
        entry = Entry(p.name)
        for line in lines:
            if line.startswith('title:'):
                entry.title = line.split(":")
            if line.startswith('date:'):
                entry.date = line.split(":")

        entries.append(entry)

print(len(entries))



