#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        try:
            print('\t- utf8 content: {}'.format(content.decode("utf-8")))
        except UnicodeDecodeError as e:
            print('\t- Error decoding UTF-8 content:', e)
            print('\t- utf8 content: {}'.format(content.decode("utf-8", "ignore")))
