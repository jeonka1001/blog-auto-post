from typing import Dict
import urllib2

class Request:
    def __init__(self, method: str, url: str, header: Dict[str, str], query: Dict[str, str], body: any=None) -> None:
        self.method = method
        self.url = url
        self.header = header
        self.body = urllib2.urlencode(body)
        self.query = self.get_query(query)

    def request(self):
        if 'GET' == self.method:
            req = urllib2.Request(self.get_url(self.url, self.query), None, self.header)
        elif 'POST' == self.method:
            req = urllib2.Request(self.get_url(self.url, self.query), self.body, self.header)

        return urllib2.urlopen(req)
    
    def get_query(self, query: Dict[str, str]) -> str:
        q_list = []
        for key, value in query.items():
            q_list.append(q_list, '{0}={1}'.format(key, value))
        
        return '&'.join(q_list)
    
    def get_url(self, url, query) -> str:
        return '{0}?{1}'.format(url, query)
    