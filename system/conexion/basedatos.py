from system.conexion.conexion import ConexionDB

def searchalldata(table):
    """_summary_

    Args:
        table (_type_): _description_

    Returns:
        _type_: _description_
    """    
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT * FROM '+table)
    resultados = conexion.cursor.fetchall()
    conexion.cerrar()
    return resultados

def convertintdata(table,campo,data):
    """_summary_

    Returns:
        _type_: _description_
    """        
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT '+campo+' FROM ' +table+  ' WHERE id= ?', (data,))
    resultados = conexion.cursor.fetchone()
    conexion.cerrar()
    return resultados

def convertdataint(table,campo,data):
    """_summary_

    Returns:
        _type_: _description_
    """        
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT id FROM ' +table+  ' WHERE '+campo+' = ?', (data,))
    resultados = conexion.cursor.fetchone()
    conexion.cerrar()
    return resultados

def datavaluescombo(table):
    """_summary_

    Args:
        table (_type_): _description_

    Returns:
        _type_: _description_
    """    
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT nombre FROM ' +table )
    resultados = conexion.cursor.fetchall()
    conexion.cerrar()
    return resultados

def dataexist(table,data,campo):
    """_summary_

    Args:
        table (_type_): _description_
        data (_type_): _description_
        campo (_type_): _description_

    Returns:
        _type_: _description_
    """    
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT '+campo+ ' FROM ' +table+  ' WHERE '+campo+'= ?', (data,))
    resultados = conexion.cursor.fetchone()
    conexion.cerrar()
    return resultados

def savedata(message,data):
    """Insertar datos en la tabla."""
    conexion=ConexionDB()
    
    conexion.cursor.execute(message,data)
    conexion.cerrar()


   