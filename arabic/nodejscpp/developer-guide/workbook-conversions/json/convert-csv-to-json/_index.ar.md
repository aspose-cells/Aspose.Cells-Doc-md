---
title: تحويل CSV إلى JSON باستخدام Node.js عبر C++
linktitle: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/nodejs-cpp/convert-csv-to-json/
description: تحويل ملف CSV إلى JSON باستخدام واجهة برمجة التطبيقات سهلة الاستخدام Aspose.Cells for Node.js via C++.
keywords: تحويل، تحويل CSV إلى JSON، CSV إلى JSON، CSV، JSON، تحويل CSV إلى JSON Node.js عبر C++، كود C++ لتحويل CSV إلى JSON
---

## **تحويل CSV إلى JSON**

تدعم Aspose.Cells تحويل CSV إلى JSON. لهذا الغرض، توفر واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) وواجهة البرمجة [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/). توفر واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) خيارات لتصدير المجال إلى JSON. تحتوي واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) على الخصائص التالية.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): يشير إذا كانت المدى يحتوي على صف رأسي.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): يشير إلى التنسيق.

تقوم الفئة [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) بتصدير JSON باستخدام خيارات التصدير المعينة باستخدام الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/).

يُظهر الكود العيني التالي استخدام واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) وواجهة البرمجة [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) لتحميل [ملف CSV المصدر](104398879.csv) ويطبع الإخراج JSON في وحدة التحكم.

### **الكود المثالي**

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

### **مخرجات الوحدة**
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
