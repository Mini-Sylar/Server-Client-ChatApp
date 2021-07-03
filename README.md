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


## Screenshots
<div class="center">
<img width="380" src="/Screenshots/Screen-01_EnterUsername.png" alt="Choose A username">
</div>
<hr>
<div>
<img width="380" src="/Screenshots/001_Bubble_Features.png" alt="Bubble Feature new">
<img width="380" src="/Screenshots/002_RandomUser_Joined.png" alt="Random User Joined">
</div>
<hr>
<div>
<img width="380" src="/Screenshots/003_ConsoleAndBubble.png" alt="Console and bubble">
<img width="380" src="/Screenshots/004_ConsoleAndBubble_Aftermath.png" alt="Console & bubble2">
</div>
<hr>
<div>
<img width="380" src="/Screenshots/005_IpsumLorem_Scaled.png" alt="IpsumLorem Scaled">
<img width="380" src="/Screenshots/005_IpsumLorem_Scaled_NOuser.png" alt="Ipsum Lorem Scaled2">
</div>

## Updates
Updates have been moved into
[Changelog](CHANGELOG.md)

## Plans
- Add custom labels like in whatsapp/telegram (ADDED!)
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
