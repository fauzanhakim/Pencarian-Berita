from bs4 import BeautifulSoup
import requests
import csv

# ================= Website Berita 1 =================
source1 = requests.get('https://www.detik.com/search/searchall?query=bencana').text
soup1 = BeautifulSoup(source1, 'lxml')

# Menyiapkan File CSV
csv_file = open('Scrape_Berita_Bencana.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tanggal', 'Penulis', 'Judul', 'Ringkasan', 'Berita', 'Laman Berita', 'Tautan Gambar', 'Tautan Thumnail'])

for article1 in soup1.find_all('article'):

    # Summary
    try:
        summary1 = article1.p.text
    except Exception as e:
        summary1 = None

    # Thumbnail
    thumb_src1 = article1.img['src']
    thumb_link1 = thumb_src1.split('?')[0]

    # Link Berita
    article_link1 = article1.a['href']

    # Headline
    headline1 = article1.h2.text

    # DETAIL Website Berita 1 ======================
    source1b = requests.get(article1.a['href']).text
    soup1b = BeautifulSoup(source1b, 'lxml')
    article1b = soup1b.find('article')

    # Penulis
    try:
        author1 = article1b.find('div', class_='author').text
        author1 = author1.split('-')[0]
        author1 = author1.strip()
    except Exception as e:
        author1 = None

    # Tanggal
    try:
        date1 = article1b.find('div', class_='date').text
    except Exception as e:
        date1 = None

    # Gambar
    try:
        img_src1 = article1b.find('div', class_='pic_artikel').img['src']
        img_link1 = img_src1.replace('w=780&q=90','w=1920&q=100')
    except Exception as e:
        img_link1 = None

    # Isi berita
    try:
        news_src1 = article1b.find('div', class_='detail_text').text
        news_src1 = news_src1.strip()
    except Exception as e:
        news_src1 = None

    # output pada Command Prompt
    print(headline1)
    print(date1)
    print(author1)
    print(summary1)
    print(news_src1)
    print(article_link1)
    print(img_link1)
    print(thumb_link1)
    print()

    csv_writer.writerow([date1, author1, headline1, summary1, news_src1, article_link1, img_link1, thumb_link1])

csv_file.close()
