import requests

response = requests.get('https://www.googletagmanager.com/ns.html?id=GTM-5CF9ZN&gtm_auth=EzJCsJwDfVlqG8d1K6KKOg&gtm_preview=env-1&gtm_cookies_win=x')

print(response.content)