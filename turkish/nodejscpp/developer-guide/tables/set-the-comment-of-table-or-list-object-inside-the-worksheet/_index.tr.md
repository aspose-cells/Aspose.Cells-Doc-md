---
title: Çalışma Sayfası içindeki Tablo veya List Nesnesinin Yorumu Node.js ve C++ ile ayarlama
linktitle: Çalışma Sayfası içinde Masa veya Liste Nesnesi Yorumunu Ayarlayın
type: docs
weight: 40
url: /tr/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma sayfasındaki tablo veya liste nesnesinin yorumunu nasıl ayarlayacağınızı öğrenin. 
---

{{% alert color="primary" %}}

Çalışma sayfasındaki Tablo veya Liste Nesnesinin yorumunu [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--) özelliği kullanarak ayarlayabilirsiniz. Yorum, xl/tables/tableName.xml dosyası içerisinde görünecektir.

{{% /alert %}}

## **Çalışma Sayfası içinde Masa veya Liste Nesnesi Yorumunu Ayarlayın**

Aşağıdaki örnek kod, [kaynak excel dosyasını](5115514.xlsx) yükler, çalışma sayfası içindeki ilk masa veya liste nesnesinin yorumunu ayarlar.

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
