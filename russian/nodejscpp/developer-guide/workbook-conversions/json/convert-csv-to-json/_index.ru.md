---
title: Конвертировать CSV в JSON с помощью Node.js через C++
linktitle: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/nodejs-cpp/convert-csv-to-json/
description: Конвертировать CSV файл в JSON, используя простое в использовании API Aspose.Cells for Node.js via C++.
keywords: Конвертация, Конвертация CSV в JSON, CSV в JSON, CSV, JSON, Конвертировать CSV в JSON через Node.js с помощью C++, код на C++ для преобразования CSV в JSON
---

## **Преобразовать CSV в JSON**

Aspose.Cells поддерживает преобразование CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) предоставляет параметры экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) имеет следующие свойства.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): Это экспортирует строковое значение ячеек в JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): Это указывает, содержит ли диапазон заголовок строки.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) экспортирует JSON с использованием параметров экспорта, установленных с помощью класса [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/).

Приведенный ниже образец кода демонстрирует использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) для загрузки [исходного файла CSV](104398879.csv) и печати JSON-вывода в консоль.

### **Образец кода**

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

### **Вывод в консоль**
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
