#!/bin/python3

import requests
import subprocess

def selected_text():
    return subprocess.check_output(["wl-paste","--primary", "--no-newline"]).decode()

def word_meaning(json_format):
    if json_format is None:
        return "Something went wrong, maybe bad internet ...😭"

    elif isinstance(json_format,dict):
        if not json_format['entries']:
            return "No meaning found of that word.🥺"
        else:
            return json_format['entries'][0]['senses'][0]['definition']

def get_example(json_format):
    if json_format is None:
        return "Can't get examples if you get errors.🥴"

    entries = json_format['entries']

    for entry in entries:
        for sense in entry['senses']:
            examples = sense.get('examples', [])
            if examples:  
                return examples[0]

    return "No example found.🫩"

def fetch_word_in_site(site):
    try:
        return requests.get(site).json()

    except requests.exceptions.RequestException as e:
        return None

def send_notification(word, meaning,json_format):
    subprocess.run(["notify-send","-t", "15000",f"Word: {word}",f"\nmeaning -> {meaning} \n\n example -> {get_example(json_format)}"])

def main():
    word = selected_text()
    site = f"https://freedictionaryapi.com/api/v1/entries/en/{word}"
    json_format = fetch_word_in_site(site)
    example = get_example(json_format)
    send_notification(word,word_meaning(json_format),json_format)

if __name__=="__main__":
    main()
