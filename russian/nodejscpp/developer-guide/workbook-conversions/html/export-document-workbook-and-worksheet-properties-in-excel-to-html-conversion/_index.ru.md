---  
title: Экспорт свойств документа, рабочей книги и листа в преобразовании Excel в HTML с помощью Node.js через C++  
linktitle: Экспорт свойств документа, книги и листа Excel в HTML  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Узнайте, как экспортировать свойства документа, рабочей книги и листа в Excel в HTML с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Когда файл Microsoft Excel экспортируется в HTML с помощью Microsoft Excel или Aspose.Cells for Node.js via C++, также экспортируются различные свойства документа, рабочей книги и листа, как показано на следующем скриншоте. Вы можете избежать экспорта этих свойств, установив [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) и [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) в **false**. Значения по умолчанию - **true**. Следующий скриншот показывает, как выглядят эти свойства в экспортированном HTML.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Экспорт свойств документа, книги и листа Excel в HTML**  

Следующий пример кода загружает [пример файла Excel](61767776.xlsx) и преобразует его в HTML без экспорта свойств документа, рабочей книги и листа в [выходной HTML](61767779.zip).  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
