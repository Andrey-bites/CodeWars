""" Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.ru") == "cnet" """
import re


def domain_name(url):
    list = []

    for index in url:
        if url[0] == 'h':
            tpl = r'//[\w\W\d]+\.'
        elif url[0] == 'w':
            tpl = r'\.[\w\W\d]+\.'
        else:
            tpl = r'[\w\W\d]+\.'
        findall_str = re.findall(tpl, url)
    
    for i in findall_str[0]:
        if i != '/':
            list.append(i)
    final_str = ''.join(list)
    tpl2 = r'\.'
    split2 = re.split(tpl2, final_str)

    for i in split2:
        if i == 'www':
            split2.remove(i)
        if i == '':
            split2.remove(i)

    res_lst = []
    for i in split2[0]:
        res_lst.append(i)
    res_str = ''.join(res_lst)
    return res_str


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.ru"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("icann.org"))