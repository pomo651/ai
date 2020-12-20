import re

def main():
    # read file line by line
    file = open( "demo.srt", "r")
    lines = file.readlines()
    file.close()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            text += '。' + line.rstrip('\n')
        text = text.lstrip()

    text_file = open("demo.txt", "w")
    text_file.write(text)
    text_file.close()

main()
