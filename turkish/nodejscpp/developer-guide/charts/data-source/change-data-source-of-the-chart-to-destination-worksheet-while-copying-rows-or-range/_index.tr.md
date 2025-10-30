---
title: Kopyalama sırasında Grafik Veri Kaynağını Hedef Çalışma sayfasına değiştirme Node.js ile C++ kullanarak
linktitle: Satırları veya Aralığı Kopyalarken Grafiklerin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme
description: Aspose.Cells for Node.js via C++ te, satır veya aralık kopyalarken, grafik veri kaynağını hedefine değiştirmeyi öğrenin. Bu kılavuz, grafiğin veri aralığını güncellemeniz ve hedef çalışma sayfasına bağlamanız için size yardımcı olacaktır.
keywords: Aspose.Cells for Node.js via C++, grafik çizimi, veri kaynağı, hedef çalışma sayfası, satırlar, aralık, kopyala, güncelle, veri aralığı, bağlantı.
type: docs
weight: 440
url: /tr/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Olası Kullanım Senaryoları**

Bir yeni çalışma sayfasına grafik içeren satır veya aralıkları kopyaladığınızda, grafiğin veri kaynağı değişmez. Örneğin, grafiğin veri kaynağı `=Sheet1!$A$1:$B$4` ise, satır veya aralık yeni bir çalışma sayfasına kopyalandıktan sonra, veri kaynağı aynı kalır yani `=Sheet1!$A$1:$B$4`. Bu hala eski çalışma sayfasını, yani Sheet1'i gösterir. Bu Microsoft Excel'de de böyle bir davranıştır. Ama yeni hedef çalışma sayfasına refere edecek şekilde ayarlamak isterseniz, lütfen [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) özelliğini kullanın ve çağırırken [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) metodunu **true** olarak ayarlayın. Hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı `=Sheet1!$A$1:$B$4`'ten `=DestSheet!$A$1:$B$4`'e değişecektir.

## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, grafik içeren satır veya aralıkları yeni bir çalışma sayfasına kopyalarken [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) özelliğinin kullanımını açıklamaktadır. Kod, [örnek excel dosyasını](5113699.xlsx) kullanmakta ve [çıktı excel dosyasını](5113697.xlsx) üretmektedir.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
