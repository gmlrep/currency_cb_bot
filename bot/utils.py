import aiohttp
import xml.etree.ElementTree as et


async def get_currency_xml():
    url = 'https://cbr.ru/scripts/XML_daily.asp'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            resp = await response.text()

    with open('currency.xml', 'w', encoding='windows-1251') as file:
        file.write(resp)


def get_pars_currency():
    tree = et.parse('currency.xml')
    root = tree.getroot()
    currency = {}
    for child in root:
        val = child.find('Value').text.replace(',', '.')
        value = float(val) / int(child.find('Nominal').text)
        data = {
            'name': child.find('Name').text,
            'value': round(value, 5),
            'num_code': child.find('NumCode').text,
        }
        currency[child.find('CharCode').text] = data
    return currency
