# LightTouch-OpenCV || Tech Tussle 2021
What if we could convert any ordinary display into a touch screen one using a useless smartphone camera.
we built this python script for you.

### HOW TO Run the program
- [x] Install python . [may follow any youtube]
- [x] Install "IP Cam" https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en in your smart phone.
- [x] Tap start server on your smartphone.
- [x] The app will provide you a IP link. Copy this link
- [x] Open Main.py script and Find for "url = "http://192.168.0.3:8080/shot.jpg" " & just replace the link only . for example your link is xxx.xxx.x.x then the link will be http://xxx.xxx.x.x:8080/shot.jpg
- [x] save the script. 
- [x] Run "Main.py" script and allow "connection" prompt.
- [x] Then keep you mobile in such a position so that its camera can cover your monitor or display.
- [x] Use a red led to move/touch/click/control your computer/laptop screen.
- [ ] [[Note: if you want to run this script in background you can make it formless ".exe" by converting this Python script [.py file] into an Executable file [.exe file.] ]]

### How does it work
- [x] Smartphone camera takes video stream of your display and sends the data to your computer though ip cam with wifi connection.
- [x] then python script crops the video image into display part.
- [x] then it converts into gray image and apply GaussianBlur so that it can easily distinguis different colors
- [x] when any red light source with a range of color code is detected, it tries to detect the position of the source relative to display position
- [ ] saves X and Y position in txt file name x.txt & y.txt
- [ ] we uses "mouse" module to set mosue position accoriding to x.txt y.txt . click accordingly

### Working Video
https://www.youtube.com/watch?v=a-89oZ5W-Ik

![plot1](https://user-images.githubusercontent.com/37979590/109395135-fdf77980-7954-11eb-9b02-842872103a8a.jpeg)
![plot](https://user-images.githubusercontent.com/37979590/109395143-08197800-7955-11eb-9570-1c031364f037.jpeg)


### If you need any help just open an issue.

## Thank You :) 
