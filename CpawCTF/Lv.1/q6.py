#!/usr/bin/env python3
'''
Q6.[Crypto] Classical Cipher
fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}
問題は上記の暗号文を古典暗号であるシーザー暗号で解読するもの。
今回は3文字ずらすと指定があるが、このスクリプトは実行時に文字数を指定できるものとする。
'''
if __name__ == "__main__":
    num = int(input("input number: "))
    text = input("input text: ")

    result_text = ""
    for char in text:
        if char.isalpha(): # アルファベットの時だけ復号処理
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            char_ascii = ord(char)
            rel = char_ascii - start
            shifted = rel - num
            result_char = shifted % 26
            result_char_ascii = result_char + start
            result_text += chr(result_char_ascii)
        else:
            result_text += char

    print(f"result: {result_text}")