def on_button_pressed_a():
    music.play_melody("E B C5 A B G A F ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    music.play_melody("E D G F B A C5 B ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    music.play_melody("B A G A G F A C5 ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)
