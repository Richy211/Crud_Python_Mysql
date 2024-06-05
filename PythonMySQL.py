import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from Clientes import *
from Conexion import *

class formularioClientes:
    
    def __init__(self):
        self.base = None
        self.textBoxId = None
        self.textBoxNombres = None 
        self.textBoxApellidos = None 
        self.combo = None
        self.groupBox = None 
        self.tree = None 
        self.Formulario()
        
    def guardarRegistros(self):
        try:
            # Verifica la inicializacion de los widget
            if self.textBoxNombres is None or self.textBoxApellidos is None or self.combo is None: 
                print("Los widget no estan inicializados")
                return 
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()
            sexo = self.combo.get() 
            
            CClientes.ingresarClientes(nombres, apellidos, sexo) 
            messagebox.showinfo("Informacion", "Los datos han sido guardados")
            
            self.actualizarTreeView()  # Llamar a la función de instancia
            
            # Limpiar los campos
            self.textBoxNombres.delete(0, END)
            self.textBoxApellidos.delete(0, END)
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))
        
    def Formulario(self):  
        try:
            self.base = Tk()
            self.base.geometry("1200x300")
            self.base.title("Formulario Python")
            
            self.groupBox = LabelFrame(self.base, text="Datos del Personal", padx=5, pady=5)
            self.groupBox.grid(row=0, column=0, padx=10, pady=10)
            
            labelId = Label(self.groupBox, text="Id:", width=13, font=("arial", 12)).grid(row=0, column=0)
            self.textBoxId = Entry(self.groupBox)
            self.textBoxId.grid(row=0, column=1)
            
            labelNombre = Label(self.groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
            self.textBoxNombres = Entry(self.groupBox)
            self.textBoxNombres.grid(row=1, column=1)
            
            labelApellido = Label(self.groupBox, text="Apellido:", width=13, font=("arial", 12)).grid(row=2, column=0)
            self.textBoxApellidos = Entry(self.groupBox)
            self.textBoxApellidos.grid(row=2, column=1)
            
            labelSexo = Label(self.groupBox, text="Sexo:", width=13, font=("arial", 12)).grid(row=3, column=0)
            seleccionSexo = tk.StringVar()
            self.combo = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            self.combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")
            
            Button(self.groupBox, text="Guardar", width=10, command=self.guardarRegistros).grid(row=4, column=0)
            Button(self.groupBox, text="Modificar", width=10,command=self.modificarRegistros).grid(row=4, column=1)
            Button(self.groupBox, text="Eliminar", width=10).grid(row=4, column=2)
            
            self.groupBox = LabelFrame(self.base, text="Lista del Personal", padx=5, pady=5)
            self.groupBox.grid(row=0, column=1, padx=5, pady=5)
            # Create a TreeView 
            
            # Configure the columns
            
            self.tree = ttk.Treeview(self.groupBox, columns=("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
            self.tree.column("# 1", anchor=CENTER)
            self.tree.heading("# 1", text="ID")
            self.tree.column("# 2", anchor=CENTER)
            self.tree.heading("# 2", text="Nombres")
            self.tree.column("# 3", anchor=CENTER)
            self.tree.heading("# 3", text="Apellidos")
            self.tree.column("# 4", anchor=CENTER)
            self.tree.heading("# 4", text="Sexo")
            
            #Agregar los datos a la tabla
            #Mostrar la tabla
            
            for row in CClientes.mostrarClientes():
                self.tree.insert("", "end", values=row)
                
            #Ejecutar la funcion de hacer click y mostrar el resultado en los Entry
            
            self.tree.bind("<<TreeviewSelect>>",self.seleccionarRegistro)
                
            self.tree.pack()
            
            self.base.mainloop()
        
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))
            
    def actualizarTreeView(self):
        try:
            # Borrar todos los elementos actuales del TreeView 
            self.tree.delete(*self.tree.get_children())
            
            # Obtener los nuevos datos que deseamos mostrar
            datos = CClientes.mostrarClientes()
            
            # Insertar los nuevos datos en el Treeview 
            for row in datos:
                self.tree.insert("", "end", values=row)
                
        except ValueError as error:
            print("Error al actualizar tabla {}".format(error))
            
    def seleccionarRegistro(self, event):
        try:
            #Obtener el Id de los registros
            itemSeleccionado = self.tree.focus()
            if itemSeleccionado:
                #Obtener los valores por columna
                values = self.tree.item(itemSeleccionado)['values']
                
                #Establecer los valores en los widget Entry 
                
                self.textBoxId.delete(0,END)
                self.textBoxId.insert(0,values[0])
                self.textBoxNombres.delete(0,END)
                self.textBoxNombres.insert(0,values[1])
                self.textBoxApellidos.delete(0,END)
                self.textBoxApellidos.insert(0,values[2])
                self.combo.set(values[3])
                
        except ValueError as error:
            print("Error al seleccionar registro {}".format(error))
            
    def modificarRegistros(self):
        
        #global textBoxtextBoxNombres,textBoxApellidos,combo,groupBox 
        
        try:
            # Verifica la inicializacion de los widget
            if self.textBoxId is None or self.textBoxNombres is None or self.textBoxApellidos is None or self.combo is None: 
                print("Los widget no estan inicializados")
                return 
            
            idUsuario= self.textBoxId.get()
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()
            sexo = self.combo.get() 
            
            CClientes.modificarClientes(idUsuario,nombres, apellidos, sexo) 
            messagebox.showinfo("Informacion", "Los datos fueron actualizados")
            
            self.actualizarTreeView()  # Llamar a la función de instancia
            
            # Limpiar los campos
            self.textBoxId.delete(0,END)
            self.textBoxNombres.delete(0, END)
            self.textBoxApellidos.delete(0, END)
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))
                
            
formularioClientes()
