# SCP sync configuration

- Recommended: On your local or cloud linux server create a new account to be used for the SCP sync.
- Create target transfer directory on linux server with your new account.
- Edit `scp-copy.exp` file and enter your account password instead of MY_PASSWORD.
- Edit `config.json`, set ActivateScpSync to 1, ActivateDropboxSync to 0 and adjust ScpPath.