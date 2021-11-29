"""Module for functionalities taking care of game performance tracking
"""
from migrave_knowledge_base.migrave_kb_interface import MigraveKBInterface
from typing import Dict, List
import rospy

class RobotPerformanceTracking(object):
    """Main component for tracking the child performance
    """
    def __init__(self):
        self.migrave_db = MigraveKBInterface()
        self.current_performance = {}

    def save_performance_record(self, performance_record: Dict) -> None:
        'Function to save single performance record in the database'
        #self.current_performance = performance_record
        result = self.migrave_db.store_performance_record(performance_record)

    def get_latest_performance_record(self) -> Dict:
        'Function to fetch latest performance record'
        #return self.current_performance
        return self.migrave_db.get_newest_performance_record()

    def get_performance_record(self, child_name: str='', game_id: int=None) -> List[Dict]:
        """
        Function to fetch performannce of the child in the given type of game.
        If child_name is not provided, overall performance for all children in the given game is fetched.
        If game_id is not provided, overall performance in all games for a given child is fetched.
        If non of the parameters are provided, performance for all children in all types of games is fetched. 
        """
        return self.migrave_db.get_performance_records(person_name=child_name, game_id=game_id)
