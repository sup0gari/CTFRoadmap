'''
Q26.[PPC]Remainder theorem
x ≡ 32134 (mod 1584891)
x ≡ 193127 (mod 3438478)
x = ?

xは1584891で割った時に32314余り、343878で割った時に193127余る。
'''

if __name__ == "__main__":
    i = 0
    while True:
        x = i * 1584891 + 32134
        if x % 3438478 == 193127:
            print(x)
            break
        i += 1
    