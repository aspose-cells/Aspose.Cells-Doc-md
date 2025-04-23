---
title: Cambios en la API pública en Aspose.Cells 8.4.2
type: docs
weight: 150
url: /es/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.4.1 hasta 8.4.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, [clases agregadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-2/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo mejorado de creación de gráficos**
La clase Aspose.Cells.Charts.Chart ha expuesto el método SetChartDataRange para facilitar la tarea de creación de gráficos. El método SetChartDataRange acepta dos parámetros, donde el primer parámetro es de tipo cadena que especifica el área de celdas desde la que trazar la serie de datos. El segundo parámetro es de tipo booleano que especifica la orientación de la trama, es decir; si trazar la serie de datos del gráfico desde un rango de valores de celdas por filas o por columnas.

El siguiente fragmento de código muestra cómo crear un gráfico de columnas con pocas líneas de código asumiendo que la serie de datos del gráfico está presente en la misma hoja de cálculo desde la celda A1 hasta D4.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Método VbaModuleCollection.Add añadido**
Aspose.Cells for .NET La versión 8.4.2 ha expuesto el método VbaModuleCollection.Add para agregar un nuevo módulo VBA a la instancia de Workbook. El método VbaModuleCollection.Add acepta un parámetro de tipo hoja de cálculo para agregar un módulo específico de hoja de cálculo.

El siguiente fragmento de código muestra cómo utilizar el método VbaModuleCollection.Add.

**C#**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Método sobrecargado Cells.CopyColumns añadido**
Aspose.Cells for .NET La versión 8.4.2 ha expuesto una versión sobrecargada del método Cells.CopyColumns para repetir las columnas fuente en el destino. El método recién expuesto acepta un total de 5 parámetros, donde los primeros 4 parámetros son iguales que el método común Cells.CopyColumns. Sin embargo, el último parámetro de tipo int especifica el número de columnas de destino en las que se deben repetir las columnas fuente.

El siguiente fragmento de código muestra cómo utilizar el método Cells.CopyColumns recién expuesto.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Se añadieron los campos de enumeración PasteType.Default & PasteType.DefaultExceptBorders**
Con el lanzamiento de v8.4.2, la API Aspose.Cells ha agregado 2 nuevos campos de enumeración para PasteType como se detalla a continuación.

- PasteType.Default: Funciona de manera similar a la funcionalidad "Todo" de Excel para pegar rango de celdas.
- PasteType.DefaultExceptBorders: Funciona de manera similar a la funcionalidad "Todo excepto bordes" de Excel para pegar rango de celdas.

El siguiente código de muestra demuestra el uso del campo PasteType.Default.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

A partir de la versión Aspose.Cells for .NET 8.4.2, el campo de enumeración PasteType.All se comporta de manera diferente en comparación con la funcionalidad "Todo" de Excel para pegar el rango de celdas. Ahora, el PasteType.All también copia los anchos de columna en el rango de destino, a diferencia de la funcionalidad "Todo" de Excel. Para imitar el comportamiento "Todo" de Excel, por favor use el PasteType.Default.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
