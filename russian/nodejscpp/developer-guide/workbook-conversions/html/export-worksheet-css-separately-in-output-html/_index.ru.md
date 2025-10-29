---  
title: Экспорт отдельного CSS листа дляWorksheet в выходной HTML с Node.js через C++  
linktitle: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML  
type: docs  
weight: 80  
url: /ru/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Узнайте, как экспортировать CSS лист worksheet отдельно при конвертации файла Excel в HTML с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**

Aspose.Cells for Node.js via C++ предоставляет функцию экспортирования CSS листа worksheet отдельно при конвертации файла Excel в HTML. Пожалуйста, используйте свойство [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) для этой цели и установите его в **true** при сохранении файла Excel в формат HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий пример создает файл Excel, добавляет текст в ячейку **B5** красным цветом, а затем сохраняет его в формате HTML с использованием свойства [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--). Пожалуйста, смотрите [выходной HTML](60489766.zip), сгенерированный по коду, для ознакомления. Внутри него вы найдете **stylesheet.css** как итог выполнения примера.

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **Экспорт книги с одним листом в HTML**

Когда книга с несколькими листами конвертируется в HTML с помощью Aspose.Cells for Node.js via C++, создается HTML-файл вместе с папкой, содержащей CSS и несколько HTML-файлов. При открытии этого HTML-файла в браузере видны вкладки. То же поведение требуется для книги с одним листом при конвертации в HTML. Ранее для книг с одним листом не создавалась отдельная папка, создавался только HTML-файл, который при открытии в браузере не показывает вкладки. MS Excel также создает отдельную папку и HTML для одного листа, и такое поведение реализовано с помощью API Aspose.Cells. Образец файла можно скачать по следующей ссылке для использования в примере ниже:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
