# Dropbox refresh token

###  Get the access code

- Use a browser and log in to your dropbox account.
- Replace APP_KEY in the URL with the app_key from you apps setting page.
```
https://www.dropbox.com/oauth2/authorize?client_id=APP_KEY&response_type=code&token_access_type=offline
```
- Copy the URL to the browser and execute. Press -> Continue -> Allow.
- Copy the generated access code for later usage.
![Access code](img/accesscode.png)

### Call the token API

- Replace ACCESS_CODE, APP_KEY and APP_SECRET with your noted values in the command:
```
curl https://api.dropbox.com/oauth2/token -d code=ACCESS_CODE -d grant_type=authorization_code -d client_id=APP_KEY -d client_secret=APP_SECRET
```

- Execute you modified command in a Command Prompt:

![Command prompt](img/commandprompt.png)

- Finally copy the refresh token from the returned result.
>  ...
>  "token_type": "bearer",
>  "expires_in": 14400,
>  "refresh_token": "**aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-1_bbbbbbbbb-y**",
>  "scope": "account_info.read files.content.read files.content.write files.metadata.read files.metadata.write",
>  ...
