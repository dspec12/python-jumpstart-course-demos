"""
Journal module
"""
import os


def load():

    data = []
    filename = get_full_pathname()

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                data.append(line.rstrip())

    return data


def save(journal_data):

    filename = get_full_pathname()

    with open(filename, 'w') as f:
        for entry in journal_data:
            f.write(entry + '\n')


def add(entry, journal_data):
    journal_data.append(entry)


def remove(entry, journal_data):
    del journal_data[entry]


def get_full_pathname():
    filename = os.path.abspath(os.path.join('.', 'save.jrl'))
    return filename
