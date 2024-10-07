from system.conexion.conexion import ConexionDB

def searchalldata(table):
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
    
    