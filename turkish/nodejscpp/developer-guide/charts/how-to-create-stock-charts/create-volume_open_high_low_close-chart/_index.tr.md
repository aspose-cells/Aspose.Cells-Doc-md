---
title: Node.js ve C++ kullanarak Hacim Açık Yüksek Düşük Kapanış (VOHLC) Hisse Senedi Grafiği Oluşturma
description: Aspose.Cells for Node.js via C++ kullanarak hacim açık yüksek düşük kapanış hisse senedi grafiği oluşturmayı öğrenin. Kılavuzumuz, daha iyi analiz ve görselleştirme için hacim, açık, yüksek, düşük ve kapanış fiyatlarını içeren borsa verilerini grafik üzerine nasıl çizeceğinizi gösterecektir.
keywords: Aspose.Cells for Node.js via C++, Hacim Açık Yüksek Düşük Kapanış Hisse Senedi Grafiği, Borsa Verileri, Analiz, Görselleştirme.
type: docs
weight: 184
url: /tr/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
 Dördüncü hisse senedi grafiğimiz Hacim Açık Yüksek Düşük Kapanış grafiği. Yine, verilerin doğru sırada olması gerektiğini tekrar etmek önemlidir. Verilerinizi yeniden düzenlemeniz gerekiyorsa, grafiği kurmadan önce yapmalısınız. Bu grafik, ilk (kategori) sütunundan hemen sonra bir hacim sütunu içerir ve grafikler bu hacmi gösteren bir ana eksende, fiyatlar ise ikincil eksende yer alır.

![todo:image_alt_text](data.png)
## **Hacim-Açılış-Yüksek-Düşük-Kapanış (VAYDK) hisse senedi grafiği**

![todo:image_alt_text](sample.png)
## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](Volume-Open-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
