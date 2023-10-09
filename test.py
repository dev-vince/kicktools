from tls_client import Session

TARGET_EMAIL = "daratmp+jabed@gmail.com"

if __name__ == "__main__":
    session = Session(client_identifier="chrome_110", random_tls_extension_order=True)

    kick_response = session.get("https://kick.com")

    token_response = session.get("https://kick.com/kick-token-provider")

    encrypted_token = token_response.json()["encryptedValidFrom"]

    print("Encrypted token: {}".format(encrypted_token))

    session.headers.update({"Accept": "*/*", 
                            "Accept-Encoding": "gzip, deflate, br", 
                            "Authorization": f"Bearer {encrypted_token}",
                            "Host": "kick.com",
                            "Origin": "https://kick.com",
                            "Referer": "https://kick.com/",
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "same-origin",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0", 
                            "X-XSRF-TOKEN": encrypted_token})

    validate_email_response = session.post("https://kick.com/api/v1/signup/verify/email", json={"email": TARGET_EMAIL})

    print(validate_email_response.status_code)
    print(validate_email_response.text)
