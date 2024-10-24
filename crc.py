def xor(a, b): 
    result = [] 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
    return ''.join(result) 
def mod2div(dividend, divisor): 
    pick = len(divisor) 
    tmp = dividend[0: pick] 
    while pick < len(dividend): 
        if tmp[0] == '1': 
            tmp = xor(divisor, tmp) + dividend[pick] 
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick] 
        pick += 1
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
    checkword = tmp 
    return checkword  
def encodeData(data, key): 
    l_key = len(key) 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
    codeword = data + remainder 
    print("Remainder : ", remainder) 
    print("Encoded Data (Data + Remainder) : ", codeword) 
    return codeword
def checkData(received_data, key): 
    remainder = mod2div(received_data, key) 
    print("Remainder after decoding: ", remainder) 
    if "1" in remainder: 
        print("Error detected in received data.") 
    else: 
        print("No error detected in received data.")
data = input("Enter the data: ")
key = input("Enter the key: ")
encoded_data = encodeData(data, key)
received_data = input("Enter the received data: ")
received_key = input("Enter the key used for checking: ")
checkData(received_data, received_key)