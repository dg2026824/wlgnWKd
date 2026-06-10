Web VPython 3.2

b = box(make_trail = True)
while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        b.pos = vec(0,0,0)
        b.opacity = 0.5
    if 'd' in k :
        b.pos.x = b.pos.x + 0.1
    if 'a' in k :
        b.pos.x = b.pos.x - 0.1
    if 'w' in k :
        b.pos.y = b.pos.y + 0.1
    if 's' in k :
        b.pos.y = b.pos.y - 0.1

-----------------------------------------------------------------------------------------------
Web VPython 3.2

body = box(pos=vec(0,0,0),size=vec(1,2,0.5),color=color.blue)
head = box(pos=vec(0,1.5,0),size=vec(0.8,0.8,0.5),color=color.yellow)
left_arm = box(pos=vec(-0.8,0.5,0),size=vec(0.4,1,0.3),color=color.red)
right_arm = box(pos=vec(0.8,0.5,0),size=vec(0.4,1,0.3),color=color.red)
left_leg = box(pos=vec(-0.4,-1.5,0),size=vec(0.4,1,0.3),color=color.green)
right_leg = box(pos=vec(0.4,-1.5,0),size=vec(0.4,1,0.3),color=color.green)
left_eye = box(pos=vec(-0.2,1.7,0.3),size=vec(0.2,0.2,0.1),color=color.black)
right_eye = box(pos=vec(0.2,1.7,0.3),size=vec(0.2,0.2,0.1),color=color.black)
mouth = box(pos=vec(0,1.3,0.3),size=vec(0.4,0.1,0.1),color=color.black)

-----------------------------------------------------------------------------------------------

Web VPython 3.2

body = box(pos=vec(0,0,0), size=vec(1.2, 2.2, 1.2), color=color.yellow, opacity=0.3)
head = box(pos=vec(0, 1.6, 0), size=vec(0.8, 0.8, 0.8), color=color.yellow)
left_arm = box(pos=vec(-0.8, 0.6, 0), size=vec(0.4, 1.2, 0.8), color=color.yellow)
right_arm = box(pos=vec(0.8, 0.6, 0), size=vec(0.4, 1.2, 0.8), color=color.yellow)
left_leg = box(pos=vec(-0.3, -1.6, 0), size=vec(0.4, 1.2, 0.8), color=color.yellow)
right_leg = box(pos=vec(0.3, -1.6, 0), size=vec(0.4, 1.2, 0.8), color=color.yellow)
left_eye = box(pos=vec(-0.2, 1.8, 0.41), size=vec(0.15, 0.15, 0.05), color=color.black)
right_eye = box(pos=vec(0.2, 1.8, 0.41), size=vec(0.15, 0.15, 0.05), color=color.black)
mouth = box(pos=vec(0, 1.4, 0.41), size=vec(0.3, 0.08, 0.05), color=color.black)
def create_dna(height, radius, total_steps):
    backbone_list = []
    rung_list = []
    rung_colors = [color.red, color.blue, color.green, color.orange]
    for i in range(total_steps):
        t = (i / total_steps) * (3 * pi) 
        y = - (height / 2) + (i / total_steps) * height
        pos1 = vec(radius * cos(t), y, radius * sin(t))
        pos2 = vec(radius * cos(t + pi), y, radius * sin(t + pi))
        p1 = sphere(pos=pos1, radius=0.03, color=color.white)
        p2 = sphere(pos=pos2, radius=0.03, color=color.white)
        backbone_list.append(p1)
        backbone_list.append(p2)
        if i % 2 == 0:
            current_color = rung_colors[(i // 2) % len(rung_colors)]
            rung_axis = pos2 - pos1
            r = cylinder(pos=pos1, axis=rung_axis, radius=0.015, color=current_color)
            rung_list.append(r)
    return backbone_list, rung_list
backbones, rungs = create_dna(height=1.6, radius=0.35, total_steps=40)
scene.camera.pos = vec(0, 0.5, 4)
while True:
    rate(30)
    for part in backbones:
        part.rotate(angle=0.03, axis=vec(0,1,0), origin=vec(0, part.pos.y, 0))
    for rung in rungs:
        rung.rotate(angle=0.03, axis=vec(0,1,0), origin=vec(0, rung.pos.y, 0))
