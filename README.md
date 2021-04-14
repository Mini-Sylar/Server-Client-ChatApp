# Server-Client-ChatApp
A configured sever which receives messages from the client and broadcasts it to everyone connected 

## Installation
Program depends on the following libraries
- pyqt5
- sys
- socket
- threading
- Other modules are provided in the client folder

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries.

```bash
pip install PyQt5
```

## Usage

```
- run server.py, a message shows you it's running
- Run client.py
- Enter your desired nickname and press confirm
- send messages to everyone connected to the server
```

## Notes
Server is connected to your localhost, it can be configured to use any ip address you want by changing the values in HOST and PORT

## Issues
Nickname in harmburger menu doesn't fully align at times, issue is being worked on

## Screenshots
<img width="100" src="/Screenshots/Screen-01_EnterUsername.png" alt="ChooseUsername Screenshot">
<img width="100" src="/Screenshots/Screen-02_ConnectedServer.png" alt="Connected to server">
<img width="100" src="/Screenshots/Screen-03_ChatExample.png" alt="Flash Gordon">
<img width="100" src="/Screenshots/Screen-04_SlidingMenu.png" alt="SlidingMenu">

## Plans
Add custom labels like in whatsapp/telegram (actively being worked on)

## License
[MIT](https://choosealicense.com/licenses/mit/)

