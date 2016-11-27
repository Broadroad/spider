"""
url entity 
"""
import re
from tld import get_tld
import mmh3

class UrlEntity:
    def __init__(self, u):
        self.url = self._check_url_and_revise(u)
        self.urlSign = 0L
        self.urlTime = 0L
        self.domain = self._get_domain_from_url(self.url) 
        self.domainSign = self._get_domain_sign(self.domain) 
    
    def _get_domain_from_url(self, url):
        try:
            return get_tld(url)
        except Exception as e:
            return "";

    def _get_domain_sign(self, domain):
        return mmh3.hash(domain)


    def _check_url_and_revise(self, url):
        if re.match(r'^https?:/{2}\w.+$', url):  
            return url
        else:
            return "http://" + url

    @UrlEntity.setter
    def set_schedule_time(self, time):
        self.urlTime = time

    def __str__(self):
        return "url[%s] domain[%s] urlSign[%d] domainSign[%d] urlTime[%d]" \
                % (self.url, self.domain, self.urlSign, self.domainSign, self.urlTime)

        
