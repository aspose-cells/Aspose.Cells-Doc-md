---
title: Node.js ile C++ kullanarak Excel dosyasının AutoFill aralığını otomatik doldurun
linktitle: Otomatik Doldurma Aralığı
type: docs
weight: 105
url: /tr/nodejs-cpp/autofill-ranges/
description: Belirli bir aralıkta AutoFill işleminin nasıl gerçekleştirileceğini öğrenin Aspose.Cells for Node.js via C++ kullanarak.
---

## **Belirtilen aralıkta Excel'de otomatik doldurma yapın**

Excel'de, bir aralık seçin, sağ-alt köşeye geçin ve "artı" simgesini sürükleyerek otomatik doldurma yapın.

## **Aspose.Cells for Node.js via C++ ile Otomatik Doldurma Aralıkları**

Aşağıdaki örnek, bir Aralık üzerinde AutoFill işleminin nasıl gerçekleştirileceğini gösterir ve bu özellik için indirilebilecek örnek dosya yer almaktadır:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
