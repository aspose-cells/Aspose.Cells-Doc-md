---
title: 通过C++和Node.js访问并修改链接Ole对象的显示标签
linktitle: 访问和修改链接的OLE对象的显示标签
type: docs
weight: 100
url: /zh/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: 学习如何使用Aspose.Cells for Node.js via C++访问和修改链接Ole对象的显示标签。 
---

## **可能的使用场景**

Microsoft Excel允许您更改Ole对象的显示标签，如下图所示。您还可以使用Aspose.Cells API和[**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--)属性访问或修改Ole对象的显示标签。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **访问和修改链接的OLE对象的显示标签**

请参见以下示例代码，它加载了包含Ole对象的[sample Excel文件](64716810.xlsx)。代码访问Ole对象并将其标签从Sample APIs更改为Aspose APIs。请查看下面的控制台输出，以了解示例代码对示例Excel文件的效果。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **控制台输出**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
