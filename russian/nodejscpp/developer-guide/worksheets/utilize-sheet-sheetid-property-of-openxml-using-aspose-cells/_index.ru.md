---
title: Используйте свойство Sheet.SheetId библиотеки OpenXml с помощью Aspose.Cells for Node.js via C++
linktitle: Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells
type: docs
weight: 200
url: /ru/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: В этой статье показано, как использовать свойство Sheet.SheetId библиотеки OpenXml программным путем с помощью Aspose.Cells for Node.js via C++.
keywords: ID листа в node.js через C++, ID листа Excel в node.js через C++
---

## **Возможные сценарии использования**

*Sheet.SheetId* доступен внутри модуля *DocumentFormat.OpenXml.Spreadsheet* и является частью OpenXml. Вы можете увидеть это свойство и его значение внутри *workbook.xml*, как показано на следующем скриншоте. Aspose.Cells предоставляет аналогичное свойство как [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Используйте свойство Sheet.SheetId библиотеки OpenXml с помощью Aspose.Cells for Node.js via C++**

В следующем образце кода загружается [образцовый Excel-файл](51740716.xlsx), читается его идентификатор листа или вкладки, затем назначается новый идентификатор вкладки и сохраняется как [выходной файл Excel](51740717.xlsx). Также обратитесь к выводу консоли приведенного ниже кода для справки.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **Вывод в консоль**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
