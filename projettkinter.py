from tkinter import  *

class cassebrique: 
    # créer une première fenetre 
    window =Tk()
    # personaliser cette fenetre 
    window.title("Jeu Casse-Brique")
    window.geometry("480x360")
    window.config(background='black')

    bas_frame = Frame(window, bg=window.cget('bg'))
    bas_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

    #création d'une forme rectangle en bas de la fenetre 
    width = 300
    height = 20
    canvas=Canvas(bas_frame,width=width,height=height,background='black', highlightthickness=0)
    canvas.create_rectangle(120, 0, 180, 20, fill='blue', outline='')
    canvas.pack(side=LEFT, expand=True, anchor=CENTER)

    #creation d'image
    #width=300
    #height=300
    #image= PhotoImage(file="image1-TP4.jpg").zoom(35).subsample(32)
    #canvas=Canvas(window,width=width,height=height,bg='black')
    #canvas.create_image(width/2,height/2, image=image )
    #canvas.pack(side= BOTTOM)

    # ajouter un premier texte
    label_title = Label(window,text= "Score:    ",font=("Courrier",10), bg ='black',fg ='yellow')
    #permet d'afficher "Score:"
    label_title.pack(side= RIGHT,anchor="n" )
    #ajouter un premier boutton
    yt_button= Button(bas_frame,text="démarrer",font=("Courrier",10), bg ='red',fg ='white')
    yt_button.pack(side=RIGHT, anchor=SE)


    #ajouter un deuxième boutton
    yt_button= Button(bas_frame,text="quitter",font=("Courrier",10), bg ='red',fg ='white',command=window.destroy)
    yt_button.pack(side=RIGHT, anchor=SE)
    # afficher la fenetre 
    window.mainloop()





class raquette: 