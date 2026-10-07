from pico2d import *

TUK_WIDTH, TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground=load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running=True
x,y=TUK_WIDTH//2,TUK_HEIGHT//2
frame=0
dirx=0
diry=0

def handle_events():
    global running
    global dirx,diry
    
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dirx+=1
            elif event.key==SDLK_LEFT:
                dirx-=1
            elif event.key==SDLK_UP:
                diry+=1
            elif event.key==SDLK_DOWN:
                diry-=1
            elif event.key==SDLK_ESCAPE:
                running=False
    pass    


while running:

    clear_canvas()
    
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    
    update_canvas()
    handle_events()
    if(x>0 and x<TUK_WIDTH):
        x+=dirx*5
    if(y>0 and y<TUK_HEIGHT):
        y+=diry*5
    frame = (frame + 1) % 8
    delay(0.05)
    
    pass