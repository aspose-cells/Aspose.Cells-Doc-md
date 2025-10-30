---
title: Node.js ve C++ kullanarak Aralık ile Adres Hücre Sayısı Ofset Tüm Sütun ve Tüm Satır Alma
linktitle: Aralığın Adres Hücre Sayısı Ofset Tüm Sütun ve Tüm Sıra Sayısını Al
type: docs
weight: 330
url: /tr/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Node.js via C++, kullanıcının Excel Aralıklarıyla kolayca çalışmasını sağlayan çeşitli yardımcı yöntemleri olan Range nesnesini sağlar. Bu makale, Range nesnesinin aşağıdaki yöntemleri veya özelliklerinin kullanımını gösterir.

- **Adres**

Aralığın adresini alır.

- **Hücre Sayısı**

Aralıktaki tüm hücre sayısını alır.

- **Ofset**

Ofset ile aralığı alır.

- **Tüm Sütun**

Belirtilen aralığı içeren tüm sütunu (veya sütunları) temsil eden bir Range nesnesi alır.

- **Tüm Satır**

Belirtilen aralığı içeren tüm satırı (veya satırları) temsil eden bir Range nesnesi alır.

## **Aralığın Adresini, Hücre Sayısını, Kaydırmayı, Tüm Sütunu ve Tüm Satırı Al**
Aşağıda verilen örnek kod, yukarıda tartışılan yöntemlerin ve özelliklerin kullanımını açıklar. Referans için aşağıdaki kodun konsol çıktısını inceleyin.

## **Örnek Kod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **Konsol Çıktısı**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
