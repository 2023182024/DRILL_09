from pico2d import *

TUK_WIDTH, TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground=load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running=True
x,y=TUK_WIDTH//2,TUK_HEIGHT//2
frame=0

def handle_events():

    pass


while running:

    clear_canvas()
    
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)
    
    pass