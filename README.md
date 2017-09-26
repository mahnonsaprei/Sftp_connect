I have realized this program to connect through sftp on centos 7.

Any help is good, remember, i'm not a programmer only a noob with python passion.

1) Connecting to the server
2) Folder change (where needed)
3) Put files on the server
4) Check if there are any files in the remote folder, if not, reboots the upload
5) Compare the timestamp (data only) with the current date of the client and, in case they are not the same, will reload the upload


# Sftp_connect
Example how connect to sftp with pysftp library.
First of all you need to import pysftp library:

On linux: sudo pip install pysftp.
On Windows: py [-python version] -m pip install.


