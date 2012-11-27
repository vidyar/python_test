

        
def login(url, username, password):
    parsed_url = urlparse(url)
    base_uri = urlunparse((parsed_url[0],parsed_url[1],"","","",""))
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, base_uri, username, password)
    auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
    auth_basic = urllib2.HTTPBasicAuthHandler(passman)
    auth_digest = urllib2.HTTPDigestAuthHandler(passman)
    proxy_handler = urllib2.ProxyHandler({})

    opener = urllib2.build_opener(proxy_handler, auth_NTLM, auth_digest, auth_basic)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url) 
    return response.read()