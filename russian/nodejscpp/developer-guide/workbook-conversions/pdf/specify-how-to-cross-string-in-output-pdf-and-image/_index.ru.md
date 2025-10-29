---  
title: Укажите, как перекрестить строку в выходном PDF и изображении с помощью Node.js через C++  
linktitle: Указание того, как пересекать строку в выходном PDF и изображении  
type: docs  
weight: 120  
url: /ru/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Научитесь управлять переполнением текста в выходном PDF/изображении, указывая тип перекрестка с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, строка переполняется, если следующая ячейка в следующем столбце равна null или пустая. При сохранении файла Excel в PDF/изображение вы можете контролировать это переполнение, задавая тип перекрестка с помощью перечисления [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Оно имеет следующие значения:

- **TextCrossType.Default**: отображение текста как в MS Excel, зависящее от следующей ячейки. Если следующая ячейка равна null, строка переполняется или обрезается.

- **TextCrossType.CrossKeep**: отображать строку как в MS Excel при экспорте в PDF/изображение.

- **TextCrossType.CrossOverride**: отображать весь текст, пересекающий другие ячейки, и переопределять содержимое пересекаемых ячеек.

- **TextCrossType.StrictInCell**: Отображать только строку в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

Следующий пример загружает пример файла Excel и сохраняет его в формате PDF/изображение, задавая разные [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Образец файла Excel и выходные файлы можно скачать по ссылкам ниже:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Образец кода

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
