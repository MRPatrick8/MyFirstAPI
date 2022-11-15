from fastapi import FastAPI, Request
from datetime import datetime
# from easynmt import EasyNMT
from fastapi.responses import HTMLResponse

# model = EasyNMT('opus-mt')

storage = FastAPI(title = 'my FASTAPI')
#flash way
@storage.get('/')#ROUTE
def index():
    return "My name is Rene, This is my API"


@storage.get('/today')
def today():
    return str(datetime.now())


@storage.get('/mynames')
def names(First_name: bool = False, last_name: bool = False, full_name: bool = True):
    full_names = ""
    if First_name:
        full_names += 'Rene'
    if last_name:
        full_names += 'Patrick'
    if full_name:
        full_names = 'Hello my name is Rene Patrick'
    return full_names

# @storage.get('/translation')
# def translate(text : str = ''):
#   response = model.translate([text], target_lang='fr')
#   return response[0]

if __name__ == "__main__":
    storage.run()
# @storage.get('/translation-form', response_class=HTMLResponse)
# def form():
#   content =  f"""<html>
#   <form action='/translation' method='GET'>
#    <input type='text' name='text' placeholder='Please Input your Sentence'>
#    <input type='submit' value='submit'>
#   </form>
#   </html>
#   """
#   return content



