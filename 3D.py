import tkinter
import math
a = tkinter.Tk()
a.title = "test"

cam_postion = [1,80,20]
point_postion =[
    #[x,y,z],[x,y]
    [[100,50,30],[0,0]],#a0
    [[100,150,30],[0,0]],#b1
    [[200,50,30],[0,0]],#c2
    [[200,150,30],[0,0]],#d3

    [[100,50,130],[0,0]],#e4
    [[100,150,130],[0,0]],#f5
    [[200,50,130],[0,0]],#g6
    [[200,150,130],[0,0]],#h7
]
bar_postion = [
    [0,1],#ab
    [1,3],#bd
    [3,2],#dc
    [2,0],#ca

    [4,5],#ef
    [5,7],#fh
    [7,6],#hg
    [6,4],#ge
    [0,4],
    [1,5],
    [2,6],
    [3,7]
]

#座標変換
def change_dimension():
    for i in range(len(point_postion)):
        for s in range(len(point_postion[i][0])):
            h = 0
            long_postion = 0
            x = 0
            if s == 0:
                #xを二次元に変換
                h = abs(cam_postion[2])/(abs(cam_postion[2])+abs(point_postion[i][0][2]))
                long_postion = abs(abs(cam_postion[0])-abs(point_postion[i][0][0]))
                # x = (long_postion*h)+point_postion[i][0][0]
                if cam_postion[0] > point_postion[i][0][0]:
                    x = point_postion[i][0][0] - (long_postion*h)
                elif cam_postion[0] < point_postion[i][0][0]:
                    x = (long_postion*h)+point_postion[i][0][0]
                    
                point_postion[i][1][0] = x
            if s == 1:
                h = abs(cam_postion[2])/(abs(cam_postion[2])+abs(point_postion[i][0][2]))
                long_postion = abs(abs(cam_postion[1])-abs(point_postion[i][0][1]))
                # x = (long_postion*h)+point_postion[i][0][1]
                if cam_postion[1] > point_postion[i][0][1]:
                    x = point_postion[i][0][1] - (long_postion*h)
                elif cam_postion[1] < point_postion[i][0][1]:
                    x = (long_postion*h)+point_postion[i][0][1]
                point_postion[i][1][1] = x

#print(point_postion)
c = tkinter.Canvas(a,width=300,height=300)
c.pack()
for i in range(len(point_postion)):
    print(point_postion[i][1])
#点を打つ
def draw():
    for u in range(len(point_postion)):
        # ln = [math.floor(point_postion[u][1][0])+2.5,math.floor(point_postion[u][1][1])+2.5,math.floor(point_postion[u][1][0])-2.5, math.floor(point_postion[u][1][1])-2.5]

        if u < 4:
            c.create_oval(point_postion[u][1][0]+2.5,point_postion[u][1][1]+2.5,point_postion[u][1][0]-2.5, point_postion[u][1][1]-2.5,fill="red")
        else:
            #c.create_oval(float(point_postion[u][1][0])+2.5, float(point_postion[u][1][1])+2.5, float(point_postion[u][1][0])-2.5, float(point_postion[u][1][1])-2.5,fill="blue")
            #print(ln)
            c.create_oval(point_postion[u][1][0]+2.5, point_postion[u][1][1]+2.5, point_postion[u][1][0]-(2.5), point_postion[u][1][1]-(2.5),fill="blue")

    #線を引く
    for o in range(len(bar_postion)):
        #c.create_line(point_postion[bar_postion[o][0]][1][0], point_postion[bar_postion[o][0]][1][1], point_postion[bar_postion[o][1]][1][0], point_postion[bar_postion[o][1]][1][1], fill='red')
        c.create_line(math.floor(point_postion[bar_postion[o][0]][1][0]), math.floor(point_postion[bar_postion[o][0]][1][1]), math.floor(point_postion[bar_postion[o][1]][1][0]), math.floor(point_postion[bar_postion[o][1]][1][1]), fill='red')
def key_press(event):
    if event.keysym=="Up":
        if cam_postion[1]-5 >0:
            cam_postion[1]-=5
            #print(cam_postion)
            main()
            #print("test")
    elif event.keysym=="Left":
        if cam_postion[0]-5 >0:
        
            cam_postion[0]-=5
            #print(cam_postion)
            
            main()
        
    elif event.keysym=="Right":
        if cam_postion[0]+5 <300:
            cam_postion[0]+=5
            #print(cam_postion)
            
            main()
        
    elif event.keysym=="Down":
        if cam_postion[1]+5 <300:
            cam_postion[1]+=5
            #print(cam_postion)
            
            main()
    elif event.keysym=="w":
        cam_postion[2]+=5
        #print(cam_postion)
        
        main()
    elif event.keysym=="s":
        if cam_postion[2]-5 >0:
                cam_postion[2]-=5
                #print(cam_postion)
                
                main()

def main():
    global c
    # c.create_rectangle(0, 0, 310, 310, fill = 'white')
    ids = c.find_all()
    for id in ids:
        c.delete(id)
    change_dimension()
    draw()
main()

def moov():
    if cam_postion[0]<300 and cam_postion[0]>0:
        cam_postion[0]+=1
        
        main()
    a.after(1,moov)
    print("test")
        
# a.after(1000,moov)
a.bind("<KeyPress>",key_press)

a.mainloop()