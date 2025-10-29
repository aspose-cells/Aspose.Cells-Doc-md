---
title: تعيين تعليق للجدول أو كائن القائمة داخل ورقة العمل باستخدام Node.js عبر C++
linktitle: ضبط التعليق للجدول أو كائن القائمة داخل ورقة العمل
type: docs
weight: 40
url: /ar/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: تعلم كيف تعيين تعليق للجدول أو كائن القائمة داخل ورقة العمل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يمكنك تعيين تعليق للجدول أو كائن القائمة داخل ورقة العمل باستخدام خاصية [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--). سيكون التعليق مرئيًا داخل ملف xl/tables/tableName.xml.

{{% /alert %}}

## **ضبط التعليق للجدول أو كائن القائمة داخل ورقة العمل**

يحمل كود العينة التالي [ملف إكسل مصدر](5115514.xlsx)، ويضبط التعليق لأول جدول أو كائن قائمة داخل ورقة العمل.

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
