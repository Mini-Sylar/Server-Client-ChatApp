# Server-Client-ChatApp
A configured sever which receives messages from the client and broadcasts it to everyone connected 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries.
- pyqt5
- sys
- socket
- threading
- Other modules are provided in the Client folder

```bash
pip install PyQt5
```

## Usage
```
- run server.py, a message shows you it's running
- Run Client_Code.py
- Enter your desired nickname and press confirm
- send messages to everyone connected to the server
```

## Notes
Server is connected to your localhost, it can be configured to use any ip address you want by changing the values in HOST and PORT

## Updates
[29th June 2021]
Code has been cleaned up and separated from UI for easy editing
Custom Bubbles have been added, there is a duplicated message bug that is being worked on
to test this feature
```
Uncomment the following lines if you want to test the bubbles
        line 34  - self.bubbleChat()
        line 61  - self.model.add_message(USER_ME, message)
        line 76  - self.model.add_message(USER_THEM, message)
        line 130 - def resizeEvent(self, e)
        
        !!! This must be done before running server and client
```

## Issues
Nickname in hamburger menu doesn't fully align at times, issue is being worked on

## Screenshots
<div>
<img width="380" src="/Screenshots/Screen-01_EnterUsername.png" alt="ChooseUsername Screenshot">
<img width="380" src="/Screenshots/Screen-02_ConnectedServer.png" alt="Connected to server">
</div>

<div>
<img width="380" src="/Screenshots/Screen-03_ChatExample.png" alt="Flash Gordon">
<img width="380" src="/Screenshots/Screen-04_SlidingMenu.png" alt="SlidingMenu">
</div>

## Plans
- Add custom labels like in whatsapp/telegram (In Progress) (ADDED!)
- Make usernames colored in console like chat are (In Progress)
- Encrypted server messages 
- Settings menu to change username,profileIcon,text window style etc.
- Admin powers, kick user etc.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Credits
[Martin](https://www.mfitzp.com/forum/u/martin) - Cloud around text

## Suggestions & Contributions
Suggestions and contributions are always welcome