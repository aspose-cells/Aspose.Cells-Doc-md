---
title: Установить комментарий таблицы или списка внутри листа с помощью Node.js и C++
linktitle: Установите комментарий к таблице или объекту списка внутри листа
type: docs
weight: 40
url: /ru/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Узнайте, как установить комментарий для таблицы или списка внутри листа с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Вы можете установить комментарий для таблицы или списка внутри листа, используя свойство [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--). Комментарий будет отображаться внутри файла xl/tables/tableName.xml.

{{% /alert %}}

## **Установите комментарий таблицы или объекта списка внутри листа.**

Нижеприведенный образец кода загружает [исходный файл Excel](5115514.xlsx), устанавливает комментарий для первой таблицы или объекта списка на листе.

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
