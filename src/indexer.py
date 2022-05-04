"""Create index.html for Zetelkasten"""
import os
from pathlib import Path

MD_DIR = '../md/'
HT_DIR = '../html/'
PLACEHOLDER = '$body$'

class Entry:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.date = None

def create_entries(md_dir) -> []:
    """Create list of Entry objects"""
    entries = []
    for p in Path(md_dir).glob('**/*.md'):
        convert_md_to_html(p.stem, HT_DIR)
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

def convert_md_to_html(file, html_dir) -> None:
    cmd = 'pandoc --standalone --template=../tmpl/html_page.template {0} -o {1}'
    md_file = MD_DIR + file + '.md'
    html_file = HT_DIR + file + '.html'
    cmd = cmd.format(md_file, html_file)
    print(cmd)
    os.system(cmd)

def create_html_block(entries) -> str:
    """Create html for the given entries"""
    html_block = ""
    for e in entries:
        paragraph = '<p><a href="{0}">{1} ({2})</a></p>\n\r'
        html_block = html_block + paragraph.format(e.url, e.title, e.date)

    return html_block

def read_template(file) -> str:
    with open(file) as f:
        return f.read()


def main():
    """Main method"""
    entries = create_entries(MD_DIR)

    # html block erstellen
    block = create_html_block(entries)

    # template einlesen
    template = read_template(r"../tmpl/index.template")
    # block in template einfügen
    index_html = str(template).replace(PLACEHOLDER, block)
    index_html = str(index_html).replace('.md', '.html')
    # template als index.html in ./html speichern
    index_file = HT_DIR + 'index.html'
    with open(index_file, "w") as f:
        f.write(index_html)


    #print(len(entries))
    #print(block)
    #print(template)



if __name__ == "__main__":
    main()




