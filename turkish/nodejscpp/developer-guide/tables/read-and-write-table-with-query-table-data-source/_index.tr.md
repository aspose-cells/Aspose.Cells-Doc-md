---
title: Query Table Veri Kaynağı ile Tabloyu Okuma ve Yazma (Node.js)
linktitle: Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma
type: docs
weight: 30
url: /tr/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Aspose.Cells for Node.js via C++ kullanarak QueryTable veri kaynağı ile tabloyu nasıl okuyup yazacağınızı öğrenin. 
---

## **Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma**
Aspose.Cells for Node.js via C++ ile, QueryTable'ı veri kaynağı olarak kullanan bir tabloyu okuyabilir ve yazabilirsiniz. Bu özellik, XLS dosyaları için de desteklidir. Aşağıdaki kod örneği, önce tabloyu okuyup sonra toplam satırını ekleyerek böyle bir tabloyu okuma ve yazmayı gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

Kaynak ve çıktı excel dosyaları referans için ekte sunulmuştur.

[Kaynak Dosya](96928091.xls)

[Çıkış Dosyası](96928092.xls)
{{< app/cells/assistant language="nodejs-cpp" >}}
