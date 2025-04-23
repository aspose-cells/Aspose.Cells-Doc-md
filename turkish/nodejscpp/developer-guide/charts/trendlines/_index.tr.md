---
title: Node.js kullanarak C++ üzerinden Grafik Trend Hattının Denklem Metnini Alınması
description: Microsoft Excel de oluşturulan bir grafik trend hattının denkleme metnini almak için Aspose.Cells for Node.js via C++ ü kullanmayı öğrenin. Kılavuzumuz, trend hattının denkleğine erişme ve çıkarma sürecini gösterecektir.
keywords: Aspose.Cells for Node.js via C++, Grafik Trend Hattı, Denklem Metni, Microsoft Excel, Veri Analizi, Görüntüleme.
linktitle: Eğilim Çizgileri
type: docs
weight: 110
url: /tr/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ kullanarak Grafik Trend Hattının Denklem Metnini alabilirsiniz. Aspose.Cells, grafikteki trend hattının denklemini döndüren [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) özelliği sağlar. Bu özelliği kullanmak için önce [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) metodunu çağırmanız gerekir.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, Trend Hattı olan ve Denklemini Kırmızı renk ile gösterilen Grafiği gösterir. Bu metni, aşağıdaki örnek kodda [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) özelliği kullanılarak alacağız.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Node.js kullanarak grafik trend hattının denkleme metnini alma kodu

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
