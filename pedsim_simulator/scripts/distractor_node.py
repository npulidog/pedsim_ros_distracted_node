#!/usr/bin/env python
import roslib
roslib.load_manifest('pedsim_simulator')
import rospy
import time
from numpy import random

from pedsim_srvs.srv import GetAgentState, SetAgentState, SetAgentStateRequest
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Pose, Point, Quaternion, Twist

def set_position(x, y, z) -> bool:

        """
            Function to set the position in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        position = Point()
        position.x = x
        position.y = y
        position.z = z

        new_agent_state = SetAgentStateRequest( 
                                        seq=orig_agent_state.seq,
                                        stamp=orig_agent_state.stamp,
                                        frame_id=orig_agent_state.frame_id,
                                        id=orig_agent_state.id,
                                        type=orig_agent_state.type,
                                        social_state=orig_agent_state.social_state,
                                        position=position,
                                        ortientation=orig_agent_state.ortientation,
                                        linear=orig_agent_state.linear,
                                        angular=orig_agent_state.angular,
                                        desired_force=orig_agent_state.desired_force,
                                        obstacle_force=orig_agent_state.obstacle_force,
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_position() -> Point:
    """
    Function to get the current value of position
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.position

def set_orientation(x, y, z, w) -> bool:

        """
            Function to set the orientation in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        orientation = Quaternion()
        orientation.x = x
        orientation.y = y
        orientation.z = z
        orientation.w = w

        new_agent_state = SetAgentStateRequest( 
                                        seq=orig_agent_state.seq,
                                        stamp=orig_agent_state.stamp,
                                        frame_id=orig_agent_state.frame_id,
                                        id=orig_agent_state.id,
                                        type=orig_agent_state.type,
                                        social_state=orig_agent_state.social_state,
                                        position=orig_agent_state.position,
                                        ortientation=ortientation,
                                        linear=orig_agent_state.linear,
                                        angular=orig_agent_state.angular,
                                        desired_force=orig_agent_state.desired_force,
                                        obstacle_force=orig_agent_state.obstacle_force,
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_orientation() -> Quaternion:
    """
    Function to get the current value of orientation
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.orientation

def set_linear(x, y, z) -> bool:

        """
            Function to set the linear in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        linear = Vector3()
        linear.x = 0.8*x
        linear.y = 0.8*y
        linear.z = 0.8*z

        new_agent_state = SetAgentStateRequest( 
                                        seq=orig_agent_state.seq,
                                        stamp=orig_agent_state.stamp,
                                        frame_id=orig_agent_state.frame_id,
                                        id=orig_agent_state.id,
                                        type=orig_agent_state.type,
                                        social_state=orig_agent_state.social_state,
                                        position=orig_agent_state.position,
                                        ortientation=orig_agent_state.ortientation,
                                        linear=linear,
                                        angular=orig_agent_state.angular,
                                        desired_force=orig_agent_state.desired_force,
                                        obstacle_force=orig_agent_state.obstacle_force,
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_linear() -> Vector3:
    """
    Function to get the current value of linear
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.linear

def set_angular(x, y, z) -> bool:

        """
            Function to set the angular in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        angular = Vector3()
        angular.x = 0.8*x
        angular.y = 0.8*y
        angular.z = 0.8*z

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
                                        angular=angular,
                                        desired_force=orig_agent_state.desired_force,
                                        obstacle_force=orig_agent_state.obstacle_force,
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_angular() -> Vector3:
    """
    Function to get the current value of angular
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.angular

def set_desired_force(x, y, z) -> bool:

        """
            Function to set the desired force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        desired_force = Vector3()
        desired_force.x = random.randrange(80,100)*x /100
        desired_force.y = random.randrange(80,100)*y /100
        desired_force.z = random.randrange(80,100)*z /100

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
                                        desired_force=desired_force,
                                        obstacle_force=orig_agent_state.obstacle_force,
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_desired_force() -> Vector3:
    """
    Function to get the current value of desired force
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.desired_force

def set_obstacle_force(x, y, z) -> bool:

        """
            Function to set the obstacle force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        obstacle_force = Vector3()
        obstacle_force.x = 0.85*x
        obstacle_force.y = 0.85*y
        obstacle_force.z = 0.85*z

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
                                        obstacle_force=obstacle_force,
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_obstacle_force() -> Vector3:
    """
    Function to get the current value of obstacle force
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.obstacle_force

def set_social_force(x, y, z) -> bool:

        """
            Function to set the social force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        social_force = Vector3()
        social_force.x = 0.8*x
        social_force.y = 0.8*y
        social_force.z = 0.8*z

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

def set_group_coherence_force(x, y, z) -> bool:

        """
            Function to set the group coherence force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        group_coherence_force = Vector3()
        group_coherence_force.x = 0.95*x
        group_coherence_force.y = 0.95*y
        group_coherence_force.z = 0.95*z

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
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_group_coherence_force() -> Vector3:
    """
    Function to get the current value of group coherence force
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.group_coherence_force

def set_group_gaze_force(x, y, z) -> bool:

        """
            Function to set the group gaze force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        group_gaze_force = Vector3()
        group_gaze_force.x = 0.95*x
        group_gaze_force.y = 0.95*y
        group_gaze_force.z = 0.95*z

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
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_group_gaze_force() -> Vector3:
    """
    Function to get the current value of group gaze force
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.group_gaze_force

def set_group_repulsion_force(x, y, z) -> bool:

        """
            Function to set the group repulsion force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        group_repulsion_force = Vector3()
        group_repulsion_force.x = 0.95*x
        group_repulsion_force.y = 0.95*y
        group_repulsion_force.z = 0.95*z

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
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=group_repulsion_force,
                                        random_force=orig_agent_state.random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_group_repulsion_force() -> Vector3:
    """
    Function to get the current value of group repulsion force
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.group_repulsion_force

def set_random_force(x, y, z) -> bool:

        """
            Function to set the random force in a random factor
        
        """

        rospy.wait_for_service("pedsim_srvs/GetAgentState")
        rospy.wait_for_service("pedsim_srvs/SetAgentState")

        client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
        orig_agent_state = client_get_agent_state()

        random_force = Vector3()
        random_force.x = x
        random_force.y = y
        random_force.z = z

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
                                        social_force=orig_agent_state.social_force,
                                        group_coherence_force=orig_agent_state.group_coherence_force,
                                        group_gaze_force=orig_agent_state.group_gaze_force,
                                        group_repulsion_force=orig_agent_state.group_repulsion_force,
                                        random_force=random_force)
    
        client_set_agent_state = rospy.ServiceProxy("pedsim_srvs/SetAgentState", SetAgentState)
        distracted_agent = client_set_agent_state(new_agent_state)

        return distracted_agent.finished

def get_random_force() -> Vector3:
    """
    Function to get the current value of random force
    """

    rospy.wait_for_service("pedsim_srvs/GetAgentState")
    client_get_agent_state = rospy.ServiceProxy("pedsim_srvs/GetAgentState", GetAgentState)
    agent_state = client_get_agent_state()

    return agent_state.random_force
