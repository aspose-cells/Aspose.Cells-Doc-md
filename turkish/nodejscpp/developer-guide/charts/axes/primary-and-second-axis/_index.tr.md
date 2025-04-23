---
title: Node.js ve C++ ile Birincil ve İkincil Eksen
description: Aspose.Cells for Node.js via C++ te birincil ve ikincil eksenleri anlamayı ve bunlarla çalışmayı öğrenin. Kılavuzumuz, birincil ve ikincil eksenler arasındaki farkları nasıl anlayacağınızı ve bunları verimli bir şekilde nasıl yapılandırıp kullanacağınızı gösterecek.
keywords: Aspose.Cells for Node.js via C++, temel eksenler, ikincil eksenler, anlama, farklar, yapılandırma, kullanım.
type: docs
weight: 190
url: /tr/nodejs-cpp/primary-and-second-axis/
---

## **Olası Kullanım Senaryoları**
Bir grafikte veri serilerinden veri serilerine geniş bir değişkenlik olduğunda veya karışık tiplerde veri (fiyat ve hacim) olduğunda, bir veya daha fazla veri serisini ikincil dikey (değer) ekseninde grafiğe plotlayın. İkincil dikey eksenin ölçeği, ilişkili veri serileri için değerleri gösterir. İkincil bir eksen, sütun ve çizgi grafiklerinin bir kombinasyonunu gösteren bir grafikte iyi çalışır.

## **Birincil ve İkinci Ekseni Microsoft Excel gibi ele alın**
Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına yerleştiren örnek kodu aşağıda inceleyiniz. 
Ardından bir grafik ekleriz ve ikinci ekseni gösteririz.

![todo:image_alt_text](excel.png)

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

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
