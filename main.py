import Five_libraries


# Calling functions from space_lib
print(Five_libraries.distance_between_planets(150, 200))
print(Five_libraries.spacecraft_speed(10, 500))

# Calling functions from robotics_lib
print(Five_libraries.move_forward(10, 5))
print(Five_libraries.pick_up_object("Box"))

# Calling functions from games_lib
print(Five_libraries.calculate_score(100, 2))
print(Five_libraries.roll_dice(6))

# Calling functions from space_explorer_lib
print(Five_libraries.escape_velocity(5.97e24, 6.371e6))
print(Five_libraries.travel_time(150000000, 50000))

# Calling functions from robot_control_lib
print(Five_libraries.turn_left(90))
print(Five_libraries.stop())
