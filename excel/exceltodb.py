import pandas as pd
import sqlite3
def verificar_existencia(cursor,conn, table_name, column_name, valor):
    print (f" { valor}")
    print (f"valor {valor} su tipo {len(valor)}")
    query = f"SELECT id FROM {table_name} WHERE {column_name} = ?"
    cursor.execute(query, (valor,))
    return cursor.fetchone()[0]

def excel_to_sqlite(excel_file, db_file, table_name):
    
    df = pd.read_excel(excel_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    for index, row in df.iterrows():
        print (row)
        values=[row[0],row[1],verificar_existencia(cursor,conn,"iva","nombre",row[2]),verificar_existencia(cursor,conn,"siap","nombre", row[3]),row[4]]
        values = tuple(values)
        placeholders = ", ".join(["?" for _ in row])
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        
        cursor.execute(insert_query, values)

    
    conn.commit()
    conn.close()


excel_file = 'excel\conceptosdecompra.xlsx'  
db_file = 'drofasa.db'  
#'excel\cuentascontables.xlsx' 

excel_to_sqlite(excel_file, db_file, "conceptocompra")
