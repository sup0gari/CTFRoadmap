import requests

TARGET_URL = f"http://ip:port"
FLAG_TEXT = "HTB{"

def main():
    req_data = {"name" : "test"}
    res = requests.post(TARGET_URL, data=req_data)
    res_data = res.text
    
    if FLAG_TEXT in res_data:
        for line in res_data.splitlines():
            if FLAG_TEXT in line:
                print(f"Found: {line.strip()}")
    else:
        print("Flag not found.")

if __name__ == "__main__":
    main()