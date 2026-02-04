#!/bin/python3

import requests
import subprocess

def selected_text():
    return subprocess.check_output(["wl-paste","--primary", "--no-newline"]).decode()

def word_meaning(json_format):
    if isinstance(json_format,tuple):
        return "Something went wrong, maybe internet..."

    elif isinstance(json_format,dict):
        return "No word Found."

    elif isinstance(json_format,list):
        return json_format[0]['meanings'][0]['definitions'][0]['definition']

def fetch_word_in_site(site):
    try:
        return requests.get(site).json()

    except requests.exceptions.RequestException as e:
        return ()

def send_notification(word, output):
    subprocess.run(["notify-send","-t", "15000",f"Word: {word}",f"meaning -> {output}"])

def main():
    word = selected_text()
    site = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    json_format = fetch_word_in_site(site)
    send_notification(word,word_meaning(json_format))

if __name__=="__main__":
    main()
