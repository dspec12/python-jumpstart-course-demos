import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line_num, line, text')


def main():

    header()

    folder = target_dir()
    print()

    if not folder:
        print('Not a valid directory')
        return

    text = target_text()
    print()

    if not text:
        print('Not a valid search string')
        return

    print('\nResults:\n')

    files = get_file_list(folder)

    for f in files:
        match = search_file(f, text)
        for m in match:
            print('Matched file: {}\nLine: {}Line #: {}\n'.format(m.file, m.line, m.line_num))


def header():
    print('--------------------------------------')
    print('          File Search App')
    print('--------------------------------------')
    print()


def target_dir():

    target_directory = input('Enter search dir: ')

    if not target_dir or not target_directory.strip():
        return None
    if not os.path.isdir(target_directory):
        return None

    return os.path.abspath(target_directory)


def target_text():

    text = input('Type your search string: ')

    return text.lower()


def get_file_list(folder):

    for root, directories, files in os.walk(folder):
        for name in files:
            if name == '.DS_Store':
                continue
            else:
                yield os.path.join(root, name)


def search_file(file, text):

    with open(file, 'r', encoding='utf-8') as fin:
        for num, line in enumerate(fin, 1):
            if text in line:
                search = SearchResult(line=line, line_num=num, file=file, text=text)
                yield search


if __name__ == '__main__':
    main()
