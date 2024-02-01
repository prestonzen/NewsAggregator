To run
```sh
python newsService.py
```

To Deploy
1. make NGROK account and get the auth token
2. Add the auth token via the command
```ini
ngrok config add-authtoken 2Td8MkYI8eoktbVktEjQCIFxQZq_JZbUyXWv8LnQUCCAsz9w
```
3. Create a tunnel on the localhost port to be deployed publicly
```sh
ngrok http 5000
```