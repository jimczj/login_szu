#coding=utf-8
import requests
from lxml import etree

from django.http import HttpResponseRedirect
from django.conf import settings


def login_szu(func):
    def wrapper(*args, **kw):

        request=args[0]
            
        ticket = request.GET.get('ticket')
        cas_server='https://auth.szu.edu.cn/cas.aspx/'
        return_url="http://"+settings.LOGIN_SZU_BUCKET_DOMAIN+request.get_full_path() if not settings.LOGIN_SZU_SECURE_URL else "https://"+settings.LOGIN_SZU_BUCKET_DOMAIN+request.get_full_path()
            
        if ticket:
            index=return_url.find("ticket=")-1#除去后面的参数ticket
            url=return_url[:index]
            response = requests.get('%sserviceValidate?ticket=%s&service=%s'%(cas_server, ticket, url)).content
            szu_no_xp = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:StudentNo')
            szu_ic_xp = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:ICAccount')
            szu_name_xp = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:PName')
            szu_org_name_xp = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:OrgName')
            szu_sex_xp = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:SexName')
            szu_rank_name_xp = ('/cas:serviceResponse/cas:authenticationSuccess/cas:attributes/cas:RankName')
            tree = etree.fromstring(response)
            request.session['szu_no'] = tree.xpath(szu_no_xp,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
            request.session['szu_ic'] = tree.xpath(szu_ic_xp,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
            request.session['szu_name'] = tree.xpath(szu_name_xp,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
            request.session['szu_org_name'] = tree.xpath(szu_org_name_xp,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
            request.session['szu_sex'] = tree.xpath(szu_sex_xp,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
            request.session['szu_rank_name'] = tree.xpath(szu_rank_name_xp,  namespaces={'cas': 'http://www.yale.edu/tp/cas'})[0].text
            request.session.set_expiry(0)
            return HttpResponseRedirect(url)

        else:
            if 'szu_no' in request.session: 
                return func(*args, **kw)
            else:
                return HttpResponseRedirect('%slogin?service=%s' %(cas_server,  return_url))
    return wrapper
