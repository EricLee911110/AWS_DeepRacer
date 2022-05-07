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

    # Angle
    next_WP = waypoints[closest_waypoints[1]]
    prev_WP = waypoints[closest_waypoints[0]]

    track_angle = math.degrees(math.atan2(next_WP[1] - prev_WP[1], next_WP[0] - prev_WP[0]))
    angle_diff = abs(heading - track_angle)

    if angle_diff > 180:
        angle_diff = abs(360 - angle_diff)

    ANGLE_THRESHOLD = 20

    if angle_diff > ANGLE_THRESHOLD:
        reward *= 0.1

    # All wheels on track
    if all_wheels_on_track == False:
        reward *= 0.01
    

    


    return float(reward)
