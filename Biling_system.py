from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


root=Tk()
root.geometry("1100x600");
root.title("BILLING SYSTEM")
root.resizable(False,False)

def Reset():
    
    #Id.delete(0,END)
    #name.delete(0,END)
    e_cb.delete(0,END)
    e_mutb.delete(0,END)
    e_vb.delete(0,END)
    e_pa.delete(0,END)
    e_ch.delete(0,END)
    e_veg.delete(0,END)
    e_th.delete(0,END)
    e_co.delete(0,END)



def Total():
    b=Id.get()
    
    b1=name.get()
    
    try:a1=int(chickenbiryani.get())
    except:a1=0
    try:a2=int(muttonbiryani.get())
    except:a2=0
    try:a3=int(vegbiryani.get())
    except:a3=0
    try:a4=int(parata.get())
    except:a4=0
    try:a5=int(chicken65.get())
    except:a5=0
    try:a6=int(vegmanchuria.get())
    except:a6=0
    try:a7=int(thumsup.get())
    except:a7=0
    try:a8=int(coca_cola.get())
    except:a8=0
    
    #define cost of each item per quantity
    c1=250*a1 
    c2=340*a2 
    c3=160*a3 
    c4=20*a4
    c5=90*a5
    c6=65*a6
    c7=20*a7
    c8=20*a8
    
    labeltotal=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg='black')
    labeltotal.place(x=0,y=50)

    Total_bill=StringVar()
    
    entrytotal=Entry(f2,font=("aria",20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='lightgreen')
    entrytotal.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="Rs.",str('%.2f'%totalcost)
    Total_bill.set(string_bill)

    #print(totalcost)
    
    """ALTERNATE WAY TO STORE DATA IN TEXT FILE
    file=open("user.txt","w")
    file.write("id:"+str(b))
    file.write(str(b1))
    file.close()"""

def Insert():
      #for inserting into database convert int to str and use those names to insert in db
      Id1=str(Id.get());
      name1=str(name.get());
      chickenbiryani1=str(chickenbiryani.get());
      muttonbiryani1=str(muttonbiryani.get());
      vegbiryani1=str(vegbiryani.get());
      parata1=str(parata.get());
      chicken651=str(chicken65.get());
      vegmanchuria1=str(vegmanchuria.get());
      thumsup1=str(thumsup.get());
      coca_cola1=str(coca_cola.get());
      #for total calculation convert original str to int and insert the total in the db
      a1=int(chickenbiryani.get())
      a2=int(muttonbiryani.get())
      a3=int(vegbiryani.get())
      a4=int(parata.get())
      a5=int(chicken65.get())
      a6=int(vegmanchuria.get())
      a7=int(thumsup.get())
      a8=int(coca_cola.get())

      c1=250*a1 
      c2=340*a2 
      c3=160*a3 
      c4=20*a4
      c5=90*a5
      c6=65*a6
      c7=20*a7
      c8=20*a8
    
      totalcost=c1+c2+c3+c4+c5+c6+c7+c8
      total=str(totalcost) 

      if(Id1=="" or name1=="" or chickenbiryani1=="" or muttonbiryani1=="" or vegbiryani1=="" or parata1=="" or chicken651=="" or vegmanchuria1=="" or thumsup1=="" or coca_cola1=="" or total==""):
          MessageBox.showinfo("Insert status","All Fields are required")
      else:
          con=mysql.connect(host="localhost",user="root",password="",database="pythontkinter")
          cursor=con.cursor();
          cursor.execute("Insert into billingsystem values('"+ Id1 +"','"+ name1 +"','"+ chickenbiryani1 +"','"+ muttonbiryani1 +"','"+ vegbiryani1 +"','"+ parata1 +"','"+ chicken651 +"','"+ vegmanchuria1 +"','"+ thumsup1 +"','"+ coca_cola1 +"','"+ total +"')")
          cursor.execute("commit");


          MessageBox.showinfo("Insert status","Inserted successfully");
          con.close();



 #here begins         

Label(text="BILL MANAGEMENT",bg="blue",font=("calibri",33),width="300",height="2").pack()

#menu card
f=Frame(root,bg='yellow',highlightbackground='black',highlightthickness=1,width=350,height=450)
f.place(x=10,y=118)
Label(f,text="Menu",font=("Gabriola",40,"bold"),bg="yellow").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="CHICKENBIRYANI.....Rs.250/full",bg="yellow").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="MUTTONBIRYANI.....Rs.340/full",bg="yellow").place(x=10,y=100)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="VEGBIRYANI.....Rs.160/full",bg="yellow").place(x=10,y=120)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="PAROTA....Rs.20/per each",bg="yellow").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="CHICKEN65....Rs.90",bg="yellow").place(x=10,y=160)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="VEGMACHURIA....Rs.65",bg="yellow").place(x=10,y=180)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="THUMSUP....Rs.20/per each",bg="yellow").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",8,'bold'),text="coca-cola....Rs.20/per each",bg="yellow").place(x=10,y=220)
Label(f,font=("Lucida Calligraphy",10,'bold'),text="fill empty boxs with zero",bg="pink").place(x=10,y=240)
Label(f,font=("Lucida Calligraphy",10,'bold'),text="Enter only the Quantity",bg="pink").place(x=10,y=260)


#bill
f2=Frame(root,bg='lightgrey',highlightbackground='black',highlightthickness=1,width=350,height=450)
f2.place(x=690,y=118)

bill=Label(f2,text="Bill",font=("calibri",20),bg="lightgrey")
bill.place(x=120,y=10)




#entry work
f1=Frame(root,bg='lightgrey',highlightbackground='black',highlightthickness=1,width=350,height=450)
f1.place(x=380,y=118)


#declare variables and use in entry
Id=StringVar()
name=StringVar()
chickenbiryani=StringVar()
muttonbiryani=StringVar()
vegbiryani=StringVar()
parata=StringVar()
chicken65=StringVar()
vegmanchuria=StringVar()
thumsup=StringVar()
coca_cola=StringVar()

#label
lid=Label(f1,font=("aria",15,'bold'),text='ENTER ID',width=12,)
lid.grid(row=1,column=0)
lname=Label(f1,font=("aria",15,'bold'),text='ENTER NAME',width=12,)
lname.grid(row=2,column=0)
lchickenbiryani=Label(f1,font=("aria",15,'bold'),text='chicken biryani',width=12,)
lchickenbiryani.grid(row=3,column=0)
lmuttonbiryani=Label(f1,font=("aria",15,'bold'),text='mutton biryani',width=12,)
lmuttonbiryani.grid(row=4,column=0)
lvegtablebiryani=Label(f1,font=("aria",15,'bold'),text=' veg biryani',width=12,)
lvegtablebiryani.grid(row=5,column=0)
lparata=Label(f1,font=("aria",15,'bold'),text='parata',width=12,)
lparata.grid(row=6,column=0)
lchicken65=Label(f1,font=("aria",15,'bold'),text='chicken65',width=12,)
lchicken65.grid(row=7,column=0)
lvegmanchuria=Label(f1,font=("aria",15,'bold'),text='vegmanchuria',width=12,)
lvegmanchuria.grid(row=8,column=0)
lthumsup=Label(f1,font=("aria",15,'bold'),text=' Thumsup',width=12,)
lthumsup.grid(row=9,column=0)
lcoca_cola=Label(f1,font=("aria",15,'bold'),text='coca-cola',width=12,)
lcoca_cola.grid(row=10,column=0)




#entry
e_id=Entry(f1,font=("aria",15,'bold'),textvariable=Id,bd=6,width=12,bg="lightblue")
e_id.grid(row=1,column=1)
e_name=Entry(f1,font=("aria",15,'bold'),textvariable=name,bd=6,width=12,bg="lightblue")
e_name.grid(row=2,column=1)
e_cb=Entry(f1,font=("aria",15,'bold'),textvariable=chickenbiryani,bd=6,width=12,bg="lightblue")
e_cb.grid(row=3,column=1)
e_mutb=Entry(f1,font=("aria",15,'bold'),textvariable=muttonbiryani,bd=6,width=12,bg="lightblue")
e_mutb.grid(row=4,column=1)
e_vb=Entry(f1,font=("aria",15,'bold'),textvariable=vegbiryani,bd=6,width=12,bg="lightblue")
e_vb.grid(row=5,column=1)
e_pa=Entry(f1,font=("aria",15,'bold'),textvariable=parata,bd=6,width=12,bg="lightblue")
e_pa.grid(row=6,column=1)
e_ch=Entry(f1,font=("aria",15,'bold'),textvariable=chicken65,bd=6,width=12,bg="lightblue")
e_ch.grid(row=7,column=1)
e_veg=Entry(f1,font=("aria",15,'bold'),textvariable=vegmanchuria,bd=6,width=12,bg="lightblue")
e_veg.grid(row=8,column=1)
e_th=Entry(f1,font=("aria",15,'bold'),textvariable=thumsup,bd=6,width=12,bg="lightblue")
e_th.grid(row=9,column=1)
e_co=Entry(f1,font=("aria",15,'bold'),textvariable=coca_cola,bd=6,width=12,bg="lightblue")
e_co.grid(row=10,column=1)



#buttons
btn_reset=Button(f1,bd=5,bg="lightgreen",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=11,column=0)


btn_total=Button(f1,bd=5,bg="lightgreen",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=11,column=1)

insert=Button(f1,bd=5,bg="lightgreen",font=("ariel",16,'bold'),width=10,text="Insert",command=Insert)
insert.grid(row=12,column=1)

root.mainloop()
