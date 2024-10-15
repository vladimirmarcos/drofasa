from system.conexion.basedatos import convertintdata
def convertintegretdata(table,campo,data):
        """_summary_

        Args:
            table (_type_): _description_
            campo (_type_): _description_
            data (_type_): _description_

        Returns:
            _type_: _description_
        """        
        newdata=convertintdata(table,campo,data)[0]
        return newdata