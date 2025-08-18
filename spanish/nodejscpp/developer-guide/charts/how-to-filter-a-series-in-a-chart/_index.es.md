---
title: Tres métodos para filtrar datos en gráficos con Node.js vía C++
linktitle: Tres métodos para filtrar datos de gráficos
description: Aprende cómo filtrar gráficos en Excel usando Aspose.Cells for Node.js via C++. Nuestra guía completa demostrará cómo aplicar filtros a gráficos, personalizar elementos del gráfico y usar herramientas de análisis de datos para obtener mejores conocimientos y tomar decisiones informadas.
keywords: Aspose.Cells for Node.js via C++, Filtrado de gráficos en Excel, Análisis de datos, Toma de decisiones, Visualización.
type: docs
weight: 2210
url: /es/nodejs-cpp/filtering-charts-in-excel/
---


## **1. Filtrado de series para representar un gráfico**

### **Pasos para filtrar series de un gráfico en Excel**
En Excel, podemos filtrar series específicas de un gráfico, haciendo que esas series filtradas no se muestren en el gráfico. El gráfico original se muestra en **Figura 1**. Sin embargo, cuando filtramos **Testseries2** y **Testseries4**, el gráfico aparecerá como en la **Figura 2**.

En Aspose.Cells for Node.js via C++, podemos realizar una operación similar. Para un archivo de [muestra](seriesFiltered.xlsx) como este, si queremos filtrar **Testseries2** y **Testseries4**, podemos ejecutar el siguiente código. Además, mantendremos dos listas: una lista ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) para almacenar todas las series seleccionadas.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](seriesFiltered.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. Filtra los datos y permite que el gráfico cambie**

Filtrar tus datos es una excelente manera de manejar filtros de gráficos con muchos datos. Cuando filtras los datos, el gráfico cambiará. Un problema que tendremos que solucionar es asegurarnos de que el gráfico permanezca en pantalla. Cuando filtras, obtienes filas ocultas, y ocasionalmente, el gráfico estará en esas filas ocultas.

![todo:image_alt_text](Figure3.png)

### **Pasos para utilizar los Filtros de Datos para cambiar el gráfico en Excel**

1. Haz clic dentro de tu rango de datos.
2. Haz clic en la pestaña **Datos** y activa los Filtros haciendo clic en Filtros. Tu fila de encabezado tendrá flechas desplegables.
3. Crea un gráfico yendo a la pestaña **Insertar** y seleccionando un gráfico de columnas.
4. Ahora filtra tus datos usando las flechas desplegables en los datos. No uses los Filtros de Gráfico.

### **Código de muestra**
El siguiente código de ejemplo muestra la misma función usando Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. Filtra los datos utilizando una Tabla y permite que el gráfico cambie**

Utilizar una Tabla es similar al Método 2, utilizando un rango, pero tienes ventajas con las tablas sobre los rangos. Cuando cambias tu rango a una Tabla y agregas datos, el gráfico se actualiza automáticamente. Con un rango, tendrás que cambiar la fuente de datos.

### **Formatear como tabla en Excel**

Haz clic dentro de tus datos y usa **CTRL + T** o ve a la pestaña Inicio, **Formato como Tabla**

![todo:image_alt_text](Figure4.png)

### **Código de muestra**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](TableFilters.xlsx) y muestra la misma función usando Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
