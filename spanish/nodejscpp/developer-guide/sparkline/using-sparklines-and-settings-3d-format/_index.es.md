---
title: Uso de Sparklines y Configuración de Formato 3D con Node.js a través de C++
linktitle: Usando mini gráficos y configuraciones de formato 3D
type: docs
weight: 40
url: /es/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Aprenda cómo usar sparklines y aplicar formato 3D en archivos de Excel con Aspose.Cells for Node.js via C++. 
---

## **Usando Sparklines**
Microsoft Excel 2010 puede analizar la información de más maneras que nunca. Permite a los usuarios realizar un seguimiento y resaltar tendencias importantes de datos con nuevas herramientas de análisis y visualización de datos. Las sparklines son mini gráficos que se pueden colocar dentro de las celdas para que puedas ver los datos y el gráfico en la misma tabla. Cuando se usan sparklines de manera adecuada, el análisis de datos es más rápido y preciso. También proporcionan una vista simple de la información, evitando hojas de cálculo sobrecargadas con una gran cantidad de gráficos ocupados.

Aspose.Cells for Node.js via C++ proporciona una API para manipular sparklines en hojas de cálculo.
### **Sparklines en Microsoft Excel**
Para insertar sparklines en Microsoft Excel 2010:

1. Selecciona las celdas donde quieres que aparezcan las sparklines. Para que sean fáciles de ver, selecciona las celdas al lado de los datos.
1. Haz clic en **Insertar** en la cinta y luego elige **columna** en el grupo de **Sparklines**.
1. Seleccione o ingrese el rango de celdas en la hoja de cálculo que contenga los datos fuente. Los gráficos aparecerán.

Los mini gráficos le ayudan a ver tendencias, por ejemplo, el registro de victorias o derrotas de una liga de softball. Incluso pueden resumir toda la temporada de cada equipo en la liga.
### **Sparklines usando Aspose.Cells for Node.js via C++**
Los desarrolladores pueden crear, eliminar o leer sparklines (en el archivo plantilla) usando la API proporcionada por Aspose.Cells for Node.js via C++. Las clases que gestionan sparklines están contenidas en el módulo [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/), por lo que primero debe requerir este módulo antes de usar estas funciones.

Al agregar gráficos personalizados para un determinado rango de datos, los desarrolladores tienen la libertad de agregar diferentes tipos de gráficos pequeños a áreas de celdas seleccionadas.

El siguiente ejemplo demuestra la función de Sparklines. El ejemplo muestra cómo:

1. Abrir un archivo de plantilla simple.
1. Leer la información de sparklines para una hoja de cálculo.
1. Agregar nuevas miniaturas para un rango de datos dado a un área de celdas.
1. Guarde el archivo de Excel en disco.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **Configuración de formato 3D**
Podría necesitar estilos de gráficos en 3D para obtener solo los resultados para su escenario. Aspose.Cells for Node.js via C++ sí proporciona la API relevante para aplicar el formato 3D de Microsoft Excel 2007.

A continuación se muestra un ejemplo completo para demostrar cómo crear un gráfico y aplicar el formato 3D de Microsoft Excel 2007. Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas (con efectos 3D) a la hoja de cálculo.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
