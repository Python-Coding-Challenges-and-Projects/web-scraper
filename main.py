import requests
from bs4 import BeautifulSoup

url = "https://www.groupon.com"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

offers = []

info_card = soup.find_all('div', class_='cui-content')
# print(info_card)

for div_tag in info_card:
    # print(div_tag)
    offer_title = div_tag.find('div', class_='cui-udc-title')
    if offer_title:
        offer_title = offer_title.text.strip()
        # print(offer_title)

    deal_address = div_tag.find('span', class_='cui-location-name')
    if deal_address:
        deal_address = deal_address.text.strip()
        # print(deal_address)

    stars_rating = div_tag.find('div', class_='cui-sr-only')
    if stars_rating:
        stars_rating = stars_rating.text
        # print(stars_rating)

    regular_price = div_tag.find('div', class_='cui-price-original')
    if regular_price:
        regular_price = regular_price.text
        # print(f'Regular price: {regular_price}')

    discount_price = div_tag.find('div', class_='cui-price-discount')
    if discount_price:
        discount_price = discount_price.text
        # print(f'Discout Price: {discount_price}')

    short_description = div_tag.find('div', class_='cui-udc-subtitle')
    if short_description:
        short_description = short_description.text.strip()
        # print(short_description)
    
    link = div_tag.find('a')
    if link:
        link_href = link['href']
        # print(link_href)


        offers.append({
        'title': offer_title,
        'location': deal_address,
        'rating': stars_rating,
        'regular_price': regular_price,
        'discount_price': discount_price,
        'short_description': short_description,
        'link': link_href
    })


# Open each deal page and get the description!!

# for deal in offers:
#     url = deal['link']
#     # print(f'url{url}')
#     if not url:
#         continue
#     page = requests.get(url)

#     soup = BeautifulSoup(page.content, "html.parser")
#     # print(soup)

#     content_div = soup.find('div', class_='description')
#     # print(f'content_div{content_div}')
#     if content_div:
#         description_tag = content_div.find('section')
#         if not description_tag:
#             continue
#         description = description_tag.text.strip()

#         deal['description'] = description
#     # print(description)

for deal in offers:
    print ("************************************")
    print(f"{deal['title']},\nLocation: {deal['location']}, \nRating: {deal['rating']}, \nRegular Price: {deal['regular_price']},\nDiscount Price: {deal['discount_price']},\nDescription: {deal['short_description']},\nMore Info: {deal['link']}")
        