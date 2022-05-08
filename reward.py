import math


def reward_function(params):
    # Example of penalize steering, which helps mitigate zig-zag behaviors

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

    # Center Line
    marker_1 = 0.12 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.5 * track_width

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.9
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Stay on right side of track
    if is_left_of_center == False:
        reward *= 1.1

    # Right-turn corner of Left-turn Corner
    next_wp = waypoints[closest_waypoints[1]]
    prev_wp = waypoints[closest_waypoints[0]]

    if closest_waypoints[1] == len(waypoints) -1:
        n_next_wp = waypoints[1]
    else:
        n_next_wp = waypoints[closest_waypoints[1] +1]

    angle_now = math.degrees(math.atan2(next_wp[1] - prev_wp[1], next_wp[0] - prev_wp[0]))
    angle_next = math.degrees(math.atan2(n_next_wp[1] - next_wp[1], n_next_wp[0] - next_wp[0]))

    if angle_next - angle_now > 10:     #Left turn
        if is_left_of_center == False:
            reward *= 0.7
    if angle_next - angle_now < -10:    #Right turn
        if is_left_of_center == True:
            reward *= 0.7

    # Speeding up by progress
    if steps % 450 == 0:    # check per 30 seconds
        if steps == 0:
            prev_progress = 0
            prev_progress_diff = 0
        progress_diff = progress - prev_progress
        prev_progress = progress
        
        if progress_diff > prev_progress_diff:
            reward *= 1.1
        prev_progress_diff = progress_diff


    return float(reward)
