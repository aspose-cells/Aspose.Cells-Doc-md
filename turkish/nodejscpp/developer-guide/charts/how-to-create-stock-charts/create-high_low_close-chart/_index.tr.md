---  
title: Node.js ile Yüksek Düşük Kapanış (HLC) Stok Grafik Oluşturma  
linktitle: Yüksek Düşük Kapanış (HLC) Hisse Senedi Grafiği Oluştur  
description: Aspose.Cells for Node.js via C++ kullanarak yüksek düşük kapanış stok grafik nasıl oluşturulur, adım adım göstereceğiz. Bu kılavuz, hisse senedi fiyatlarını, yüksek, düşük ve kapanış fiyatlarını grafik üzerinde nasıl göstereceğinizi anlatır.  
keywords: Aspose.Cells for Node.js, Yüksek Düşük Kapanış Stok Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme.  
type: docs  
weight: 181  
url: /tr/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Olası Kullanım Senaryoları**  
Yüksek-Düşük-Kapanış (HLC) stok grafiği, dört sütundan oluşur. Birinci sütun genellikle bir kategori, genellikle bir tarih, ancak hisse senedi isimleri de kullanılabilir. Sonraki üç sütun ise sırasıyla yüksek, düşük ve kapanış fiyatları içindir. Her kategori için fiyat aralığı, düşükten yükseğe doğru dik bir çizgi ile gösterilir ve kapanış fiyatı bu çizginin sağında uzanan bir işaretle gösterilir.  

![todo:image_alt_text](sample.png)  
## **Grafikte görünürlük iyileştirmeleri**  
Grafik daha sezgisel görünmesi için bazen işaretin görünümünü değiştirebilir veya ikincil eksen üzerinde göstermesini sağlayabiliriz.  

![todo:image_alt_text](sample2.png)  
## **Örnek Kod**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

