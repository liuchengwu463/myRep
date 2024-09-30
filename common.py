import random


def zto_head(cookie):
    headers = {
        'content-type': 'application/json',
        'Cookie': cookie,
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    return headers


def ticket_head(cookie):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json',
        'Cookie': cookie,
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'X-Canvas-Fingerprint': '-',
        'X-Webrtc-Addr': "",
        'Force': 'true',
    }
    return headers


def orderinfo_head(cookie, bill_id, ticket, ticket_type, length):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': length,
        'content-type': 'application/json',
        'Cookie': cookie,
        'Host': 'ydzx-web.gw.zt-express.com',
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'X-Bill-Code': bill_id,
        'X-Bill-Token': ticket,
        'X-Bill-Type': ticket_type,
    }
    return headers


def bill_head(cookie, param_ticket):
    headers = {
        'content-type': 'application/json',
        'Cookie': cookie,
        'Host': 'waybill-service.zt-express.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
        'X-Bill-Token': param_ticket,
        'X-Bill-Type': 'A014',
        'X-Requested-With': 'XMLHttpRequest'
    }
    return headers


def waybill_head(cookie):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '226',
        'content-type': 'application/json',
        'Cookie': cookie,
        'Host': 'waybill-service.zt-express.com',
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    return headers


def get_query_result():
    query_result_list = ['f0', 'f1', 'f2', 'f3', '客服登记，请忽略', '忽略登记', '略']
    query_result = random.choice(query_result_list)
    return query_result


def query_record_head(cookie, length):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': length,
        'content-type': 'application/json',
        'Cookie': cookie,
        'Host': 'query-record.gw.zt-express.com',
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'X-Sv-V': 'v0.2.6',
    }
    return headers


def query_void_head(cookie):
    headers = {
        'content-type': 'application/json',
        'Cookie': cookie,
        'Host': 'sms-manage.gw.zt-express.com',
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    }
    return headers


def hdgateway_head():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '41',
        'content-type': 'application/json',
        'Host': 'hdgateway.zto.com',
        'Origin': 'https://www.zto.com',
        'Referer': 'https://www.zto.com/',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Captcha-Code': 'E75D32F1B8941A790BA04C111F9B5C007EA5D85EB8CB7B1EDFA1ECC2EE1F41D44775610EEC4A8E737FC20C9FDC56FE4B8B381FB5EC81F974E3A62AF89E11484A591E2DE095C5D289DB700AA5AEAA2760:664d8c94KRTkXibiqozmjdvnYVgrLcw2cMkw3eC1',
        'X-Captcha-Id': '8bfcb45f-597c-4f8e-9077-3ce83e54a1b8',
        'X-Clientcode': 'pc',
        'X-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0aGlyZFBhcnR5U2lnbiI6IlVTRVJDRU5URVIiLCJhdWQiOiJXZWJVc2VyQ2VudGVyIiwic3ViIjoiMzk0MjU0MDAyIiwiY2xpZW50Q29kZSI6InBjIiwiaXNzIjoiV2ViVXNlckNlbnRlciIsImZhdCI6MTcxNjM1ODkwOCwibW9iaWxlIjoiMTMxMTc5MTAyMDUiLCJleHAiOjE3MTYzODA1MDgsImlhdCI6MTcxNjM1ODkwOCwidXNlcklkIjoiMzk0MjU0MDAyIiwianRpIjoiOTRhNTIxNzhlNTAwNDUyMTlkOWM1ZGYwZTc2YjUzZjEifQ.ejBXX1EHNYlD3dP3cwBS3yWQNMLH8urjNnWX6rnfTJ-lpq2Fz_uPsnWWylroBctZwVxyj1OjahzQzP5LR800Etg19PgHbsYUlIayvWGN9ReEldHIqxEtA_XJ_DtE5PO1cARXtaKMMam9Gl09F3W-boCzFx42czIuhfuptBIrQByD6DQOlHby5fjFhQXqdSKVmzMAa3EN7VjBvm3GTknqObEYFtOu86OcYbuaUFsejSnjTLKZUvYeqC2PA4RjExFjaySSuxCJ2Y4fihNOWiKM-YhMmOYG858aApKbR0jNs_XAuYiluZqyp113SysYbrvTsNlwcPG_N5IWSkqZDyLYog',
    }
    return headers


def order_query_head(cookie, length):
    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': length,
        'content-type': 'application/json;charset=UTF-8',
        'Cookie': cookie,
        'Host': 'order-query-center.gw.zt-express.com',
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    return headers


def test_head(cookie):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': "707",
        'content-type': 'application/json',
        'Cookie': cookie,
        'Host': 'szapi.zt-express.com',
        'Origin': 'https://www.zt-express.com',
        'Referer': 'https://www.zt-express.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    return headers


def yto(cookie):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'ec.yto.net.cn',
        'Jwt-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAEWRzW7CMBCE38XXArLXju3kBvlRqRBFKvTS9BCIRS1BHNlORYV497oOFSdrZ2Z3P3mvSF16lBFBUgksScQEuWGPMnStUW_Nt26VXTdnVaOsRm9ntzJH3W3uRo0mNXJmsIfR3-RRGZyy3X8PEVwSmWIKIprq4lXXvtpjblrlQuTjM6hBazq_bGNLzJ2a7viorDk9wu1gG69NF2pGAeOYdj6ibfV9L2BgU8ynmGyJyDBkVMwogScsM4zjzGbwX8Zqrx-T_8gjBBEpl5DylDGShJ9JUhrss9nrk3rX1g_N6Q5bCk4SqAqeF4uySEXFAFMKcyiAMllyRqqqSBe5xEXBJJ3zedDCk0NSVkyyEaXvtz_9CK4OUTK96pbtSjv_DzcqI-sNTZBufDycAArxcNq5cLjV8mW3nj3v0O0Xe_EwydwBAAA.ENbDIx2WY8X61Dfdxf3bhi1Z2-9no7TSvJDI4fXkkGY',
        'Referer': 'https://ec.yto.net.cn/myOrder',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Source': 'PC',
        'Trace': '{"loginSource":"","terminalModel":""}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    return headers
