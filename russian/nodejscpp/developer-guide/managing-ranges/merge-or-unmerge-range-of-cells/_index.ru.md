---
title: Объединить или разъединить диапазон ячеек с помощью Node.js через C++
linktitle: Объединение или разъединение диапазона ячеек
type: docs
weight: 190
url: /ru/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Объединить и разъединить ячейки в диапазоне в Excel с помощью Node.js через C++ код.
keywords: Объединение и разъединение ячеек в диапазоне с помощью Node.js, объединение и разъединение ячеек в диапазоне, объединение и разъединение ячеек в диапазоне с помощью Node.js, объединение и разъединение ячеек в диапазоне с использованием Node.js, объединение и разъединение ячеек в Excel с помощью Node.js, объединение и разъединение ячеек в Excel с помощью Node.js, Node.js объединение и разъединение ячеек в Excel, Node.js объединение ячеек в Excel, Node.js разъединение ячеек в Excel, объединение ячеек в диапазоне с помощью Node.js
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для объединения или разделения диапазона ячеек. Aspose.Cells предоставляет методы [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) и [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) для этой цели. В этой статье объясняется, как объединить диапазон ячеек в одну ячейку.

{{% /alert %}}

## **Пример**

Следующий пример кода сначала создает диапазон - A1:D4 - затем объединяет ячейки в диапазоне в одну с помощью метода [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--). Аналогично, можно разбить ячейки, создав диапазон и вызвав метод [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
