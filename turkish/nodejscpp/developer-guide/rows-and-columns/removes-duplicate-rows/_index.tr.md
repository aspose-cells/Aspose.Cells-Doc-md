---
title: Node.js kullanarak C++ ile Çalışma Sayfasında Yinelenen Satırları Kaldırma
linktitle: Çalışma sayfasında tekrarlanan satırları kaldırma
type: docs
weight: 370
url: /tr/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfasında yinelenen satırları nasıl kaldıracağınızı ve hangi sütunların yinelenmeye göre kontrol edilmesi gerektiğini öğrenin.
---


Yinelenen satırları kaldırmak, Microsoft Excel’in birçok kullanışlı özelliklerinden biridir. Bu, kullanıcıların yinelenen satırları kaldırmasına imkan sağlar ve hangi sütunların yinelenen bilgiyi kontrol edeceğini seçebilirsiniz.

Aspose.Cells for Node.js via C++, bunun için `Cells.removeDuplicates()` metodunu sağlar. Ayrıca `startRow`, `startColumn`, `endRow` ve `endColumn` ayarlarıyla yinelenenleri kontrol edilecek alan aralığını belirleyebilirsiniz.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
