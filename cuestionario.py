
from tkinter import *

#crear interface 
mywindow = Tk()
mywindow.geometry("500x600")
mywindow.title("Registros de pacientes.")
mywindow.resizable(False,False)
mywindow.config(background = "#C4FCFF")
main_title = Label(text = "Registro de Pacientes.", font = ("Arial Black", 18), bg = "#2DBEC6", fg = "white", width = "600", height = "1")
main_title.pack()

def enviar():
  usuario_info = usuario.get()
  especialidad_info = especialidad.get()
  medico_info = medico.get()
  prescripcion_info = prescripcion.get()

  print(usuario_info,"\t", especialidad_info,"\t", prescripcion_info,"\t",medico_info)
 
#Archivo
  archivo = open("paciente.txt", "a")
  archivo.write(usuario_info)
  archivo.write("\t")
  archivo.write(especialidad_info)
  archivo.write("\t")
  archivo.write(medico_info)
  archivo.write("\t")
  archivo.write(prescripcion_info)
  archivo.write("\t")
  archivo.close()
  print(" registro. usuario: {} | Nombre: {}   ".format(usuario_info, prescripcion_info))
 
#Eliminar datos
  usuario_entry.delete(0, END)
  especialidad_entry.delete(0, END)
  medico_entry.delete(0, END)
  prescripcion_entry.delete(0, END)

# Datos a ingresar del paciente
usuario_label = Label(text = "Nombres y Apellidos.", bg = "#C4FCFF", font = ("Arial", 14))
usuario_label.place(x = 22, y = 70)
especialidad_label = Label(text = "Especialidad Medica.", bg = "#C4FCFF", font = ("Arial", 14))
especialidad_label.place(x = 22, y = 130)
medico_label = Label(text = "Medico Asignado.", bg = "#C4FCFF", font = ("Arial", 14))
medico_label.place(x = 22, y = 190)
prescripcion_label = Label(text = "Tratamiento asignado.", bg = "#C4FCFF", font = ("Arial", 14))
prescripcion_label.place(x = 22, y = 250,)

 
usuario = StringVar()
especialidad = StringVar()
medico = StringVar()
prescripcion = StringVar()

 
usuario_entry = Entry(textvariable = usuario, width = "40")
especialidad_entry = Entry(textvariable = especialidad, width = "40")
medico_entry = Entry(textvariable = medico, width = "40")
prescripcion_entry = Entry(textvariable = prescripcion, width = "40")

 
usuario_entry.place(x = 22, y = 100, width =250, height =20)
especialidad_entry.place(x = 22, y = 160, width =250, height =20)
medico_entry.place(x = 22, y = 220, width =250, height =20)
prescripcion_entry.place(x = 22, y = 280, width =250, height =200)

#boton de enviar
submit_btn = Button(mywindow,text = "Registrar.", width = "30", height = "2", command = enviar, bg = "#0799A1", font = ("Arial Black", 9))
submit_btn.place(x = 22, y = 500)

mywindow.mainloop()
