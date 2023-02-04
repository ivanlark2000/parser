import logging
from def_list import *
from avito_pars import parsAvitoFlat
from urllib.error import HTTPError
from transliterate import translit
from load_to_base import load_to_base, get_id_in_base

logger = logging.getLogger('PARSER')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('log/pars_avito.log', 'w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)

CITY_ID = 24741 
CITY_RUS = 'Калининград'
CITY = translit(CITY_RUS.lower(), language_code='ru', reversed=True)


def main():
    count = 1
    for url in getting_url(city=CITY):
        try:
            html = getting_html(url)  # Получаем html стартовой страницы
        except HTTPError as e:
            logger.warning(f'{url} \n ', exc_info=True)
        list_links = getting_links(html)  # получаем список ссылок квартир
        lst_id_in_base = get_id_in_base(CITY_ID)
        if lst_id_in_base.count(list_links[0]):
            print()
        list_links = [link[2] for link in list_links]
        links = getting_rendom_link(list_links)  # извлекаем рандомную ссылку
        for link in next(links):
            try:
                html_flat = getting_html(link)
            except HTTPError as e:
                logger.warning(f'{url} \nОшибка в скачке данных с Авито', exc_info=True)
                continue
            try:
                flat_in_avito = parsAvitoFlat(html_flat, url=link, city=CITY_RUS)
                load_to_base(flat_in_avito, count)
                count += 1
            except Exception as e:
                logger.warning(f'{url} \nNot correct data from site', exc_info=True)


if __name__ == "__main__":
    #main()
    print(get_id_in_base(CITY_ID))
