---  
title: Игнорировать ошибки при рендеринге Excel в PDF через Node.js и C++  
linktitle: Игнорировать ошибки при преобразовании Excel в PDF  
type: docs  
weight: 80  
url: /ru/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Узнайте, как игнорировать ошибки во время преобразования файлов Excel в PDF с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

 Иногда при конвертации файла Excel в PDF возникают ошибки или исключения, и процесс конвертации прекращается. Вы можете игнорировать все такие ошибки во время конвертации, используя свойство [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--). Таким образом, процесс конвертации завершится гладко без выброса ошибок или исключений, но возможна потеря данных. Поэтому используйте это свойство только в случае, если потеря данных для вас не критична.  

## **Игнорировать ошибки при преобразовании Excel в PDF**  

Следующий код загружает [образец файла Excel](55541778.xlsx), но этот файл содержит ошибки и вызывает ошибку при [преобразовании в PDF](55541779.pdf) в 17.11. Однако, поскольку мы используем свойство [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--), ошибка не возникает. Однако одна *округлая красная стрелка*, как показано на скриншоте, теряется.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

