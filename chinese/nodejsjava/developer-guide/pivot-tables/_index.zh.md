---
title: 插入数据透视表
description: 使用 Aspose.Cells for Node.js via Java 创建和格式化 Excel 电子表格中的数据透视表。
linktitle: 数据透视表
url: /zh/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: 创建数据透视表, 插入数据透视表, 格式化数据透视表, Aspose.Cells for Node.js via Java。
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **创建数据透视表**
可以使用 Aspose.Cells 以编程方式向电子表格添加数据透视表。

### **数据透视表对象模型**
Aspose.Cells 提供了一组用于创建和控制数据透视表的类。其构建块如下:
- `PivotField` 表示 `PivotTable` 中的一个字段。
- `PivotFieldCollection` 表示 `PivotTable` 中所有 `PivotField` 对象的集合。
- `PivotTable` 表示工作表上的数据透视表。
- `PivotTableCollection` 表示工作表上所有 `PivotTable` 对象的集合。

### **使用 Aspose.Cells 创建简单的数据透视表**
1. 使用单元格的 `putValue` 方法向工作表添加数据。此数据将用作数据透视表的数据源。
2. 通过调用封装在工作表对象中的 `PivotTables` 集合的 `add` 方法，向工作表添加数据透视表。
3. 通过传递数据透视表的索引，从 `PivotTables` 集合访问新的 `PivotTable` 对象。
4. 使用上述任何一个 `PivotTable` 对象来管理数据透视表。

执行示例代码后,数据透视表将添加到工作表中。

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
将单元格范围指定为数据源时,范围必须从左上到右下。例如,"A1:C3" 是有效的,但 "C3:A1" 无效。
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/zh/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/zh/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}