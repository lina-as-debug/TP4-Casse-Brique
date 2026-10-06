from tkinter import  *
# créer une première fenetre 
window =Tk()
# personaliser cette fenetre 
window.title("Jeu Casse-Brique")
window.geometry("480x360")
window.config(background='black')

#creation d'image
width=300
height=300
image= PhotoImage(file="image1-TP4.jpg").zoom(35).subsample(32)
canvas=Canvas(window,width=width,height=height,bg='black')
canvas.create_image(width/2,height/2, image=image )
canvas.pack(side= BOTTOM)

# ajouter un premier texte
label_title = Label(window,text= "Score:    ",font=("Courrier",10), bg ='black',fg ='yellow')
#permet d'afficher "Score:"
label_title.pack(side= RIGHT,anchor="n" )
#ajouter un premier boutton
yt_button= Button(window,text="démarrer",font=("Courrier",10), bg ='red',fg ='white')
yt_button.pack(side=BOTTOM)


#ajouter un deuxième boutton
yt_button= Button(window,text="quitter",font=("Courrier",10), bg ='red',fg ='white',command=window.destroy)
yt_button.pack(side=BOTTOM)
# afficher la fenetre 
window.mainloop()