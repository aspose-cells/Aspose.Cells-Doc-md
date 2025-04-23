---
title: Экспорт комментариев при сохранении файла Excel в HTML с помощью Node.js через C++
linktitle: Экспорт комментариев при сохранении файла Excel в HTML
type: docs
weight: 40
url: /ru/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Возможные сценарии использования**

Когда вы сохраняете файл Excel в HTML, комментарии не экспортируются. Однако Aspose.Cells for Node.js via C++ предоставляет эту функцию с помощью свойства [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). Если установить его в **true**, то HTML также будет отображать комментарии из файла Excel.

## **Экспортировать комментарии при сохранении файла Excel в HTML**

Следующий образец кода объясняет использование свойства [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). На скриншоте показан эффект этого кода на HTML, когда он установлен в **true**. Для справки загрузите [образец Excel файла](50528260.xlsx) и [сгенерированный HTML](5052826.txt).

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
