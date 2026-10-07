from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
CHARACTER_FRAME_SIZE = 100
CHARACTER_FRAME_COUNT = 8
MOVE_DISTANCE = 10
FRAME_INTERVAL = 0.05
CHARACTER_HALF_SIZE = CHARACTER_FRAME_SIZE // 2

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dirx = 0
diry = 0


def handle_events():
    global running
    global dirx, diry

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx = 1
            elif event.key == SDLK_LEFT:
                dirx = -1
            elif event.key == SDLK_UP:
                diry = 1
            elif event.key == SDLK_DOWN:
                diry = -1
            elif event.key == SDLK_ESCAPE:
                running = False


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    source_x = frame * CHARACTER_FRAME_SIZE
    source_y = CHARACTER_FRAME_SIZE

    if dirx == -1:
        character.clip_composite_draw(
            source_x, source_y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE,
            0, 'h', x, y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE
        )
    elif diry == 1:
        character.clip_composite_draw(
            source_x, source_y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE,
            math.pi / 2, '', x, y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE
        )
    elif diry == -1:
        character.clip_composite_draw(
            source_x, source_y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE,
            -math.pi / 2, '', x, y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE
        )
    else:
        character.clip_draw(
            source_x, source_y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE,
            x, y, CHARACTER_FRAME_SIZE, CHARACTER_FRAME_SIZE
        )

    update_canvas()
    handle_events()

    # Clamp the character center so its 100x100 frame remains fully visible.
    x = max(CHARACTER_HALF_SIZE, min(TUK_WIDTH - CHARACTER_HALF_SIZE, x + dirx * MOVE_DISTANCE))
    y = max(CHARACTER_HALF_SIZE, min(TUK_HEIGHT - CHARACTER_HALF_SIZE, y + diry * MOVE_DISTANCE))

    frame = (frame + 1) % CHARACTER_FRAME_COUNT
    delay(FRAME_INTERVAL)
