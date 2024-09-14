controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    farmer.setImage(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f . . . . . . 
        . . . . f f e e e e f f . . . . 
        . . . f e e e f f e e e f . . . 
        . . . f f f f 2 2 f f f f . . . 
        . . f f e 2 e 2 2 e 2 e f f . . 
        . . f e 2 f 2 f f f 2 f e f . . 
        . . f f f 2 f e e 2 2 f f f . . 
        . . f e 2 f f e e 2 f e e f . . 
        . f f e f f e e e f e e e f f . 
        . f f e e e e e e e e e e f f . 
        . . . f e e e e e e e e f . . . 
        . . . e f f f f f f f f 4 e . . 
        . . . 4 f 2 2 2 2 2 e d d 4 . . 
        . . . e f f f f f f e e 4 . . . 
        . . . . f f f . . . . . . . . . 
        `)
    farmer.y += -5
    farmer.startEffect(effects.spray, 100)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    scene.setBackgroundImage(img`
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999bbb999999999999999999999999999999999999999999999999999999999999999991111111999
        999999999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbb9999999999999999999999999999999999999999999999999999999999999911111111199
        99999999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbb9999999999999999999999999999999999999999999999999999999999999111111111119
        9999999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbbb999999999999999999999999999999999999999999999999999999999999111111111111
        999999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbbbbbb9999999999999999999999999999999999999999999999999999111111111111111111
        99999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbbbbbbbb999999999999999999999999999999999999999999999999991111111111111111111
        9999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbbbbbbbbbb99999999999999999999999999999999999999999999999991111111111111111111
        999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbcccccbbbbbbbb999999999999999999999999999999999999999999999911111111111111111111
        9999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbbcccccccbbbbbbbb9999999999999999999999999999999999999999999911111111111111111111
        111999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbccccccccccbbbbbbbb999999999999999999999999999999999999999991111111111111111111111
        1111199999999999999999999999999999999999999999999999999999999999999999bbbbbbbbccccccccccccbbbbbbbbb9999999999999999999999999999999999999111111111111111111111111
        111111999999999999999999999999999999999999999999999999999999999999999bbbbbbccccccccccccccccbbbbbbbbbb99999999999999999999999999999999911111111111111111111111111
        1111119999999999999999999999999999999999999999999999999999999999999bbbbbbccccccccccccccccccccbbbbbbbbbb999999999999999999999999999999911111111111111111111111111
        11111199999999999999999999999999999999999999999999999999999999999bbbbbcccccccccccccccccccccccccbbbbbbbbbb9999999999999999999999999111111111111111111111111111111
        11111119999999999999999999999999999999999999999999999999999999bbbbbbcccccccccccccccccccccccccccccccbbbbbbb999999999999999999999111111111111111111111111111111111
        111111199999999999999999999999999999999999999999999999999999bbbbbbbccccccccccccccccccccccccccccccccccbbbbbbbb999999999999999911111111111111111111111111111111111
        1111111999999999999999999999999999999999999999999999999999bbbbbbbbbccccccccccccccccccccccccccccccccccbbbbbbbbbb9999999999999911111111111111111111111111111111111
        1111111999999999999999999999999999999999999999999999999bbbbbbbbbbbbccccccccccccccccccccccccccccccccccbbbbbbbbbbbb99999999999911111111111111111111111111111111111
        111111119999999999999999999999999999999999999999999bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbb999999999911111111111111111111111111111111111
        111111111199999999999999999999999999999999999999bbbbbbbbbbbbbbbbb222bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9999999911111111111111111111111111111111111
        11111111111999999999999999999999999999999999999bbbbbbbbbbbbbbbbb2bbbbbbb2bb2bbbbbbb222bbbbb2222bbbbbbbbbbbbbbbbbbbbbbbb99999991111111111111111111111111111111111
        1111111111111999999999999999999999999999999999bbbbbbbbbbbbbbbbbb22bbbbbb2bb22bbbbb2bbb2bbbb2bbb2bbbbbbbbbbbbbbbbbbbbbbb99999999991111111111111111111111111111111
        1111111111111119999999999999999999999999999999bbbbbbbbbbbbbbbbbbb22bbbbb22222bbbbb2bbb2bbbb2bb2bbbbbbbbbbbbbbbbbbbbbbbb99999999999991111111111111111111111111111
        1111111111111119999999999999999999999999999999bbbbbbbbbbbbbbbbbbbb2bbbbb2bbb2bbbbb2222bbbbb2222bbbbbbbbbbbbbbbbbbbbbbbb99999999999999999911111111111111111111111
        111111111111111199999999999999999999999999999999999bbbbbbbbbbbb2222bbbbb2bbb2bbbbbbbbbbbbbb2bbbbbbbbbbbbbbbbb999999999999999999999999999999911111111111111111111
        111111111111111119999999999999999999999999999999999bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb2bbbbbbbbbbbbbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111199999999999999999999999999999999bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111999999999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111199999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111199999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111119999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111119999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111119999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111119999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111119999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111111199999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111111119999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        111111111111111111111999999999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccccccccc777ccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccccccccc777ccccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccccccccc7777cccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccccccccc777777ccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccccccccc777777ccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccccccccc777777ccccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccccccccc7777777cccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccccccccc77777777ccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccccc77777777777ccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccccc7777777777777ccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc77777777777777ccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc77777777777777ccccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc777777677777777cccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc7777777777776667ccccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc66677777777766677cccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccc666677777777766677cccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccc666677677777766677cccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccc666667777777767777cccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc76667777776777777cccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccccc766677777777777777ccccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccccc77777777777777777777cccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbcccccccccccc7777777777777777777777ccccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccccc777767777777777777677777cccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccccc777777777776777777777666777ccccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccc777777777777777777777776667777cccccccccccbbbbb999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999bbbbbccccccc7777777777767777777777766677777ccccccccccbbbbb999999999999999999999999999999999999999999999999999
        977777779999999999999999999999999999999999999999999bbbbbccccccc7777777777777766677777777777777ccccccccccbbbbb999999999999999999999999999999999999999999999999999
        777777777777777999999999999999999977777777777777777bbbbbccccccc7777777777777766677777777777777ccccccccccbbbbb999999999999999999999999999777777777777777777777779
        777777777777777777779999999999777777777777777777777bbbbbcccccccccc777777777776667777777777777cccccccccccbbbbb777777799999999999777777777777777777777777777777779
        777777777777777777777777777777777777777777777777777bbbbbcccccccccccc77777777777777777777777cccccccccccccbbbbb777777777777777777777777777777777777777777777777779
        777777777777777777777777777777777777777777777777777bbbbbccccccccccccccc777777777777777777cccccccccccccccbbbbb777777777777777777777777777777777777777777777777779
        777777777777777777777777777777777777777777717777777bbbbbccccccccccccccccc7777bbbc777ccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777779
        777777777777777777777777777777777777777777777777777bbbbbcccccccccccccccccccccbbbccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777711177777777
        777777777777717777777777777777777777777777777777777bbbbbcccccccccccccccccccccbbbccccccccccccccccccccccccbbbbb777777777777777777777777777777777717777711177777777
        777777777777777777777777777777777777777177777777777bbbbbcccccccccccccccccccccbbbccccccccccccccccccccccccbbbbb777777777777777777777771777777777777777711177777777
        777777777777777777777777777777777777771117777777777bbbbbcccccccccccccccccccccbbbccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777777777777777777777777777777777777771117777777777bbbbbcccccccccccccccccccccbbbccccccccccccccccccccccccbbbbb777771777777777777777777777777777777777777777777777
        777777777111777777777777777777777777771117777777777bbbbbcccccccccccccccccccccbbbccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777777777111777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777777777111777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777111777777777777777777777777777777777777
        777777777777777777777777777771117777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777111777777777777777777777777777777777777
        777777777777777777777777777771117777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777111777777777777777777711177777777777777
        777777777777777777777777777771117777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777711177777777777777
        777777777777777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777711177777777777777
        777777777777777777777777777777777777777771777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777717777777777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777777777777777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777777777777777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777717777777
        777777777777777777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777717777777777777
        777777777711177777777777777777777777777777777777777bbbbbccccccccccccccccccccccccccccccccccccccccccccccccbbbbb777777777777777777777777777777777777777777777777777
        777777777711177777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777717777777777777777777777777777777777777777777
        777777777711177777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777777777777777777777777777777777777
        777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777777777777777777777777777777777777
        777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777777777777777777777777777777777777
        777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777777777777777777777777777777777777
        7777777777777777777777771777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777717777777777777777777777777
        7777777777777777777777777777777771117777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777771117777777777
        7777777777777777777777777777777771117777777777777777777777777777777777777777777777777777777777777777777777777777777777777777711177777777777777777771117777777777
        7777777777777777777777777777777771117777777777777777717777777777777777777777777777777777777777777777777777777777777777777777711177777777777777777771117777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777711177777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777177777777777777777777777777777777777777777777777777777777777777777777777777777777777777771777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777177777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777771777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        `)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    farmer.setImage(img`
        . . . . . . . . . . . . . . . . 
        . . . . f f f f f f . . . . . . 
        . . . f 2 f e e e e f f . . . . 
        . . f 2 2 2 f e e e e f f . . . 
        . . f e e e e f f e e e f . . . 
        . f e 2 2 2 2 e e f f f f . . . 
        . f 2 e f f f f 2 2 2 e f . . . 
        . f f f e e e f f f f f f f . . 
        . f e e 4 4 f b e 4 4 e f f . . 
        . . f e d d f 1 4 d 4 e e f . . 
        . . . f d d d e e e e e f . . . 
        . . . f e 4 e d d 4 f . . . . . 
        . . . f 2 2 e d d e f . . . . . 
        . . f f 5 5 f e e f f f . . . . 
        . . f f f f f f f f f f . . . . 
        . . . f f f . . . f f . . . . . 
        `)
    farmer.x += -5
    farmer.startEffect(effects.spray, 100)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    farmer.setImage(img`
        . . . . . . . . . . . . . . . . 
        . . . . . f f f f f f . . . . . 
        . . . f f e e e e f 2 f . . . . 
        . . f f e e e e f 2 2 2 f . . . 
        . . f e e e f f e e e e f . . . 
        . . f f f f e e 2 2 2 2 e f . . 
        . . f e 2 2 2 f f f f e 2 f . . 
        . f f f f f f f e e e f f f . . 
        . f f e 4 4 e b f 4 4 e e f . . 
        . f e e 4 d 4 1 f d d e f . . . 
        . . f e e e e e d d d f . . . . 
        . . . . f 4 d d e 4 e f . . . . 
        . . . . f e d d e 2 2 f . . . . 
        . . . f f f e e f 5 5 f f . . . 
        . . . f f f f f f f f f f . . . 
        . . . . f f . . . f f f . . . . 
        `)
    farmer.x += 5
    farmer.startEffect(effects.spray, 100)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    farmer.setImage(img`
        . . . . . . f f f f . . . . . . 
        . . . . f f f 2 2 f f f . . . . 
        . . . f f f 2 2 2 2 f f f . . . 
        . . f f f e e e e e e f f f . . 
        . . f f e 2 2 2 2 2 2 e e f . . 
        . . f e 2 f f f f f f 2 e f . . 
        . . f f f f e e e e f f f f . . 
        . f f e f b f 4 4 f b f e f f . 
        . f e e 4 1 f d d f 1 4 e e f . 
        . . f e e d d d d d d e e f . . 
        . . . f e e 4 4 4 4 e e f . . . 
        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
        . . . . . f f f f f f . . . . . 
        . . . . . f f . . f f . . . . . 
        `)
    farmer.y += 5
    farmer.startEffect(effects.spray, 100)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    scene.setBackgroundImage(assets.image`nightFarm`)
})
let farmer: Sprite = null
scene.setBackgroundImage(assets.image`dayFarm`)
farmer = sprites.create(assets.image`farmer`, SpriteKind.Player)
music.play(music.stringPlayable("G B A G C5 B A B ", 120), music.PlaybackMode.UntilDone)
