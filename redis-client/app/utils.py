import asyncio
import json
from pprint import pprint

import aiohttp
import xml.etree.ElementTree as et


async def get_currency_xml() -> str:
    url = 'https://cbr.ru/scripts/XML_daily.asp'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            resp = await response.text()
    return resp


async def get_pars_currency() -> dict:

    resp = await get_currency_xml()

    tree = et.fromstring(resp)
    currency = {}
    for child in tree:
        val = child.find('Value').text.replace(',', '.')
        value = float(val) / int(child.find('Nominal').text)
        data = {
            'name': child.find('Name').text,
            'value': round(value, 5),
        }
        data = json.dumps(data)
        currency[child.find('CharCode').text] = data
    return currency
