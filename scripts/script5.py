from html.parser import HTMLParser


class MyHTMLParser1(HTMLParser):
    def handle_comment(self, data):
        if (data.find("\n") > 1):
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if (data != "\n"):
            print(">>> Data")
            print(data)


class MyHTMLParser2(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")


def main():
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser1()
    parser.feed(html)
    parser.close()


if __name__ == "__main__":
    main()
