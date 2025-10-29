---  
title: Экспорт диапазона области печати в HTML с помощью Node.js через C++  
linktitle: Экспорт диапазона области печати в HTML  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/export-print-area-range-to/  
---  

## **Возможные сценарии использования**

Это распространенный сценарий, когда необходимо экспортировать только область печати, то есть выбранный диапазон ячеек вместо всей таблицы в HTML. Эта функция уже доступна для рендеринга в PDF; теперь же вы можете выполнить аналогичную задачу и для HTML. Для этого сначала установите область печати в объекте настройки страницы листа, а затем используйте флаг [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) для экспорта только выбранного диапазона.

## Образец кода

Следующий образец кода загружает книгу и затем экспортирует область печати в HTML. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
