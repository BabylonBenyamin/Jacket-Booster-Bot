# This file is for strategy

from util.objects import  *
from util.routines import *
from util.tools import find_hits



class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
        

    def run(self):
        if self.intent is not None:
            return
        self.get_closest_large_boost()
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        is_in_front_of_ball = d1 > d2    
        if self.kickoff_flag:
            # set_intent tells the bot what it's trying to do
            self.set_intent(kickoff())
            return
        
        left_post = Vector3(20, -800, 0)
        right_post = Vector3(-20, -800, 0)

        left_post_alt = Vector3(left_post.x*2, left_post.y, left_post.z)
        right_post_alt = Vector3(right_post.x*2, left_post.y, left_post.z)

        targets = {
            "at_opponent_goal": (self.foe_goal.left_post, self.foe_goal.right_post),
            "away_from_our_net": (left_post_alt, right_post_alt)
        }
        hits = find_hits(self,targets)
        if len(hits["at_opponent_goal"]) > 0:
            print("at their goal")
            self.set_intent(hits["at_opponent_goal"][0])
            return
        
        if len(hits["away_from_our_net"]) > 0:
            print("away from our goal")
            self.set_intent(hits["away_from_our_net"][0])
            return
        # this one if statement is under testing
        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            return
        
        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe_goal.location))
            return
        
              
        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            self.set_intent(goto(target_boost.location))
            return
            
        # self.set_intent(goto(self.foe_goal.location))
        self.set_intent(self.get_closest_large_boost())

        # if len(d1<1) and len(d2>1):
        #     print("ball is behind me!")
        
        if (d1 < d2) or d1 == self.foe_goal.location.x - 10:
            self.set_intent(goto(self.ball.location.x))
            print("testing im behind ball")

            
            


      




        


            
         
        
    # junk area
        # if len(available_boosts) > 0:
        #     self.set_intent(goto(available_boosts[0].location))
        #     print("boost availible!", available_boosts[0].index)
        #     return
# junk area ends here


    # this is the place where you should add more defense logic and the anti-own goal logic.