#!/usr/bin/env python3
import csv
import requests
from bs4 import BeautifulSoup
import sys

url_portal = "http://ufm.edu/Portal"
try:
    html_content = requests.get(url_portal).text
except:
    print(f"unable to get {url_portal}")
    sys.exit(1)

soup_portal = BeautifulSoup(html_content, "html.parser")


class PortalOne():
    def __init__(self, soup_portal):
        self.soup = soup_portal

    def get_title(self):
        title = []
        for titulo in self.soup.find_all("title"):
            titulo = str(titulo).replace('<title>', '')
            titulo = str(titulo).replace('</title>', '')
            title.append(titulo)
        M = ''
        for i in title:
            M = M + i
        return M
# <a href="#myModal" data-toggle="modal">Calle Manuel F. Ayau <span style="font-size:10px;">(6 Calle final),</span> zona 10</a>

    def get_address(self):
        a = []
        for _a_ in self.soup.find_all("a"):
            a.append(str(_a_))
        for h in a:
            if 'Calle Manuel F.' in h:
                h = h.replace(
                    '<a data-toggle="modal" href="#myModal">', '')
                h = h.replace(
                    '<span style="font-size:10px;">', '')
                h = h.replace('</span>', '')
                h = h.replace('</a>', '')
                return h
# <a href="mailto:inf@ufm.edu" style="color:#333;">inf@ufm.edu</a>

    def get_phone_and_email(self):
        a = []
        for _a_ in self.soup.find_all("a"):
            a.append(str(_a_))
            # print(_a_)
        telephone = None
        mail = None
        for tel in a:
            if 'tel' in tel:
                tel = tel.replace('<a href="', '')
                tel = tel.replace('</a>', '')
                telephone = tel
            if 'mailto:inf' in tel:
                tel = tel.replace(
                    '<a href="mailto:inf@ufm.edu" style="color:#333;">', '')
                tel = tel.replace('</a>', '')
                mail = tel
        return telephone, mail

    def get_menu_table(self):
        nav = self.soup.find(id="menu-table").text
        nav = str(nav).replace('    ', '')
        nav = str(nav).replace(' ', '')
        nav = str(nav).replace('\n', '')
        nav = str(nav).split()
        nav = str(nav).replace("'", "")
        nav = str(nav).replace('[', '')
        nav = str(nav).replace(']', '')
        return nav

    def properties_href(self):
        links = []
        for hr in self.soup.find_all("a", href=True):
            if 'http' in str(hr):
                links.append(hr['href'])
        return links
# <a href="https://accounts.google.com/o/oauth2/auth?response_type=code&amp;access_type=online&amp;client_id=753553871119-42rgfeitjhbrq449nj1906662pupr1j0.apps.googleusercontent.com&amp;redirect_uri=https%3A%2F%2Fwww.ufm.edu%2Fautenticacion%2Foauth2_init.php&amp;state=d1bdd94b96451faeabbf8f07ba21e046&amp;scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&amp;approval_prompt=auto&amp;hd=ufm.edu" id="ufmail_" style="padding:5px 16px;" class="btn btn-custom-darken">UFMail</a>

    def get_href_ufm_mail_button(self):
        for mail_button in self.soup.find_all(id="ufmail_"):
            mail_button = str(mail_button).replace(
                '<a class="btn btn-custom-darken" href=', '')
            mail_button = str(mail_button).replace(
                ' id="ufmail_" style="padding:5px 16px;">UFMail</a>', '')
            mail = mail_button
        return mail
# <a href="https://accounts.google.com/o/oauth2/auth?response_type=code&amp;access_type=offline&amp;client_id=514583071787-mcsoogoa3kb7v56n7r78obvusehc81br.apps.googleusercontent.com&amp;redirect_uri=https%3A%2F%2Fmiu.ufm.edu%2Findex.php&amp;state=5aa6fb23f2dcfacdf77a35dce36481a9&amp;scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&amp;approval_prompt=force&amp;hd=ufm.edu&amp;login_hint=ejemplo%40ufm.edu" id="miu_" style="padding:5px 16px;;" class="btn btn-custom-darken">MiU</a>

    def get_href_MiU_button(self):
        for MiU_button in self.soup.find_all(id="miu_"):
            MiU_button = str(MiU_button).replace(
                '<a class="btn btn-custom-darken" href=', '')
            MiU_button = str(MiU_button).replace(
                ' id="miu_" style="padding:5px 16px;;">MiU</a>', '')
            MiU = MiU_button
        return MiU

    def hrefs_img(self):
        for i in self.soup.findAll('img'):
            print(i)

    def count_a(self):
        pass


instance = PortalOne(soup_portal)
print(instance.hrefs_img())
