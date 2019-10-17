#!/usr/bin/env python3
import re
import csv
import requests
from bs4 import BeautifulSoup
import sys
import urllib
import json
import ast


def portal_getter(url_portal):
    try:
        html_content = requests.get(url_portal).text

    except:
        print(f"unable to get {url_portal}")
        html_content = None
        sys.exit(1)

    return html_content

####################################################### PORTALONE #######################################################
####################################################### PORTALONE #######################################################
####################################################### PORTALONE #######################################################
####################################################### PORTALONE #######################################################

class PortalOne1():
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def get_address(self):
        a = []
        for _a_ in self.soup.find_all("a"):
            a.append(str(_a_))
        acounter = 0
        for h in a:
            if 'Calle Manuel F.' in h:
                a[acounter] = a[acounter].replace(
                    '<a data-toggle="modal" href="#myModal">', '')
                a[acounter] = a[acounter].replace(
                    '<span style="font-size:10px;">', '')
                a[acounter] = a[acounter].replace('</span>', '')
                a[acounter] = a[acounter].replace('</a>', '')
                acounter += 1
        return h
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def properties_href(self):
        links = []
        for hr in self.soup.find_all("a", href=True):
            if 'http' in str(hr):
                links.append(hr['href'])
        return links
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def get_href_ufm_mail_button(self):
        for mail_button in self.soup.find_all(id="ufmail_"):
            mail_button = str(mail_button).replace(
                '<a class="btn btn-custom-darken" href=', '')
            mail_button = str(mail_button).replace(
                ' id="ufmail_" style="padding:5px 16px;">UFMail</a>', '')
            mail = mail_button
        return mail
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def get_href_MiU_button(self):
        for MiU_button in self.soup.find_all(id="miu_"):
            # MiU_button = str(MiU_button).replace(
            #     '<a class="btn btn-custom-darken" href=', '')
            # MiU_button = str(MiU_button).replace(
            #     ' id="miu_" style="padding:5px 16px;;">MiU</a>', '')
            MiU = MiU_button
        return MiU
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def hrefs_img(self):
        img = []
        for i in self.soup.findAll('img'):
            img.append(str(i).replace('\n', ''))
        filt = []
        # counter = 0
        for a in img:
            if '<img src' in a:
                filt.append(a.replace('\n',''))
                
        return img, filt
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def count_a_and_csv_write(self):
        counter = 0
        a = []
        for _ in self.soup.find_all("a"):
            a.append(_)
            counter += 1
        # print(counter)

        with open('log/extra_as.txt','w+') as f:
            f.seek(0)
            f.truncate()
            f.seek(0)
            for line in a:
                f.write(str(line))
        return counter
    
    
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################

####################################################### ESTUDIOS2 #######################################################
####################################################### ESTUDIOS2 #######################################################
####################################################### ESTUDIOS2 #######################################################
####################################################### ESTUDIOS2 #######################################################

class Estudios2():
    def __init__(self, soup_estudios):
        self.soup_estudios = soup_estudios
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def navigate_to_estudios(self):
        url_portal = "https://www.ufm.edu/Portal"
        url_estudios = url_portal.replace('Portal', 'Estudios')
        return url_estudios
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def display_estudios(self):
        estudios = self.soup_estudios.findAll("div", {"class": "estudios"})
        estudios = list(estudios)
        counter = 0
        for i in estudios:
            estudios[counter] = str(estudios[counter]).replace('<div class="estudios">', '').replace(
                '</div>', '').replace('<div class="estudios" style="color:#294b9a;">', '').replace('<b>', '').replace('</b>', '')
            counter += 1
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def display_leftbar(self):
        lft_bar = self.soup_estudios.findAll("div", {"class": "leftbar"})
        for i in lft_bar:
            L = i.find_all('li')
        print(L)
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def count_all_a(self):
        A = self.soup_estudios.find_all("a")
        counter = 0
        for i in A:
            counter += 1
        return counter

####################################################### CS3CS3CS3CS3 #######################################################
####################################################### CS3CS3CS3CS3 #######################################################
####################################################### CS3CS3CS3CS3 #######################################################
####################################################### CS3CS3CS3CS3 #######################################################

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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def count_all_a(self):
        A = self.soup_cs.findAll("a")
        counter = 0
        for i in A:
            counter += 1
        return counter
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def count_all_divs(self):
        div = self.soup_cs.findAll("div")
        counter = 0
        for i in div:
            counter += 1
        return counter

####################################################### DIRECTORIO4 #######################################################
####################################################### DIRECTORIO4 #######################################################
####################################################### DIRECTORIO4 #######################################################
####################################################### DIRECTORIO4 #######################################################

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

        return email_L

    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################

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
    ####################################################### SEPARATOR #######################################################
    ####################################################### SEPARATOR #######################################################
    def get_the_info_for_json(self):
        master = {'Edificio Academico':[],'Edificio Escuela de Negocios':[],'6 Avenida 7-55':[],'6 Calle 7-11':[],'Centro estudiantil':[],'Centro Cultural':[],'Centro Estudiantil':[],'Edificio Biblioteca':[],'No location':[],'Campus Madrid':[],'Facultad de Arquitectura':[],'Facultad de Ciencias Economicas':[],'Facultad de Derecho':[],'Facultad de Medicina':[],'Facultad de Odontologia':[],'Escuela de Cine y Artes Visuales':[],'Escuela de Negocios':[],'Escuela de Nutricion':[],'Escuela de Posgrado':[],'Escuela Superior de Ciencias Sociales':[],'Instituto de Estudios Politicos y Relaciones Internacionales':[],'Departamento de Psicologia':[],'Departamento de Educacion':[],'Michael Polanyi College':[],'Programa de Doctorado':[],'UFM Acton MBA in Entrepreneurship':[]}
        table = self.soup_directorio.find_all("table",{"class":"tabla ancho100"})
        tablaUno = table[0] 
        tablaDos = table[1]
        # print(tablaUno,tablaDos)

        for fila in tablaUno.find_all("tr"):
            row = fila.find_all("td") #genera una lista de columnas
            if len(row) == 5:
                # print('yeah')
                primeraColumna = row[0].text  #find(text=True).replace('\n','').replace(',','') #primera columna
                quintaColumna = row[4].text #segunda columna en cuestión
                
                temp = []
                if 'Edificio Académico' in str(quintaColumna):
                    master['Edificio Academico'].append(primeraColumna)

                elif 'Edificio Escuela de Negocios' in str(quintaColumna):
                    master['Edificio Escuela de Negocios'].append(primeraColumna)
                
                elif '6 Avenida 7-55' in str(quintaColumna):
                    master['6 Avenida 7-55'].append(primeraColumna)
                
                elif '6 Calle 7-11' in str(quintaColumna):
                    master['6 Calle 7-11'].append(primeraColumna)
                
                elif ('Edificio Académico' not in str(quintaColumna)) and ('Edificio Escuela de Negocios' not in str(quintaColumna)) and ('6 Avenida 7-55' not in str(quintaColumna)) and ('6 Calle 7-11' not in str(quintaColumna)):
                    master['No location'].append(primeraColumna)
            
        for fila in tablaDos.find_all("tr"):
            row = fila.find_all("td") #genera una lista de columnas
            if len(row) == 5:
                # print('yeah')
                primeraColumna = row[0].text  #find(text=True).replace('\n','').replace(',','') #primera columna
                quintaColumna = row[4].text #segunda columna en cuestión
                
                if 'Edificio Académico' in str(quintaColumna):
                    master['Edificio Academico'].append(primeraColumna)

                elif 'Edificio Escuela de Negocios' in str(quintaColumna):
                    master['Edificio Escuela de Negocios'].append(primeraColumna)
                
                elif '6 Avenida 7-55' in str(quintaColumna):
                    master['6 Avenida 7-55'].append(primeraColumna)
                
                elif '6 Calle 7-11' in str(quintaColumna):
                    master['6 Calle 7-11'].append(primeraColumna)

                elif 'Centro estudiantil' in str(quintaColumna):
                    master['Centro estudiantil'].append(primeraColumna)
                
                elif 'Edificio Biblioteca' in str(quintaColumna):
                    master['Edificio Biblioteca'].append(primeraColumna)

                elif 'Centro Cultural' in str(quintaColumna):
                    master['Centro Cultural'].append(primeraColumna)
                    
                elif ('Edificio Academico' not in str(quintaColumna)) and ('Edificio Escuela de Negocios' not in str(quintaColumna)) and ('6 Avenida 7-55' not in str(quintaColumna)) and ('6 Calle 7-11' not in str(quintaColumna)):
                    master['No location'].append(primeraColumna)

        for k,v in master.items():
            counter = 0
            for element in v:
                v[counter] = str(v[counter]).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U')
                counter += 1

        master = str(master).replace("'",'"')
        master = ast.literal_eval(master)
        # print(master)

        try:
            with open('logs/4directorio.json','w+') as f:
                f.seek(0)
                f.truncate()
                f.seek(0)
                json.dump(master,f)
        except:
            print(master, 'could not write to log file')    

    def corelate_deans(self):
        try:
            with open('logs/4directorio.json','r+') as f:
                Master = json.load(f)
                if len(Master.items()) == 0:
                    Master = {}
        except:
            Master = {}
        print(Master)
        table = self.soup_directorio.find_all("table",{"class":"tabla ancho100 col3"})
        tableOne = table[1]
        for fila in tableOne.find_all("tr"):
            row = fila.find_all("td")
            if len(row) == 3:
                primeraColumna = str(row[0].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                segundaColumna = str(row[1].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                terceraColumna = str(row[2].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                
                if primeraColumna in Master.items():
                    Master[str(primeraColumna)].append(segundaColumna,terceraColumna)
                if primeraColumna not in Master.items():
                    Master[str(primeraColumna)] = [segundaColumna,terceraColumna]
        with open('logs/4directorio.json','r+') as f:
            json.dump(Master,f)
            print('done')
    
    def csv_dump(self):
        rector = []
        CamMad = []
        Alumni = []
        
        table = self.soup_directorio.find_all("table",{"class":"tabla ancho100 col3"})
        tableOne = table[0]
        for fila in tableOne.find_all("tr"):
            row = fila.find_all("td")
            if len(row) == 3:
                primeraColumna = str(row[0].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                segundaColumna = str(row[1].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                terceraColumna = str(row[2].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                
                if 'Gabriel Calzada' in segundaColumna:
                    rector1 = primeraColumna
                    rector2 = segundaColumna
                    rector3 = terceraColumna
                    rector.append([rector1,rector2,rector3])
                    
        # print(rector)
        tableTwo = table[1]
        # print(tableTwo)
        for fila1 in tableTwo.find_all("tr"):
            row2 = fila1.find_all("td")
            if len(row2) == 3:
                primeraColumna1 = str(row2[0].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                segundaColumna1 = str(row2[1].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                terceraColumna1 = str(row2[2].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')

                if 'Gonzalo Mel' in segundaColumna1:
                    CamMad1 = primeraColumna1
                    CamMad2 = segundaColumna1
                    CamMad3 = terceraColumna1
                    CamMad.append([CamMad1,CamMad2,CamMad3])
                    
        # print(CamMad)
        tableThree = table[2]
        for fila2 in tableThree.find_all("tr"):
            row3 = fila2.find_all("td")
            if len(row3) == 3:
                primeraColumna2 = str(row3[0].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                segundaColumna2 = str(row3[1].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                terceraColumna2 = str(row3[2].text).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('ñ','n').replace('\n','')
                
                if 'Porta' in segundaColumna2:
                    Alumni1 = primeraColumna2
                    Alumni2 = segundaColumna2
                    Alumni3 = terceraColumna2
                    Alumni.append([Alumni1,Alumni2,Alumni3])
                    
        Master = rector + CamMad + Alumni  
        print(Master)
        with open('logs/4directorio_3column_tables.csv','w') as f:
            writer = csv.writer(f)
            writer.writerows(Master)
            f.close()
    
        



# InstanceFour = Directorio(BeautifulSoup(portal_getter(
    # 'https://www.ufm.edu/Directorio'), "html.parser"))
# InstanceFour.get_the_info_for_json()
# InstanceFour.corelate_deans()
# InstanceFour.csv_dump()

def ALL():
    ONE()
    TWO()
    THREE()
    FOUR()

def ONE():
    Instance = PortalOne1(BeautifulSoup(portal_getter('https://www.ufm.edu/Portal'),'html.parser'))
    TI = Instance.get_title()
    print(Instance.get_title())
    
    AD = Instance.get_address()
    print(Instance.get_address())
    
    PE = Instance.get_phone_and_email()
    print(Instance.get_phone_and_email())

    MN = Instance.get_menu_table()
    print(Instance.get_menu_table())

    print('Currently exceding 30 lines thus writing to log')

    PR = Instance.properties_href() #excedes
    MA = Instance.get_href_ufm_mail_button()
    BU = Instance.get_href_MiU_button()
    HR = Instance.hrefs_img()
    CV = Instance.count_a_and_csv_write()

    Master = [TI,AD,PE,MN,PR,MA,BU,HR,CV]
    with open('log/all_master_excedes_30_lines.log', 'w+') as f:
        f.seek(0)
        f.truncate()
        f.seek(0)
        for line in Master:
            f.write(str(line))


def TWO():
    InstanceTwo = Estudios2(BeautifulSoup(portal_getter(
    "http://ufm.edu/Estudios"), "html.parser"))
    print('============================2===============================================================================')
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceTwo.navigate_to_estudios())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceTwo.display_items_topmenu())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceTwo.display_estudios())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceTwo.display_leftbar())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceTwo.social_media_links())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceTwo.count_all_a())
    print('------------------------------------------------------------------------------------------------------------')
    print('==============================================================================================================')

def THREE():
    InstanceThree = cs3(BeautifulSoup(portal_getter(
    "https://fce.ufm.edu/carrera/cs/"), "html.parser"))
    print('============================3===============================================================================')
    print('------------------------------------------------------------------------------------------------------------')
    TI=InstanceThree.get_title()
    print(TI)
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceThree.download_FCE_logo(),'printed logo')
    print('Excedes 30! writind to log')
    HR = InstanceThree.get_href()
    DES = InstanceThree.meta_title_description()
    COUNT = InstanceThree.count_all_a()
    DIVS = InstanceThree.count_all_divs()
    Master = [TI,HR,DES,COUNT,DIVS]
    with open('log/THREE_LOG_EXCEDES30.txt','w+') as f:
        f.seek(0)
        f.truncate()
        f.seek(0)
        for line in Master:
            f.write(str(line))
    print('==============================================================================================================')

def FOUR():
    InstanceFour = Directorio(BeautifulSoup(portal_getter(
    'https://www.ufm.edu/Directorio'), "html.parser"))
    print('============================4=================================================================================')
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceFour.sort_emails_alphabetically())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceFour.vowel_emails())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceFour.get_the_info_for_json())
    print('------------------------------------------------------------------------------------------------------------')
    print(InstanceFour.corelate_deans())
    print('------------------------------------------------------------------------------------------------------------')
    InstanceFour.csv_dump()
    print('==============================================================================================================')



