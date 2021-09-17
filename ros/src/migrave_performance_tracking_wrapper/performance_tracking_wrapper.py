import rospy

from migrave_performance_tracking.performance_tracking import RobotPerformanceTracking
from migrave_ros_msgs.msg import GamePerformance, GameActivity

class PerformanceTrackingWrapper(object):
    def __init__(self):
        self.current_performance = {}
        self.game_performance_tracker = RobotPerformanceTracking()
        self.can_receive_new_feedback = True

        game_performance_topic = rospy.get_param('~performance_topic', '/migrave/game_performance')
        # Should be ros action in the future
        self.action_sub = rospy.Subscriber(game_performance_topic,
                                          GamePerformance,
                                          self.game_performance_cb)
        self.action_pub = rospy.Publisher(game_performance_topic, GamePerformance, queue_size=1)

    def game_performance_cb(self, performance_msg: GamePerformance) -> None:
        if self.can_receive_new_feedback:
            self.can_receive_new_feedback = False

            self.current_performance['time'] = {'secs': performance_msg.stamp.secs, 'nsecs': performance_msg.stamp.nsecs}
            self.current_performance['person'] = {'name': performance_msg.person.name,
                                                'age': performance_msg.person.age,
                                                'gender': performance_msg.person.gender,
                                                'mother_tongue': performance_msg.person.mother_tongue}
            self.current_performance['game_activity'] = {'game_id': performance_msg.game_activity.game_id,
                                                        'game_activity_id': performance_msg.game_activity.game_activity_id,
                                                        'difficulty_level': performance_msg.game_activity.difficulty_level}
            self.current_performance['answer_correctness'] = performance_msg.answer_correctness

            self.game_performance_tracker.save_performance_record(self.current_performance)
            
            rospy.sleep(1)
            
            self.can_receive_new_feedback = True
            