---
title: Node.js aracılığıyla C++ kullanarak CSV den JSON a dönüştür
linktitle: CSV den JSON a Dönüştürme
type: docs
weight: 220
url: /tr/nodejs-cpp/convert-csv-to-json/
description: Aspose.Cells for Node.js via C++ API sini kullanarak CSV dosyasını JSON a dönüştürün.
keywords: Dönüştür, CSV yi JSON a dönüştür, CSV, JSON, Node.js aracılığıyla C++ kullanarak CSV yi JSON a dönüştür
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'nin JSON'a dönüştürülmesini destekler. Bunun için API, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) sınıfı, JSON'a dönüştürmek için aralık ihracatı için seçenekler sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) sınıfında aşağıdaki özellikler bulunmaktadır.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Sekme boşluğunu belirtir.

[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) sınıfı, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) sınıfı ile belirlenen dışa aktarma seçeneklerini kullanarak JSON'u dışa aktarır.

Aşağıdaki kod örneği, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) sınıflarını kullanarak [kaynak CSV dosyasını](104398879.csv) yükler ve konsolda JSON çıktısını yazdırır.

### **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Load CSV file
const filePath = path.join(sourceDir, "SampleCsv.csv");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);
const lastCell = workbook.getWorksheets().get(0).getCells().getLastCell();

// Set JsonSaveOptions
const jsonSaveOptions = new AsposeCells.JsonSaveOptions();
const range = workbook.getWorksheets().get(0).getCells().createRange(0, 0, lastCell.getRow() + 1, lastCell.getColumn() + 1);
const data = AsposeCells.JsonUtility.exportRangeToJson(range, jsonSaveOptions);

// Print JSON
console.log(data);
```

### **Konsol Çıktısı**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
