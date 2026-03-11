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