---
title: Node.js ile C++ kullanarak su basma grafiği nasıl oluşturulur
linktitle: Suş grafik nasıl oluşturulur
type: docs
weight: 160
url: /tr/nodejs-cpp/creating-waterfall-chart/
description: Node.js ve Aspose.Cells for Node.js via C++ kullanarak Excel de su basma grafikleri oluşturma.
keywords: Node.js ve C++ kullanarak Excel de su basma grafiği oluşturma, nasıl oluşturulur, hangi adımlar izlenir.
---

{{% alert color="primary" %}}

Bir su basma grafiği, başlangıç konumunun artıp azalmasını göstermek için kullanılan özel bir grafik türüdür. Microsoft Excel birçok ön tanımlı grafik türüne sahiptir; kolonda, çizgi, pasta, çubuk, radar vb. ama su basma grafiği temel grafiklerin ötesindedir ve mevcut grafik türleri kullanılarak az veya çok özelleştirilerek oluşturulabilir.

{{% /alert %}} 

Aspose.Cells API’leri, çizgi grafiği yardımıyla su basma grafiği oluşturmayı sağlar. API ayrıca, [**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--) ve [**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--) özelliklerini ayarlayarak grafiğin şeklini değiştirme ve su basma şeklini verme özelliğine sahiptir.

Aşağıdaki kod parçası, sıfırdan bir su basma grafiği oluşturmak için Aspose.Cells for Node.js via C++ kullanımını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Retrieve the first Worksheet in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Retrieve the Cells of the first Worksheet
const cells = worksheet.getCells();

// Input some data which chart will use as source
cells.get("A1").putValue("Previous Year");
cells.get("A2").putValue("January");
cells.get("A3").putValue("March");
cells.get("A4").putValue("August");
cells.get("A5").putValue("October");
cells.get("A6").putValue("Current Year");

cells.get("B1").putValue(8.5);
cells.get("B2").putValue(1.5);
cells.get("B3").putValue(7.5);
cells.get("B4").putValue(7.5);
cells.get("B5").putValue(8.5);
cells.get("B6").putValue(3.5);

cells.get("C1").putValue(1.5);
cells.get("C2").putValue(4.5);
cells.get("C3").putValue(3.5);
cells.get("C4").putValue(9.5);
cells.get("C5").putValue(7.5);
cells.get("C6").putValue(9.5);

// Add a Chart of type Waterfall in same worksheet as of data
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Waterfall, 4, 4, 25, 13);

// Retrieve the Chart object
const chart = worksheet.getCharts().get(idx);

// Add Series
chart.getNSeries().add("$B$1:$C$6", true);

// Add Category Data
chart.getNSeries().setCategoryData("$A$1:$A$6");

// Series has Up Down Bars
chart.getNSeries().get(0).setHasUpDownBars(true);

// Set the colors of Up and Down Bars
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Red);

// Make both Series Lines invisible
chart.getNSeries().get(0).getBorder().setIsVisible(false);
chart.getNSeries().get(1).getBorder().setIsVisible(false);

// Set the Plot Area Formatting Automatic
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.Automatic);

// Delete the Legend
chart.getLegend().getLegendEntries().get(0).setIsDeleted(true);
chart.getLegend().getLegendEntries().get(1).setIsDeleted(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## İlgili Makaleler

- [Grafikler Oluşturma](/cells/tr/nodejs-cpp/creating-charts/)
- [Grafikleri Özelleştirme](/cells/tr/nodejs-cpp/customizing-charts/)
