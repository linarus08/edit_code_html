import os
import html
import glob


def change_encoding(path):
    # for HEX html CRLC
    for (dir_path, dir_names, file_names) in os.walk(path):
        for file in glob.glob('**/*.html', recursive=True):
            with open(file, 'r', encoding='cp1251') as f:
                text = html.unescape(f.read())
                new_file = f.name
                with open(new_file, 'w', encoding='utf-8') as nf:
                    nf.write(text)
        break


if __name__ == "__main__":
    path = r'...'
    change_encoding(path)
