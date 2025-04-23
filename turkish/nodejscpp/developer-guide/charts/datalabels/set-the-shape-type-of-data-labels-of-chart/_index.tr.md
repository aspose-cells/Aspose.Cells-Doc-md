---
title: Node.js ve C++ kullanarak Çizelgedeki Veri Etiketlerinin Şekil Türünü Ayarlama
linktitle: Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama
description: Aspose.Cells for Node.js via C++ kullanarak çizelgelerde veri etiketlerinin şekil türünü nasıl ayarlayacağınızı öğrenin. Bu rehber, kullanılabilir farklı şekil türlerini açıklayacak ve veri etiketlerinize uygun şekli seçerek sunumu ve kullanımı artırmayı gösterecek.
keywords: Aspose.Cells for Node.js via C++, grafik çizimi, veri etiketleri, şekil tipleri, sunum, kullanılabilirlik.
type: docs
weight: 110
url: /tr/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Olası Kullanım Senaryoları**
`DataLabels.shapeType` özelliğini kullanarak grafik içindeki veri etiketlerinin şekil tipini değiştirebilirsiniz. Bu, `DataLabelShapeType` enumerasyonunun değerini alır ve veri etiketlerinin şekil tipini buna göre değiştirir. Bazı değerleri şunlardır

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama**
 Aşağıdaki örnek kod, grafik veri etiketlerinin şekil türünü `DataLabelShapeType.WedgeEllipseCallout` olarak değiştirir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](60489778.xlsx) ve onun tarafından oluşturulan [çıktı Excel dosyasını](60489779.xlsx) görün. Ekran görüntüsü, kodun örnek Excel dosyasındaki etkisini göstermektedir.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Örnek Kod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
