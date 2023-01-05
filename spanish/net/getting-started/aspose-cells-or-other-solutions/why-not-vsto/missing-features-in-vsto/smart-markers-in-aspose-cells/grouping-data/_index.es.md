---
title: Agrupación de datos
type: docs
weight: 10
url: /es/net/grouping-data/
---
En algunos informes de Excel, es posible que deba dividir los datos en grupos para facilitar la lectura y el análisis. Uno de los principales propósitos de dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes Aspose.Cells le permiten agrupar sus datos por campo(s) y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si agrupa datos por Customers.CustomerID, puede agregar un registro de resumen cada vez que cambie el grupo.

Los fragmentos de código de ejemplo que siguen muestran cómo agrupar datos en un informe de Excel usando marcadores inteligentes.
## **Parámetros**
Los siguientes son algunos de los parámetros de marcadores inteligentes utilizados para agrupar datos.
**grupo:normal/fusionar/repetir**

Admitimos tres tipos de grupos entre los que puede elegir.

- normal: el valor de grupo por campo(s) no se repite para los registros correspondientes en la columna; en su lugar, se imprimen una vez por grupo de datos.
- fusionar: el mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en el grupo por campo(s) para cada conjunto de grupos.
- repetir: el valor de grupo por campo(s) se repite para los registros correspondientes.

Si tiene varios parámetros, sepárelos con comas, pero sin espacios: parámetroA, parámetroB, parámetroC
### **Ejemplo**
Este ejemplo muestra algunos de los parámetros de agrupación en acción. Utiliza la base de datos de acceso Northwind.mdb Microsoft y extrae datos de la tabla denominada "Detalles del pedido". Creamos un archivo de diseñador llamado SmartMarker_Designer.xls en Microsoft Excel y colocamos marcadores inteligentes en varias celdas de las hojas de trabajo. Los marcadores se procesan para llenar las hojas de trabajo. Los datos se colocan y organizan por un campo de grupo.

El archivo del diseñador tiene dos hojas de trabajo. En el primero, colocamos marcadores inteligentes con parámetros de agrupación como se muestra en la captura de pantalla a continuación. Se colocan tres marcadores inteligentes (con parámetros de agrupación):
&=Detalles del pedido.ID del pedido(grupo:combinar,saltar:1),
&=Detalles del pedido.Cantidad(subtotal9:Detalles del pedido.ID del pedido), y
&=Detalles del pedido.Precio unitario(subtotal9:Detalles del pedido.ID del pedido) vaya a A5, B5 y C5 respectivamente.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Grouping Data OLE DB.xlsx";

//Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=~\\..\\..\\..\\Data\\Northwind.mdb");

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

wd.Workbook = new Workbook(FileName);

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save(FileName);

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
