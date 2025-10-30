---
title: Cómo agrupar datos en Smart Markers
type: docs
weight: 30
url: /es/net/how-to-group-data-in-smart-markers/
---

## **Escenarios de uso posibles**
En algunos informes de Excel es posible que necesite dividir los datos en grupos para que sea más fácil de leer y analizar. Uno de los propósitos principales para dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes de Aspose.Cells le permiten agrupar los datos por campos y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si está agrupando datos por Cliente.IDCliente, puede agregar un registro de resumen cada vez que cambie el grupo.

## **Parámetros de agrupamiento de datos en Smart Markers**
A continuación se muestran algunos de los parámetros de marcadores inteligentes utilizados para agrupar datos.
### **group:normal/merge/repeat**
Soportamos tres tipos de grupos entre los que puede elegir.

- **normal** - El valor del campo o campos de agrupación no se repite para los registros correspondientes en la columna; en su lugar se imprimen una vez por grupo de datos.
- **merge** - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en los campos de agrupación para cada conjunto de grupos.
- **repeat** - El valor del campo o campos de agrupación se repite para los registros correspondientes.

Por ejemplo: &=Clientes.IDCliente(grupo:merge)
### **skip**
Salta un número especificado de filas después de cada grupo.

Por ejemplo, &=Empleados.IDEmpleado(grupo:normal,saltar:1)
### **subtotalN**
Realiza una operación de resumen para un campo de datos especificado relacionado con un campo de agrupación. La N representa números del 1 al 11 que especifican la función utilizada al calcular los subtotales dentro de una lista de datos. (1=PROMEDIO, 2=CONTAR, 3=CONTARA, 4=MÁXIMO, 5=MÍNIMO,...9=SUMA, etc.) Consulta la referencia de subtotales en la ayuda de Microsoft Excel para más detalles.

El formato realmente se declara como:
subtotalN:Ref donde Ref se refiere a la columna de agrupación.

Por ejemplo,

- &=Productos.Unidades(subtotal9:Productos.IDProducto) especifica la función de resumen sobre el campo **Unidades** con respecto al campo **IDProducto** en la tabla **Productos**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) especifica la función de resumen sobre el campo **Col3** agrupado por **Col1** en la tabla **Tabx**.
- &=Tabla1.ColumnaD(subtotal9:Tabla1.ColumnaA&Tabla1.ColumnaB) especifica la función de resumen sobre el campo **ColumnaD** agrupado por **ColumnaA** y **ColumnaB** en la tabla **Tabla1**.

## **Cómo agrupar datos en Smart Markers**

Este ejemplo muestra algunos de los parámetros de agrupación en acción. Utiliza la base de datos de Microsoft Access Northwind.mdb y extrae datos de la tabla llamada "Detalles del Pedido". Creamos un archivo de diseño llamado SmartMarker_Designer.xls en Microsoft Excel y colocamos marcadores inteligentes en varias celdas de las hojas de cálculo. Los marcadores se procesan para llenar las hojas de cálculo. Los datos se colocan y organizan por un campo de grupo.

El archivo de diseño tiene dos hojas de cálculo. En la primera colocamos marcadores inteligentes con parámetros de agrupación como se muestra en la captura de pantalla a continuación. Se colocan tres marcadores inteligentes (con parámetros de agrupación):
&=[Order Details].OrderID(group:merge,skip:1),
&=[Detalles del pedido].Cantidad(subtotal9:Detalles del pedido.IDPedido), y
&=[Detalles del pedido].PrecioUnitario(subtotal9:Detalles del pedido.IDPedido) se van a A5, B5 y C5 respectivamente.

|**La primera hoja de trabajo en el archivo SmartMarker_Designer.xls, completa con marcadores inteligentes**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
En la segunda hoja de trabajo del archivo de diseñador, colocamos algunos marcadores inteligentes más como se muestra en la figura a continuación. Colocamos los siguientes marcadores inteligentes:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), y
&=subtotal9:Detalles del pedido.IDPedido en A5, B5, C5, D5 y C6 respectivamente.

|**La segunda hoja de trabajo del archivo SmartMarker_Designer.xls, mostrando marcadores inteligentes mixtos.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Aquí está el código fuente usado en el ejemplo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Si necesita agregar sus propias etiquetas personalizadas a las filas de resumen o si desea concatenar el nombre del campo con una etiqueta, por ejemplo, "Subtotal de pedidos", Aspose.Cells le proporciona atributos de Etiqueta y PosiciónEtiqueta, para que pueda colocar sus etiquetas personalizadas en los Marcadores Inteligentes mientras se concatenan con las filas de Subtotal en datos de agrupación. Consulte el documento sobre Cómo agregar etiquetas personalizadas para concatenar con las filas de subtotal en los Marcadores Inteligentes como referencia.

{{% /alert %}} 
