---
title: 使用Node.js通过C++移除数据透视连接
linktitle: 删除数据透视连接
type: docs
weight: 30
url: /zh/nodejs-cpp/remove-pivot-connection/
description: 学习如何使用Aspose.Cells for Node.js via C++移除数据透视连接。
keywords: 使用Node.js通过C++移除数据透视连接（不需要Office 2013、Office 2016、Office 2019和Office 365）
---

## **可能的使用场景**

如果您想在Excel中解除切片器和数据透视表的关联，右键点击切片器并选择“报告连接...”项。在选项列表中，您可以操作复选框。同样地，如果您想使用Aspose.Cells API编程方式解除切片器与数据透视表的关联，请使用[**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-)方法。它将解除两者关联。

## **取消切片器与数据透视表的关联**

以下示例代码加载了包含现有切片器的[示例Excel文件](remove-pivot-connection.xlsx)。它访问切片器，然后解除切片器与数据透视表的关联，最后将工作簿保存为[输出Excel文件](remove-pivot-connection-out.xlsx)。

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
