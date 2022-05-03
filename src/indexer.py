"""Create index.html for Zetelkasten"""
from pathlib import Path

MD_DIR = '../md/'
HT_DIR = '../html/'

class Entry:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.date = None

def create_entries(md_dir) -> []:
    """Create list of Entry objects"""
    entries = []
    for p in Path(md_dir).glob('**/*.md'):
        with p.open() as f:
            lines = f.readlines()
            entry = Entry(p.name)
            for line in lines:
                if line.startswith('title:'):
                    entry.title = line.split(":")[1].strip()
                if line.startswith('date:'):
                    entry.date = line.split(":")[1].strip()

            entries.append(entry)

    return entries


def main():
    """Main method"""
    entries = create_entries(MD_DIR)

    print(len(entries))


if __name__ == "__main__":
    main()




