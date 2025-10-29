---  
title: Конвертация Excel в HTML с подсказками с помощью Node.js через C++  
linktitle: Преобразовать Excel в HTML c всплывающей подсказкой  
type: docs  
weight: 200  
url: /ru/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Узнайте, как преобразовать файлы Excel в формат HTML с подсказками для полного отображения текста с помощью Aspose.Cells for Node.js via C++.  
---  

## **Преобразование Excel в HTML со всплывающей подсказкой**

Могут возникнуть случаи, когда текст обрезается в сгенерированном HTML, и вы хотите отображать полный текст в виде подсказки при наведении. Aspose.Cells for Node.js via C++ поддерживает это через свойство [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--). Установка свойства [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) в **true** добавит полный текст как подсказку в сгенерированный HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Следующий пример кода загружает [исходный Excel-файл](98107416.xlsx) и генерирует [выходной HTML-файл](98107417.zip) с подсказкой.

Образец кода

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
