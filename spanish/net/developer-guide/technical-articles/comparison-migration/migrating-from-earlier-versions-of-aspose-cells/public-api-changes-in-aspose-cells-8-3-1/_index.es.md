---
title: Público API Cambios en Aspose.Cells 8.3.1
type: docs
weight: 110
url: /es/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.3.0 a la 8.3.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **API añadidas**
### **Propiedad DataLabels.ShowCellRange agregado**
 La propiedad ShowCellRange se ha agregado a la clase DataLabels para imitar la funcionalidad de Excel de formatear las etiquetas de datos del gráfico en tiempo de ejecución. Tenga en cuenta que Excel proporciona esta función a través de los siguientes pasos.

1. Seleccione Etiquetas de datos de la serie y haga clic con el botón derecho para abrir el menú emergente.
1.  Haga clic en el**Formatear etiquetas de datos...** y se mostrará**Opciones de etiqueta**.
1.  Marque o desmarque la casilla de verificación**La etiqueta contiene: valor desde Cells**.

 El código de muestra a continuación accede a las etiquetas de datos de la serie de gráficos y luego establece el método DataLabels.ShowCellRange en verdadero para imitar la característica de Excel de**La etiqueta contiene: valor desde Cells**.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Mostrando el rango Cell como las etiquetas de datos](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) para más información.

{{% /alert %}} 

### **Métodos Cell.GetTable & ListObject.PutCellValue agregado**
Los métodos Cell.GetTable & ListObject.PutCellValue se agregaron con Aspose.Cells for .NET 8.3.1 para facilitar a los usuarios el acceso a ListObject desde una celda y agregar valores dentro de ella usando los desplazamientos de fila y columna. El siguiente código de ejemplo carga la hoja de cálculo de origen y agrega valores dentro de la tabla.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Acceder a la tabla desde Cell y agregar valores dentro de ella usando compensaciones de fila y columna](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) para más información.

{{% /alert %}} 

### **Propiedad OdsSaveOptions.IsStrictSchema11 Agregada**
La propiedad IsStrictSchema11 se agregó a la clase OdsSaveOptions para permitir que los desarrolladores guarden la hoja de cálculo en un formato que cumpla con la especificación ODF v1.2. El valor predeterminado de la propiedad IsStrictSchema11 es falso, lo que significa que a partir de la versión 8.3.1 de las API Aspose.Cells, los archivos ODS se guardarán en formato ODF versión 1.2 de forma predeterminada.

El fragmento de código proporcionado a continuación guarda el archivo ODS en formato ODF 1.2.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Guarde el archivo ODS en ODF 1.1 y 1.2 Especificaciones](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) para más información.

{{% /alert %}} 

### **Método SparklineCollection.Add Agregado**
 Aspose.Cells Las API han expuesto el método SparklineCollection.Add(string dataRange, int row, int column) para especificar el rango de datos y la ubicación del grupo Sparkline. Tenga en cuenta que Excel proporciona la misma característica a través de los siguientes pasos.

1. Seleccione la celda que contiene su minigráfico.
1.  Seleccione**Editar datos desde el minigráfico** sección dentro de la**Diseño** pestaña
1.  Elegir**Editar ubicación y datos del grupo**.
1. Especificar**Rango de datos** & **Ubicación**.

 El siguiente código de ejemplo carga la hoja de cálculo de origen, accede al primer grupo de minigráficos y agrega nuevos rangos de datos y ubicaciones para el grupo de minigráficos.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Copie Sparkline especificando el rango de datos y la ubicación del grupo Sparkline](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) para más información.

{{% /alert %}}
