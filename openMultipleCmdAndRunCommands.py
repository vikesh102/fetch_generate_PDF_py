import os
import time
a = ["roslaunch navstack_pub robo_nav7.launch"," rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200", "rosrun feedback_mech line_follower.py", "rosrun localization_data_pub initial_pose_amcl"]
for i in a:
    if (i == a[2]):
        time.sleep(5)
    os.system("start /B start cmd.exe @cmd /k {}".format(i))
    time.sleep(3)


