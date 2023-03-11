import datetime
from email.mime.text import MIMEText
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from geocoder import ip, osm
from socket import gethostname, gethostbyname
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from os import urandom, walk, path
from json import load
from subprocess import Popen


def Get_Geo_Location():

    # Get the latitude and longitude coordinates of the device's IP address
    latitude, longitude = ip("me").latlng

    # reverse geocode to get human-readable location
    geolocation = osm([latitude, longitude], method="reverse")

    return geolocation.country, geolocation.city


# Define a function to pad plaintext to a multiple of 16 bytes
def Padding(data):
    # Create a PKCS7 object with 128 bit block size
    padder = PKCS7(128).padder()

    # Pad the data
    padded_data = padder.update(data)

    # Finalize the padding
    padded_data += padder.finalize()

    return padded_data


def Encrypt_File(filename):

    # Generate a random 16 bytes <=> 128-bit IV
    initial_vect = urandom(16)

    # Create a Cipher object using AES in CBC mode with a random IV
    cipher = Cipher(AES(Encryption_key), CBC(
        initial_vect), backend=default_backend())

    with open(filename, 'rb') as UnencryptedFile:

        # Read the content of the file
        file_content = UnencryptedFile.read()

        # Create an encryptor object associated with the cipher object
        encryptor = cipher.encryptor()

        with open(filename, 'wb') as EncryptedFile:
            # Write the initialization vector to the output file
            EncryptedFile.write(initial_vect)

            # Iterate over the file content in chunks of 1024 bytes and encrypt each chunk
            for i in range(0, len(file_content), 1024):

                plain_text_chunk = file_content[i:i+1024]

                if not plain_text_chunk:
                    break

                # Pad the plaintext chunk
                padded_plaintext = Padding(plain_text_chunk)

                # Encrypt the plaintext chunk
                ciphertext = encryptor.update(padded_plaintext)

                # Write the encrypted data to the output file
                EncryptedFile.write(ciphertext)

            # Finalize the encryption process
            ciphertext = encryptor.finalize()

            # Write the encrypted data to the output file
            EncryptedFile.write(ciphertext)


def SecureData(RootDir):

    global Encryption_key

    # Generate a 32 bytes <=> 256-bit Encryption_key
    Encryption_key = urandom(32)

    for path, _, files in walk(RootDir):
        for file_name in files:
            Encrypt_File('/'.join([path, file_name]))


def Send_Alert_Message():

    # Read the JSON file into a dictionary
    with open('.User__Data.json', 'r') as UserDataFile:
        UserData = load(UserDataFile)

    # Secure data before snding the alert message to the client
    SecureData(UserData['root_dir'])

    # get the current coordinates of the machine
    ip_addr = gethostbyname(gethostname())
    country, city = Get_Geo_Location()

    Alert_Message = MIMEMultipart()
    Alert_Message["Subject"] = "\u26A0 Alert from Houey Pot \u26A0"

    # Attach the message body to the email message
    Alert_Message.attach(
        MIMEText(
            f"""<p style="color:red; font-size:16px;">Alert: Your computer has been breached!</p>
                            <p>The current estimated coordinates of your machine are:</p>
                            <ul>
                                <li>IP Address: {ip_addr}</li>
                                <li>Country: {country}</li>
                                <li>City: {city}</li>
                            </ul>
                            <p>The breach incidence was detected at: {datetime.datetime.now()}</p>
                            <p>Your data is now secured and encrypted. To recover the data, run the Recover.exe program and then insert the following key:</p>
                            <p >Decryption key: <strong style="color:red;text-decoration: underline;">  {Encryption_key.hex()}</strong></p>
                            
                """,
            "html",
        )
    )

    # Send the email using SMTP

    # the UserData['email']  here representes the user's email address  and the UserData['password'] the password

    with SMTP("smtp.gmail.com", 587) as SMTP_Server:
        SMTP_Server.starttls()
        SMTP_Server.login(UserData['email'], UserData['password'])

        SMTP_Server.sendmail(
            UserData['email'], UserData['email'], Alert_Message.as_string()
        )


if __name__ == "__main__":
    # Check if the hidden file exists
    if path.exists('.User__Data.json'):
        Send_Alert_Message()
    else:
        Popen('py -u .GetUserData.py').wait()
