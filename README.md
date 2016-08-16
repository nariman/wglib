# Wargaming API Python 3 Library

Wargaming API Library with [asyncio](https://docs.python.org/3/library/asyncio.html) support  
Compatible only with a Python 3.5.

[![Build Status](https://travis-ci.org/woofilee/wglib.svg?branch=master)](https://travis-ci.org/woofilee/wglib)
[![Coverage Status](https://coveralls.io/repos/github/woofilee/wglib/badge.svg?branch=master)](https://coveralls.io/github/woofilee/wglib?branch=master)

## It's important

Library is created for personal use and may contain bugs and strange code :)

## Installation

¯\_(ツ)_/¯
Only manual

## Getting started

#### Creating an API

```python
>>> from wglib import api
 
>>> wot  = api.WoT("application_id", "region")  # World of Tanks API
>>> wotb = api.WoTB("application_id", "region")  # World of Tanks Blitz API
>>> wotx = api.WoTX("application_id", "platform")  # World of Tanks Console API
>>> wows = api.WoWS("application_id", "region")  # World of Warships API
>>> wowp = api.WoWS("application_id", "region")  # World of Warplanes API
>>> wgn  = api.WGN("application_id", "region")  # Wargaming Network API
```

Available regions can be found in the [Wargaming PAPI documentation](https://developers.wargaming.net/documentation/guide/getting-started/).  
Available platforms at the moment are `xbox` and `ps4`.

You can also specify a default language for API:

```python
>>> wot = api.WoT("demo", "ru", language="en")  # World of Tanks API
```

#### Creating a request

Available request methods can be found in the [Wargaming PAPI reference](https://developers.wargaming.net/reference/).

```python
"""
Game servers info
https://developers.wargaming.net/reference/all/wgn/servers/info/
"""
 
>>> res = wgn.servers.info(game="wot")
<wglib.api.base.Response object>
```

Response object contains raw (json) data in the `res.raw` and parsed data in the `res.data`.

```python
>>> res.data
{'status': 'ok', 'data': {'wot': [{'server': 'RU1', 'players_online': 47845} ...
 
>>> res.data["status"]
'ok'
>>> res["status"]  # dict-like
'ok'
```

## License

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
