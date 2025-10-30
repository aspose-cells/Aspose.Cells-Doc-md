---
title: Node.js ile C++ kullanarak İşlevsiz Satır ve Sütunları Silme
linktitle: Çalışma Sayfasındaki Boş Satır ve Sütunları Silme
type: docs
weight: 300
url: /tr/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak bir sayfadan tüm boş satır ve sütunları nasıl silebileceğinizi öğrenin. 
---

{{% alert color="primary" %}}

Bir sayfadan boş satır ve sütunların tamamını silebilmek mümkündür. Bu, örneğin, Microsoft Excel dosyasından PDF dosyası oluştururken, yalnızca veri içerip içermeyen satır ve sütunları dönüştürmek istendiğinde faydalıdır.

Boş satır ve sütunları silmek için aşağıdaki Aspose.Cells yöntemlerini kullanın:

1. Boş satırları silmek için [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--) yöntemini kullanın. Silinecek boş satırlar için, [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) sadece doğru olmalıdır, ayrıca bu satırlarda herhangi bir hücre için görünür bir yorum tanımlanmamış olmalı ve bunlarla kesişen bir pivota tablonun olmaması gerekir.
2. Boş sütunları silmek için [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--) yöntemini kullanın.

{{% /alert %}}

## Node.js kullanarak Boş Satırları Silme Kodu

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Node.js kullanarak Boş Sütunları Silme Kodu

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
