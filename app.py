from aiohttp import web
from datetime import datetime
import asyncio,json,time,os
import logging

logging.basicConfig(level=logging.INFO)

def index(request):
    text = '<h1>你好,Awesome!</h1>'
    return web.Response(body=text.encode(encoding='gbk'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server start at http://127.0.0.1:9000')
    return srv

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

