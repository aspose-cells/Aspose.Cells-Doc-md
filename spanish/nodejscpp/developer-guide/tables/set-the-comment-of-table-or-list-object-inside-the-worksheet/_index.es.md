---
title: Configurar el Comentario de una Tabla u Objeto de Lista dentro de la Hoja de cálculo con Node.js a través de C++
linktitle: Establecer el comentario de una tabla o un objeto de lista dentro de la hoja de cálculo
type: docs
weight: 40
url: /es/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Aprenda cómo configurar el comentario de la tabla u objeto de lista dentro de la hoja de cálculo usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puede establecer el comentario de la Tabla u Objeto de Lista dentro de la hoja de cálculo usando la propiedad [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--). El comentario será visible dentro del archivo xl/tables/tableName.xml.

{{% /alert %}}

## **Establecer el Comentario de la Tabla o Objeto de Lista dentro de la Hoja de Cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de origen](5115514.xlsx), establece el comentario de la primera tabla u objeto de lista dentro de la hoja de cálculo.

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
