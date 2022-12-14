---
title: Público API Cambios en Aspose.Cells 8.4.2
type: docs
weight: 160
url: /es/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.4.1 a la 8.4.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-4-2/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo de creación de gráficos mejorado**
La clase com.aspose.cells.charts.Chart ha expuesto el método setChartDataRange para facilitar la tarea de creación de gráficos. El método setChartDataRange acepta dos parámetros, donde el primer parámetro es de tipo cadena que especifica el área de la celda desde la cual trazar la serie de datos. El segundo parámetro es de tipo booleano que especifica la orientación de la trama, es decir; si trazar la serie de datos del gráfico a partir de un rango de valores de celda por fila o por columnas.

El siguiente fragmento de código muestra cómo crear un gráfico de columnas con pocas líneas de código, suponiendo que los datos de la serie de gráficos del gráfico están presentes en la misma hoja de trabajo desde la celda A1 hasta la D4.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Método VbaModuleCollection.add Agregado**
Aspose.Cells for Java 8.4.2 ha expuesto el método VbaModuleCollection.add para agregar un nuevo módulo VBA a la instancia de Workbook. El método VbaModuleCollection.add acepta un parámetro de tipo Hoja de trabajo para agregar un módulo específico de la hoja de trabajo.

El siguiente fragmento de código muestra cómo usar el método VbaModuleCollection.add.

**Java**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Método sobrecargado Cells.copyColumns agregado**
Aspose.Cells for Java 8.4.2 ha expuesto una versión sobrecargada del método Cells.copyColumns para repetir las columnas de origen en el destino. El método recientemente expuesto acepta 5 parámetros en total, donde los primeros 4 parámetros son los mismos que los del método común Cells.copyColumns. Sin embargo, el último parámetro de tipo int especifica el número de columnas de destino en las que se deben repetir las columnas de origen.

El siguiente fragmento de código muestra cómo usar el método Cells.copyColumns recientemente expuesto.

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Campos de enumeración PasteType.DEFAULT y PasteType.ALL_EXCEPT_BORDERS agregados**
Con el lanzamiento de v8.4.2, Aspose.Cells API agregó 2 nuevos campos de enumeración para PasteType como se detalla a continuación.

- PasteType.DEFAULT: funciona de manera similar a la funcionalidad "Todos" de Excel para pegar el rango de celdas.
- PegarTipo.TODO_EXCEPTO_FRONTERAS: funciona de manera similar a la funcionalidad "Todo excepto los bordes" de Excel para pegar el rango de celdas.

El código de ejemplo siguiente muestra el uso del campo PasteType.DEFAULT.

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

A partir del lanzamiento de Aspose.Cells for Java 8.4.2, el archivo de enumeración PasteType.ALL se comporta de manera diferente en comparación con la funcionalidad "Todos" de Excel para pegar el rango de celdas. Ahora, PasteType.ALL también copia los anchos de columna en el rango de destino a diferencia de la funcionalidad "Todos" de Excel. Para imitar el comportamiento "Todos" de Excel, utilice PasteType.DEFAULT.

{{% /alert %}}
