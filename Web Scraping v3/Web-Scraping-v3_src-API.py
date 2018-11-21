# Setup
import urllib.parse
import requests
import json
import datetime
import time
import pytz
import re
import pandas as pd

print()
print()
print('   :syyo.+                sN`      ./ooooo/-                  sN`                                   ')
print(' `hd-  .hM`               :s         mM:.-oMy                 :s`   -                               ')
print(' dm`     d.                          yM.   oM+                     /o                               ')
print('+Mo      :-  `..`   `. .` `.         yM.   :My    ..`   `. .` `.  -Ns`  `..`        ```..  ````  ```')
print('dM-         +h+hd. +ddoNh:hN         yM.  `yM/  `soym+ /dmoNh:hM`.sMdo..dooN+     `om+yNMs -dNo` .do')
print('MM`         No `Mo .mN://`yM         yMs+odMo   h:  yM..mN://`yM`  Mo  ym  hm     `:Md:.hM+ :M+  `d`')
print('MM`         +.`:Ms  hd    sM  `````  yM:--+md: .Mo++yd/ dm    oM`  Mo  :/ -hN      .M/  .Mh  hm` +o ')
print('mM-         `os:Ms  hd    sM  ymmmy  yM.   :MN`:M.````  dm    oM`  Mo   /s+yN      .M/   mm  -M+ d` ')
print('sMo       .`do  Ns  hd    sM  :///:  yM.    NM.:M/   `. dm    oM`  Mo  od` sN      .M/   dh   hm:y  ')
print('`mN.     o./M- `Ms` hd    sM         yM.   -Mm `Nm-  o- dm    oM`  Mo `Ny  yN  `-  .M+  `N+   -MN-  ')
print(' -dm+-.:s: -Md+sMdo`mN`   yM.       `mM/--+mm:  +MNhds `mN`   yM.  Nmo-dN+sdMs`oN: .Md``oh`    hd   ')
print('  `/sys+.   :s+`+o`/++/` -++/`     ./+++//+:`    :sy/  :++/` -++/` -s: .ss.-s- -y. .Msoo+`     s/   ')
print('                                                                                   .M/        `d    ')
print('   by: Fauzan Aidinul Hakim                                                        .M/     `ysh+    ')
print('                                                                                  -yMd:    `NN+     ')
print()
print('==================================   APLIKASI PENCARIAN BERITA   ===================================')
print('---------------------------- Aplikasi ini membutuhkan koneksi internet. ----------------------------')
print()

# Fitur Pencarian
try:
    while True:
        print('=====  Advanced Search  ============================================================================')
        print('|| # Berikan tanda kutip (") sebelum dan sesudah frasa untuk pencarian yang benar-benar sesuai.   ||')
        print('|| # Berikan tanda tambah (+) sebelum frasa/kata untuk keyword yang harus muncul.                 ||')
        print('|| # Berikan tanda kurang (-) sebelum kata untuk keyword yang tidak boleh muncul.                 ||')
        print('|| # Alternatif: Anda dapat menggunakan AND / OR / NOT dan tanda kurung untuk pengelompokan.      ||')
        print('||   misal: bencana AND (banjir OR longsor) NOT tsunami                                           ||')
        print('====================================================================================================')
        print()
        keyword = input('>> Keyword:  ')
        print()
        if len(keyword) < 1:
            print('++========================================++')
            print('   Silakan masukkan kata kunci pencarian.   ')
            print('++========================================++')
            print('   Tekan Ctrl + C untuk menutup aplikasi.   ')
            print()
            continue
        print('Tentukan jumlah hasil yang ingin ditampilkan (max: 1000, default: 20)')
        raw_result = (input('>> Jumlah:  '))
        default_result = '20'
        max_result = '1000'
        if len(raw_result) < 1:
            result = default_result
            print(result)
        elif raw_result.isnumeric():
            if int(raw_result) > 1000:
                result = max_result
                print(result)
            elif raw_result == '0':
                result = default_result
                print(result)
            elif int(raw_result) <= 1000:
                result = raw_result
                print(result)
        else:
            print('++========================================++')
            print('     Silakan masukkan angka 1 s/d 1000      ')
            print('++========================================++')
            print('   Tekan Ctrl + C untuk menutup aplikasi.   ')
            print()
            continue
        print()

        if result == '1000':
            page_tot = (int(result)/100)
        elif result == '900':
            page_tot = (int(result)/100)
        elif result == '800':
            page_tot = (int(result)/100)
        elif result == '700':
            page_tot = (int(result)/100)
        elif result == '600':
            page_tot = (int(result)/100)
        elif result == '500':
            page_tot = (int(result)/100)
        elif result == '400':
            page_tot = (int(result)/100)
        elif result == '300':
            page_tot = (int(result)/100)
        elif result == '200':
            page_tot = (int(result)/100)
        elif result == '100':
            page_tot = (int(result)/100)
        else:
            page_tot = (int(result)/100) + 1

        if int(result) / int(page_tot) == 100:
            pageSize = 100
        elif int(result) < 100:
            pageSize = result
        else:
            pageSize = int(result)/int(page_tot) + 1

        print('Tentukan cara pengurutan berita (default: Terbaru)')
        print('piihan: (1) Terbaru, (2) Relevansi, (3) Popularitas')
        sort_choice = input('>> Urutkan Berdasar: ')
        default_sort = 'publishedAt'
        if len(sort_choice) < 1:
            sortBy = default_sort
            ket_urutan = 'baru'
            print('Berita Terbaru')
        elif sort_choice == '1':
            sortBy = 'publishedAt'
            ket_urutan = 'baru'
            print('Berita Terbaru')
        elif sort_choice == '2':
            sortBy = 'relevancy'
            ket_urutan = 'relevan'
            print('Berita Terelevan')
        elif sort_choice == '3':
            sortBy = 'popularity'
            ket_urutan = 'popular'
            print('Berita Terpopular')
        else:
            print('++========================================++')
            print('       Silakan masukkan 1, 2, atau 3        ')
            print('++========================================++')
            print('   Tekan Ctrl + C untuk menutup aplikasi.   ')
            print()
            continue
        print()

        pagenumb = 1

        main_api = 'https://newsapi.org/v2/everything?'
        apikey = 'c41426780ab441c9a135ede0d452f3a1'

        apiurl = main_api + urllib.parse.urlencode({'q': keyword}) + '&sortBy=' + str(sortBy) + '&pageSize=' + str(pageSize) + '&page=' + str(pagenumb) + '&apiKey=' + apikey
        source_file = requests.get(apiurl).json()

        search_status = source_file['status']
        search_found = source_file['totalResults']
        print('Status Pencarian: ' + str(search_status.upper()) + ' | Detemukan ' + str(search_found) + ' berita yang sesuai.' + '\n')

        if search_status == 'ok':
            print('=============== HASIL PENCARIAN ================')
            print("(Berita diurutkan berdasarkan yang paling " + ket_urutan + ".)")
            json_data = source_file['articles']
            print()

            nomor_elem = []
            sumber_elem = []
            tanggal_elem = []
            judul_elem = []
            penulis_elem = []
            deskripsi_elem = []
            ringkasan_elem = []
            laman_elem = []
            gambar_elem = []

            start_time = datetime.datetime.now()
            nomor_berita = 1
            for src_news in json_data:
                sumber = src_news['source']['name']
                sumber_elem.append(sumber)
                tanggal = src_news['publishedAt']
                tanggal_elem.append(tanggal)
                judul = src_news['title']
                judul_elem.append(judul)
                penulis = src_news['author']
                penulis_elem.append(penulis)
                deskripsi = src_news['description']
                deskripsi_elem.append(deskripsi)
                ringkasan = src_news['content']
                ringkasan_elem.append(ringkasan)
                laman = src_news['url']
                laman_elem.append(laman)
                gambar = src_news['urlToImage']
                gambar_elem.append(gambar)
                nomor_elem.append(nomor_berita)

                print(str(nomor_berita))
                print('Sumber    : '+str(sumber))
                print('Tanggal   : '+str(tanggal))
                print('Judul     : '+str(judul))
                print('Penulis   : '+str(penulis))
                print('Deskripsi : '+str(deskripsi))
                print('Ringkasan : '+str(ringkasan))
                print('Laman     : '+str(laman))
                print('Gambar    : '+str(gambar))
                nomor_berita = nomor_berita + 1
                print()

            if page_tot > 1:
                pagenumb = pagenumb + 1
                for page_news in range(2, int(page_tot) + 1):
                    apiurl = main_api + urllib.parse.urlencode({'q': keyword}) + '&sortBy=' + str(sortBy) + '&pageSize=' + str(pageSize) + '&page=' + str(pagenumb) + '&apiKey=' + apikey
                    source_file = requests.get(apiurl).json()
                    json_data = source_file['articles']
                    for src_news in json_data:
                        sumber = src_news['source']['name']
                        sumber_elem.append(sumber)
                        tanggal = src_news['publishedAt']
                        tanggal_elem.append(tanggal)
                        judul = src_news['title']
                        judul_elem.append(judul)
                        penulis = src_news['author']
                        penulis_elem.append(penulis)
                        deskripsi = src_news['description']
                        deskripsi_elem.append(deskripsi)
                        ringkasan = src_news['content']
                        ringkasan_elem.append(ringkasan)
                        laman = src_news['url']
                        laman_elem.append(laman)
                        gambar = src_news['urlToImage']
                        gambar_elem.append(gambar)
                        nomor_elem.append(nomor_berita)

                        print(str(nomor_berita))
                        print('Sumber    : '+str(sumber))
                        print('Tanggal   : '+str(tanggal))
                        print('Judul     : '+str(judul))
                        print('Penulis   : '+str(penulis))
                        print('Deskripsi : '+str(deskripsi))
                        print('Ringkasan : '+str(ringkasan))
                        print('Laman     : '+str(laman))
                        print('Gambar    : '+str(gambar))
                        nomor_berita = nomor_berita + 1
                        print()
                    pagenumb = pagenumb + 1

            # Membuat Datafame
            hasil_pencarian = []
            for sum_sumber, sum_tanggal, sum_judul, sum_penulis, sum_deskripsi, sum_ringkasan, sum_laman, sum_gambar in zip(sumber_elem, tanggal_elem, judul_elem, penulis_elem, deskripsi_elem, ringkasan_elem, laman_elem, gambar_elem):
                hasil_pencarian.append({'Sumber':sum_sumber,'Tanggal':sum_tanggal,'Judul':sum_judul,'Penulis':sum_penulis,'Deskripsi':sum_deskripsi,'Ringkasan':sum_ringkasan,'Laman':sum_laman,'Gambar':sum_gambar})
            df_berita = pd.DataFrame(hasil_pencarian)

            finish_time = datetime.datetime.now()
            elapsed_time = finish_time - start_time

            print('Pencarian selesai dalam ' + str(elapsed_time.total_seconds()) + ' detik.')
            print(finish_time.strftime('%A, %d %B %Y - %H:%M:%S'))
            print()

            while True:
                print()
                print('Apakah Anda ingin menyimpan hasil pencarian dalam format .CSV? (y/n)')
                csv_default = 'Berita-' + (str(keyword)).capitalize() + '_' + str(finish_time.strftime('%Y-%m-%d_%H-%M-%S'))
                simpan = (input('>>  '))
                if re.match(r'(y|ya|iya)', simpan, re.I):
                    nama_file = (input('>> Nama file:  '))
                    if len(nama_file) < 1:
                        print('(Nama file default)')
                        csv_name = csv_default
                        df_berita.to_csv(csv_name  + ".csv", encoding="utf-8")
                        print()
                        print('## File berhasil disimpan dengan nama "' + csv_name.replace(" ", "-") + '.csv" ##')
                        print()
                        print()
                        print()
                        break
                    elif re.match(r'default', nama_file, re.I):
                        print('(Nama file default)')
                        csv_name = csv_default
                        df_berita.to_csv(csv_name  + ".csv", encoding="utf-8")
                        print()
                        print('## File berhasil disimpan dengan nama "' + csv_name.replace(" ", "-") + '.csv" ##')
                        print()
                        print()
                        print()
                        break
                    elif not re.match("^[a-zA-Z0-9_ ,.~`^';!@#$%&+-=()]*$", nama_file):
                        print('ERROR! tidak dapat menggunakan simbol ^\/:*?"<>|{}[]')
                        continue
                    else:
                        csv_name = nama_file
                        df_berita.to_csv(csv_name  + ".csv", encoding="utf-8")
                        print()
                        print('## File berhasil disimpan dengan nama "' + csv_name.replace(" ", "-") + '.csv" ##')
                        print()
                        print()
                        print()
                        break
                elif len(simpan) < 1:
                    continue
                elif re.match(r'(n|no|tidak)', simpan, re.I):
                    print()
                    print()
                    print()
                    break
                else:
                    continue

except KeyboardInterrupt:
    print()
    print()
    print('Closing Application...')
    time.sleep(1)
    print()
    print('-------- DONE --------')
    print()
    print()
    print()
    print()
