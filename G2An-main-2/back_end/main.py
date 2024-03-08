import os
from api import app
from uvicorn import run
from unzip import unzipfile

def delete_gtfs_except_zip(folder_path, except_filename):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through each file
    for file_name in files:
        # Check if the file has the ".gtfs" extension and it's not the exception file
        if file_name.endswith('.txt') and file_name != except_filename:
            # Delete the file
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

def main():
    # Unzip the file
    path=r'C:/Users/USER/Desktop/G2An-main-2/back_end/testzip'
    # delete_gtfs_except_zip(path, 'gtfs.zip')
    unzipfile(path)
    # Run the FastAPI application
    run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()