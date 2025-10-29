---
title: 在Node.js via C++中使用Sparklines和3D格式设置
linktitle: 使用Sparklines和设置3D格式
type: docs
weight: 40
url: /zh/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: 学习如何使用Aspose.Cells for Node.js via C++在Excel文件中利用Sparklines并应用3D格式。 
---

## **使用迷你图**
Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。 Sparklines是迷你图，可以放置在单元格内，以便您可以在同一张表格中查看数据和图表。当Sparklines被正确使用时，数据分析更快捷、更简洁。它们还提供信息的简单视图，避免了拥挤的工作表和繁忙的图表。

Aspose.Cells for Node.js via C++提供了操作电子表格中Sparklines的API。
### **Microsoft Excel 中的迷你图**
如何在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了方便查看，选择数据旁边的单元格。
1. 在功能区上单击**插入**，然后在**迷你图**组中选择**柱**。
1. 选择或输入包含源数据的工作表中的单元格范围。图表将出现。

迷你图可帮助您查看趋势，例如垒球联赛的胜负记录。迷你图甚至可以总结联赛中每支队伍整个赛季的情况。
### **利用Aspose.Cells for Node.js via C++实现Sparklines**
开发者可以使用Aspose.Cells for Node.js via C++提供的API创建、删除或读取模板文件中的Sparklines。管理Sparklines的类包含在[SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/)模块中，使用这些功能之前需要引入该模块。

通过为给定的数据范围添加自定义图形，开发人员可以自由地向选定的单元区域添加不同类型的迷你图。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围向单元区域添加新的迷你图。
1. 将 Excel 文件保存到磁盘。


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
## **设置 3D 格式**
你可能需要3D图表样式，以便获得适合你的场景的结果。Aspose.Cells for Node.js via C++确实提供相关API以应用Microsoft Excel 2007的3D格式。

下面给出了一个完整的示例，演示如何创建图表并应用 Microsoft Excel 2007 的 3D 格式。执行示例代码后，工作表中将添加一个带有 3D 效果的柱状图。


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
{{< app/cells/assistant language="nodejs-cpp" >}}
