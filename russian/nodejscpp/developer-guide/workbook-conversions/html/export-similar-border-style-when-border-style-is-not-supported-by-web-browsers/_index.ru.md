---  
title: Экспорт похожего стиля границы, когда стиль границы не поддерживается веб браузерами с помощью Node.js через C++  
linktitle: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами  
type: docs  
weight: 70  
url: /ru/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Узнайте, как экспортировать границы, которые не поддерживаются веб браузерами, при преобразовании Excel в HTML с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. При преобразовании такого файла Excel в HTML с помощью Aspose.Cells for Node.js via C++ такие границы будут удалены. Однако Aspose.Cells также может поддерживать отображение таких границ с помощью свойства [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--). Установите его значение в **true**, и неподдерживаемые границы также будут экспортированы в HTML.  

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**  

Следующий пример загружает [образец файла Excel](64716806.xlsx), содержащий некоторые неподдерживаемые границы, как показано на следующем скриншоте. Скриншот дополнительно иллюстрирует эффект свойства [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) внутри [выходного HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

