---
title: Node.js ve C++ kullanarak Excel grafiklerinin başlıklarını yönetme
description: Aspose.Cells for Node.js via C++ kullanarak Microsoft Excel de grafik ve eksen başlıklarını nasıl ekleyeceğinizi ve biçimlendireceğinizi öğrenin. Kılavuzumuz, farklı başlık türleri nasıl ayarlanır, görünüm nasıl değiştirilir ve eksen başlıkları nasıl güncellenir gösterir.
keywords: Aspose.Cells for Node.js via C++, Grafik Başlıkları, Eksen Başlıkları, Microsoft Excel, Veri Temsili, Görünüm.
linktitle: Başlıklar
type: docs
weight: 50
url: /tr/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Excel grafiklerinde 2 türde başlık bulunur:
1. Grafik Başlığı 
1. Eksen Başlıkları

{{% /alert %}}

## **Başlık Seçenekleri**
Aspose.Cells for Node.js via C++ ayrıca grafiğin başlıklarını çalışma zamanında yönetmenize olanak tanır. [Başlık](https://reference.aspose.com/cells/nodejs-cpp/title/) nesnesi ile başlıkların metnini, yazı tipini ve dolgu biçimini değiştirebilirsiniz.

|![todo:image_alt_text](chart_title.png)|

## **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**
Microsoft Excel kullanarak WYSIWYG ortamında grafik ve eksen başlıklarını ayarlayabilirsiniz. Aspose.Cells for Node.js via C++ ayrıca, geliştiricilerin grafik ve eksen başlıklarını çalışma zamanında ayarlamalarına izin verir. Tüm grafikler ve eksenleri, aşağıda bir örnek gösterildiği gibi başlık ayarlarına izin veren [Başlık](https://reference.aspose.com/cells/nodejs-cpp/title/) özelliğine sahiptir.

Aşağıdaki kod örneği, grafik ve eksenlere başlık ayarlamanın yolunu gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Gelişmiş Konular**
- [ODS Dosyasından Grafik Alt Başlığını Okuma](/cells/tr/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
