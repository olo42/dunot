"""Create index.html for Zetelkasten"""
from pathlib import Path

MD_DIR = '../md/'
HT_DIR = '../html/'

class Entry:
    def __init__(self, url):
        self.url = url
        self.title = ''
        self.date = ''

    def set_title(self, title):
        self.title = title

    def get_title(self) -> str:
        return self.title

    def set_date(self, date):
        self.date = date

def create_entries(md_dir) -> []:
    """Create list of Entry objects"""

    entries = []

    for p in Path(md_dir).glob('**/*.md'):
        with p.open() as f:
            lines = f.readlines()
            entry = Entry(p.name)
            for line in lines:
                if line.startswith('title:'):
                    entry.set_title(line.split(":"))
                if line.startswith('date:'):
                    entry.set_date(line.split(":"))

            entries.append(entry)

    return entries


def main():
    """Main method"""
    entries = create_entries(MD_DIR)

    print(len(entries))
    
    for e in entries:
        print(e.get_title())


if __name__ == "__main__":
    main()




