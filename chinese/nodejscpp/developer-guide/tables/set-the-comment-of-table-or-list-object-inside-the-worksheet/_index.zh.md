---
title: 使用Node.js与C++设置工作表中表或列表对象的注释
linktitle: 在工作表内设置表格或列表对象的备注
type: docs
weight: 40
url: /zh/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: 学习如何使用Aspose.Cells for Node.js via C++设置工作表内表或列表对象的注释。 
---

{{% alert color="primary" %}}

你可以使用[**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--)属性设置工作表中表或列表对象的注释，注释将显示在xl/tables/tableName.xml文件中。

{{% /alert %}}

## **设置工作表内表格或列表对象的批注**

以下示例代码加载[源Excel文件](5115514.xlsx)，设置工作表中第一个表格或列表对象的注释。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "table_comment.xlsx"));
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access first list object or table.
const lstObj = worksheet.getListObjects().get(0);
// Set the comment of the list object
lstObj.setComment("This is Aspose.Cells comment.");
// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "SetCommentOfTableOrListObject_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
