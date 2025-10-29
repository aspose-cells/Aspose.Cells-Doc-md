---
title: 使用Node.js通过C++更新切片器
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/nodejs-cpp/updating-slicer/
description: 本文展示了如何通过更新切片器，使用Aspose.Cells for Node.js via C++更新链接的树状图表。
keywords: Aspose.Cells Node.js通过C++，更新切片器，Node.js中如何更改切片器，如何在Node.js中调整切片器，如何通过C++在Node.js中选择或取消选择切片器项。
---

## **可能的使用场景**

如果你想在Microsoft Excel中更新切片器，选择或取消选择其项目，切片器表或数据透视表将相应更新。请使用[**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--)通过Aspose.Cells选择或取消选择切片器项，然后调用[**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--)方法来更新切片器表或数据透视表。

## **如何更新数据透视切片器**

以下示例代码加载包含现有数据透视切片器的[示例 Excel 文件](67338475.xlsx)，取消选择数据透视切片器的第 2 和第 3 个项目，并刷新数据透视切片器，然后将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。如屏幕截图所示，使用选定项目刷新数据透视切片器也已相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
