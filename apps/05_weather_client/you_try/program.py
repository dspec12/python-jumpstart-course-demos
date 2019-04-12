import requests
import bs4
import collections


def main():
    header()
    location = get_location_from_user()
    html = get_html(location)
    report = parse_html(html)

    print('The weather in {} is {} and {}.'.format(report.loc, report.temp, report.cond))


def header():
    print('--------------------------------------------')
    print('           WEATHER CLIENT APP')
    print('--------------------------------------------')
    print('')


def get_location_from_user():
    ask_zip = input('Enter your zip code (e.g. 94101): ')
    return ask_zip


def get_html(loc):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(loc)
    r = requests.get(url)
    return r.text


def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    location = soup.find(class_='small-12').find('h1').get_text().strip()
    condition = soup.find(class_='condition-icon').get_text().strip()
    temp = soup.find(class_='current-temp').get_text().strip().split('\n')
    temp = ''.join(temp).replace(' ', '')

    weather_report = collections.namedtuple('WeatherReport',
                                            'loc, cond, temp')

    report = weather_report(loc=location, cond=condition, temp=temp)

    return report


if __name__ == '__main__':
    main()
