import hashlib

key = "bgvyzdsv"

def advent_coin(key: str):
    n = 1
    while True:
        code_input = key + str(n)

        hash_code = hashlib.md5(code_input.encode()).hexdigest()
        if hash_code.startswith("00000"):
            return n
        n += 1

def advent_coin2(key: str):
    n = 1
    while True:
        code_input = key + str(n)

        hash_code = hashlib.md5(code_input.encode()).hexdigest()
        if hash_code.startswith("000000"):
            return n
        n += 1

print(advent_coin(key))
print(advent_coin2(key))