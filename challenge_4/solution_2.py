import math


def norm(x1, y1, x2=0, y2=0):
    """
    Gives the distance between (x1, y1) and (x2, y2)
    """
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def cartesian_to_polar(x, y):
    """
    convert cartesian coordinates (x, y) to polar coordinates (angle, norm)
    """
    if x != 0:
        alpha = math.atan2(y, x)
    elif y > 0:
        alpha = math.pi/2
    elif y < 0:
        alpha = -math.pi/2
    else:
        alpha = 0
    length = norm(x, y)
    return alpha, length


def solution(dimensions, your_position, trainer_position, distance):
    dimension_x, dimension_y = dimensions
    your_position_x, your_position_y = your_position
    trainer_position_x, trainer_position_y = trainer_position

    # polar coordinates normalised with your_position at (0, 0)
    polar_positions = list()

    # Get all positions, including reflected positons in the mirrors) for yourself and the trainers
    for x in range(distance//dimension_x+2):
        for y in range(distance//dimension_y+2):
            if y % 2 == 0:
                trainer_temp_pos_y = y*dimension_y + trainer_position_y
                your_temp_pos_y = y*dimension_y + your_position_y
            else:
                trainer_temp_pos_y = y*dimension_y + (dimension_y - trainer_position_y)
                your_temp_pos_y = y*dimension_y + (dimension_y - your_position_y)
            if x % 2 == 0:
                trainer_temp_pos_x = x*dimension_x + trainer_position_x
                your_temp_pos_x = x*dimension_x + your_position_x
            else:
                trainer_temp_pos_x = x*dimension_x + (dimension_x - trainer_position_x)
                your_temp_pos_x = x*dimension_x + (dimension_x - your_position_x)

            for i in (-1, 1):
                for j in (-1, 1):
                    # Normalise positons by setting your_positon at (0, 0)
                    polar_trainer_alpha, polar_trainer_length = cartesian_to_polar(i*trainer_temp_pos_x-your_position_x, j*trainer_temp_pos_y-your_position_y)
                    if polar_trainer_length <= distance:
                        polar_positions.append((polar_trainer_alpha, polar_trainer_length, "trainer"))
                    polar_your_alpha, polar_your_length = cartesian_to_polar(i*your_temp_pos_x-your_position_x, j*your_temp_pos_y-your_position_y)
                    if 0 < polar_your_length <= distance:
                        polar_positions.append((polar_your_alpha, polar_your_length, "your"))
    
    # Sort the positions to be able to iterate through them
    # just as if you are turning on yourself to look towards every reflection
    polar_positions.sort()

    count = 0
    hit = False
    last_alpha = None
    for alpha, _, target_type in polar_positions:
        # If same amgle as previous iteration
        # it means the laser has been intercepted and cannot go further
        hit = alpha == last_alpha
        
        # if target is the trainer and the laser has not been intercepted yet
        if target_type == "trainer" and not hit:
            count += 1
        
        last_alpha = alpha

    return count


print(solution([3, 2], [1, 1], [2, 1], 4))  # A: 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # A: 9
print(solution([300, 275], [150, 150], [185, 100], 20000))  # A: 15195
print(solution([2, 3], [1, 1], [1, 2], 400))  # A: 46143 ?
