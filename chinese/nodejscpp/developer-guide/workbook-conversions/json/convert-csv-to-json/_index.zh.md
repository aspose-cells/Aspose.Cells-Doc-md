---
title: 使用 Node.js 通过 C++ 将 CSV 转换为 JSON
linktitle: 将CSV转换为JSON
type: docs
weight: 220
url: /zh/nodejs-cpp/convert-csv-to-json/
description: 使用 Aspose.Cells for Node.js via C++ 简单易用的 API 将 CSV 文件转换为 JSON。
keywords: 转换、将 CSV 转为 JSON、CSV 转 JSON、CSV、JSON、通过 C++ 让 Node.js 实现 CSV 转 JSON
---

## **将CSV转换为JSON**

Aspose.Cells 支持将 CSV 转换为 JSON。为此，API 提供了 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) 类。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) 类提供了导出范围到 JSON 的选项。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) 类具有以下属性。

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--)：导出单元格的字符串值给JSON。
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--)：指示范围是否包含标题行。
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--)：表示缩进。

[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)类使用与[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)类设置的导出选项导出JSON。

以下代码示例演示了使用 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) 类加载 [源 CSV 文件](104398879.csv) 并在控制台打印 JSON 输出。

### **示例代码**

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

### **控制台输出**
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
