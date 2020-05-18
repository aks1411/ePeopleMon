from tkinter import *
import webbrowser
root = Tk(className="Oncor e-People")
can=Canvas(root,width=1000,height=1000)
can.pack()
ePeople=StringVar()
fileData = StringVar()
dB=StringVar()

    
def ePeople():
    print("Inside function ePeople")
    f = open( 'fileData.txt', 'w' )
    f.write( fileData.get())
    f.close()
    fdB = open( 'dBdata.txt', 'w' )
    fdB.write( dB.get())
    fdB.close()
    f=open('fileData.txt', 'r' )
    fileDataValues=f.readlines();
    f.close();
    fdB = open( 'dBdata.txt', 'r' )
    dBValues=fdB.readlines()
    fdB.close()
    htmlcontent="<!DOCTYPE html><html><head><style>table {border: 1px solid black;border-collapse: collapse;font-family:\"Trebuchet MS\";}"
    htmlcontent=htmlcontent+"th {background-color:#4298f4;border: 1px solid black;border-collapse: collapse; padding:3px 7px 3px 7px;}"
    htmlcontent=htmlcontent+"td {border: 1px solid black;border-collapse: collapse;padding:3px 7px 3px 7px;}</style></head><body>"
    htmlcontent=htmlcontent+"<p>Hi All,</p><p>PFB E-people Reconciliation for today.</p>"
    htmlcontent=htmlcontent+"<table><tr><th width=\"10\" colspan=\"2\">Work Centre</th><th width=\"10\">File Count</th><th width=\"10\">DB Count</th></tr>"
    ePeopleConsolidation=""
    for i,data in enumerate(fileDataValues):
        workcentre=data.split(":")[0]
        for j,dbData in enumerate(dBValues):
            if (workcentre in dbData):
                ePeopleConsolidation=ePeopleConsolidation+dbData.split(":")[0]+"|"+dbData.split(":")[1]+"|"+data.split(":")[1].rstrip()+"|"+dbData.split(":")[2].rstrip()+"\n"
                htmlcontent=htmlcontent+"<tr><td>"+dbData.split(":")[0]+"</td><td>"+dbData.split(":")[1]+"</td><td>"+data.split(":")[1]+"</td><td>"+dbData.split(":")[2]+"</td></tr>"
                
    htmlcontent=htmlcontent+"</table></body></html>"
    print (htmlcontent)
    
    ePeopleResult.insert(END,ePeopleConsolidation)
    
    f = open('ePeople.html','w')
    f.write(htmlcontent)
    f.close
    
    webbrowser.open_new_tab('ePeople.html')

tkfile=Label(can,text="Enter File Data",anchor="w")
tkfile.grid(row=0)
tkfilevalue=Entry(can,textvariable=fileData,width=100)
tkfilevalue.grid(row=0,column=2)

tkdB=Label(can,text="Enter DB Data",anchor="w")
tkdB.grid(row=1)
tkdBvalue=Entry(can,textvariable=dB,width=100)
tkdBvalue.grid(row=1,column=2)


genResultButton=Button(can,text="Generate Result",width=10,command=ePeople)
genResultButton.grid(row=3,column=2)

ePeopleResult=Text(can,width=120,height=10)
ePeopleResult.grid(row=4,column=2)

Button(can, text='Quit', command=root.destroy).grid(row=4, column=3, sticky=W, pady=4)

root.mainloop()


