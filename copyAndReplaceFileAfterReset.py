#!/usr/bin/env python3

# Move the file to the /etc/init.d/ directory:
# sudo mv /path/to/file_operations.py /etc/init.d/
#
# Make the file executable using the chmod command:
# chmod +x /etc/init.d/file_operations.py
#
# Create a symbolic link to the file in the /etc/rc.d/ directory:
# sudo ln -s /etc/init.d/file_operations.py /etc/rc.d/

import os
import shutil


def file_operations():
    current_path = "/home/locobot/interbotix_ws/src/interbotix_ros_rovers/interbotix_ros_xslocobots/examples/interbotix_xslocobot_landmark_nav/scripts/"
    # Delete the file 'old_file.txt'
    os.remove(current_path+'rtabmap.db')

    # Rename the file 'new_file.txt' to 'old_file.txt'
    os.rename(current_path+'rtabmap_bkp.db', current_path+'rtabmap.db')

    # Set the source file path
    src_file = current_path+'rtabmap.db'

    # Create the new file name by adding '_bkp' to the original file name
    # new_file_name = os.path.splitext("rtabmap.db")[0] + '_bkp' + os.path.splitext("rtabmap.db")[1]
    new_file_name = "rtabmap_bkp.db"

    # Set the destination file path
    dst_file = os.path.join(current_path, new_file_name)

    # Copy the file to the same folder with a new name
    shutil.copy2(src_file, dst_file)


if __name__ == '__main__':
    file_operations()
