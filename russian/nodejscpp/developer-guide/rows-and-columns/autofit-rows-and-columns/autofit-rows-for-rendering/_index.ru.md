---  
title: Автоподгонка строк для отображения с помощью Node.js через C++  
linktitle: Автонастройка строк для визуализации  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/autofit-rows-for-rendering/  
description: Узнайте, как автоподогнать строки для отображения в Excel с помощью Aspose.Cells for Node.js via C++. Предотвратите обрезку текста при сохранении в PDF.  
---  

Обычно, чтобы отображать весь текст в ячейке, можно автоподогнать строку в нормальном режиме с масштабом 100% в Microsoft Excel. Это позволяет полностью видеть текст в обычном режиме, а при печати или сохранении файла как PDF текст отображается правильно.

Однако в некоторых случаях автоподгонка строки хорошо работает в нормальном режиме, но при переключении на режим печати или сохранении файла как PDF, текст обрезается. Проверьте исходный файл [Book1.xlsx](Book1.xlsx) и скриншоты.

![текст обрезан в виде для печати](text_clipped_in_printview.png)

Если хотите предотвратить обрезку текста при сохранении PDF, то можно автоподогнать строку с помощью опции [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

Теперь текст не обрезается в сохраненном файле PDF.

![текст не обрезается в сохраненном pdf](text_not_clipped_in_saved_pdf.png)  
