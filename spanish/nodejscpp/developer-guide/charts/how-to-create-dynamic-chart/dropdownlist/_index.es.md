---
title: Cómo crear un gráfico dinámico con lista desplegable usando Node.js vía C++
linktitle: Cómo crear un Gráfico Dinámico con Lista Desplegable
description: Aprende cómo crear un gráfico dinámico que se actualice basado en la selección de una lista desplegable usando Aspose.Cells for Node.js via C++. Nuestra guía paso a paso demostrará cómo integrar una lista desplegable en tu gráfico para una visualización de datos flexible.
keywords: Aspose.Cells for Node.js via C++, gráfico dinámico, lista desplegable, visualización de datos, integración, visualización flexible.
type: docs
weight: 76
url: /es/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Escenarios de uso posibles**
Un Gráfico Dinámico con Lista Desplegable en Excel es una herramienta poderosa que permite a los usuarios crear gráficos interactivos que pueden actualizarse dinámicamente en función de los datos seleccionados. Esta característica es particularmente útil en situaciones en las que se necesita analizar múltiples conjuntos de datos o comparar varios escenarios.

Una aplicación común de un Gráfico Dinámico con Lista Desplegable es en el análisis financiero. Por ejemplo, una empresa puede tener múltiples conjuntos de datos financieros para diferentes años o departamentos. Al utilizar una lista desplegable, los usuarios pueden seleccionar el conjunto de datos específico que desean analizar y el gráfico se actualizará automáticamente para mostrar la información correspondiente. Esto permite una fácil comparación e identificación de tendencias o patrones.

Otra aplicación está en ventas y marketing. Una empresa puede tener datos de ventas para diferentes productos o regiones. Con un Gráfico Dinámico con Lista Desplegable, los usuarios pueden elegir un producto o región específica de la lista desplegable y el gráfico se actualizará dinámicamente para mostrar el rendimiento de ventas para la opción seleccionada. Esto ayuda a identificar las áreas o productos más destacados y a tomar decisiones basadas en datos.

En resumen, un Gráfico Dinámico con Lista Desplegable en Excel proporciona una forma flexible e interactiva de visualizar y analizar datos. Es valioso en situaciones en las que se necesita comparar múltiples conjuntos de datos o explorar diferentes escenarios, convirtiéndolo en una herramienta versátil para el análisis financiero, ventas y marketing, y muchas otras aplicaciones.

## **Utiliza Aspose Cells para crear un Gráfico Dinámico con Lista Desplegable**
En los siguientes párrafos, te mostraremos cómo crear un gráfico dinámico con lista desplegable usando Aspose.Cells for Node.js via C++. Mostraremos el código del ejemplo, así como el archivo Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico Dinámico con Lista Desplegable](DynamicChartWithDropdownlist.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Notas**
En el archivo generado, el gráfico contará dinámicamente los datos para el mes seleccionado. Esto se hace utilizando la fórmula "OFFSET" en el código de ejemplo:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Puedes intentar cambiar el valor de la lista desplegable en la celda "Hoja1!$A$10", y verás el cambio dinámico del gráfico. Ahora hemos creado un gráfico dinámico con lista desplegable usando Aspose.Cells con éxito.
{{< app/cells/assistant language="nodejs-cpp" >}}
