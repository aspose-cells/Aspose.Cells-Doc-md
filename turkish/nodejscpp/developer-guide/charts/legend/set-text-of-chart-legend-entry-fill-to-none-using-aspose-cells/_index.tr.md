---
title: Aspose.Cells for Node.js via C++ kullanarak grafikteki gösterge satırının içeriğini olmayan renge ayarlayın.
linktitle: Grafik lejant giriş dolgu metnini Aspose.Cells kullanarak hiçbir şeye ayarlayın
description: Aspose.Cells for Node.js via C++ kullanarak göstergenin içeriğinin doldurma rengini yok yapmayı öğrenin. Bu kılavuz, Microsoft Excel grafikleri içindeki gösterge satırı içeriğinin dolgusunu nasıl değiştireceğinizi gösterecek ve görselleştirmeyi ve özelleştirmeyi sağlayacaktır.
keywords: Aspose.Cells for Node.js via C++, Grafik Gösterge Satırı Doldurma, Microsoft Excel, Görselleştirme, Özelleştirme.
type: docs
weight: 320
url: /tr/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Grafik gösterge satırı içeriğinin doldurma rengini yok yapmak istiyorsanız, lütfen [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--)’yi **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, grafik efsanesinin ikinci giriş doldurmasını hiçbiri olarak ayarlar. Lütfen bu kodda kullanılan [örnek excel dosyasını](5115219.xlsx) ve bununla oluşturulan [çıktı excel dosyasını](5115217.xlsx) indirin.

Aşağıdaki ekran görüntüsü, bu kodun [örnek Excel dosyası](5115219.xlsx) üzerindeki etkisini vurgulamaktadır.

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
