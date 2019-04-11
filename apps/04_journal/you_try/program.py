import journal
import datetime


def main():
    header()
    run_loop()


def header():
    print('-------------------------------------')
    print('           JOURNAL APP')
    print('-------------------------------------')


def run_loop():
    cmd = None

    journal_data = journal.load()

    while cmd != 'x':
        cmd = input('\n[L]ist entries, [A]dd an entry, [R]emove an entry, E[x]it: \n')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'r':
            remove_entry(journal_data)
        elif cmd == 'x':
            save_entry(journal_data)
        else:
            print('\nNot a valid command\n')


def list_entries(data):
    print('\nListing entries...\n')
    list_order = reversed(data)
    for item in list_order:
        print(item)
#    for index, item in enumerate(list_order, 1):
#        print('{}.) - {}'.format(index, item))


def add_entry(data):
    time_get = datetime.datetime.now()
    time_format = time_get.strftime("%Y-%m-%d %H:%M:%S - ")
    entry = time_format + input('\nType your entry: \n')
    journal.add(entry, data)


def remove_entry(data):
    print('\nSelect the entry to remove:\n')

    for index, item in enumerate(data):
        print(index, ' - ', item)

    entry = input('\nType the item number: \n')
    entry = int(entry)

    target_item = data[entry]
    confirm = None

    while confirm != 'n' and confirm != 'y':

        confirm = input('\nAre you sure you want to remove \'{}\' from your journal? [y/n]\n'.format(target_item))
        confirm = confirm.lower().strip()

        if confirm == 'y':
            journal.remove(entry, data)
            print('\n\'{}\' removed...\n'.format(target_item))
        elif confirm == 'n':
            print('\nCanceling...\n')
        else:
            print('\nNot a valid command\n')


def save_entry(data):
    journal.save(data)
    print('\nSaving journal to disk....\nExiting\n')


if __name__ == '__main__':
    main()
