---
title: Cambios en la API pública en Aspose.Cells 8.4.2
type: docs
weight: 160
url: /es/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.4.1 a la 8.4.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, [clases agregadas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-4-2/), sino también una descripción de cualquier cambio en el comportamiento detrás de escenas en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo mejorado de creación de gráficos**
La clase com.aspose.cells.charts.Chart ha expuesto el método setChartDataRange para facilitar la tarea de creación de gráficos. El método setChartDataRange acepta dos parámetros, siendo el primer parámetro de tipo cadena que especifica el área de celdas desde la cual trazar las series de datos. El segundo parámetro es de tipo booleano que especifica la orientación del trazado, es decir; si trazar las series de datos del gráfico desde un rango de valores de celda por fila o por columnas.

El siguiente fragmento de código muestra cómo crear un gráfico de columnas con pocas líneas de código asumiendo que la serie de datos del gráfico está presente en la misma hoja de cálculo desde la celda A1 hasta D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Método VbaModuleCollection.add agregado**
Aspose.Cells for Java 8.4.2 ha expuesto el método VbaModuleCollection.add para agregar un nuevo módulo VBA a la instancia de Workbook. El método VbaModuleCollection.add acepta un parámetro de tipo Worksheet para agregar un módulo específico de la hoja de cálculo.

El siguiente fragmento de código muestra cómo usar el método VbaModuleCollection.add.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.4.2 ha expuesto una versión sobrecargada del método Cells.copyColumns para repetir las columnas de origen en el destino. El nuevo método expuesto acepta un total de 5 parámetros, donde los primeros 4 parámetros son iguales que los del método común Cells.copyColumns. Sin embargo, el último parámetro de tipo entero especifica el número de columnas de destino en las cuales se deben repetir las columnas de origen.

El siguiente fragmento de código muestra cómo usar el método Cells.copyColumns recientemente expuesto.

**Java**

{{< highlight csharp >}}

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

### **Adición de los campos de enumeración PasteType.DEFAULT y PasteType.ALL_EXCEPT_BORDERS**
Con el lanzamiento de v8.4.2, la API Aspose.Cells ha agregado 2 nuevos campos de enumeración para PasteType como se detalla a continuación.

- PasteType.DEFAULT: Funciona de manera similar a la funcionalidad "Todo" de Excel para pegar un rango de celdas.
- PasteType.ALL_EXCEPT_BORDERS: Funciona de manera similar a la funcionalidad "Todo excepto bordes" de Excel para pegar un rango de celdas.

El siguiente código de ejemplo demuestra el uso del campo PasteType.DEFAULT.

**Java**

{{< highlight csharp >}}

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

A partir del lanzamiento de Aspose.Cells for Java 8.4.2, el campo de enumeración PasteType.ALL se comporta de manera diferente en comparación con la funcionalidad "Todo" de Excel para pegar un rango de celdas. Ahora, el PasteType.ALL también copia los anchos de columna en el rango de destino en oposición a la funcionalidad "Todo" de Excel. Para imitar el comportamiento "Todo" de Excel, por favor use el PasteType.DEFAULT.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
