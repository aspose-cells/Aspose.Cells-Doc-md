---
title: FormülText fonksiyonunu Aspose.Cells for Node.js via C++ te kullanma
linktitle: Aspose.Cells te FormulaText Fonksiyonu Kullanma
description: Bu makale, Aspose.Cells kütüphanesinde FormülText fonksiyonunun Microsoft Excel deki formülleri işlemede nasıl kullanılacağını anlatmaktadır. Hücrelerin formül metnini nasıl alıp ayarlayacağınızı ve değiştirilmiş Excel dosyalarını Node.js kullanarak C++ ile kaydetmeyi öğrenin.
keywords: Aspose.Cells, Excel, FormulaText fonksiyonları Node.js ile C++
type: docs
weight: 60
url: /tr/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText, Excel 2013 ve sonrası sürümlerde bulunan bir fonksiyondur. Önceki sürümler, örneğin Excel 2010 veya 2007 gibi, desteklenmemektedir. İsmi gibi, bu fonksiyon belirli bir hücrede bulunan formülün metnini yazdırır. Bu makale, Aspose.Cells for Node.js via C++ kullanarak bu fonksiyonu nasıl kullanacağınızı gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, Aspose.Cells for Node.js via C++ ile FormulaText kullanımını gösterir. Kod önce A1 hücresine bir formül yazar ve ardından A2 hücresinde FormülText kullanarak formül metnini yazdırır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
