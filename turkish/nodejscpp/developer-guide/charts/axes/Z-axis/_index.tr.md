---
title: Node.js ile C++ kullanarak Z Eksen
description: Aspose.Cells for Node.js via C++ te Z ekseni ile çalışma hakkında bilgi edinin. Kılavuzumuz, Z eksenini yapılandırma ve özelleştirme, ölçekte ve etiketlerde dahil olmak üzere, grafikleri geliştirmek için size yardımcı olacaktır.
keywords: Aspose.Cells for Node.js via C++, Z ekseni, grafik oluşturma, yapılandırma, özelleştirme, ölçek, etiketler.
type: docs
weight: 210
url: /tr/nodejs-cpp/z-axis/
---

## **Olası Kullanım Senaryoları**
3D sütun, 3D koni veya 3D piramit gibi derinliğe (seri) sahip 3D grafikler için, Z ekseni olarak da bilinen bir derinlik ekseninin ayarlanabileceği özellikler. İşaretçilerin veya etiketlerin arasındaki aralığı belirleyebilirsiniz.

## ** Microsoft Excel gibi Birincil ve İkincil Eksenleri Yönetme**
 Lütfen ilk grafik verilerini ve grafiğin ilk çalışma sayfasına yerleştirildiği örnek kodu inceleyiniz. Ardından, grafiği ekleyin ve grafik türünü Column3D olarak ayarlayın, böylece Z Ekseninin, Derinlik Ekseninin de gözüktüğünü görebilirsiniz. 

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
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
