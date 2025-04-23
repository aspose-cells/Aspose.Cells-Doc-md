---
title: Node.js kullanarak ODS dosyasından Grafik Altbaşlığını C++ aracılığıyla okuma
linktitle: ODS Dosyasından Grafik Altyazısını Oku
description: OpenDocument Spreadsheet (ODS) dosyasından grafik altbaşlığını okumak için Aspose.Cells for Node.js via C++ nasıl kullanılacağını öğrenin. Kılavuzumuz, grafik altbaşlığını çıkarmak ve erişmek için nasıl kullanılacağını gösterecek ve daha fazla analiz veya gösterim için size yardımcı olacaktır.
keywords: Aspose.Cells for Node.js via C++, Grafik Altbaşlığı Oku, OpenDocument Spreadsheet, ODS Dosyası, Grafik Çıkarma, Veri Analizi.
type: docs
weight: 160
url: /tr/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **ODS Dosyasından Grafik Alt Başlığını Okuma**

Aspose.Cells, [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) özelliğini kullanarak ODS dosyalarında grafik altbaşlıklarını okuma yeteneği sağlar. Aşağıdaki örnek kod, [örnek ODS dosyasını](89620481.ods) yükler ve grafik altbaşlığını [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) özelliğiyle okur ve Konsol Penceresine yazdırır. Referans olması için aşağıdaki kodun konsol çıkışını inceleyin.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
