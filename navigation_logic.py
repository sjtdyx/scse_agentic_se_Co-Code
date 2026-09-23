def decide_action(front_blocked, left_blocked, right_blocked, goal_direction):
    if goal_direction == "ahead":
        if not front_blocked:
            return "FORWARD"
    elif goal_direction == "left":
        if not left_blocked:
            return "LEFT"
    elif goal_direction == "right":
        if not right_blocked:
            return "RIGHT"
    if not front_blocked:
        return "FORWARD"
    elif not left_blocked:
        return "LEFT"
    elif not right_blocked:
        return "RIGHT"
    else:
        return "STOP"