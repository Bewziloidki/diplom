import aiohttp
import asyncio

async def check_instagram_status() -> str:
    url = "https://www.instagram.com/"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    return "✅ Instagram доступен"
                else:
                    return f"❌ Instagram недоступен (код {response.status})"

    except aiohttp.ClientError:
        return "❌ Instagram недоступен (ошибка соединения)"
    except asyncio.TimeoutError:
        return "❌ Instagram недоступен (таймаут)"
