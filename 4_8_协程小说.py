import requests
import aiohttp
import asyncio
import aiofile
import json


async def aindownload(cid, book_id, title):
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofile.async_open(title, mode="w", encoding="utf8") as f:
                await f.write(dic['data']['novel']['content'])


async def get_catalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(aindownload(cid, book_id, title))
        # print(title, cid)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+book_id+'"}'
    asyncio.run(get_catalog(url))
