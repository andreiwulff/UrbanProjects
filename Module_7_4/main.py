import os
import time
def explore_directory(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			filepath = os.path.join(root, file)
			filetime = os.path.getmtime(filepath)
			formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
			filesize = os.path.getsize(filepath)
			parent_dir = os.path.dirname(filepath)
			print(
				f'File found: {file}, Path: {filepath}, Size: {filesize} bytes, Change time: {formatted_time}, Parent directory: {parent_dir}')
directory = "."
explore_directory('C:\\Users\Andrew\\UrbanProject\\Module_7_4')


