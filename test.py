class Reward:
    def __init__(self):
        self.prev_speed = 0
        self.speed_list = [0]

    def reward_function_in_class(self, params):
        score = 0
        
        speed = params['speed']

        if self.prev_speed < speed:
            score += 1
            self.prev_speed = speed
            print(self.prev_speed)
        self.speed_list.append(speed)
        print(self.speed_list)
        print(sum(self.speed_list))
        self.speed_list = []
        
        return score


reward_object = Reward()

def reward_function(params):
    return reward_object.reward_function_in_class(params)

reward_function({'speed':100})
reward_function({'speed':200})
reward_function({'speed':300})
reward_function({'speed':400})