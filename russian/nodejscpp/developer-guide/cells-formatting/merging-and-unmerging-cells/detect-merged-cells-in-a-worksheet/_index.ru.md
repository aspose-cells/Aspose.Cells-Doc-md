---
title: Обнаружение объединённых ячеек в листе с помощью Node.js через C++
linktitle: Обнаружение объединенных ячеек на листе
description: Узнайте, как обнаружить объединённые ячейки в листе с помощью Aspose.Cells for Node.js via C++. В этой статье вы узнаете, как использовать эту библиотеку для определения и работы с объединёнными ячейками.
keywords: Aspose.Cells, Лист, Объединение ячеек, Обнаружение, Идентификация, Работа Node.js через C++
type: docs
weight: 80
url: /ru/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Эта статья предоставляет информацию о том, как получить области объединенных ячеек в рабочем листе.

 Aspose.Cells for Node.js via C++ позволяет получать области объединённых ячеек в листе. Также можно разделять их. В этой статье представлен самый простой код с использованием API **Aspose.Cells** для выполнения этой задачи.

{{% /alert %}}

Компонент предоставляет метод [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--), который может получить все объединённые ячейки. Следующий пример показывает, как обнаружить объединённые ячейки в листе.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
