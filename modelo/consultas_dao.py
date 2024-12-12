from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql= '''
        CREATE TABLE "Categorias" (
            "ID"	INTEGER,
            "Categoria"	TEXT,
            PRIMARY KEY("ID" AUTOINCREMENT)
        );
        
        CREATE TABLE "Sucursales" (
            "ID"	INTEGER,
            "Sucursal"	TEXT,
            PRIMARY KEY("ID" AUTOINCREMENT)
        );
        
        CREATE TABLE "Antiguedades" (
            "ID"	INTEGER,
            "Articulo"	TEXT,
            "Precio"	INTEGER,
            "Disponibilidad"	TEXT,
            "Ingreso"	TEXT,
            "CategoriaID"	INTEGER,
            "SucursalID"	INTEGER,
            PRIMARY KEY("ID" AUTOINCREMENT),
            FOREIGN KEY("CategoriaID") REFERENCES "Categorias"("ID"),
            FOREIGN KEY("SucursalID") REFERENCES "Sucursales"("ID")
        );

    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


class Antiguedades():

    def __init__(self,articulo, precio, disponibilidad, ingreso, categoriaID, sucursalID):
       self.articulo = articulo
       self.precio = precio
       self.disponibilidad = disponibilidad
       self.ingreso = ingreso
       self.categoriaID = categoriaID
       self.sucursalID = sucursalID
       
    def __str__(self):
        return f'Antiguedad[{self.articulo},{self.precio},{self.vendido},{self.ingreso},{self.categoriaID},{self.sucursalID}]'

def guardar_antiguedad(antiguedad):
    conn = Conneccion()

    sql= f'''
        INSERT INTO Antiguedades(Articulo, Precio, Disponibilidad, Ingreso, CategoriaID, SucursalID)
        VALUES('{antiguedad.articulo}',{antiguedad.precio},'{antiguedad.disponibilidad}','{antiguedad.ingreso}', {antiguedad.categoriaID},{antiguedad.sucursalID});
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def listar_antiguedades():
    conn = Conneccion()
    listar_antiguedades = []

    sql = '''
        SELECT A.ID, A.Articulo, A.Precio, A.Disponibilidad, A.Ingreso, C.Categoria, S.Sucursal
        FROM Antiguedades A
        LEFT JOIN Categorias C ON A.CategoriaID = C.ID
        LEFT JOIN Sucursales S ON A.SucursalID = S.ID;
    '''
    try:
        conn.cursor.execute(sql)
        listar_antiguedades = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_antiguedades
    except Exception as e:
        print(f"Error al listar antigüedades: {e}")
        conn.cerrar_con()
        return []


def listar_categorias():
    conn = Conneccion()
    listar_categorias = []

    sql = '''
        SELECT * FROM Categorias;
    '''
    try:
        conn.cursor.execute(sql)
        listar_categorias = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_categorias
    except:
        conn.cerrar_con()
        return []

def listar_sucursales():
    conn = Conneccion()
    listar_sucursales = []

    sql = '''
        SELECT * FROM Sucursales;
    '''
    try:
        conn.cursor.execute(sql)
        listar_sucursales = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_sucursales
    except:
        conn.cerrar_con()
        return []

def editar_antiguedad(antiguedad, id):
    conn = Conneccion()

    sql = f'''
    UPDATE Antiguedades
    SET Articulo = '{antiguedad.articulo}', 
        Precio = {antiguedad.precio}, 
        Disponibilidad = '{antiguedad.disponibilidad}', 
        Ingreso = '{antiguedad.ingreso}', 
        CategoriaID = {antiguedad.categoriaID}, 
        SucursalID = {antiguedad.sucursalID}
    WHERE ID = {id}
    ;
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def borrar_antiguedad(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM Antiguedades
        WHERE ID = {id}
        ;
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass