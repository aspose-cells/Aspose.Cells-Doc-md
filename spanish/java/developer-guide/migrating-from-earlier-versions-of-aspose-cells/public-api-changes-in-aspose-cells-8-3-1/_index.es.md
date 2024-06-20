---
title: Cambios en la API pública en Aspose.Cells 8.3.1
type: docs
weight: 120
url: /es/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.3.0 a la 8.3.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **APIs Añadidas**
### **Se ha añadido la propiedad ShowCellRange a DataLabels.**
El getter/setter para la propiedad ShowCellRange se ha añadido a la clase DataLabels para imitar la funcionalidad de Excel de formatear las etiquetas de datos del gráfico en tiempo de ejecución. Tenga en cuenta que Excel proporciona esta función a través de los siguientes pasos. 

1. Selecciona las etiquetas de datos de la Serie y haz clic derecho para abrir el menú emergente.
1. Haz clic en **Formato de las etiquetas de datos...** y se mostrará **Opciones de etiqueta**.
1. Marca o desmarca la casilla de verificación **La etiqueta contiene - Valor de las celdas**.

El código de muestra a continuación accede a las Etiquetas de Datos de la Serie de Gráficos y luego establece el método DataLabels.setShowCellRange() en true para imitar la función de Excel de **La etiqueta contiene - Valor de Celdas**.

**Java**

{{< highlight csharp >}}

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

Por favor, revise el artículo [Mostrando Rango de Celdas como Etiquetas de Datos](/cells/es/java/showing-cell-range-as-the-data-labels/) para más información.

{{% /alert %}} 

### **Añadidos los Métodos Cell.getTable & ListObject.putCellValue**
Los métodos Cell.getTable & ListObject.putCellValue se han añadido con Aspose.Cells for Java 8.3.1 para facilitar a los usuarios el acceso a ListObject desde una celda y agregar valores dentro de ella utilizando los desplazamientos de fila y columna. El siguiente código de muestra carga la hoja de cálculo fuente y agrega valores dentro de la tabla.

**Java**

{{< highlight csharp >}}

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

Por favor, revise el artículo [Accediendo a la Tabla desde la Celda y Agregando Valores dentro de ella utilizando los Desplazamientos de Fila y Columna](/cells/es/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) para más información.

{{% /alert %}} 

### **Añadidos los Métodos OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11**
Los métodos isStrictSchema11 & setStrictSchema11 se han añadido a la clase OdsSaveOptions para permitir a los desarrolladores guardar la hoja de cálculo en un formato conforme a la especificación ODF v1.2. El valor predeterminado de la propiedad setStrictSchema11 es false, lo que significa que a partir de la versión 8.3.1 de Aspose.Cells APIs los archivos ODS se guardarán como formato ODF versión 1.2 por defecto.

El fragmento de código proporcionado a continuación guarda el archivo ODS en formato ODF 1.2.

**Java**

{{< highlight csharp >}}

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

Por favor, revise el artículo [Guardar archivo ODS en las Especificaciones ODF 1.1 y 1.2](/cells/es/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) para más información.

{{% /alert %}} 

### **Añadido el Método SparklineCollection.add**
Aspose.Cells APIs han expuesto el método SparklineCollection.add(String dataRange, int row, int column) para especificar el Rango de Datos y la Ubicación del Grupo de Sparkline. Ten en cuenta que Excel proporciona la misma función a través de los siguientes pasos. 

1. Selecciona la celda que contiene tu Sparkline.
1. Selecciona **Editar Datos desde la sección de Sparkline** dentro de la pestaña **Diseño**
1. Elige **Editar Ubicación de Grupo y Datos**.
1. Especifica **Rango de Datos** & **Ubicación**.

El siguiente código de muestra carga la hoja de cálculo fuente, accede al primer grupo de sparkline y agrega nuevos rangos de datos y ubicaciones para el grupo de sparkline. 

**Java**

{{< highlight csharp >}}

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

Por favor, revisa el artículo [Copiar Sparkline Especificando Rango de Datos y Ubicación del Grupo de Sparklines](/cells/es/java/copiar-sparkline-especificando-rango-de-datos-y-ubicacion-del-grupo-de-sparklines/) para más información.

{{% /alert %}}
