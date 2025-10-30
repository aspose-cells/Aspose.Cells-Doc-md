---
title: Node.js ile C++ kullanarak X Eksen ve Kategori Eksenleri
linktitle: X Ekseni ve Kategori Ekseni Arasındaki Fark
description: Aspose.Cells for Node.js via C++ te X ekseni ve Kategori ekseninin kullanım ve özellikleri arasındaki farkları nasıl ayırt edeceğinizi öğrenin. Kılavuzumuz, kullanım ve özelliklerdeki farkları anlamanıza ve ihtiyaçlarınıza göre nasıl yapılandıracağınızı gösterecektir.
keywords: Aspose.Cells for Node.js via C++, X ekseni, Kategori ekseni, fark, kullanım, özellikler, yapılandırma.
type: docs
weight: 180
url: /tr/nodejs-cpp/X-axis-vs-category-axis/
---

## **Olası Kullanım Senaryoları**
Farklı türde X ekseni bulunmaktadır. Y ekseni Bir Değer tipi ekseni iken X ekseni Kategori tipi eksen veya Değer tipi eksen olabilir. Değer eksenini kullanarak, veri sürekli değişen sayısal veri olarak işlenir ve işaretçi, numerik değerine göre değişen bir noktaya yerleştirilir. Kategori ekseni kullanarak, veri, sayısal olmayan metin etiketlerinden oluşan bir dizi olarak işlenir ve işaretçi, dizideki konumuna göre eksen boyunca bir noktaya yerleştirilir. Aşağıdaki örnek, Değer ve Kategori Eksenleri arasındaki farkı açıklar.
Örnek verilerimiz [örnek Tablo dosyasında](sample.png) gösterilmektedir. İlk sütun, Kategori veya Değer olarak işleme alınabilen X ekseni verilerimizi içerir. Sayıların eşit aralıklarla dağılmadığına veya hatta sayısal sırayla görünmediğine dikkat edin.

![todo:image_alt_text](sample.png)
## **X ve Kategori eksenini Microsoft Excel gibi ele alın**
İlk grafik XY (Dağılım) grafiği olup X değerleri Eksen olarak kullanılır; ikinci grafik ise çizgi grafik olup X, Kategori Eksenidir.

![todo:image_alt_text](compare.png)
## **Örnek Kod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
