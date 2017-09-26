# ------------ Marcello Colangelo (2017) -------------------------------------
# Linkedin profile: https://www.linkedin.com/in/marcello-colangelo-146b877b/
# Scripts to load and control files by comparing client data
# this program performs a connection to SFTP on the server observing these steps:
# 1) Connecting to the server
# 2) Folder change (where needed)
# 3) Put files on the server
# 4) Check if there are any files in the remote folder, if not, reboots the upload
# 5) Compare the timestamp (data only) with the current date of the client and, in case they are not the same, will reload the upload


import pysftp, os, datetime, time

#---Variables to NOT modify----------------------------------------------------
currentTime = datetime.datetime.now().date()#Assigns the current time to the variable
strTime = str(currentTime) # modify the currenTime variable changing to string and assign to strTime

#---Variables to be edited for connecting to the server-------------------------
server = '192.168.0.114' #Insert ip of server
user = 'chiara' #Insert user
pwd= 'Test001' #Insert password

#---Variables to be modified according to client types--------------------------------
seconds = 5 # Insert seconds to loop while
cDirectory = ('chiaraDir') #Enter between '' the name of the folder that you'll upload the files
local_path = 'c:\\test\\' #Enter the local location where you want to take the data
remote_path = "/chiaraDir/" #Enter the remote location where you upload and check the files
#---Ending variables------------------------------------------------------------------

#------------------Start Program-------------------------------------------------

#---Function that creates the link and uploads to the server-----------------
def connect_to_server():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None #Error hostkey ignored
    s = pysftp.Connection(host=server, username=user, password=pwd, cnopts=cnopts)
    print ('Check data : ', strTime)
    s.cd()
    s.chdir(cDirectory) #Change the directory to compare
    s.put_d(local_path, remote_path) #Put on  remote_path of files of the local
    return (s, cnopts)
#---End of function----------------------------------------------------------------


#---Function compares files and, in case you re-upload the upload----------------------------
def compare_date(s, cnopts):
    file_list_attr = s.listdir_attr() #
    if  not len(file_list_attr): #Check if the folder is empty
        s.put_d(local_path, remote_path) #put the files
    for pfile in file_list_attr:#Running the loop to scan the list
        if datetime.datetime.fromtimestamp(pfile.st_mtime).strftime('%Y-%m-%d') != strTime: #Compare if different to current date
            s.put_d(local_path, remote_path)
            print("Effettuo di nuovo l'upload")
        else:
           print("File esistente")
#---End of function----------------------------------------------------------------

#---Starting loop--------------------------------------------------------------------
while True:
    (s, cnopts) = connect_to_server()
    compare_date(s, cnopts)
    time.sleep(seconds) #Control time loop definited from the variable seconds

#------------Marcello Colangelo (2017) ------------------------------------
