from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.merdeka.com/peristiwa/tanggap-darurat-bencana-banjir-padang-ditetapkan-selama-7-hari.html'

# membuka koneksi, mengambil web-page, dan mengunduh web-page sebagai client
uClient = uReq(my_url)

# menyimpan hasil unduhan (konten) web-page sebagai variabel
page_html = uClient.read()

# menutup koneksi internet ketika proses pengunduhan sudah selesai
uClient.close()

# melakukan html parsing dan disimpan sebagai variabel
page_soup = soup(page_html, "html.parser")

# mengecek bahwa konten sudah terunduh
#page_soup.h1
#page_soup.p
#page_soup.a

# menulis file CSV
filename = "berita.csv"
f = open(filename, "w")
headers = "Tanggal; Judul; Penulis; Kategori\n"
f.write(headers)

# mengambil setiap post
section = page_soup.head.findAll("meta",{"property":"section"})
kategori_berita = section[0]["content"]

containers = page_soup.findAll("div",{"class":"mdk-body-detail"})
#container = containers[0]
for container in containers:
    judul_berita = container.div.h1.text

    metadata = container.div.div.div
    date_container = metadata.findAll("span", {"class":"date-post"})
    tanggal_berita = date_container[0].text
    reporter_container = metadata.findAll("span", {"class":"reporter"})
    penulis_berita = reporter_container[0].a.text

# ===================== belum berhasil menyusun paragraf ====================

    #paragraph_container = container.findAll("div", {"class":"mdk-body-paragpraph"})
    #berita_terkait = paragraph_container[0].findAll("div",{"id":"section_terkait"})
    #paragraph_container[0].replace(berita_terkait, "")

# ===========================================================================

    print("Tanggal: " + tanggal_berita)
    print("Judul: " + judul_berita)
    print("Penulis: " + penulis_berita)
    print("Kategori: " + kategori_berita)

    f.write(tanggal_berita + ";" + judul_berita + ";" + penulis_berita + ";" + kategori_berita + "\n")

f.close()
