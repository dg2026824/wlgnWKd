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
