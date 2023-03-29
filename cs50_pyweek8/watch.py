import re
import sys

def main():
    print(parse(input("HTML: ")))

# extracts the youtube link from <iframe src="x"></iframe>
# where x can be one of the following:
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

def parse(s):
    if match := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{match.group(2)}"
    else:
        return None
    
main()

