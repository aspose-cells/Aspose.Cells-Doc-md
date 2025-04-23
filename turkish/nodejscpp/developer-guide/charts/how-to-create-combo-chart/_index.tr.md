---
title: Node.js ve C++ kullanarak Kombine Grafik Oluşturma
linktitle: Kombo Grafik Nasıl Oluşturulur
description: Aspose.Cells for Node.js via C++ kullanarak kombine grafik nasıl oluşturulacağını öğrenin. Kapsamlı kılavuzumuz, farklı grafik türlerini nasıl birleştireceğinizi ve daha etkili veri sunumu için tek bir kombine grafik oluşturmayı gösterecektir.
keywords: Aspose.Cells for Node.js via C++, Kombine Grafik, Grafik Türlerini Birleştirme, Veri Sunumu, Etkili Görselleştirme.
type: docs
weight: 73
url: /tr/nodejs-cpp/create-combo-chart/
---

## **Olası Kullanım Senaryoları**
Excel'deki kombo grafikler, verinizi anlaşılır hale getirmek için iki veya daha fazla grafik türünü kolayca birleştirebileceğiniz bu seçeneği kullanmanızı sağlar. Kombo grafikler, verinizin fiyat ve hacim dahil olmak üzere birden çok türde değeri içerdiğinde yardımcı olur. Ayrıca, veri serilerinizin sayıları seriye göre geniş ölçüde değiştiğinde Kombo grafikler uygundur.
Aşağıdaki veri kümesini örnek olarak alırsak, bu verilerin [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/) 'de bahsedilen verilere oldukça benzer olduğunu gözlemleyebiliriz. Series0'ı "Toplam Gelir" olarak görselleştirmek istiyorsak, bunu bir Çizgi grafiği olarak nasıl yapmalıyız?

![todo:image_alt_text](sample.png)
## **Kombo grafik**
Aşağıdaki kodu çalıştırdıktan sonra, aşağıda gösterildiği gibi Kombo grafiği göreceksiniz.

![todo:image_alt_text](result.png)
## **Örnek Kod**
Aşağıdaki örnek kod [örnek Excel dosyasını](combo.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
