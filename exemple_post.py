#Exemplo envio de arquivos  em request py
files = [
            ('logo_1', ('Brasol.png', base64.b64decode(self.logo), 'image/png')),
            ('logo_favicon', ('Brasol.png', base64.b64decode(self.favicon), 'image/png'))
        ]
        response = requests.request("POST", url, data=vals, files=files)
