---
title: Node.js ile C++ üzerinden Çalışma Sayfasını Gizleme ve Sıfırlama
linktitle: Çalışma Taşraflarındaki Sıfır Değerlerinin Gizlenmesi
type: docs
weight: 50
url: /tr/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Bu makale, Node.js kütüphanesi kullanılarak Excel elektronik tablosundaki sıfır değerlerin programatik olarak nasıl gizleneceğine dair örnek kod açıklamalarını gösterecektir.
keywords: Node.js ve C++ kullanarak Excel çalışma sayfasını gizle
---

{{% alert color="primary" %}} 

Bazen çalışma taşrasındaki sıfır değerlerini gizlemeniz gerekir. Bu kişisel tercih veya biçimlendirme standardı olabilir.

{{% /alert %}} 

Microsoft Excel'de bir çalışma taşrasındaki sıfır değerlerini gizlemek için (örneğin Microsoft Excel 2003):

1. **Araçlar** menüsünden **Seçenekler**'i seçin, ardından **Görünüm** sekmesini seçin.
1. **Sıfır değerleri** seçeneğini kaldırın.
1. **Tamam**'a tıklayın.

Aspose.Cells for Node.js via C++ kullanarak sıfırları gizlemeyi gösteren aşağıdaki örnek kodlara bakın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
