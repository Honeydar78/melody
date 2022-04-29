input.onButtonPressed(Button.A, function () {
    music.playMelody("E B C5 A B G A F ", 120)
})
input.onGesture(Gesture.Shake, function () {
    music.playMelody("E D G F B A C5 B ", 120)
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("B A G A G F A C5 ", 120)
})
