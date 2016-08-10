"""
Wargaming API Python 3 Library
wglib.aio.api.base.

The MIT License (MIT)
Copyright (c) 2016 Nariman Safiulin
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp
from wglib import settings
from wglib.api import base


class Request(base.Request):
    def __getattr__(self, method):
        return Request(self._api, self._method + method)

    async def __call__(self, **kwargs):
        self._data.update(kwargs)
        return await self._api.request(self)


class API(base.API):
    def __getattr__(self, method):
        return Request(self, method)

    async def request(self, request):
        """
        :type request: :class:`wglib.api.base.Request`
        :param request: Request object

        :rtype: :class:`wglib.api.base.Response`
        :return: Response object
        """
        data = self._global_parameters.copy()
        data.update(request.data)

        async with aiohttp.ClientSession() as session:
            async with session.post(self._cluster + request.method,
                                    params=data,
                                    headers={
                                        "User-Agent":
                                            settings.HTTP_USER_AGENT_HEADER}
                                    ) as resp:
                return base.Response(request, await resp.text())
