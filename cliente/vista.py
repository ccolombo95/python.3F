import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from modelo.consultas_dao import Antiguedades, crear_tabla, listar_antiguedades, listar_categorias, listar_sucursales, guardar_antiguedad, editar_antiguedad, borrar_antiguedad

class Frame(tk.Frame):  
    def __init__(self, root=None):    
        super().__init__(root, width=680, height=900)    
        self.root = root
        self.id_antiguedad = None   
        self.pack()    

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.mostrar_tabla()
    
    def label_form(self):    
        self.label_articulo = tk.Label(self, text="Articulo: ")    
        self.label_articulo.config(font=('Arial', 12, 'bold'))    
        self.label_articulo.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_precio = tk.Label(self, text="Precio: ")    
        self.label_precio.config(font=('Arial', 12, 'bold'))    
        self.label_precio.grid(row=1, column=0, padx=10, pady=10) 
        
        self.label_disponibilidad = tk.Label(self, text="Disponibilidad: ")    
        self.label_disponibilidad.config(font=('Arial', 12, 'bold'))    
        self.label_disponibilidad.grid(row=2, column=0, padx=10, pady=10) 
        
        self.label_ingreso = tk.Label(self, text="Ingreso: ")    
        self.label_ingreso.config(font=('Arial', 12, 'bold'))    
        self.label_ingreso.grid(row=3, column=0, padx=10, pady=10)      
        
        self.label_categoria = tk.Label(self, text="Categoria: ")    
        self.label_categoria.config(font=('Arial', 12, 'bold'))    
        self.label_categoria.grid(row=4, column=0, padx=10, pady=10)
        
        self.label_sucursal = tk.Label(self, text="Sucursal: ")    
        self.label_sucursal.config(font=('Arial', 12, 'bold'))    
        self.label_sucursal.grid(row=5, column=0, padx=10, pady=10)
    
    def input_form(self):
        self.articulo = tk.StringVar()    
        self.entry_articulo = tk.Entry(self, textvariable=self.articulo)    
        self.entry_articulo.config(width=50)    
        self.entry_articulo.grid(row=0, column=1, padx=10, pady=10)    
        
        self.precio = tk.IntVar()
        self.entry_precio = tk.Entry(self, textvariable=self.precio)    
        self.entry_precio.config(width=50)    
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10)
    
        self.disponibilidad = tk.BooleanVar()
        self.entry_disponibilidad = tk.Checkbutton(self, variable=self.disponibilidad)    
        self.entry_disponibilidad.grid(row=2, column=1, padx=10, pady=10)
    
        self.ingreso = tk.StringVar()
        self.entry_ingreso = DateEntry(self, textvariable=self.ingreso, date_pattern='yyyy-mm-dd')    
        self.entry_ingreso.config(width=50)    
        self.entry_ingreso.grid(row=3, column=1, padx=10, pady=10) 
        
        categorias = listar_categorias() or []
        categorias_values = ['Seleccione Uno'] + [categoria[1] for categoria in categorias]
    
        self.entry_categoria = ttk.Combobox(self, state="readonly", values=categorias_values)
        self.entry_categoria.current(0)
        self.entry_categoria.config(width=25)    
        self.entry_categoria.grid(row=4, column=1, padx=10, pady=10)
        
        sucursales = listar_sucursales() or []
        sucursales_values = ['Seleccione Uno'] + [sucursal[1] for sucursal in sucursales]
    
        self.entry_sucursal = ttk.Combobox(self, state="readonly", values=sucursales_values)
        self.entry_sucursal.current(0)
        self.entry_sucursal.config(width=25)    
        self.entry_sucursal.grid(row=5, column=1, padx=10, pady=10)

    def botones_principales(self):    
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)    
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_alta.grid(row= 6, column=0,padx=10,pady=10)    
    
        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)    
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')    
        self.btn_modi.grid(row= 6, column=1,padx=10,pady=10)    
    
        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)    
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_cance.grid(row= 6, column=2,padx=10,pady=10)
    
    def guardar_campos(self):
        antiguedad = Antiguedades(
            self.articulo.get(),
            self.precio.get(),
            self.disponibilidad.get(),
            self.ingreso.get(),
            self.entry_categoria.current(),
            self.entry_sucursal.current()
        )
    
        if self.id_antiguedad is None:
            guardar_antiguedad(antiguedad)
        else:
            editar_antiguedad(antiguedad, int(self.id_antiguedad))
    
        self.bloquear_campos()
        self.mostrar_tabla()
    
    def habilitar_campos(self):    
        self.entry_articulo.config(state='normal')    
        self.entry_precio.config(state='normal')    
        self.entry_disponibilidad.config(state='normal')  
        self.entry_ingreso.config(state='normal')    
        self.entry_categoria.config(state='normal')    
        self.entry_sucursal.config(state='normal')    
        self.btn_modi.config(state='normal')    
        self.btn_cance.config(state='normal')    
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):    
        self.entry_articulo.config(state='disabled')    
        self.entry_precio.config(state='disabled')    
        self.entry_disponibilidad.config(state='disabled')  
        self.entry_ingreso.config(state='disabled')    
        self.entry_categoria.config(state='disabled')    
        self.entry_sucursal.config(state='disabled')   
        self.btn_modi.config(state='disabled')    
        self.btn_cance.config(state='disabled')    
        self.btn_alta.config(state='normal')
        self.articulo.set('')
        self.precio.set(0)
        self.disponibilidad.set(False)
        self.ingreso.set('')
        self.entry_categoria.current(0)
        self.entry_sucursal.current(0)
        self.id_antiguedad = None

    def mostrar_tabla(self):
        self.lista_a = listar_antiguedades() or []
        self.lista_a.reverse()
    
        self.tabla = ttk.Treeview(self, columns=('Articulo', 'Precio', 'Disponibilidad', 'Ingreso', 'Categoria', 'Sucursal'))
        self.tabla.grid(row=7, column=0, columnspan=4, sticky='nse')
    
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=7, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
    
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Articulo')
        self.tabla.heading('#2', text='Precio')
        self.tabla.heading('#3', text='Disponibilidad')
        self.tabla.heading('#4', text='Ingreso')
        self.tabla.heading('#5', text='Categoria')
        self.tabla.heading('#6', text='Sucursal')
    
        for a in self.lista_a:
            self.tabla.insert('', 0, text=a[0], values=(a[1], a[2], a[3], a[4], a[5], a[6]), tags=('data',))
    
        self.tabla.tag_configure('data', foreground='black')  # Configura el color del texto a negro
    
        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)    
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')    
        self.btn_editar.grid(row=8, column=0, padx=10, pady=10)    
        
        self.btn_delete = tk.Button(self, text='Eliminar', command=self.eliminar_registro)    
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')    
        self.btn_delete.grid(row=8, column=1, padx=10, pady=10)


    def editar_registro(self):
        try:
            self.id_antiguedad = self.tabla.item(self.tabla.selection())['text']

            self.articulo_antiguedad = self.tabla.item(self.tabla.selection())['values'][0]
            self.precio_antiguedad = self.tabla.item(self.tabla.selection())['values'][1]
            self.disponibilidad_antiguedad = self.tabla.item(self.tabla.selection())['values'][2]
            self.ingreso_antiguedad = self.tabla.item(self.tabla.selection())['values'][3]
            self.categoria_antiguedad = self.tabla.item(self.tabla.selection())['values'][4]
            self.sucursal_antiguedad = self.tabla.item(self.tabla.selection())['values'][5]

            self.habilitar_campos()
            self.articulo.set(self.articulo_antiguedad)
            self.precio.set(self.precio_antiguedad)
            self.disponibilidad.set(self.disponibilidad_antiguedad)
            self.ingreso.set(self.ingreso_antiguedad)
            self.entry_categoria.current(self.categorias.index(self.categoria_antiguedad))
            self.entry_sucursal.current(self.sucursales.index(self.sucursal_antiguedad))

        except:
            pass


    def eliminar_registro(self):
        self.id_antiguedad = self.tabla.item(self.tabla.selection())['text']

        borrar_antiguedad(int(self.id_antiguedad))

        self.mostrar_tabla()


def barrita_menu(root):  
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_inicio2 = tk.Menu(barra, tearoff=0)

    # niveles 
    # #principal
    barra.add_cascade(label='Inicio', menu = menu_inicio) 
    barra.add_cascade(label='Consultas', menu = menu_inicio)  
    barra.add_cascade(label='Acerca de..', menu = menu_inicio)  
    barra.add_cascade(label='Ayuda', menu= menu_inicio2)  
    
    #submenu 
    menu_inicio.add_command(label='Conectar DB', command= crear_tabla)  
    menu_inicio.add_command(label='Desconectar DB')  
    menu_inicio.add_command(label='Salir', command= root.destroy)

    #submenu ayuda
    menu_inicio2.add_command(label='Contactanos')  
    menu_inicio2.add_command(label='lalala')  
    menu_inicio2.add_command(label='ola komo stas')