# Server-Client-ChatApp
A configured sever which receives messages from the client and broadcasts it to everyone connected 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries.
- pyqt5
- Other modules are provided in the Client folder or are provided in the python setup

```bash
pip install PyQt5
```

## Usage
```
- run server.py, a message shows you it's running
- Run Client_Code.py
- Enter your desired nickname and press confirm
- send messages to everyone connected to the server
- send images to everyone [NEW]
```

## Notes
Server is connected to your localhost, it can be configured to use any ip address you want by changing the values in HOST and PORT


## Screenshots
<div>
  <p align="center">
    <img width="380" src="/Screenshots/Screen-01_EnterUsername.png" alt="Choose A username">
  </p>
</div>
<div>
<img width="380" src="/Screenshots/DecemberScreenshots.png" alt="New Interface">
<img width="380" src="/Screenshots/DecemberScreenshots2.png" alt="New Interface">
</div>
<div>
<img width="100%" src="/Screenshots/SendImageScreenshot.png" alt="Image Sending">
</div>

## Updates
Updates have been moved into
[Changelog](CHANGELOG.md)

## Plans
- [x] Add custom labels like in whatsapp/telegram (ADDED!)
- [x] Add image sending support (ADDED!) [NEW]
- [ ] Add video sending support [NEW]
- [ ] Add document sending support [NEW]
- [ ] Encrypted server messages 
- [ ] Settings menu to change username,profileIcon,text window style etc.
- [ ] Admin powers, kick user etc.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Credits
[Martin](https://www.mfitzp.com/forum/u/martin) - Cloud around text

## Suggestions & Contributions
Suggestions and contributions are always welcome
