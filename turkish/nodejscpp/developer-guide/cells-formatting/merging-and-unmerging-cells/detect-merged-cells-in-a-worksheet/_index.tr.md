---
title: Node.js via C++ kullanarak Bir Çalışma Sayfasında Birleştirilmiş Hücreleri Tespit Etme
linktitle: Çalışma sayfasında birleştirilmiş hücreleri tespit et
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfasında birleştirilmiş hücreleri nasıl tespit edeceğinizi öğrenin. Bu makale, kütüphaneyi kullanarak birleştirilmiş hücreleri nasıl tanımlayıp işleyeceğinizi gösterecek.
keywords: Aspose.Cells, Çalışma Sayfası, Hücreleri Birleştir, Tespit Et, Tanımla, İşle Node.js via C++
type: docs
weight: 80
url: /tr/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Bu makale, çalışma sayfasındaki birleştirilmiş hücre alanlarını nasıl alacağınız hakkında bilgi sağlar.

Aspose.Cells for Node.js via C++, bir çalışma sayfasında birleştirilmiş hücre alanlarını almanıza izin verir. Ayrıca bunları ayırabilirsiniz. Bu makale, görevi yerine getirmek için **Aspose.Cells API** kullanarak en basit kodu gösteriyor.

{{% /alert %}}

Bileşen, tüm birleştirilmiş hücreleri alabilen [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) yöntemini sağlar. Aşağıdaki kod örneği, bir çalışma sayfasında birleştirilmiş hücreleri nasıl tespit edeceğinizi gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
