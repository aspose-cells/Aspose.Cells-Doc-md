---
title: Node.js ile C++ kullanarak Chart.SetChartDataRange metodu ile Grafik Kurulumu için Kolay Yöntem
linktitle: Chart.SetChartDataRange yöntemini kullanarak Kolay Grafik Kurulumu
description: Aspose.Cells for Node.js via C++ te, Chart.SetChartDataRange metodunu kullanarak grafiklerin nasıl kolayca kurulacağını öğrenin. Kılavuzumuz, grafiğiniz için veri aralığını belirlemenize yardımcı olur ve profesyonel ve doğru grafikler oluşturmanıza olanak tanır.
keywords: Aspose.Cells for Node.js via C++, grafik çizimi, SetChartDataRange metodu, veri aralığı, profesyonel, doğru, grafikler.
type: docs
weight: 190
url: /tr/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cells artık grafikleri kolayca kurmak için [**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-) yöntemi sağlar. Bu yöntemi kullanarak, artık seri ve kategori ekseni verilerini ayrı ayrı eklemeniz gerekmez.

{{% /alert %}}

Aşağıdaki örnek kod, grafiği kolayca kurmak için [**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-) metodunun nasıl kullanılacağını açıklar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for chart

// Category Axis Values
worksheet.getCells().get("A2").putValue("C1");
worksheet.getCells().get("A3").putValue("C2");
worksheet.getCells().get("A4").putValue("C3");

// First vertical series
worksheet.getCells().get("B1").putValue("T1");
worksheet.getCells().get("B2").putValue(6);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("B4").putValue(2);

// Second vertical series
worksheet.getCells().get("C1").putValue("T2");
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(2);
worksheet.getCells().get("C4").putValue(5);

// Third vertical series
worksheet.getCells().get("D1").putValue("T3");
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(4);
worksheet.getCells().get("D4").putValue(2);

// Create Column chart with easy way
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Column, 6, 5, 20, 13);
const ch = worksheet.getCharts().get(idx);
ch.setChartDataRange("A1:D4", true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
