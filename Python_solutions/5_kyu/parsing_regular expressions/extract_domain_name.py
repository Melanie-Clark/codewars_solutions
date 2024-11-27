"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""


def domain_name(url):
    if url.find("www") != -1:
        domain_start = url.find("www") + 4
    elif url.find("//") != -1:
        domain_start = url.find("//") + 2
    else:
        domain_start = 0

    url = url[domain_start:]
    domain_end = url.find(".")
    domain = url[: domain_end]

    return domain
