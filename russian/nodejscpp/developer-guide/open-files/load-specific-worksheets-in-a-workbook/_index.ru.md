---
title: Загрузка определенных листов в книге с помощью Node.js через C++
linktitle: Загрузка конкретных листов в книге
type: docs
weight: 100
url: /ru/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Узнайте, как загружать определенные листы в книге с помощью Aspose.Cells for Node.js via C++. Улучшите производительность и снизьте потребление памяти.
---

{{% alert color="primary" %}}

По умолчанию Aspose.Cells загружает всю электронную таблицу в память. Возможно загрузить только определенные листы. Это может улучшить производительность и потребление памяти. Такой подход полезен при работе с большой рабочей книгой, состоящей из многих рабочих листов.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

Вот реализация класса CustomLoad.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


