---  
title: Исключить неиспользуемые стили при конвертации Excel в HTML с помощью Node.js через C++  
linktitle: Исключить неиспользуемые стили во время конвертации Excel в HTML  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Узнайте, как исключить неиспользуемые стили при конвертации Excel в HTML с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Файлы Microsoft Excel могут содержать много неиспользуемых стилей. При экспорте файла Excel в HTML эти неиспользуемые стили также экспортируются, что может увеличить размер HTML. Можно исключить неиспользуемые стили при преобразовании Excel в HTML с помощью свойства [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--). При установке его в **true**, все неиспользуемые стили исключаются из выходного HTML. Следующий скриншот показывает пример неиспользуемого стиля внутри сформированного HTML.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**  

Следующий пример кода создает рабочую книгу и также создает неиспользуемый именованный стиль. Так как [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) установлено в **true**, этот неиспользуемый стиль не будет экспортирован в [выходной HTML](61767778.zip). Но если установить его в **false**, этот неиспользуемый стиль будет присутствовать внутри HTML, что видно в разметке, как показано в предыдущем скриншоте.  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

