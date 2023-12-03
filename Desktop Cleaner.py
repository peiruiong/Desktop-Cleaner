import datetime
import os;
import shutil;

def clean_desktop():
    print("Script started")
    #Set path to desktop
    desktop_path= os.path.join(os.path.expanduser("~"),"Desktop")

    #Set path to folder storing garbage
    cleaned_folder_path=os.path.join(desktop_path,"Desktop Files")
    # cleaned_folder_path= desktop_path+'/Desktop Files'
    os.makedirs(cleaned_folder_path,exist_ok=True)

    #Get current datetime
    current_date=datetime.datetime.now()

    #Get a list of files on desktop, check whether it is file or folder
    desktop_files= [f for f in os.listdir(desktop_path) if os.path.isfile(desktop_path+'/'+f)]
    print("Script started")
    for file_name in desktop_files:
        file_path = os.path.join(desktop_path,file_name)

        #get created date of the file
        created_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

        #Only clean those created <7 days
        if(current_date - created_date).days<7:
            # "_," to ignore filename, file_extension to store filetype
            _, file_extension = os.path.splitext(file_name)
            # take file_extension from position 1 (ignore ".")
            file_extension = file_extension[1:].lower()  

            file_type_folder = os.path.join(cleaned_folder_path, file_extension)
            os.makedirs(file_type_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(file_type_folder, file_name))
            print(f"Moved {file_name} to {file_type_folder}")

if __name__ == "__main__":
    clean_desktop()
