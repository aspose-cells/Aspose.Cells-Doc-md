---
title: Node.js ve C++ ile Çizelge Noktası için Zengin Metinli Özelleştirilmiş Veri Etiketi
description: Aspose.Cells for Node.js via C++ te çizelge noktaları için zengin metinli özel veri etiketleri eklemeyi öğrenin. Rehberimiz, farklı fontlar, renkler ve hizalama seçenekleriyle etiketleri biçimlendirme yollarını gösterecek, böylece çizelgelerinizin görünümünü ve okunabilirliğini artıracaksınız.
keywords: Aspose.Cells for Node.js via C++, çizelgeleme, zengin metin, özel veri etiketleri, fontlar, renkler, hizalama, görünüm, okunabilirlik
type: docs
weight: 10
url: /tr/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak çizelge noktaları için zengin metinli özel veri etiketleri oluşturabilirsiniz. Aspose.Cells, [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) metodunu sağlar, bu da [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) nesnesini döndürür ve bu nesne, metnin renk, kalınlık gibi yazı tipi özelliklerini ayarlamak için kullanılabilir.

{{% /alert %}}

## Grafiğin Noktasının Zengin Metin Özel Veri Etiketi

Aşağıdaki kod, ilk serinin ilk grafik noktasına erişir, metnini ayarlar ve ardından ilk 10 karakterin fontunu kırmızıya ayarlar ve kalınlığı **true** yapar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
