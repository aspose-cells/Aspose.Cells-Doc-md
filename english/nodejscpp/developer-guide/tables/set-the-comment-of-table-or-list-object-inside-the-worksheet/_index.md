---
title: Set the Comment of Table or List Object inside the Worksheet with Node.js via C++
linktitle: Set the Comment of Table or List Object inside the Worksheet
type: docs
weight: 40
url: /nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Learn how to set the comment of the table or list object inside the worksheet using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can set the comment of the Table or List Object inside the worksheet using the [**ListObject.setComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#setComment--) method. The comment will be visible inside the xl/tables/tableName.xml file.

{{% /alert %}}

## **Set the Comment of Table or List Object inside the Worksheet**

The following sample code loads the source Excel file, and sets the comment of the first table or list object inside the worksheet.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
