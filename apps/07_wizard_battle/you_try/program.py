import random
import characters
import time
import sys


def main():
    header()

    player = player_name()
    game_loop(player)


def header():
    print('----------------------------------------------')
    print('             Wizard Battle!')
    print('----------------------------------------------')
    print()


def player_name():
    player = input('What\'s your name? ')
    return player


def bad_guy_gen():
    names = [
        'Boar',
        'Bat',
        'Bear',
        'Snake',
        'Tiger',
        'Wizard',
        'Warlock'
    ]
    return characters.BadGuy(random.choice(names), random.randint(1, 100))


def game_loop(player):

    bad_guys = [
        bad_guy_gen(),
        bad_guy_gen(),
        bad_guy_gen(),
        bad_guy_gen(),
        bad_guy_gen()
    ]

    hero = characters.Hero(player, 75)

    while len(bad_guys) >= 1:

        active_creature = random.choice(bad_guys)

        print('\nA level {} {} emerges and is looking to fight.'.format(active_creature.lvl ,active_creature.name))
        time.sleep(1)

        choice = input('\nDo you [a]ttack or [r]un away, [l]ook around? '.format('pass', 'pass'))
        choice = choice.lower()

        if choice == 'a':
            print('\n{} attacks the {}'.format(hero.name, active_creature.name))

            battle = hero.attack(active_creature)

            if battle[0]:

                time.sleep(1)
                print('{} rolls a {}'.format(hero.name, battle[1]))
                time.sleep(1)
                print('{} rolls a {}'.format(active_creature.name, battle[2]))
                time.sleep(1)
                print('\nHero wins')
                time.sleep(1)

                bad_guys.remove(active_creature)

            else:
                time.sleep(1)
                print('{} rolls a {}'.format(hero.name, battle[1]))
                time.sleep(1)
                print('{} rolls a {}'.format(active_creature.name, battle[2]))
                time.sleep(1)
                print('\nHero was defeated and needs to time recover!')

                for i in range(10, 0, -1):
                    time.sleep(1)
                    sys.stdout.write(str(i) + ' ')
                    sys.stdout.flush()

                print(' recovered!')
                time.sleep(1)

        elif choice == 'r':
            time.sleep(1)
            print('\n{} runs away!'.format(hero.name))
            bad_guys.remove(active_creature)
            bad_guys.append(bad_guy_gen())
            time.sleep(1)

        elif choice == 'l':
            print('\n{} looks around and sees the following enemies still standing\n'.format(hero.name))
            time.sleep(1)
            for guys in bad_guys:
                print('A {} of level {}'.format(guys.name, guys.lvl))
            time.sleep(1)

        else:
            print('\nGame over')
            break


if __name__ == '__main__':
    main()
