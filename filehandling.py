
def file_open(ufile):
    global file
    file = open(ufile + '.html', 'w')


def text_write(text):
    file.write(f'{text}<br>')


def link_write(text, link):
    file.write(f'<a herf = "{link}">{text}</a><br>')


def image_write(path):
    file.write(f'<img src="{path}"><br>')


def header_write(text):
    file.write(f'<h2>{text}</h2><br>')


def file_close():
    file.close()