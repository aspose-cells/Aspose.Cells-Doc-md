---
title: C++ aracılığıyla Node.js kullanarak Microsoft Excel Formül İzleme Penceresine Hücre Ekleme
linktitle: Microsoft Excel Formül İzleme Penceresine Hücreler Ekle
description: Aspose.Cells kütüphanesini kullanarak Node.js aracılığıyla C++ da Excel de formül izleme penceresine hücre ekleme. Var olan bir Excel dosyasını yükleyerek veya yeni oluşturarak hücreleri manipüle edebilir ve formüller ayarlayabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, Formül İzleme Penceresi, Hücreler, Ekleme, Node.js C++ aracılığıyla
type: docs
weight: 60
url: /tr/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formüllerini rahatça izlemek için kullanışlı bir araçtır. Excel'de *Formüller > İzleme* penceresine tıklayarak *İzleme Penceresi*ni açabilirsiniz. Bu pencereyi kullanmak için *İzleme Ekle* düğmesi vardır ve bu düğme, inceleme için hücreleri eklemenizi sağlar. Benzer şekilde, [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) yöntemi kullanılarak hücreler *İzleme Penceresi*ne Aspose.Cells API'si kullanılarak eklenebilir.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, C1 ve E1 hücrelerinin formüllerini ayarlar ve her ikisini de İzleme Penceresine ekler. Ardından çalışma kitabını [çıktı Excel dosyası](67338481.xlsx) olarak kaydeder. Çıktı Excel dosyasını açıp *İzleme Penceresi*ni görüntülediğinizde, her iki hücreyi de ekrandaki gibi göreceksiniz.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
