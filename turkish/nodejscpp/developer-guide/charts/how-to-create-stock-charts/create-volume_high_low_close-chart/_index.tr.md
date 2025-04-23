---
title: Node.js ve C++ kullanarak Hacim Yüksek Düşük Kapanış (VHLC) Hisse Senedi Grafiği Oluşturma
linktitle: Hacim Yüksek Düşük Kapanış(VYDK) Hisse Senedi Grafiği Oluşturma
description: Aspose.Cells for Node.js via C++ kullanarak hacim yüksek düşük kapanış hisse senedi grafiği oluşturmayı öğrenin. Kılavuzumuz, daha iyi analiz ve görselleştirme için hacim, yüksek, düşük ve kapanış fiyatlarını içeren borsa verilerini grafik üzerine nasıl çizeceğinizi gösterecektir.
keywords: Aspose.Cells for Node.js via C++, Hacim Yüksek Düşük Kapanış Hisse Senedi Grafiği, Borsa Verileri, Analiz, Görselleştirme.
type: docs
weight: 183
url: /tr/nodejs-cpp/create-volume-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
Üçüncü hisse senedi grafiğimiz Hacim Yüksek Düşük Kapanış grafiği olacak. Yine, verilerin doğru sırada olması gerektiğini tekrar etmek önemlidir. Eğer veri tablonuzu yeniden düzenlemeniz gerekiyorsa, grafik kurmadan önce yapmalısınız.
Bu grafikte, ilk (kategori) sütunun hemen ardından bir hacim sütunu bulunur ve grafikler bu hacmi gösteren bir sütun grafiği içerir; fiyatlar ise ikincil eksende yer alır.

![todo:image_alt_text](data.png)
## **Hacim-Yüksek-Düşük-Kapanış (VYDK) hisse senedi grafiği**

![todo:image_alt_text](sample.png)
## **Örnek Kod**
Aşağıdaki örnek kod [örnek Excel dosyasını](Volume-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series(Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
