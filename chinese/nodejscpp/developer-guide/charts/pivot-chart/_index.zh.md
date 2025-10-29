---
title: 如何使用Aspose.Cells for Node.js via C++添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/nodejs-cpp/how-to-add-pivot-chart/
description: 如何使用Aspose.Cells for Node.js via C++添加数据透视图
keywords: 数据透视图 Node.js 通过 C++
---
## 什么是数据透视图

透视图表是数据透视表的可视化表现形式。透视图表提供了汇总、分析、探索和展示汇总数据的方式。以下是透视图表的一些主要功能和特性：

1. 动态数据表示：数据透视图会自动更新以反映数据透视表的变化。如果在数据透视表中添加或删除字段，数据透视图也会相应更新。

1. 交互性强：数据透视图具有交互性，允许用户筛选、排序和深入分析数据。这使得探索数据的不同方面变得容易。

1. 灵活布局：用户可以通过拖放字段改变数据透视图的布局，为数据可视化提供灵活性。

1. 多种图表类型：可以根据数据的性质和需要获得的洞察，创建柱状图、折线图、饼图等多种类型的图表。

1. 汇总：数据透视图汇总大量数据，可以显示总计、平均值、计数或其他统计信息。

1. 筛选：提供筛选功能，仅显示符合特定条件的数据。

<br>
透视图表常用于商业智能和数据分析，帮助客户清晰、简洁地展示复杂数据，是做出数据驱动决策的强大工具。

## 使用Aspose.Cells for Node.js via C++添加数据透视图表的方法

### **添加数据透视表**

使用 Aspose.Cells for Node.js via C++ 创建数据透视表的方法：

1. 使用单元格对象的`putValue`方法向工作表添加一些数据。您也可以使用已填充数据的模板文件。数据将作为数据透视表的数据源。
1. 通过调用`PivotTables`集合的`add`方法在工作表中添加数据透视表。
1. 通过传入索引从`PivotTables`集合访问新创建的PivotTable对象。使用封装在PivotTable对象中的任何数据透视表对象来管理表格。

下面是代码示例。

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

### **添加数据透视图**

使用 Aspose.Cells for Node.js via C++ 创建数据透视图的方法：

1. 添加图表。
1. 设置图表的`PivotSource`，指向工作表中的现有数据透视表。
1. 设置其他属性。

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
