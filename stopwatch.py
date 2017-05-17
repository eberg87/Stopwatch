# template for "Stopwatch: The Game"

import simplegui

# define global variables
count = 0
stp_count = 0
stp = 0
start = 1
suc_stp = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t_min = t/600
    t_rem = t%600
    t_seg = t_rem/10
    t_mseg = t_rem%10
    if t_seg<10:
        adj_seg = "0" + str(t_seg)
    else:
        adj_seg = str(t_seg)

    return str(t_min) + ":" + adj_seg + "." + str(t_mseg)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stp, start
    if start == 0:
        timer.start()
        stp = 0
        start = 1
    else:
        pass

def stop():
    global stp_count, stp, start, suc_stp
    if stp == 0:
        stp_count += 1
        timer.stop()
        stp = 1
        start = 0
        if count%600%10 == 0:
            suc_stp += 1
        else:
            pass
    else:
        pass
    
def reset():
    global count, stp_count, stp, start, suc_stp
    timer.stop()
    count = 0
    stp_count = 0
    stp = 1
    start = 0
    suc_stp = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    print count
    count += 1

# define draw handler
def draw_handler(canvas):
    global count, stp_count, suc_stp
    # convert count to string.
    str_count = str(format(count))
    canvas.draw_text(str_count, (110, 165), 40, 'White')
    str_stp = str(suc_stp) + "/" + str(stp_count)
    canvas.draw_text(str_stp, (215, 50), 40, 'White')

# create frame
f = simplegui.create_frame ("Stopwatch: The game", 300, 300)
timer = simplegui.create_timer (100, tick)

# register event handlers
f.set_draw_handler(draw_handler)
f.add_button("Start", start, 100)
f.add_button("Stop", stop, 100)
f.add_button("Reset", reset, 100)

# start frame
f.start()
timer.start()

# Please remember to review the grading rubric
