import os
import requests
import shutil
import platform
import subprocess


def main():
    header()

    cats_dir = set_file_dir()
    number_of_cats = input('\nHow many cat pictures do you want? ')

    for i in range(1, int(number_of_cats) + 1):
        i = 'cat {}'.format(i)
        save_cat(i, cats_dir)

    display_cats(cats_dir)


def header():
    print('-------------------------------')
    print('        LOLCAT FACTORY')
    print('-------------------------------')
    print()


def set_file_dir():
    cats_dir = os.path.join(os.getcwd(), 'cats')

    if not os.path.exists(cats_dir):
        print('\'cats\' dir does not exist. Creating \'{}\''.format(cats_dir))
        os.makedirs(cats_dir)

    return cats_dir


def download_cat():
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random/'

    response = requests.get(url, stream=True)
    return response.raw


def save_cat(filename, save_dir):

    data = download_cat()
    filename = filename + '.jpg'
    relevant_filename = os.path.join(save_dir, filename)

    with open(relevant_filename, 'wb') as fout:
        print('Downloading {} ....done'.format(filename))
        shutil.copyfileobj(data, fout)


def display_cats(open_dir):

    client_os = platform.system()

    if client_os == 'Linux':
        subprocess.call(['xdg-open', open_dir])
    elif client_os == 'Darwin':
        subprocess.call(['open', open_dir])
    elif client_os == 'Windows':
        subprocess.call(['explorer', open_dir])
    else:
        print('This app does not support your OS')


if __name__ == '__main__':
    main()
