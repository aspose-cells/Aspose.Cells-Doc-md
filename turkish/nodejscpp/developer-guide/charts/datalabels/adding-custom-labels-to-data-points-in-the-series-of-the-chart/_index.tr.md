---  
title: Node.js ve C++ kullanarak Grafik serilerinde Veriye Özel Etiketler Ekleyin  
linktitle: Grafiğin Serisinde Veri Noktalarına Özel Etiketler Ekleme  
description: Aspose.Cells for Node.js via C++ teki serideki veri noktalarına özel etiketler nasıl eklenir öğrenin. Bu kılavuz, etiketlerin görünümünü, konumunu ve biçimlendirmesini değiştirirken, doğru temsiliyet için onları veri kaynağınıza nasıl bağlayacağınızı gösterecek.  
keywords: Aspose.Cells for Node.js, çizelgeleme, özel etiketler, veri noktaları, seri, görünüm, konum, biçimlendirme, veri kaynağı, temsil  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Bir grafik serisinin veri noktalarına özel etiketler ekleyebilirsiniz. Aspose.Cells, bu özel etiketleri eklemek için [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) özelliğini sağlar. Bu makale, bu özelliği veri noktalarının serisine özel etiketler eklemek için nasıl kullanacağınızı açıklayacaktır.

{{% /alert %}}  

Aşağıdaki kod, **Veri Noktalarıyla Bağlantılı Noktalar Çizgiyle Bağlı Dağılım Çizelgesi** oluşturur ve ardından **Özel Etiketler** ekler. Her özel etiket, **Seri Adı** ve **Nokta Adı** gösterir. İstediğiniz başka bir metin kullanabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

