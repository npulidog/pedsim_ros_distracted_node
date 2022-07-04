#!/usr/bin/env python
import roslib
roslib.load_manifest('pedsim_simulator')
import rospy
import time
from numpy import random

from pedsim_srvs.srv import GetAgentState, SetAgentState, SetAgentStateRequest
from geometry_msgs.msg import Vector3


def set_social_force(x, y, z) -> bool:

        """
            Function to set the social force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        social_force = Vector3()
        social_force.x = x
        social_force.y = -0.9*y
        social_force.z = z

        new_agent_state = SetAgentStateRequest( 
                                        seq=orig_agent_state.seq,
                                        stamp=orig_agent_state.stamp,
                                        frame_id=orig_agent_state.frame_id,
                                        id=orig_agent_state.id,
                                        type=orig_agent_state.type,
                                        social_state=orig_agent_state.social_state,
                                        position=orig_agent_state.position,
                                        ortientation=orig_agent_state.ortientation,
                                        linear=orig_agent_state.linear,
                                        angular=orig_agent_state.angular,
                                        desired_force=orig_agent_state.desired_force,
                                        obstacle_force=orig_agent_state.obstacle_force,
                                        social_force=social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_social_force() -> Vector3:
    """
    Function to get the current value of social force

    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.social_force