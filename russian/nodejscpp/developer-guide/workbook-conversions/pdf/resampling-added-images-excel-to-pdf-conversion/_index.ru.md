---
title: Повторное изменение размера добавленных изображений — преобразование Excel в PDF с помощью Node.js через C++
linktitle: Повторное изменение размера добавленных изображений
type: docs
weight: 150
url: /ru/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Узнайте, как сжать изображения, добавленные в файлы Excel, чтобы уменьшить размер PDF и повысить производительность преобразования с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

При работе с большими файлами Excel с множеством изображений, возможно потребуется сжать изображения, чтобы уменьшить размер итогового файла PDF и повысить общую производительность преобразования. Aspose.Cells for Node.js via C++ поддерживает повторное изменение размера добавленных изображений для уменьшения размера PDF и повышения производительности.

{{% /alert %}}

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, описывающим, как выполнить задачу с использованием API Aspose.Cells. В примере происходит преобразование файла Microsoft Excel в файл PDF с одновременным сжатием изображений в файле.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

Использование опции [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) минимизирует размер выходного PDF, но может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
