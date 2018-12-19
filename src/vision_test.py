import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
import time

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()
        robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
        robot.vision.enable_display_camera_feed_on_face()
        robot.vision.enable_face_detection(estimate_expression=True)
        time.sleep(60)

if __name__ == "__main__":
    main()