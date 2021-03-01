from mycroft import MycroftSkill, intent_file_handler
import subprocess

class RosTwoFoxyGazebo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gazebo.foxy.two.ros.intent')
    def handle_gazebo_foxy_two_ros(self, message):
        self.speak_dialog('gazebo.foxy.two.ros')
        subprocess.call([". /opt/ros/foxy/setup.bash"],shell=True)
        subprocess.call([". ~/ros2_foxy/install/setup.bash"],shell=True)
        subprocess.call(["gazebo --verbose /opt/ros/foxy/share/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world"],shell=True)

def create_skill():
    return RosTwoFoxyGazebo()

