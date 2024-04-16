&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Capture d'écran 2023-03-04 153033](https://user-images.githubusercontent.com/120426068/222917504-48e3e6be-a161-4be9-b57e-c1f4ab7ca587.png)




# Houney-Trap-Alert-System


## Description
<br/>



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  This tool is designed to protect against unauthorized access by creating a fake text file that appears to be a valuable document, such as a file labeled "My passwords." This deception is intended to trick potential attackers into opening the file, hoping to gain access to sensitive information.

Once the fake file is opened, the tool triggers one of two scenarios, depending on the security mode specified by the user. In the first scenario, the tool continues to run in the background without the intruder's knowledge, while recording logs of their activity. This allows the user to monitor the attacker's actions and gain insight into their motives and methods.

In the second scenario, the tool takes more aggressive action to protect the system. Specifically, it encrypts the system data, preventing the intruder from accessing any sensitive information or files. Additionally, it takes a snapshot of the system and transmits this data, along with the geolocation and current IP address, to a secure location. This provides valuable information that can be used to identify the attacker and take appropriate action to prevent future attacks.


program that encrypts the data and retrieves the machine's coordinates, including the country, city, and current IP address. The program then sends this information to the client's email address, which was provided during the startup process.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  In addition to this feature, the program also includes another program that allows authorized users to recover the encrypted data using the decryption key that is transmitted along with the machine's coordinates. This ensures that only authorized users can access and recover the encrypted data.

<br/>

## Run Locally

Clone the project

```bash
  https://github.com/fouadbq/Houney-Trap-Alert-System.git
```

Install the required packages on your local machine 

```bash
py -m pip install -r requirements.txt
```

 Navigate to the directory where the houney trap package was installed in.

```bash
cd 'HouneyTrap/The Houney Trap Exe files'
```
<br/>
In order to start the tool do as follows :<br/><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  >Now first run the 'init.exe' file file to provide the necessary information (Email address, password, and the root directory from which the data encryption shall begin). This program shall be automatically deleted after fulfilling the required information, and a hidden file where this information is stored is created.<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  >Next create a folder Name it for instance 'My passwords' in some location of your choice.<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  >Next, go to your defender settings and follow the steps as shown in this article :
```bash
https://www.elevenforum.com/t/add-or-remove-exclusions-for-microsoft-defender-antivirus-in-windows-11.8797/
````
<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >>This shall allow you to exclude the Houney trap tool from beeing deleted by the Windows defender.
<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  >Finaly, exract the  'My passwords.rar' file 

![image](https://user-images.githubusercontent.com/120426068/224515247-3c4ba21f-12a5-4913-bbb8-f524b80f0a1b.png)


Note : Report not finished  yet














## Feedback

If you have any feedback, please do reach out to me at fouadelbaqqaly@gmail.com
