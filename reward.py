import math

class Reward():
    def __init__(self):
        self.prev_speed = 0
        self.speed_list = []
        self.prev_progress = 0
        self.prev_progress_diff = 0

    def reward_function_in_class(self, params):
        # Read input parameters
        distance_from_center = params['distance_from_center']
        track_width = params['track_width']
        waypoints = params['waypoints']
        closest_waypoints = params['closest_waypoints']
        heading = params['heading']
        all_wheels_on_track = params['all_wheels_on_track']
        progress = params['progress']
        steering_angle = params['steering_angle']
        x = params['x']
        y = params['y']
        steps = params['steps']
        is_left_of_center = params['is_left_of_center']
        speed = params['speed']

        # Center Line
        reward = 1

        marker_1 = 0.12 * track_width
        marker_2 = 0.3 * track_width
        marker_3 = 0.4 * track_width
        marker_4 = 0.5 * track_width

        # Right-turn corner of Left-turn Corner
        next_wp = waypoints[closest_waypoints[1]]
        prev_wp = waypoints[closest_waypoints[0]]

        if closest_waypoints[1] == len(waypoints) -1:
            n_next_wp = waypoints[0]
        else:
            n_next_wp = waypoints[closest_waypoints[1] +1]

        angle_now = math.degrees(math.atan2(next_wp[1] - prev_wp[1], next_wp[0] - prev_wp[0]))
        angle_next = math.degrees(math.atan2(n_next_wp[1] - next_wp[1], n_next_wp[0] - next_wp[0]))

        if angle_next - angle_now > 0:     #Trun left
            if is_left_of_center == False:
                reward *= 0.6
            else:
                reward *= 1.02
            if distance_from_center > marker_1 and distance_from_center <= marker_4:
                reward *= 1.21
            else:
                reward *= 0.6

        else:   #straight line or turn right
            if is_left_of_center == False:
                reward *= 1.01
            if distance_from_center <= marker_1:
                reward *= 1.25
            elif distance_from_center <= marker_2:
                reward *= 1.2
            elif distance_from_center <= marker_3:
                reward *= 0.8
            elif distance_from_center <= marker_4:
                reward *= 0.6
            else:
                reward = 1e-3  

        # Speeding up by average speed
        self.speed_list.append(speed)
        if steps % 15 == 0:    # check every 1 seconds
            avg_speed = sum(self.speed_list) / 15
            if avg_speed > self.prev_speed:
                reward *= 1.22
            self.prev_speed = avg_speed
            self.speed_list = []

        return float(reward)


reward_object = Reward()

def reward_function(params):
    return reward_object.reward_function_in_class(params)