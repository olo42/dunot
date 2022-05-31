"""Create index.html for Zetelkasten"""
import os
from datetime import datetime
from pathlib import Path

MD_DIR = '../md/'
HT_DIR = '../html/'
PLACEHOLDER = '$body$'

class Entry:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.date = None
        self.time = None

def create_entries(MD_DIR) -> [Entry]:
    """Create list of Entry objects"""
    entries = []
    for p in Path(MD_DIR).glob('**/*.md'):
        convert_md_to_html(p.stem, HT_DIR)
        with p.open() as f:
            lines = f.readlines()
            entry = Entry(p.name)
            for line in lines:
                if line.startswith('title:'):
                    entry.title = line.split(":")[1].strip()
                if line.startswith('date:'):
                    date_time_str = line.split(": ")[1].strip()
                    date_time = date_time_str.split(" ")
                    entry.date = datetime.strptime(date_time[0].strip(), '%d.%m.%Y')
                    if len(date_time) > 1:
                        entry.time = datetime.strptime(date_time[1].strip(), '%H:%M')

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
        paragraph = '<p><a href="{0}">{1}</a><br /><small>{2} {3}</small></p>\n\r'
        date = e.date.strftime("%d.%m.%Y") 
        if e.time != None:
            time = e.time.strftime("%H:%M")
        html_block = html_block + paragraph.format(e.url, e.title, date, time)

    return html_block

def read_template(file) -> str:
    with open(file) as f:
        return f.read()

def parse_template(template, block) -> str:
    index_html = str(template).replace(PLACEHOLDER, block)
    index_html = str(index_html).replace('.md', '.html')
    return index_html


def main():
    """Main method"""
    entries = create_entries(MD_DIR)
    entries.sort(key=lambda x: x.date, reverse=True)
    block = create_html_block(entries)
    template = read_template(r"../tmpl/index.template")
    index_html = parse_template(template, block)

    # save template as index.html
    index_file = HT_DIR + 'index.html'
    with open(index_file, "w") as f:
        f.write(index_html)

if __name__ == "__main__":
    main()




