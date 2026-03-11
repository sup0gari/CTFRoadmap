# Easy

## Riddle Registry
`confidential.pdf`をダウンロード
```bash
file confidential.pdf
exiftool confidential.pdf
```

## Log Hunt
`server.log`をダウンロード
```bash
cat server.log
cat server.log | grep -i flagpart
cat server.log | grep -i flagpart | cut -d ' ' -f 5 | sort | uniq
```