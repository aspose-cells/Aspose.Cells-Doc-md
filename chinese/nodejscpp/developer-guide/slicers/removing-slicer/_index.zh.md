---
title: 使用Node.js通过C++删除切片器
linktitle: 移除切片器
type: docs
weight: 30
url: /zh/nodejs-cpp/removing-slicer/
---

## **可能的使用场景**

如果您想删除Excel中的切片器，只需选中它并按*删除*键。同样地，如果您想通过Aspose.Cells API编程方式移除切片器，请使用[**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-)方法。它将从工作表中移除切片器。

## **移除切片器**

以下示例代码加载了包含现有切片器的[示例Excel文件](67338478.xlsx)。它访问切片器然后将其删除，最后将工作簿保存为[输出Excel文件](67338477.xlsx)。下面的截图显示了执行示例后将被删除的切片器。

![todo:image_alt_text](removing-slicer_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
