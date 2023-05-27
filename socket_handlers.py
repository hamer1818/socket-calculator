from fastapi import FastAPI
from fastapi_socketio import SocketManager
from fastapi.middleware.cors import CORSMiddleware

# terminalin arkaplan renkerlini ayarlayan ANSI kodları
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


 
app = FastAPI()

 
sio = SocketManager(app=app)

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.sio.on('join')
async def handle_join(sid, *args, **kwargs):
    print("Bağlantı gerçekleşti...")
    await sio.emit('lobby', 'User joined')

@sio.on('topla')
async def test(sid,*args, **kwargs):
    sonuc = args[0][0] + args[0][1]
    print(f"{bcolors.WARNING}{bcolors.BOLD}Toplama işlemi gerçekleşti...\nSonuç = {sonuc}")
    await sio.emit('toplam',sonuc)
@sio.on('cikar')
async def test(sid,*args, **kwargs):
    sonuc = args[0][0] - args[0][1]
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}Çıkarma işlemi gerçekleşti...\nSonuç = {sonuc}")
    await sio.emit('cikar',sonuc)
@sio.on('carp')
async def test(sid,*args, **kwargs):
    sonuc = args[0][0] * args[0][1]
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}Çarpma işlemi gerçekleşti...\nSonuç = {sonuc}")
    await sio.emit('carp',sonuc)
@sio.on('bol')
async def test(sid,*args, **kwargs):
    sonuc = args[0][0] / args[0][1]
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Bölme işlemi gerçekleşti...\nSonuç = {sonuc}")
    await sio.emit('bol',sonuc)

if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(level=logging.DEBUG,
                        stream=sys.stdout)

    import uvicorn

    uvicorn.run("socket_handlers:app", host='127.0.0.1', port=8081, reload=True)