---
title: Cambios en la API pública en Aspose.Cells 8.3.1
type: docs
weight: 110
url: /es/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.3.0 a la 8.3.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **APIs Añadidas**
### **Se ha añadido la propiedad ShowCellRange a DataLabels.**
Se ha agregado la propiedad ShowCellRange a la clase DataLabels para imitar la funcionalidad de formato de las etiquetas de datos del gráfico en tiempo de ejecución, similar a Excel. Tenga en cuenta que Excel proporciona esta función a través de los siguientes pasos. 

1. Selecciona las etiquetas de datos de la Serie y haz clic derecho para abrir el menú emergente.
1. Haz clic en **Formato de las etiquetas de datos...** y se mostrará **Opciones de etiqueta**.
1. Marca o desmarca la casilla de verificación **La etiqueta contiene - Valor de las celdas**.

El código de muestra a continuación accede a las etiquetas de datos de la serie del gráfico y luego establece el método DataLabels.ShowCellRange en true para simular la característica de Excel de **La etiqueta contiene - Valor de celdas**.

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}



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

Consulte el artículo [Mostrar el rango de celdas como las etiquetas de datos](http://aspose.com/docs/display/cellsnet/Mostrar+el+rango+de+celdas+como+las+etiquetas+de+datos) para obtener más información.

{{% /alert %}} 

### **Se agregaron los métodos Cell.GetTable y ListObject.PutCellValue**
Los métodos Cell.GetTable y ListObject.PutCellValue se agregaron con Aspose.Cells for .NET 8.3.1 para facilitar a los usuarios el acceso a ListObject desde una celda y agregar valores en ella utilizando los desplazamientos de fila y columna. El siguiente código de muestra carga la hoja de cálculo de origen y agrega valores dentro de la tabla.

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

Consulte el artículo [Acceder a la tabla desde la celda y agregar valores en ella mediante desplazamientos de fila y columna](http://aspose.com/docs/display/cellsnet/Acceder+a+la+tabla+desde+la+celda+y+agregar+valores+en+ella+mediante+desplazamientos+de+fila+y+columna) para obtener más información.

{{% /alert %}} 

### **Se agregó la propiedad IsStrictSchema11 a la clase OdsSaveOptions para permitir a los desarrolladores guardar la hoja de cálculo en un formato conforme a la especificación ODF v1.2. El valor predeterminado de la propiedad IsStrictSchema11 es falso, lo que significa que, a partir de la versión 8.3.1 de las API de Aspose.Cells, los archivos ODS se guardarán como formato ODF versión 1.2 de forma predeterminada.**
Se ha agregado la propiedad IsStrictSchema11 a la clase OdsSaveOptions para permitir a los desarrolladores guardar la hoja de cálculo en un formato que cumple con la especificación ODF v1.2. El valor predeterminado de la propiedad IsStrictSchema11 es falso, lo que significa que a partir de la versión 8.3.1 de las API de Aspose.Cells, los archivos ODS se guardarán como formato ODF versión 1.2 de forma predeterminada.

El fragmento de código proporcionado a continuación guarda el archivo ODS en formato ODF 1.2.

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

Consulte el artículo [Guardar archivo ODS en las especificaciones ODF 1.1 y 1.2](http://aspose.com/docs/display/cellsnet/Guardar+archivo+ODS+en+las+especificaciones+ODF+1.1+y+1.2) para obtener más información.

{{% /alert %}} 

### **Se agregó el método SparklineCollection.Add**
Las API de Aspose.Cells han expuesto el método SparklineCollection.Add(string dataRange, int row, int column) para especificar el rango de datos y la ubicación del grupo de minigráficos. Tenga en cuenta que Excel proporciona la misma función a través de los siguientes pasos. 

1. Selecciona la celda que contiene tu Sparkline.
1. Selecciona **Editar Datos desde la sección de Sparkline** dentro de la pestaña **Diseño**
1. Elige **Editar Ubicación de Grupo y Datos**.
1. Especifica **Rango de Datos** & **Ubicación**.

El siguiente código de muestra carga la hoja de cálculo fuente, accede al primer grupo de sparkline y agrega nuevos rangos de datos y ubicaciones para el grupo de sparkline. 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

Por favor, consulte el artículo [Copiar Mini Gráfico Especificando el Rango de Datos y la Ubicación del Grupo de Mini Gráficos](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) para obtener más información.

{{% /alert %}}
