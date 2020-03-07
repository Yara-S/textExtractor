#import aiohttp
#import extractor
#import pytesseract


#pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\yara.de.souza.lima\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

import extractor
from aiohttp import web

def handle(request):
    name = request.match_info['file_name']
    html_response = extractor.extractor(name)
    return web.Response(text=html_response, content_type='text/html')

app = web.Application()
app.add_routes([web.get('/{file_name}', handle)])

if __name__ == '__main__':
    web.run_app(app)