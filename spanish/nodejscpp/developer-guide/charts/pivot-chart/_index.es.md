---
title: Cómo agregar un PivotChart usando Aspose.Cells for Node.js via C++
linktitle: Gráfico de Tabla Dinámica
type: docs
weight: 100
url: /es/nodejs-cpp/how-to-add-pivot-chart/
description: Cómo agregar un PivotChart usando Aspose.Cells for Node.js via C++.
keywords: PivotChart Node.js a través de C++
---
## ¿Qué es un PivotChart?

Un gráfico dinámico es una representación visual de los datos en una tabla dinámica. Los gráficos dinámicos ofrecen una forma de resumir, analizar, explorar y presentar datos resumidos. Aquí algunas características clave y aspectos de los gráficos dinámicos:

1. Representación dinámica de datos: Los gráficos dinámicos se actualizan automáticamente para reflejar cambios en la tabla dinámica. Si añades o eliminas campos en la tabla dinámica, el gráfico dinámico se actualiza en consecuencia.

1. Interactivo: Los gráficos dinámicos son interactivos, permitiendo a los usuarios filtrar, ordenar y profundizar en los datos. Esto facilita explorar diferentes aspectos del conjunto de datos.

1. Diseño flexible: Los usuarios pueden cambiar el diseño del gráfico dinámico arrastrando y soltando campos, lo que ofrece flexibilidad en la visualización de datos.

1. Diversos tipos de gráficos: Los gráficos dinámicos se pueden crear usando varios tipos de gráficos, como barras, líneas, tartas y más, dependiendo de la naturaleza de los datos y las ideas que deseas obtener.

1. Resumen: Los gráficos dinámicos resumen grandes cantidades de datos y pueden mostrar totales, promedios, conteos u otras estadísticas resumidas.

1. Filtrado: Proporcionan capacidades de filtrado, permitiendo mostrar solo los datos que cumplen ciertos criterios.

<br>
Los gráficos dinámicos se usan comúnmente en inteligencia empresarial y análisis de datos para ofrecer un resumen visual claro y conciso de conjuntos de datos complejos. Son una herramienta poderosa para tomar decisiones basadas en datos.

## Cómo agregar un gráfico dinámico usando Aspose.Cells for Node.js via C++

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells for Node.js via C++:

1. Agrega algunos datos a una hoja de cálculo usando el método `putValue` de un objeto Cell. También puedes usar un archivo de plantilla ya lleno de datos. Los datos se usarán como fuente de datos para la tabla dinámica.
1. Agrega una tabla dinámica a la hoja de cálculo llamando al método `add` de la colección `PivotTables`.
1. Accede al objeto PivotTable nuevo desde la colección `PivotTables` pasando su índice. Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para gestionar la tabla.

A continuación se muestran ejemplos de código.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Añadiendo un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells for Node.js via C++:

1. Agregue un gráfico.
1. Establece el `PivotSource` del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
