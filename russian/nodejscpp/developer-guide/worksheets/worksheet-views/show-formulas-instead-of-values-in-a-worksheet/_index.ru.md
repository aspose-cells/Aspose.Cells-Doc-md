---
title: Показать формулы вместо значений в листе с помощью Node.js через C++
linktitle: Показать формулы вместо значений в рабочем листе
type: docs
weight: 20
url: /ru/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: В этой статье представлен пример кода для использования API Node.js через C++, чтобы программно отображать формулы вместо значений в листе или таблице Excel.
---

{{% alert color="primary" %}}

В Microsoft Excel возможно отображать формулы вместо рассчитанных значений с помощью опции **Показать формулы** на ленте **Формулы**. Когда отображаются формулы, Microsoft Excel показывает формулы в листе. Вы можете добиться этого также с помощью Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--). Установите его в **true**, чтобы задать отображение формул в Microsoft Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
