import requests
import os
from bs4 import BeautifulSoup
import re


print('Ниже введиде дату в формате ММ.ГГГГ, которая не ранее 09.2010:')
while True:
    date = input()
    if len(date) == 7:
        if (date[0:2]) in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            if date[2] == '.':
                if int(date[3:]) >= 2010:
                    print('Формат даты верен')
                    break
    else:
        print('Дата введена неверно, повторите ввод')
        continue

date_split = date.split('.')
date_year = date_split[1]
date_month = date_split[0]

accordance = {'01':'january', '02':'february', '03':'march', '04':'april', '05':'may','06':'june',
              '07':'july', '08':'august', '09':'september', '10':'october', '11':'november', '12':'december'}

shift_month = {'01':'12', '02':'01', '03':'02', '04':'03', '05':'04', '06':'05',
              '07':'06', '08':'07', '09':'08', '10':'09', '11':'10', '12':'11'}

date_year_shift = str(int(date_year) - 1) if (date_month == '01') else date_year
date_month_word = accordance[date_month]
date_month_shift = shift_month[date_month]

#исключения
if date == '03.2017':
    your_request_url = 'https://www.smashingmagazine.com/2017/02/hibernation-time-is-over-inspiring-desktop-wallpapers-to-fuel-your-creativity/'
elif date == '02.2017':
    your_request_url = 'https://www.smashingmagazine.com/2017/01/from-the-community-with-love-unique-inspiring-desktop-wallpapers/'
elif date == '12.2016':
    your_request_url = 'https://www.smashingmagazine.com/2016/11/christmas-wallpaper-calendars-2016/'
elif date == '10.2012':
    your_request_url = 'https://www.smashingmagazine.com/2012/09/desktop-wallpapers-calendars-october-2012-halloween-edition/'
elif date == '09.2012':
    your_request_url = 'https://www.smashingmagazine.com/2012/08/free-desktop-wallpaper-calendars-september-2012/'
elif date == '10.2011':
    your_request_url = 'https://www.smashingmagazine.com/2011/09/free-desktop-wallpapers-october-2011/'
elif date == '09.2011':
    your_request_url = 'https://www.smashingmagazine.com/2011/08/free-desktop-wallpaper-calendar-september-2011/'
elif date == '01.2011':
    your_request_url = 'https://www.smashingmagazine.com/2010/12/desktop-wallpaper-calendar-january-2011-new-year/'
elif date in ['09.2010', '12.2010', '02.2011', '03.2011', '04.2011',
            '05.2011', '06.2011', '11.2011', '12.2011', '06.2012', '07.2012']:
    your_request_url = f'https://www.smashingmagazine.com/{date_year_shift}/{date_month_shift}/desktop-wallpaper-calendar-{date_month_word}-{date_year}/'
else:
    your_request_url = f'https://www.smashingmagazine.com/{date_year_shift}/{date_month_shift}/desktop-wallpaper-calendars-{date_month_word}-{date_year}/'

print(your_request_url)
resp = requests.get(your_request_url)
if resp.status_code != 200:
    print('!!!', 'код ошибки: ', resp.status_code, '!!!')
    print('Запрашиваемый Вами адрес не доступен. Возможные причины: ')
    print('     *отсутствует соединение с сетью')
    print('     *по запрашиваемой дате отсутствуют публикации')
    print('     *прошел большой промежуток времени с написания данного приложения (01.10.2019), требуется обновление')
else:
    html = resp.text
    #поиск всех размеров изображений на странице
    re_links = re.findall(r'\d{3,4}x\d{3,4}', html)
    all_size = set(re_links)
    not_valid = set(['114x114', '120x120', '144x144', '152x152']) #данные для служебных изображений
    valid_size = all_size - not_valid
    print('По выбранной дате Вы можете скачать изображения в тако размере: ')
    count = 0
    for x in valid_size:
        count += 1
        print(x, end='   ')
        if count % 6 == 0:
            print()
    print()

    print('Введите необходимый вам размер изображения: ')
    your_request_pixel_resolution = input()
    while your_request_pixel_resolution not in valid_size:
        print('Вводить данные необходимо из вариантов, представленных выше (буковака x - на английском)')
        print('Повторите ввод:')
        your_request_pixel_resolution = input()

    soup = BeautifulSoup(html, 'lxml')
    tags = soup('a', string=your_request_pixel_resolution) #размер в пикселях

    print('Ожидайте, изображения загружаются в текущую директорию:  ', os.path.abspath(os.curdir))
    print()
    for tag in tags:
        #print(tag['href'])
        url_file = tag['href']
        name_of_file = url_file.split('/')[-1]
        if 'nocal' in name_of_file:
            print('Загружается:    ',  name_of_file)
            with open(name_of_file, 'bw') as f:
                image = requests.get(url_file)
                f.write(image.content)

    print('Загрузка завершена')



