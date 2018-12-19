import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.say_text("Welcome to Vector's Way. Programmed by Alex and Dad. Let's go!")
        b = robot.behavior
        b.drive_off_charger()
        right = degrees(-90)
        left = degrees(90)
        b.turn_in_place(right)
        b.drive_straight(distance_mm(150), speed_mmps(100))
        b.turn_in_place(left)
        b.drive_straight(distance_mm(180), speed_mmps(100))
        robot.say_text("Hmm... Which way should I go?")
        b.turn_in_place(left)
        b.drive_straight(distance_mm(180), speed_mmps(100))
        robot.say_text("I think I'll take a right!")
        b.turn_in_place(right)
        b.drive_straight(distance_mm(180), speed_mmps(100))
        robot.say_text("Should I go off the table? Or should I go this way? Ok! I'll go this way.")
        b.turn_in_place(right)
        b.drive_straight(distance_mm(250), speed_mmps(300))
        robot.say_text("Whoa! Almost there.")
        b.turn_in_place(left)
        b.drive_straight(distance_mm(120), speed_mmps(100))

        end_anim = 'anim_eyepose_happy'
        robot.anim.play_animation(end_anim)
        robot.say_text("I made it! Woo hoo!")
        lift_up(b)
        lift_down(b)
        lift_up(b)
        for i in range(0,1):
            b.turn_in_place(degrees(1080),degrees(360))
            i +=1
        robot.anim.play_animation('anim_dizzy_reaction_hard_01')
        robot.say_text("Ooo. I'm dizzy!")
        robot.say_text("All that driving made me tired. I'm going home now.")

        b.drive_on_charger()

def lift_up(b):
    b.set_lift_height(1,duration=0)

def lift_down(b):
    b.set_lift_height(0,duration=0)

if __name__ == "__main__":
    main()
