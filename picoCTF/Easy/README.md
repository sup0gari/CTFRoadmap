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