---
title: Использование Sparklines и настроек 3D формата с помощью Node.js через C++
linktitle: Использование мини графиков и настройки 3D формата
type: docs
weight: 40
url: /ru/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Узнайте, как использовать спарклайны и применять 3D форматирование в файлах Excel с помощью Aspose.Cells for Node.js via C++. 
---

## **Использование мини-графиков**
Microsoft Excel 2010 позволяет анализировать информацию более чем когда-либо прежде. С его помощью пользователи могут отслеживать и выделять важные тенденции данных с помощью новых средств анализа и визуализации. Мини-графики - это миниатюрные графики, которые можно разместить внутри ячеек, чтобы одновременно просматривать данные и диаграмму на одной и той же таблице. При правильном использовании мини-графиков анализ данных становится более быстрым и точным. Они также обеспечивают простой просмотр информации, избегая переполненных листов с множеством занятых диаграмм.

Aspose.Cells for Node.js via C++ предоставляет API для манипулирования спарклайнами в таблицах.
### **Мини-графики в Microsoft Excel**
Для вставки мини-графиков в Microsoft Excel 2010:

1. Выберите ячейки, где вы хотите разместить мини-графики. Чтобы упростить их просмотр, выберите ячейки сбоку от данных.
1. Нажмите **Вставка** на ленте и затем выберите **столбец** в группе **Мини-графики**.
1. Выберите или введите диапазон ячеек на листе, который содержит исходные данные. Диаграммы появятся.

Мини-графики помогают видеть тенденции, например, победы или поражения в лиге по софтболу. Мини-графики могут даже подвести итоги всего сезона каждой команды в лиге.
### **Спарклайны с использованием Aspose.Cells for Node.js via C++**
Разработчики могут создавать, удалять или считывать спарклайны (в шаблонном файле) с помощью API, предоставляемого Aspose.Cells for Node.js via C++. Классы, управляющие спарклайнами, содержатся в модуле [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/), поэтому перед использованием этих функций необходимо подключить этот модуль.

Добавляя пользовательские графики для определенного диапазона данных, разработчики имеют возможность добавлять различные типы маленьких диаграмм в выбранные области ячеек.

Приведенный ниже пример демонстрирует функцию мини-графиков. Пример показывает, как:

1. Открыть простой файл шаблона.
1. Прочитать информацию о мини-графиках для листа.
1. Добавьте новые искры для определенного диапазона данных в область ячейки.
1. Сохраните файл Excel на диск.


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
## **Настройка 3D формата**
Вам могут понадобиться стили 3D-графиков, чтобы получить только результаты, подходящие для вашего сценария. Aspose.Cells for Node.js via C++ действительно предоставляет соответствующий API для применения 3D-форматирования в Microsoft Excel 2007.

Ниже приведен полный пример для демонстрации того, как создать диаграмму и применить форматирование 3D Microsoft Excel 2007. После выполнения примерного кода на листе будет добавлена столбчатая диаграмма (с 3D эффектами).


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
