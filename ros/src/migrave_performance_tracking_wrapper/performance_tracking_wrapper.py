import rospy

from migrave_performance_tracking.performance_tracking import RobotPerformanceTracking
from migrave_ros_msgs.msg import GamePerformance

class PerformanceTrackingWrapper(object):
    def __init__(self):
        pass

    def act(self) -> None:
        rospy.loginfo('Tracking the game performance.')

    def robot_action_cb(self, robot_performance_msg: GamePerformance) -> None:
        pass