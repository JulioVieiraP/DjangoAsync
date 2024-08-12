import asyncio
from django.http import HttpResponse
import httpx


async def counter():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print (num)
    async with httpx.AsyncClient() as client:
        r = await client.get('http://httpbin.org/')
        print(r)

async def http_call_async(request):
    asyncio.create_task(counter())
    return HttpResponse("Renderizado com sucesso")
        
        