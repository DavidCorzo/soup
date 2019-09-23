#!/usr/bin/env python3
import re
import csv
import requests
from bs4 import BeautifulSoup
import sys
import urllib


def ALL():
    InstanceOne = PortalOne(BeautifulSoup(portal_getter("http://ufm.edu/Portal"), "html.parser"))
    print('============================1==========================')
    print('------------------------------------------------------')
    print('Title:',InstanceOne.get_title())
    print('------------------------------------------------------')
    print('Address',InstanceOne.get_address())
    print('------------------------------------------------------')
    print(InstanceOne.get_phone_and_email())
    print('------------------------------------------------------')
    print(InstanceOne.get_menu_table())
    print('------------------------------------------------------')
    print(InstanceOne.properties_href())
    print('------------------------------------------------------')
    print(InstanceOne.get_href_ufm_mail_button())
    print('------------------------------------------------------')
    print(InstanceOne.get_href_MiU_button())
    print('------------------------------------------------------')
    print(InstanceOne.hrefs_img())
    print('------------------------------------------------------')
    print(InstanceOne.count_a())
    print('------------------------------------------------------')
    print('=======================================================') 
    ####################################################### Next Instance #######################################################
    ####################################################### Next Instance #######################################################
    InstanceTwo = Estudios2(BeautifulSoup(portal_getter(
    "http://ufm.edu/Estudios"), "html.parser"))
    print('============================2==========================')
    print('------------------------------------------------------')
    print(InstanceTwo.navigate_to_estudios())
    print('------------------------------------------------------')
    print(InstanceTwo.display_items_topmenu())
    print('------------------------------------------------------')
    print(InstanceTwo.display_estudios())
    print('------------------------------------------------------')
    print(InstanceTwo.display_leftbar())
    print('------------------------------------------------------')
    print(InstanceTwo.social_media_links())
    print('------------------------------------------------------')
    print(InstanceTwo.count_all_a())
    print('------------------------------------------------------')
    print('=======================================================')
    ####################################################### Next Instance #######################################################
    ####################################################### Next Instance #######################################################
    InstanceThree = cs3(BeautifulSoup(portal_getter(
    "https://fce.ufm.edu/carrera/cs/"), "html.parser"))
    print('============================3==========================')
    print('------------------------------------------------------')
    print(InstanceThree.get_title())
    print('------------------------------------------------------')
    print(InstanceThree.get_href())
    print('------------------------------------------------------')
    print(InstanceThree.download_FCE_logo())
    print('------------------------------------------------------')
    print(InstanceThree.meta_title_description())
    print('------------------------------------------------------')
    print(InstanceThree.count_all_a())
    print('------------------------------------------------------')
    print(InstanceThree.count_all_divs())
    print('------------------------------------------------------')
    print('=======================================================')
    ####################################################### Next Instance #######################################################
    ####################################################### Next Instance #######################################################
    InstanceFour = Directorio(BeautifulSoup(portal_getter(
    'https://www.ufm.edu/Directorio'), "html.parser"))
    print('============================4==========================')
    print('------------------------------------------------------')
    print(InstanceFour.sort_emails_alphabetically())
    print('------------------------------------------------------')
    print(InstanceFour.vowel_emails())
    print('------------------------------------------------------')
    print(InstanceFour.get_the_info_for_json())
    print('------------------------------------------------------')
    print('=======================================================')
    ####################################################### Next Instance #######################################################
    ####################################################### Next Instance #######################################################

def ONE():
    InstanceOne = PortalOne(BeautifulSoup(portal_getter("http://ufm.edu/Portal"), "html.parser"))
    print('============================1==========================')
    print('------------------------------------------------------')
    print(InstanceOne.get_title())
    print('------------------------------------------------------')
    print(InstanceOne.get_address())
    print('------------------------------------------------------')
    print(InstanceOne.get_phone_and_email())
    print('------------------------------------------------------')
    print(InstanceOne.get_menu_table())
    print('------------------------------------------------------')
    print(InstanceOne.properties_href())
    print('------------------------------------------------------')
    print(InstanceOne.get_href_ufm_mail_button())
    print('------------------------------------------------------')
    print(InstanceOne.get_href_MiU_button())
    print('------------------------------------------------------')
    print(InstanceOne.hrefs_img())
    print('------------------------------------------------------')
    print(InstanceOne.count_a())
    print('------------------------------------------------------')
    print('=======================================================') 

def TWO():
    InstanceTwo = Estudios2(BeautifulSoup(portal_getter(
    "http://ufm.edu/Estudios"), "html.parser"))
    print('============================2==========================')
    print('------------------------------------------------------')
    print(InstanceTwo.navigate_to_estudios())
    print('------------------------------------------------------')
    print(InstanceTwo.display_items_topmenu())
    print('------------------------------------------------------')
    print(InstanceTwo.display_estudios())
    print('------------------------------------------------------')
    print(InstanceTwo.display_leftbar())
    print('------------------------------------------------------')
    print(InstanceTwo.social_media_links())
    print('------------------------------------------------------')
    print(InstanceTwo.count_all_a())
    print('------------------------------------------------------')
    print('=======================================================')

def THREE():
    InstanceThree = cs3(BeautifulSoup(portal_getter(
    "https://fce.ufm.edu/carrera/cs/"), "html.parser"))
    print('============================3==========================')
    print('------------------------------------------------------')
    print(InstanceThree.get_title())
    print('------------------------------------------------------')
    print(InstanceThree.get_href())
    print('------------------------------------------------------')
    print(InstanceThree.download_FCE_logo())
    print('------------------------------------------------------')
    print(InstanceThree.meta_title_description())
    print('------------------------------------------------------')
    print(InstanceThree.count_all_a())
    print('------------------------------------------------------')
    print(InstanceThree.count_all_divs())
    print('------------------------------------------------------')
    print('=======================================================')

def FOUR():
    InstanceFour = Directorio(BeautifulSoup(portal_getter(
    'https://www.ufm.edu/Directorio'), "html.parser"))
    print('============================4==========================')
    print('------------------------------------------------------')
    print(InstanceFour.sort_emails_alphabetically())
    print('------------------------------------------------------')
    print(InstanceFour.vowel_emails())
    print('------------------------------------------------------')
    print(InstanceFour.get_the_info_for_json())
    print('------------------------------------------------------')
    print('=======================================================')

def portal_getter(url_portal):
    try:
        html_content = requests.get(url_portal).text

    except:
        print(f"unable to get {url_portal}")
        html_content = None
        sys.exit(1)

    return html_content


# soup_portal = BeautifulSoup(portal_getter(
#     "http://ufm.edu/Portal"), "html.parser")


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

    def get_href_ufm_mail_button(self):
        for mail_button in self.soup.find_all(id="ufmail_"):
            mail_button = str(mail_button).replace(
                '<a class="btn btn-custom-darken" href=', '')
            mail_button = str(mail_button).replace(
                ' id="ufmail_" style="padding:5px 16px;">UFMail</a>', '')
            mail = mail_button
        return mail

    def get_href_MiU_button(self):
        for MiU_button in self.soup.find_all(id="miu_"):
            # MiU_button = str(MiU_button).replace(
            #     '<a class="btn btn-custom-darken" href=', '')
            # MiU_button = str(MiU_button).replace(
            #     ' id="miu_" style="padding:5px 16px;;">MiU</a>', '')
            MiU = MiU_button
        return MiU

    def hrefs_img(self):
        img = []
        for i in self.soup.findAll('img'):
            img.append(str(i).replace('\n', ''))
        filt = []
        # counter = 0
        for a in img:
            if '<img src' in a:
                filt.append(a)
                # print(a, counter)
                # counter += 1
        return img, filt

    def count_a(self):
        counter = 0
        a = []
        for _ in self.soup.find_all("a"):
            a.append(_)
            counter += 1
        return a, counter

    def write_to_csv(self, from_count_A):
        with open('logs/extra_as.txt', 'w+') as f:
            f.writelines()


# Instance1 = PortalOne(soup_portal)
# Instance1.get_href_MiU_button()


class Estudios2():
    def __init__(self, soup_estudios):
        self.soup_estudios = soup_estudios

    def navigate_to_estudios(self):
        url_portal = "https://www.ufm.edu/Portal"
        url_estudios = url_portal.replace('Portal', 'Estudios')
        return url_estudios

    def display_items_topmenu(self):
        div = ''
        for _ in self.soup_estudios.find_all(id="topmenu"):
            _ = str(_).replace('\n', '')
            div = div + _

        topmenu = {}

        div = div.replace(
            '<div class="clearfix pull-right" id="topmenu" style="">', '').replace('<ul>', '').replace('<li>', ',').replace('<a class="external text" href="https://www.ufm.edu/english/" rel="nofollow noreferrer noopener" target="_blank">', '').replace('</a>', '').replace('<a class="external text" href="https://foufm.org" rel="nofollow noreferrer noopener" target="_blank">', '').replace('<a class="external text" href="https://www.ufm.edu/checkout/donaciones/" rel="nofollow noreferrer noopener" target="_blank">', '').replace('<a href="/Especial:Sugerencias" title="Especial:Sugerencias">', '').replace('<a class="external text" href="http://admisiones.ufm.edu/" rel="nofollow noreferrer noopener" target="_blank">', '').replace('<a class="external text" href="https://alumni.ufm.edu/" rel="nofollow noreferrer noopener" target="_blank">', '').replace('<a class="external text" href="https://madrid.ufm.edu/?referer=ufm" rel="nofollow noreferrer noopener" target="_blank">', '').replace('', '').replace('<a href="/Redes_Sociales" title="Redes Sociales">', '').replace('</li>', ',').replace('<b>', '').replace('</div>', '').replace('</ul>', '').replace('</b>', '').replace(',,', ',')
        div = div.split(',')
        div = list(filter(None, div))
        return div

    def display_estudios(self):
        estudios = self.soup_estudios.findAll("div", {"class": "estudios"})
        estudios = list(estudios)
        counter = 0
        for i in estudios:
            estudios[counter] = str(estudios[counter]).replace('<div class="estudios">', '').replace(
                '</div>', '').replace('<div class="estudios" style="color:#294b9a;">', '').replace('<b>', '').replace('</b>', '')
            counter += 1

    def display_leftbar(self):
        lft_bar = self.soup_estudios.findAll("div", {"class": "leftbar"})
        for i in lft_bar:
            L = i.find_all('li')
        print(L)

    def social_media_links(self):
        social_media_links = self.soup_estudios.find_all(
            "div", {"class": "social pull-right"})
        for i in social_media_links:
            L = i.find_all("a")

        counter = 0
        for a in list(L):
            L[counter] = str(L[counter]).replace('<a href=', '').replace(
                ' target="_blank"><i class="fa fa-linkedin-square"></i></a>', '').replace(' target="_blank"><i class="fa fa-facebook-square"></i></a>', '').replace(' target="_blank"><i class="fa fa-twitter-square"></i></a>', '').replace(' target="_blank"><i class="fa fa-google-plus-square"></i></a>', '').replace(' target="_blank"><i class="fa fa-youtube"></i></a>', '').replace(' target="_blank"><i class="fa fa-pinterest-square"></i></a>', '')
            counter += 1

        return L

    def count_all_a(self):
        A = self.soup_estudios.find_all("a")
        counter = 0
        for i in A:
            counter += 1
        return counter


# Instance = Estudios2(soup_estudios)
# Instance.count_all_a()


soup_cs = BeautifulSoup(portal_getter(
    "https://fce.ufm.edu/carrera/cs/"), "html.parser")


class cs3():
    def __init__(self, soup_cs):
        self.soup_cs = soup_cs

    def get_title(self):
        title = self.soup_cs.find_all("title")
        counter = 0
        for i in title:
            title[counter] = str(title[counter]).replace(
                '<title>', '').replace('</title>', '')
        T = ''
        for a in title:
            T = T + str(a)
        return T

    def get_href(self):
        href = self.soup_cs.find_all("a")
        H = []
        for h in href:
            if 'href' in str(h):
                H.append(h)
        F = []
        for i in H:
            i = str(i).split()
            for a in i:
                if ('href' in a) and ('https://' in a):
                    F.append(a.replace('href=', ''))
        return F

    def download_FCE_logo(self):
        url = self.soup_cs.find_all("img", {
                                    "src": "https://fce.ufm.edu/carrera/wp-content/uploads/2017/10/MapaLogotipos-CIENCIAS-ECONOMICAS_1H-1Col-Inv.png"})
        for i in url:
            i = str(i)
            if 'https://fce.ufm.edu/carrera/wp-content/uploads/2017/10/MapaLogotipos-CIENCIAS-ECONOMICAS_1H-1Col-Inv.png' in i:
                image = i

        image = image.replace(
            '<img class="img-responsive" src="', '').replace('"/>', '')
        url = image
        files = requests.get(url)

        open('image_logo.png',
             'wb').write(files.content)

    def meta_title_description(self):
        meta = self.soup_cs.find_all("meta")
        title = []
        description = []
        for i in meta:
            i = str(i)
            if 'title' in i:
                title.append(i)
            if 'description' in i:
                description.append(i)
        return meta

    def count_all_a(self):
        A = self.soup_cs.findAll("a")
        counter = 0
        for i in A:
            counter += 1
        return counter

    def count_all_divs(self):
        div = self.soup_cs.findAll("div")
        counter = 0
        for i in div:
            counter += 1
        return counter


# Instance = cs3(soup_cs)
# print(Instance.count_all_divs())


class Directorio():
    def __init__(self, soup_directorio):
        self.soup_directorio = soup_directorio

    def sort_emails_alphabetically(self):
        email = self.soup_directorio.findAll("a")
        email_L = []
        for i in email:
            i = str(i)
            if 'mailto:' in i:
                email_L.append(i)
        counter = 0
        for a in email_L:
            email_L[counter] = email_L[counter].replace('<a class="external text" href="mailto:', '').replace('" rel="nofollow noreferrer noopener" target="_blank">', ',').replace(
                '</a>', '').replace('<a href="mailto:', '').replace('" style="color:#333;">', '').replace('', '').replace('', '').replace('', '')
            email_L[counter] = email_L[counter].split(',')[0]
            counter += 1

        email_L.sort()
        # for z in email_L:
        #     print(z)
        # self.email_L = email_L

        return email_L

    def vowel_emails(self):
        L = self.sort_emails_alphabetically()
        # print(L)

        counter = 0
        vowels = 'aeiou'

        vowelized = []
        for i in L:
            if L[counter][0] in vowels:
                vowelized.append(L[counter])
            counter += 1
        # for a in vowelized:
        #     print(a)
        return vowelized

    def get_the_info_for_json(self):
        master = {'Edificio Académico':[],'Edificio Escuela de Negocios':[],'6 Avenida 7-55':[],'Edificio Centro Estudiantil':[],'':[],'':[],'6 Calle 7-11':[],'Edificio Biblioteca':[],'Centro Cultural':[]}
        table = self.soup_directorio.findAll("table",{"class":"tabla ancho100"})
        counter = 0
        chld = []
        for i in table:
            child = table[counter].findAll('tr')
            chld.append(child)
        for a in chld:
            a = str(a)
            a = a.replace('\n','')
        tr = []
        for z in chld:
            z = str(z)
            if 'tr' in z:
                tr.append(z)

        for b in tr:
            if ('Edificio Académico' in b) and ('Arquitectura' in b):
                print(1)
                

        # for k,v in master.items():
        #     print("key",k,"val",v)
# Instance = Directorio(soup_directorio)
# print(Instance.get_the_info_for_json())
