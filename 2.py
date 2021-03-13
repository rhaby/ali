import requests

url = ("https://web.facebook.com/ajax/login/help/identify.php?ctx=recover")
payload = {
        "jazoest": "21026",
        "lsd": "AVrXDjmXvkM",
        "email": "ajsiri72@gmail.com",
        "did_submit": "1",
        "__user": "0",
        "__a": "1",
        "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEdEc8uxa0z8S2S4o720SUhwem0nCq1ewcG0KEswaq0woy1Qw5MKdwl8G0DE7e2l0FG7o4y0Mo5W3S1lwlEbE28xe3C0D85a2W2K0zE5W0HU1jo",
        "__csr": "",
        "__req": "10",
        "__beoa": "0",
        "__pc": "PHASED:DEFAULT",
        "__bhv": "1",
        "dpr": "1",
        "__ccg": "MODERATE",
        "__rev": "1003442869",
        "__s": "dm3u32:skudni:58xmss",
        "__hsi": "6938909374973484888-0",
        "__comet_req": "0",
        "__spin_r": "1003442869",
        "__spin_b": "trunk",
        "__spin_t": "1615590736"
        }
headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ar-AE,ar;q=0.9",
        "content-length": "453",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "fr=1KxSHrW5gldtOwofX..BgS_Jw.NU.AAA.0.0.BgS_Jw.AWVI5Ro1kLA; sb=cPJLYDm6Z-aSkrAr2PLBIWEt; datr=cPJLYJRUYWWjqfca-EKnoZ2B; sfiu=AYhZG-MDUhBCnc0Ql2NziehKFCq-x2lR8QhgZGQFknEOsjql31raUOzMTbVEWyw-z3Bl4i-Wiy7hU6Jt96QLu_mlpfZmHSFYrUSAZm82pNqQGfhx513vjxGLbkXB2S33fVL-KcHVeMpMYJZHFlP9aPQub1cKOew9b76lWgRxwPwwGsXTg7COu9cCwDq6IccCyEhZ-vS4YcLGNDJjyvpR7Rtiio7tvAXBgeV9FgREviJawQ; wd=846x757",
        "origin": "https://web.facebook.com",
        "referer": "https://web.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "x-fb-lsd": "AVrXDjmXxLA"
}
r = requests.post(url, data=payload, headers=headers).text

print (r)





