---
title: 使用Node.js通过C++更改切片器属性
linktitle: 更改切片器属性
type: docs
weight: 70
url: /zh/nodejs-cpp/change-slicer-properties/
---

## **可能的使用场景**

可能会有需要更改切片器属性（如位置或行高）的时候，Aspose.Cells for Node.js via C++为您提供了更新这些属性的选项。

## **更改切片器属性**

请查看以下示例代码。它加载包含表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器，并更改其属性，如行高、宽度、是否可打印、标题等。将工作簿另存为[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing a table.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateSlicerToExcelTable.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first table inside the worksheet.
const table = worksheet.getListObjects().get(0);

// Add slicer
const idx = worksheet.getSlicers().add(table, 0, "H5");

const slicer = worksheet.getSlicers().get(idx);
slicer.setPlacement(AsposeCells.PlacementType.FreeFloating);
slicer.setRowHeightPixel(50);
slicer.setWidthPixel(500);
slicer.setTitle("Aspose");
slicer.setAlternativeText("Alternate Text");
slicer.setIsPrintable(false);
slicer.setIsLocked(false);

// Refresh the slicer.
slicer.refresh();

// Save the workbook in output XLSX format.
workbook.save(path.join(outputDir, "outputChangeSlicerProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
