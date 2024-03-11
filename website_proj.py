from browser import document, html

editor_elt = document['left']
editor_elt.attrs['style'] = "width:75%;"
console_elt = document['right']
console_elt.attrs['style'] = "width: 25%;"

def page_inc(ev):
    global last
    global page 
    page += 1 
    print("Redraw page", page)
    redraw()
    if page>last:
        last=page

def page_dec(ev):
    global page
    page -= 1
    if page < 0:
        page = 0
    print("Redraw page", page) 
    redraw()
    
def page_fir(ev):
    global page
    page = page*0
    print("Redraw page", page)
    redraw()
    
def page_las(ev):
    global last
    global page
    page = last
    print("Redraw page", page)
    redraw()

last = 0
page = 0
button = html.BUTTON("Next")
button.bind("click", page_inc)
buttonp = html.BUTTON("Prev")
buttonp.bind("click", page_dec)

buttonf = html.BUTTON("First")
buttonf.bind("click", page_fir)

buttonl = html.BUTTON("Last")
buttonl.bind("click", page_las)





def redraw():
    main_elt = html.DIV(style="border: solid; width: 80%;")
    main_elt <= buttonp
    main_elt <= button
    main_elt <= buttonf
    main_elt <= buttonl
    main_elt <= html.H1(f"Hello! This is page {page+1}")
    main_elt <= html.UL([html.LI(f"item {page*3 + 1 + i}") for i in range(3)])

    document['main_container'].clear()
    document['main_container'] <= main_elt

document['main_container'].clear()
document['main_container'] <= buttonp
document['main_container'] <= button
document['main_container'] <= buttonf
document['main_container'] <= buttonl

redraw()
