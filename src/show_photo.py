import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees


def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        # If necessary, move Vector's Head and Lift to make it easy to see his face
        robot.behavior.set_head_angle(degrees(45.0))
        robot.behavior.set_lift_height(0.0)

        current_directory = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_directory, "..", "face_images", "cozmo_image.jpg")

        # Load an image
        # image_file = Image.open(image_path)
        robot.camera.init_camera_feed()
        robot.anim.play_animation('anim_photo_focus_01')
        image_file = robot.camera.latest_image
        robot.anim.play_animation('anim_photo_shutter_01')
        image_file = robot.camera.latest_image
        image_file = image_file.resize((184, 96))

        screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
        robot.behavior.set_head_angle(degrees(45.0))
        robot.behavior.set_lift_height(0.0)

        # Convert the image to the format used by the Screen
        print("Display image on Vector's face...")
        
        robot.screen.set_screen_to_color(anki_vector.color.off, 4, interrupt_running=True)
        robot.screen.set_screen_with_image_data(screen_data, 4.0)
        time.sleep(5)

        robot.camera.close_camera_feed()


if __name__ == "__main__":
    main()