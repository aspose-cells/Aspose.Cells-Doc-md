---
title: Worksheet te Sorgu Tablosu Okuma ve Yazma ile Node.js kullanımı
linktitle: Çalışsaydı, Çalışma Sorgusu Tablosu Okuma ve Yazma
type: docs
weight: 40
url: /tr/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells, İçerikSorgusunu döndüren Worksheet.QueryTables koleksiyonunu sağlar. Bu koleksiyon bir endekse göre QueryTable türünde bir nesne döndürür. Aşağıdaki iki özelliğe sahiptir

- SorguTablosu. sütun genişliğini ayarla
- SorguTablosu.formatlamayı koru

Bunlar her ikisi de Boolean değerlerdir. Bunları Microsoft Excel'de Veri > Bağlantılar > Özellikler menüsünde görebilirsiniz.

{{% /alert %}}

## Çalışsayfa Sorgu Tablosu Okuma ve Yazma

Aşağıdaki örnek kod, ilk çalışma sayfasındaki ilk SorguTablosu'nu okur ve her ikisi de olan QueryTable özelliklerini yazdırır. Daha sonra, QueryTable.preserveFormatting özelliğini true yapar.

Bu kodda kullanılan kaynak Excel dosyasını ve kod tarafından oluşturulan çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

- [Kaynak Excel Dosyası](5115533.xlsx)
- [Çıktı Excel Dosyası](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Konsol Çıktısı

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Sorgu tablosu sonuç aralığını alın

Aspose.Cells, bir sorgu tablosu için hücrelerin adresini yani sonuç aralığını okuma seçeneği sağlar. Aşağıdaki kod, bir sorgu tablosunun sonuç aralığının adresini okuyarak bu özelliği göstermektedir. Örnek dosyayı [buradan](72417290.xlsx) indirebilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
