import urllib.request as urllib
import json
import os

if not os.path.exists("images"):
    os.makedirs("images")

basic_request_link = "https://www.copart.com/public/lots/search?draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=8&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=9&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=10&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=11&columns%5B11%5D%5Bname%5D=&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=12&columns%5B12%5D%5Bname%5D=&columns%5B12%5D%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=true&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=13&columns%5B13%5D%5Bname%5D=&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=true&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=14&columns%5B14%5D%5Bname%5D=&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D%5Borderable%5D=false&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B15%5D%5Bdata%5D=15&columns%5B15%5D%5Bname%5D=&columns%5B15%5D%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=false&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=<START>&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&sort=auction_date_type+desc%2Cauction_date_utc+asc&defaultSort=true&filter%5BMISC%5D=title_group_code%3ATITLEGROUP_J&query=*&watchListOnly=false&freeFormSearch=false&page=<PAGE>&size=100"

i = 0

for page in range(62):
    print("Parsing page", page)
    req = urllib.Request(basic_request_link.replace('<PAGE>', str(page)).replace('<START>', str(100*page)), method='POST')
    req.add_header('Cookie',
                   "userLang=en; visid_incap_242093=B0HM/B3ZR1mzJOkBALc7jkTRPVsAAAAAQUIPAAAAAAB2DJBYtVuvE/okEsoX+4oI; copartTimezonePref=%7B%22displayStr%22%3A%22EEST%22%2C%22offset%22%3A3%2C%22dst%22%3Atrue%2C%22windowsTz%22%3A%22Europe%2FHelsinki%22%7D; timezone=Europe%2FHelsinki; s_fid=7EB025AD805588A1-3D085E363421BF15; s_cc=true; __cfduid=dfe5779f08cbf5325c72c2dde462957b81530778052; g2usersessionid=6cfeeb1fc99e48746940221b14e3a43e; G2JSESSIONID=4DC6F732F28DB6EDB0451DFC7C291CC3-n2; incap_ses_108_242093=l0xsYcDHnx/SHP6xl7N/AVYmQ1sAAAAAMMvhajYMU91ffN6Z9F0tjQ==; s_depth=1; s_vnum=1533369931191%26vn%3D5; s_invisit=true; s_lv_s=Less%20than%201%20day; s_pv=member%3AsearchResults; s_ppvl=public%253Ahomepage%2C53%2C32%2C759%2C1536%2C759%2C1536%2C864%2C1.25%2CP; s_ppv=member%253AsearchResults%2C28%2C28%2C759%2C999%2C759%2C1536%2C864%2C1.25%2CP; s_nr=1531134630377-Repeat; s_lv=1531134630379; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmember%25253AsearchResults%2526link%253D2%2526region%253DserverSideDataTable_paginate%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmember%25253AsearchResults%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.copart.com%25252Fquickpick%25252Fnonrepairable%25252F%25253FdisplayStr%25253DNon-repairable%252526from%25253D%2525252F%252526page%25253D2%2526ot%253DA")

    f = urllib.urlopen(req)
    data = f.read()

    lot_numbers = map(lambda x: x["lotNumberStr"], json.loads(data)["data"]["results"]["content"])
    for lot in lot_numbers:
        req = urllib.Request("https://www.copart.com/public/data/lotdetails/solr/lotImages/" + lot + "/USA")

        req.add_header('Cookie',
                       "userLang=en; visid_incap_242093=lmp+k/9IR++TXGe4XpGthaaGQlsAAAAAQUIPAAAAAAD8Dk//7y732sSYInHce38j; _ga=GA1.2.366943305.1531086504; _gid=GA1.2.836179826.1531086504; copartTimezonePref=%7B%22displayStr%22%3A%22EEST%22%2C%22offset%22%3A3%2C%22dst%22%3Atrue%2C%22windowsTz%22%3A%22Europe%2FHelsinki%22%7D; timezone=Europe%2FHelsinki; s_fid=759C8DE60F7E4DF8-339170816D7CBC8B; s_cc=true; s_vi=[CS]v1|2DA1435685314748-6000010BA0001939[CE]; OAGEO=UA%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; __gads=ID=72da27249f625893:T=1531086510:S=ALNI_MaUJz7H6Dl0CiD3P_AUWb77gr7dMQ; OAID=ff158164244f2f5d55d17dac7a2fefa7; __cfduid=d990d0f61ba67a336a91f056b409ec5601531087788; g2usersessionid=e969aeb8b3517b2967639ea6c5ab1a58; G2JSESSIONID=DD91CC877C16B566A0E478D9DE535DF7-n1; incap_ses_108_242093=8/jYKPlMPRDSHP6xl7N/AbcmQ1sAAAAAaKt/UthubFM7x/yKpyfMAQ==; s_vnum=1533678507790%26vn%3D4; s_invisit=true; s_lv_s=Less%20than%201%20day; usersessionid=b8d4872aca78e4e741920941deb62716; _gat=1; _uetsid=_uet962ef03a; s_depth=2; s_pv=public%3Alotdetails; s_ppvl=public%253Alotphotos%2C10%2C10%2C759%2C1016%2C759%2C1536%2C864%2C1.25%2CP; s_ppv=public%253Alotdetails%2C42%2C42%2C759%2C1016%2C759%2C1536%2C864%2C1.25%2CP; s_nr=1531141824381-Repeat; s_lv=1531141824382; s_sq=%5B%5BB%5D%5D")

        f = urllib.urlopen(req)
        data = f.read()
        try:
            pic_url = json.loads(data)["data"]["imagesList"]["FULL_IMAGE"][0]["url"]
            urllib.urlretrieve(pic_url, "images/" + "damaged_" + "".join(["0"]*(4-len(str(i)))) + str(i) + ".jpg")
        except:
            print("Can't download image", i)

        i += 1

