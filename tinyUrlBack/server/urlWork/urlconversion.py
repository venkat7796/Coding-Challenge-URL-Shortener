import time

def create_mapping_fn():
    hMap = {0:"0",
            1:"1",
            2:"2",
            3:"3",
            4:"4",
            5:"5",
            6:"6",
            7:"7",
            8:"8",
            9:"9",
            }
    key = max(hMap.keys()) + 1
    for i in range(26):
        hMap[key] = chr(ord('a') + i)
        key += 1
    for i in range(26):
        hMap[key] = chr(ord('A') + i)
        key += 1
    get_timestamp = time.time()
    timestamp_milliseconds = get_timestamp * 1000
    int_timestamp = int(timestamp_milliseconds)
    num = int_timestamp
    tiny_url_ret = ""
    q = r = 0
    while num > 0:
        q = num // 62
        r = num % 62
        tiny_url_ret += hMap[r]
        num = q
    return tiny_url_ret
