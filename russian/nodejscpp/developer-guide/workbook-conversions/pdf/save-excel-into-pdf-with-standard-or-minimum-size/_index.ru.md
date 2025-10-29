---
title: Сохраняйте Excel в PDF с помощью стандартного или минимального размера через Node.js с помощью C++
linktitle: Сохранить Excel в формат PDF со стандартным или минимальным размером
type: docs
weight: 340
url: /ru/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Узнайте, как сохранять файлы Excel в формат PDF с использованием стандартного или минимального размера с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

По умолчанию, Aspose.Cells сохраняет Excel в PDF с размером Стандартный. Однако, также можно сохранить с минимальным размером, используя свойство [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--). Оно принимает следующие значения:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Сохраняйте Excel в PDF с помощью стандартного или минимального размера с помощью Aspose.Cells for Node.js via C++**
Следующий пример показывает, как сохранить Excel в PDF с помощью параметра [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) с размером Стандартный или Минимальный.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Load excel file into workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save into Pdf with Minimum size
const opts = new AsposeCells.PdfSaveOptions();
opts.setOptimizationType(AsposeCells.PdfOptimizationType.MinimumSize);

workbook.save(path.join(dataDir, "OptimizedOutput_out.pdf"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
