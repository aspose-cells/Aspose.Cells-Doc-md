---
title: Público API Cambios en Aspose.Cells 8.3.1
type: docs
weight: 120
url: /es/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.3.0 a la 8.3.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **API añadidas**
### **Propiedad DataLabels.ShowCellRange agregado**
El getter/setter para la propiedad ShowCellRange se ha agregado a la clase DataLabels para imitar la funcionalidad de Excel de formatear las etiquetas de datos del gráfico en tiempo de ejecución. Tenga en cuenta que Excel proporciona esta función a través de los siguientes pasos.

1. Seleccione Etiquetas de datos de la serie y haga clic con el botón derecho para abrir el menú emergente.
1.  Haga clic en el**Formatear etiquetas de datos...** y se mostrará**Opciones de etiqueta**.
1.  Marque o desmarque la casilla de verificación**La etiqueta contiene: valor desde Cells**.

 El código de muestra a continuación accede a las etiquetas de datos de la serie de gráficos y luego establece el método DataLabels.setShowCellRange() en verdadero para imitar la característica de Excel de**La etiqueta contiene: valor desde Cells**.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Mostrando el rango Cell como las etiquetas de datos](/cells/es/java/showing-cell-range-as-the-data-labels/) para más información.

{{% /alert %}} 

### **Métodos Cell.getTable & ListObject.putCellValue agregado**
Los métodos Cell.getTable y ListObject.putCellValue se agregaron con Aspose.Cells for Java 8.3.1 para facilitar a los usuarios el acceso a ListObject desde una celda y agregar valores dentro de ella utilizando los desplazamientos de fila y columna. El siguiente código de ejemplo carga la hoja de cálculo de origen y agrega valores dentro de la tabla.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Acceder a la tabla desde Cell y agregar valores dentro de ella usando compensaciones de fila y columna](/cells/es/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) para más información.

{{% /alert %}} 

### **Métodos OdsSaveOptions.isStrictSchema11 y OdsSaveOptions.setStrictSchema11 agregados**
Los métodos isStrictSchema11 y setStrictSchema11 se agregaron a la clase OdsSaveOptions para permitir que los desarrolladores guarden la hoja de cálculo en un formato que cumpla con la especificación ODF v1.2. El valor predeterminado de la propiedad setStrictSchema11 es falso, lo que significa que a partir de la versión 8.3.1 de las API Aspose.Cells, los archivos ODS se guardarán en formato ODF versión 1.2 de forma predeterminada.

El fragmento de código proporcionado a continuación guarda el archivo ODS en formato ODF 1.2.

**Java**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Guarde el archivo ODS en ODF 1.1 y 1.2 Especificaciones](/cells/es/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) para más información.

{{% /alert %}} 

### **Método SparklineCollection.add Agregado**
 Aspose.Cells Las API han expuesto el método SparklineCollection.add(String dataRange, int row, int column) para especificar el rango de datos y la ubicación del grupo Sparkline. Tenga en cuenta que Excel proporciona la misma característica a través de los siguientes pasos.

1. Seleccione la celda que contiene su minigráfico.
1.  Seleccione**Editar datos desde el minigráfico** sección dentro de la**Diseño** pestaña
1.  Escoger**Editar ubicación y datos del grupo**.
1.  Especificar**Rango de datos** & **Localización**.

 El siguiente código de ejemplo carga la hoja de cálculo de origen, accede al primer grupo de minigráficos y agrega nuevos rangos de datos y ubicaciones para el grupo de minigráficos.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Copie Sparkline especificando el rango de datos y la ubicación del grupo Sparkline](/cells/es/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) para más información.

{{% /alert %}}
