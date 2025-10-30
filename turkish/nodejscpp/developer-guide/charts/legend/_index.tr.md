---
title: Node.js kullanarak C++ ile Excel Grafiklerinin Efsane Kontrolü
description: Microsoft Excel de grafik efsanelerini etkin bir şekilde kullanmak ve özelleştirmek için Aspose.Cells for Node.js via C++ ü nasıl kullanacağınızı öğrenin. Kapsamlı rehberimiz, efsanenin işlevselliğini, erişim ve düzenleme yollarını, ayrıca efsanelerle görselleştirmeyi ve veri anlayışını nasıl geliştireceğinizi açıklar.
keywords: Aspose.Cells for Node.js via C++, Grafik Efsaneleri, Microsoft Excel, Görselleştirme, Veri Anlayışı.
linktitle: Açıklama
type: docs
weight: 50
url: /tr/nodejs-cpp/chart-legend/
---

## **Açıklama Seçenekleri**
Aspose.Cells for Node.js via C++, aynı zamanda bir grafiğin efsanesini çalışma zamanında yönetmenize olanak tanır. [Efsane](https://reference.aspose.com/cells/nodejs-cpp/legend/) nesnesi taşınabilir, güncellenebilir ve biçimlendirilebilir.

|![todo:image_alt_text](chart_legend.png)|

## **Grafiğin Açıklamasını Ayarlama**
Aspose.Cells'in [Efsane](https://reference.aspose.com/cells/nodejs-cpp/legend/) ile grafiğin efsanesini yönetmek çok basittir.

Aşağıdaki kod parçacığı, legend yönetimini nasıl yapacağınızı göstermektedir:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

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

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **Gelişmiş Konular**
- [Grafik lejant giriş dolgu metnini hiçbir şeye ayarlayın using Aspose.Cells](/cells/tr/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
