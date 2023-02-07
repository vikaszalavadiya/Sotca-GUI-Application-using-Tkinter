# SOTCA-GUI-Application
-------------------------

We can monitor real time data of SOTCA conveter. alos we can control converter data remotly over serial and telnet. 


### Required Library  
--------------------

install pip  =>  apt install python3-pip  
first check installed. => pip --version  

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
python get-pip.py  
dir  


pip install pyserial  
pip install Pillow  
pip install pyinstaller  
pip freeze  
pip install auto-py-to-exe


### Run code:
-----------------------

python app.py

### Convert python file (.py) to exe file or Installer file
-----------------------
Installation:

pip install pyinstaller  
pip install auto-py-to-exe  

** Make exe one file. ** 
-	Store python file, other related files & exe file Icon (pspl.ico) in same project folder.
-	Go to this project folder location in cmd command prome and run command for make exe file.


- pyinstaller.exe --onefile -w --windowed --icon="C:\Users\cziot\Desktop\pythonProject1\icon.ico" main.py
-	Set icon location and python file name ion above command.
-	Exe file create in “dist” folder in project folder.

Make Installer file. (This is only for share other people)
 

** Download NSIS from this link. **

https://sourceforge.net/projects/nsis/

1.	Create zip file of this project folder. And rename to “setup” file.
2.	Open NSIS app and select “Installer base on zip file”
3.	Select your zip file and select generate btn.
4.	It’s create exe setup file.
5.	Install this setup file on particular folder on desktop folder in your pc. Also Shortcut create on desktop. 
6.	After installer run. It is just create folder. That before you zipped.



### Screenshots
-----------------------

![image](https://user-images.githubusercontent.com/47386222/217330537-47bed963-1e37-461b-8625-f1ad6e4426b0.png)
![image](https://user-images.githubusercontent.com/47386222/217330622-4098b194-841c-4568-8de6-5eab905169c3.png)

![image](https://user-images.githubusercontent.com/47386222/217330696-b59c846f-bd2a-4107-ba98-1ba32df9b6dd.png)
![image](https://user-images.githubusercontent.com/47386222/217330759-b8266a4e-0a8f-4565-95a3-f0fb09529c0e.png)

