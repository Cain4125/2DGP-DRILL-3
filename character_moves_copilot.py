import pico2d
from pico2d import *
import math

# 캔버스 크기
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# 이미지 위치
GRASS_X, GRASS_Y = 400, 30
CHAR_START_X, CHAR_START_Y = 400, 90

# 상태 정의
STATE_RECT = 0
STATE_TRI = 1
STATE_CIRC = 2

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 경로 좌표 (시작점 포함)
rect_path = [
    (400, 90), (CANVAS_WIDTH - 30, 90), (CANVAS_WIDTH - 30, CANVAS_HEIGHT - 30),
    (30, CANVAS_HEIGHT - 30), (30, 90), (400, 90)
]
# 삼각형 경로 좌표 (이등변삼각형, 시작점 포함)
tri_path = [
    (400, 90), (770, 90), (400, 570), (30, 90), (400, 90)
]
# 원 경로 정보 (400,90에서 시작해 한 바퀴 돌고 돌아오도록)
CIRC_CENTER_X = 400
CIRC_CENTER_Y = 330  # 90에서 240만큼 위
CIRC_RADIUS = 240
CIRC_START_ANGLE = -math.pi / 2  # (400,90)에서 위쪽 방향

state = STATE_RECT
running = True

# 경로 인덱스 및 각도
rect_idx = 0
tri_idx = 0
circ_angle = CIRC_START_ANGLE

x, y = CHAR_START_X, CHAR_START_Y

# 이동 속도
SPEED = 5
ANGLE_SPEED = 0.03

def move_toward(target_x, target_y, cur_x, cur_y, speed):
    dx, dy = target_x - cur_x, target_y - cur_y
    dist = math.hypot(dx, dy)
    if dist < speed:
        return target_x, target_y, True
    else:
        nx = cur_x + speed * dx / dist
        ny = cur_y + speed * dy / dist
        return nx, ny, False

while running:
    clear_canvas()
    grass.draw(GRASS_X, GRASS_Y)
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            running = False

    if state == STATE_RECT:
        tx, ty = rect_path[rect_idx + 1]
        x, y, arrived = move_toward(tx, ty, x, y, SPEED)
        if arrived:
            rect_idx += 1
            if rect_idx == len(rect_path) - 1:
                rect_idx = 0
                state = STATE_TRI
                x, y = CHAR_START_X, CHAR_START_Y
    elif state == STATE_TRI:
        tx, ty = tri_path[tri_idx + 1]
        x, y, arrived = move_toward(tx, ty, x, y, SPEED)
        if arrived:
            tri_idx += 1
            if tri_idx == len(tri_path) - 1:
                tri_idx = 0
                state = STATE_CIRC
                x, y = CHAR_START_X, CHAR_START_Y
                circ_angle = CIRC_START_ANGLE
    elif state == STATE_CIRC:
        circ_angle -= ANGLE_SPEED  # 시계방향
        x = CIRC_CENTER_X + CIRC_RADIUS * math.cos(circ_angle)
        y = CIRC_CENTER_Y + CIRC_RADIUS * math.sin(circ_angle)
        # 한 바퀴 돌고 시작점 근처면 종료
        if circ_angle <= CIRC_START_ANGLE - 2 * math.pi:
            x, y = CHAR_START_X, CHAR_START_Y
            state = STATE_RECT

close_canvas()
