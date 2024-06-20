---
title: Agrupar Datos en Aspose.Cells
type: docs
weight: 10
url: /es/net/grouping-data-in-aspose-cells/
---

En algunos informes de Excel es posible que necesite dividir los datos en grupos para que sea más fácil de leer y analizar. Uno de los propósitos principales para dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes de Aspose.Cells le permiten agrupar sus datos por campo(s) y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si agrupa datos por Clientes.CustomerID, puede agregar un registro de resumen cada vez que cambie el grupo.

Los fragmentos de código de ejemplo que siguen muestran cómo agrupar datos en un informe de Excel utilizando marcadores inteligentes.
## **Parámetros**
A continuación se muestran algunos de los parámetros de marcadores inteligentes utilizados para agrupar datos.
**group:normal/merge/repeat**

Soportamos tres tipos de grupos entre los que puede elegir.

- normal - El valor del campo(s) de agrupación no se repite para los registros correspondientes en la columna; en su lugar, se imprimen una vez por grupo de datos.
- merge - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en el campo(s) de agrupación para cada conjunto de grupo.
- repeat - El valor del campo(s) de agrupación se repite para los registros correspondientes.

Si tiene múltiples parámetros, sepárelos con comas, pero sin espacio: parámetroA,parámetroB,parámetroC
### **Ejemplo**
Este ejemplo muestra algunos de los parámetros de agrupación en acción. Utiliza la base de datos de Microsoft Access Northwind.mdb y extrae datos de la tabla llamada "Detalles del Pedido". Creamos un archivo de diseño llamado SmartMarker_Designer.xls en Microsoft Excel y colocamos marcadores inteligentes en varias celdas de las hojas de cálculo. Los marcadores se procesan para llenar las hojas de cálculo. Los datos se colocan y organizan por un campo de grupo.

El archivo de diseño tiene dos hojas de cálculo. En la primera colocamos marcadores inteligentes con parámetros de agrupación como se muestra en la captura de pantalla a continuación. Se colocan tres marcadores inteligentes (con parámetros de agrupación):
&=Order Details.OrderID(group:merge,skip:1),
&=Detalles del Pedido.Cantidad(subtotal9:Detalles del Pedido.OrderID), y
&=Detalles del Pedido.PrecioUnitario(subtotal9:Detalles del Pedido.OrderID) van en A5, B5 y C5 respectivamente.

{{< highlight csharp >}}

 //Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

//Open the connection object.

con.Open();

//Create a command object and specify the SQL query.

OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

//Create a data adapter object.

OleDbDataAdapter da = new OleDbDataAdapter();

//Specify the command.

da.SelectCommand = cmd;

//Create a dataset object.

DataSet ds = new DataSet();

//Fill the dataset with the table records.

da.Fill(ds, "Order Details");

//Create a datatable with respect to dataset table.

DataTable dt = ds.Tables["Order Details"];

//Create WorkbookDesigner object.

WorkbookDesigner wd = new WorkbookDesigner();

//Open the template file (which contains smart markers).

wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save("outSmartMarker_Designer.xls");

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
