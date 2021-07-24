import os
import fnmatch

directory_path = '.'  # Path to the directory with config files
file_list = list()

# Creating a list of files from chosen directory which contain the word "config" in file names
# In this case the number of config files could be any. Not only 100
for file_name in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, file_name)) and fnmatch.fnmatch(file_name, "*config*"):
        file_list.append(file_name)

# Reading data from config files into a list of strings
for file_name in file_list:
    with open(f"{directory_path}/{file_name}", "r") as file:
        file_data = file.readlines()
    # Changing server name and creating a new data to write into a file (as a list of strings)
    new_file_data = [string.replace("server_name_old", "server_name_new") for string in file_data]

    # Writing new data into config files
    with open(f"{directory_path}/{file_name}", "w") as file:
        file.writelines(new_file_data)
