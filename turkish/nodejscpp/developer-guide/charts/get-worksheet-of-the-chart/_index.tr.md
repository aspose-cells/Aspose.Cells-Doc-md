---
title: Node.js ile C++ kullanarak Grafik Sayfasını Erişme
linktitle: Grafik Çalışsayısını Al
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel grafiğine ait çalışma sayfasını nasıl alacağınızı öğrenin. Grafiklerin temel verilerini verimli bir şekilde erişip manipüle edin.
keywords: Aspose.Cells for Node.js, Excel grafikler, çalışma sayfaları, veri manipülasyonu, temel veriler, işlemler, Node.js via C++
type: docs
weight: 1000
url: /tr/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, grafik referansından bir çalışsayısına erişmek istersiniz. Aspose.Cells, grafiği içeren çalışsayısının referansını döndüren [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki örnek, [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) özelliğinin nasıl kullanılacağını gösterir. Kod önce çalışma sayfasının adını yazdırır, ardından sayfa üzerindeki ilk grafiğe erişir. Sonra tekrar çalışma sayfası adını, [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) özelliği kullanarak yazar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

Örnek kodun sonucunda ortaya çıkan konsol çıktısı aşağıda verilmiştir. Görebileceğiniz gibi, aynı çalışsayı adını her iki seferde de yazdırır.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
