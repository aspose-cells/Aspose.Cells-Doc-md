---
title: Node.js kullanarak Birden Çok Çalışma Sayfasını Tek Bir Çalışma Sayfasına Birleştir
linktitle: Birden Fazla Çalışsayfayı Tek Bir Çalışsayfada Birleştirme
type: docs
weight: 160
url: /tr/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak birden çok çalışma sayfasını tek bir çalışma sayfasına nasıl birleştireceğinizi öğrenin. 
---

{{% alert color="primary" %}} 

Bazen birden fazla çalışsayfayı tek bir çalışsayfada birleştirmeniz gerekebilir. Bu, Aspose.Cells API'sını kullanarak kolayca gerçekleştirilebilir. Bu makale, bir kaynak çalışma kitabını okuyan ve tüm kaynak çalışsayfaların verilerini bir hedef çalışma kitabının içinde tek bir çalışsayfada birleştiren bir kod örneği gösterecektir.

{{% /alert %}} 

Aşağıdaki kod parçacığı, birden fazla çalışsayfayı tek bir çalışsayfada birleştirmenin nasıl yapılacağını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const destWorkbook = new AsposeCells.Workbook();
const destSheet = destWorkbook.getWorksheets().get(0);

let TotalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
const sourceSheet = workbook.getWorksheets().get(i);

const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
const destRange = destSheet.getCells().createRange(
sourceRange.getFirstRow() + TotalRowCount,
sourceRange.getFirstColumn(),
sourceRange.getRowCount(),
sourceRange.getColumnCount()
);

destRange.copy(sourceRange);
TotalRowCount += sourceRange.getRowCount();
}

const outputFilePath = path.join(dataDir, "Output.out.xlsx");
destWorkbook.save(outputFilePath);
``` 
