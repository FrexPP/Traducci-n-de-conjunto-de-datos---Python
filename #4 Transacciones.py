# Importando el archivo .csv llamado "products" y convirtiendo a DataFrame
transacciones_df = pd.read_csv('transactions.csv')

# Eliminando la columna "campaign_id"

# Debido a que no se utilizará la tabla "campaigns", elimino la columna que la conecta.
transacciones_df.drop('campaign_id', axis = 1, inplace = True)

# Examinando el nombre de las columnas y información básica
transacciones_df.info()

# Traduciendo el nombre de las columnas
transacciones_df.rename(columns = {
    'transaction_id' : 'Transacción ID',
    'timestamp' : 'Marca de Tiempo',
    'customer_id' : 'Cliente ID',
    'product_id' : 'Producto ID',
    'quantity' : 'Cantidad',
    'discount_applied' : 'Descuento Aplicado',
    'gross_revenue' : 'Ingresos Brutos',
    'refund_flag' : 'Reembolso'
}, inplace = True)

# Creando un diccionario ampliable con los valores de las columnas a traducir

# Si bien este método de crear un diccionario e iterarlo para traducir los valores no es
# necesario debido a que hay una sola columna a traducir, lo utilizo igual para poder 
# ampliarlo en caso de que haya más columnas o valores posteriormente.
# Los valores binarios de la columna "Reembolso" también los traduje pansando en el consumo humano. 
t_traduccion = {
    'Reembolso' : {
        0 : 'No Realizado',
        1 : 'Realizado'
    }
}

# Iterando el diccionario para asignarle los valores a la columna "Reembolso"
for col, dic in t_traduccion.items():
    transacciones_df[col].replace(dic, inplace = True)

# Examinando porcentaje de valores nulos por columna
(transacciones_df.isna().mean() * 100)
# Algo interesante es que "Producto ID" y "Ingresos Brutos" comparten valores nulos en las mismas filas,
# un 10.13% del total de estas. Como esto puede significar un problema con el sistema que registra la 
# informacion de la transacción, decidí dejarlo para poder notificar el problema con los datos y filtrarlo después 
# en Power Query para análisis de ventas.

# Convirtiendo el DataFrame a un nuevo archivo .csv traducido
transacciones_df.to_csv('Transacciones.csv')
