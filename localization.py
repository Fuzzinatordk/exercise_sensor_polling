"""
Actual localization is beyond this course.
Imagine a smart sensor fusion algorithm in the update function.

Don't change this file.
"""


def update(state, acc_data, cam_data, gps_data):
    new_state = state + acc_data + cam_data + gps_data
    return new_state * 0.2
