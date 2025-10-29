---
title: Различные способы открытия файлов с помощью Node.js через C++
linktitle: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/nodejs-cpp/different-ways-to-open-files/
description: В этой статье объясняется, как открыть файл Excel с помощью API Aspose.Cells for Node.js via C++.
keywords: Открытие файла Excel в Node.js без Excel, как открыть файл Excel с помощью Node.js.
---

{{% alert color="primary" %}}

С Aspose.Cells легко открыть файлы, например, для получения данных или использования шаблона дизайнера для ускорения процесса разработки.

{{% /alert %}}

## **Как открыть файл Excel через путь**

Разработчики могут открыть файл Microsoft Excel, указав его путь на локальном компьютере, с помощью конструкции [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Просто передайте путь в конструктор как *строку*. Aspose.Cells автоматически определит тип формата файла.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Как открыть файл Excel через поток**

Также просто открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, которая принимает объект *Stream*, содержащий файл.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Как открыть файл только с данными**

Чтобы открыть файл только с данными, используйте классы [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) и [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter), чтобы установить соответствующие атрибуты и параметры классов для загрузки файла-шаблона.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Как загрузить только видимые листы**

При загрузке [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) иногда требуется загрузить только данные в видимых листах рабочей книги. Aspose.Cells позволяет пропускать данные в невидимых листах при загрузке книги. Для этого создайте пользовательскую функцию, наследующуюся от класса [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter), и передайте ее экземпляр в свойство [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Вот реализация класса *CustomLoad*, упомянутого в приведенной выше части кода.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Если вы попробуете открыть не нативные файлы Excel или другие форматы файлов (например, PPT/PPTX, DOC/DOCX и т. д.) с помощью Aspose.Cells, будет выброшено исключение.

{{% /alert %}} 

{{% alert color="primary" %}}

Есть хорошие шансы, что конструктор [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) может выбросить *OutOfMemoryError* при загрузке больших таблиц. Это исключение означает, что доступной памяти недостаточно для полной загрузки таблицы в память; поэтому таблица должна загружаться с включенными настройками памяти.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
