# All settings in config.json

| Entry                | Description |
|----------------------|---------------|
| ActivateDropboxSync  | Activate (1) or deactivate (0) sync to dropbox  |
| Dropbox...           | [Prepare and configure for Dropbox sync](doc/dropbox.md) |
| ActivateScpSync      | Activate (1) or deactivate (0) sync to a linux server via SCP |
| Scp...               | [Prepare and configure for linux server sync](doc/scp.md) |
| KeepMaxFilesOnUSB    | Maximum number of files kept in the Raspi USB image |
| DeleteOnUSBCycleTime | Cycle time in seconds after which files above KeepMaxFilesOnUSB are deleted |
| CopyCheckCycleTime   | Cycle time in seconds after which the Raspi USB image is checked for new files |