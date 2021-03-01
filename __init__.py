from mycroft import MycroftSkill, intent_file_handler


class RosTwoFoxyGazebo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gazebo.foxy.two.ros.intent')
    def handle_gazebo_foxy_two_ros(self, message):
        self.speak_dialog('gazebo.foxy.two.ros')


def create_skill():
    return RosTwoFoxyGazebo()

