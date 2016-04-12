import requests
from lxml import etree

from django.http import HttpResponseRedirect



def login_szu(return_url):
    def decorator(func):
        def wrapper(*args, **kw):

            request=args[0]
            ticket = request.GET.get('ticket')
            cas_server='https://auth.szu.edu.cn/cas.aspx/'
            
            if ticket:
                response = requests.get('%sserviceValidate?ticket=%s&service=%s'%(cas_server, ticket, return_url)).content
                xp1 = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:StudentNo')
                xp2 = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:ICAccount')
                tree = etree.fromstring(response)
                request.session['stu_no'] = tree.xpath(xp1,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
                request.session['stu_ic'] = tree.xpath(xp2,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
                request.session.set_expiry(0)
                return HttpResponseRedirect(return_url)

            else:
                if 'stu_no' in request.session: 
                    return func(*args, **kw)
                else:
                    return HttpResponseRedirect('%slogin?service=%s' %(cas_server,  return_url))
        return wrapper
    return decorator