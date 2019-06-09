# -*- coding: utf-8 -*-

import re as regex   
from tldextract import extract
import ssl
import socket
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlencode
import requests
import whois
import datetime
from links import backlinks


def url_having_ip(url):
    domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
    try:
        socket.inet_aton(domain)
        return -1
    except:
        return 1
    


def url_length(url):
    length=len(url)
    if(length<54):
        return [1,length]
    elif(54<=length<=75):
        return [0,length]
    else:
        return [-1,length]


def url_short(url):
    domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
    shortening_services = ['bit.do','goo.gl','ow.ly','bit.ly','tinyurl','is.gd','branch.io','buff.ly','tiny.cc','soo.gd','s2r.co','clicky.me','budurl.com']
    for shortening_service in shortening_services:
        if shortening_service in domain:
            return -1
        else:
            return 1

def having_at_symbol(url):
    symbol=regex.findall(r'@',url)
    if(len(symbol)==0):
        return 1
    else:
        return -1 
    
def doubleSlash(url):
    if len(url.split("//"))>2:
        return -1
    else:
        return 1

def prefix_suffix(url):
    domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
    if(domain.count('-')):
        return -1
    else:
        return 1

def sub_domain(url):
    domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
    if(domain.count('.')<=1):
        return 1
    elif(domain.count('.')<=2):
        return 0
    else:
        return -1

def SSLfinal_State(url):
    try:
#check wheather contains https       
        if(regex.search('^https',url)):
            usehttps = 1
        else:
            usehttps = 0
#getting the certificate issuer to later compare with trusted issuer 
        #getting host name
        subDomain, domain, suffix = extract(url)
        host_name = domain + "." + suffix
        context = ssl.create_default_context()
        sct = context.wrap_socket(socket.socket(), server_hostname = host_name)
        sct.connect((host_name, 443))
        certificate = sct.getpeercert()
        issuer = dict(x[0] for x in certificate['issuer'])
        certificate_Auth = str(issuer['commonName'])
        certificate_Auth = certificate_Auth.split()

        if(certificate_Auth[0] == "Network" or certificate_Auth == "Deutsche"):
            certificate_Auth = certificate_Auth[0] + " " + certificate_Auth[1]
        else:
            certificate_Auth = certificate_Auth[0] 
        trusted_Auth = ['Google','Comodo','Symantec','GoDaddy','GlobalSign','DigiCert','StartCom','Entrust','Verizon','Trustwave','Unizeto','Buypass','QuoVadis','Deutsche Telekom','Network Solutions','SwissSign','IdenTrust','Secom','TWCA','GeoTrust','Thawte','Doster','VeriSign']        
#getting age of certificate
        startingDate = str(certificate['notBefore'])
        endingDate = str(certificate['notAfter'])
        startingYear = int(startingDate.split()[3])
        endingYear = int(endingDate.split()[3])
        Age_of_certificate = endingYear-startingYear
        
#checking final conditions
        if((usehttps==1) and (certificate_Auth in trusted_Auth) and (Age_of_certificate>=1) ):
            return 1 #legitimate
        elif((usehttps==1) and (certificate_Auth not in trusted_Auth)):
            return 0 #suspicious
        else:
            return -1 #phishing
        
    except Exception as e:
        return -1

def domain_registration(url):
    try:
        w = whois.whois(url)
        updated = w.updated_date
        exp = w.expiration_date
        length=0
        try:
            length = (exp[0]-updated[0]).days
        except:
            try:
                length = (exp-updated).days
            except:
                try:
                    length = (exp[0]-updated).days
                except:
                    length = (exp-updated[0]).days

        if(length<=365):
            return [1,length]
        else:
            return [-1,length]
    except:
        return [-1,0]

def favicon(url):
    #ongoing
    return 0

def port(url):
    #ongoing
    return 0

def https_token(url):
    subDomain, domain, suffix = extract(url)
    host =subDomain +'.' + domain + '.' + suffix 
    if(host.count('https')): #attacker can trick by putting https in domain part
        return -1
    else:
        return 1

def request_url(url):
    try:
        subDomain, domain, suffix = extract(url)
        websiteDomain = domain
        
        opener = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(opener, 'lxml')
        imgs = soup.findAll('img', src=True)
        total = len(imgs)
        
        linked_to_same = 0
        avg =0
        for image in imgs:
            subDomain, domain, suffix = extract(image['src'])
            imageDomain = domain
            if(websiteDomain==imageDomain or imageDomain==''):
                linked_to_same = linked_to_same + 1
        vids = soup.findAll('video', src=True)
        total = total + len(vids)
        
        for video in vids:
            subDomain, domain, suffix = extract(video['src'])
            vidDomain = domain
            if(websiteDomain==vidDomain or vidDomain==''):
                linked_to_same = linked_to_same + 1
        linked_outside = total-linked_to_same
        if(total!=0):
            avg = linked_outside/total
            
        if(avg<0.22):
            return [1,avg]
        if(avg>=0.22 and avg<=0.61):
            return [0,avg]
        elif(avg>0.61):
            return [-1,avg]
    except:
        return [0,-1]


def url_of_anchor(url):
    try:
        subDomain, domain, suffix = extract(url)
        websiteDomain = domain
        
        opener = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(opener, 'lxml')
        anchors = soup.findAll('a', href=True)
        total = len(anchors)
        linked_to_same = 0
        avg = 0
        for anchor in anchors:
            subDomain, domain, suffix = extract(anchor['href'])
            anchorDomain = domain
            if(websiteDomain==anchorDomain or anchorDomain==''):
                linked_to_same = linked_to_same + 1
        linked_outside = total-linked_to_same
        if(total!=0):
            avg = linked_outside/total
            
        if(avg<0.31):
            return [1,avg]
        elif(0.31<=avg<=0.67):
            return [0,avg]
        else:
            return [-1,avg]
    except:
        return [0,-1]
    
def Links_in_tags(url):
    try:
        opener = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(opener, 'lxml')
        
        no_of_meta =0
        no_of_link =0
        no_of_script =0
        anchors=0
        avg =0
        for meta in soup.find_all('meta'):
            no_of_meta = no_of_meta+1
        for link in soup.find_all('link'):
            no_of_link = no_of_link +1
        for script in soup.find_all('script'):
            no_of_script = no_of_script+1
        for anchor in soup.find_all('a'):
            anchors = anchors+1
        total = no_of_meta + no_of_link + no_of_script+anchors
        tags = no_of_meta + no_of_link + no_of_script
        if(total!=0):
            avg = tags/total

        if(avg<0.17):
            return [1,avg]
        elif(0.17<=avg<=0.81):
            return [0,avg]
        else:
            return [-1,avg]        
    except:        
        return [0,-1]

def sfh(url):
    #ongoing
    return 0

def email_submit(url):
    try:
        opener = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(opener, 'lxml')
        if(soup.find('mailto:')):
            return -1
        else:
            return 1 
    except:
        return -1

def abnormal_url(url):
    #ongoing
    return 0

def redirect(url):
    try:
        response = requests.get(url)
        if (len(response.history)<4):
            return 1
        else:
            return 0
    except:
        return 0


def on_mouseover(url):
    #ongoing
    return 0

def rightClick(url):
    #ongoing
    return 0

def popup(url):
    #ongoing
    return 0

def iframe(url):
    try:
        opener = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(opener, 'lxml')
        if(soup.find('iframe')):
            return -1
        else:
            return 1
    except:
        return -1

def age_of_domain(url):
    try:
        w = whois.whois(url)
        start_date = w.creation_date
        current_date = datetime.datetime.now()
        age=0
        try:
            age =(current_date-start_date[0]).days
        except:
            age =(current_date-start_date).days
        if(age>=180):
            return [1,age]
        else:
            return [-1,age]
    except Exception as e:
        print(e)
        return [-1,0]
        
def dns(url):
    #ongoing
    return 0

def web_traffic(url):
    try:
        domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
        req = urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+domain)
        rank = BeautifulSoup(req.read(), "xml").find("REACH")['RANK']
        if int(rank)<100000:
            return [1,rank]
        elif int(rank)>100000:
            return [0,rank]
    except Exception as e:
        print(e)
        return [-1,-1]

def page_rank(url):
    #ongoing
    return 0

def google_index(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        headers = { 'User-Agent' : user_agent}
        
        original_domain=url.split("//")[-1].split("/")[0].split("www.")[-1] 
        query = {'q': 'info:' + original_domain}
        google = "https://www.google.com/search?" + urlencode(query)
        data = requests.get(google, headers=headers)
        soup = BeautifulSoup(str(data.content), "html.parser")
        href = soup.find(id="rso").find("div").find("div").find("a")["href"]
        found_domain = href.split("//")[-1].split("/")[0].split("www.")[-1]
        if found_domain == original_domain:
            return 1
        else:
            return -1
    except AttributeError:
        return -1


def links_pointing(url):
    return backlinks.find(url)

def statistical(url):
    #ongoing
    return 0

def main(url): 
    f1= url_having_ip(url)  
    f2= url_length(url)
    f3= url_short(url)
    f4= having_at_symbol(url)
    f5= doubleSlash(url) 
    f6= prefix_suffix(url)
    f7= sub_domain(url)
    f8= SSLfinal_State(url)
    f9= domain_registration(url)
    f10= https_token(url) 
    f11= request_url(url)
    f12= url_of_anchor(url)
    f13= Links_in_tags(url)
    f14= email_submit(url)
    f15= redirect(url)
    f16= iframe(url)
    f17= age_of_domain(url)
    f18= web_traffic(url)
    f19= google_index(url)
    f20= links_pointing(url)

    check = [[f1,
    f2[0],
    f3,
    f4,
    f5,
    f6,
    f7,
    f8,
    f9[0],
    favicon(url),
    port(url),
    f10,
    f11[0],
    f12[0],
    f13[0],
    sfh(url),f14,
    abnormal_url(url),
    f15,
    on_mouseover(url),
    rightClick(url),
    popup(url),
    f16,
    f17[0],
    dns(url),
    f18[0],
    page_rank(url),
    f19,
    f20[0],
    statistical(url)]]
    
    metadata = [f1,f2[1],f3,f4,f5,f6,f7,f8,f9[1],f10,f11[1],f12[1],f13[1],f14,f15,f16,f17[1],f18[1],f19,f20[1]]
    return [check,metadata]
