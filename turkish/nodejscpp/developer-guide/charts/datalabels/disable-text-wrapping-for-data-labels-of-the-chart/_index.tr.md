---
title: Node.js ve C++ kullanarak Çizelgedeki Veri Etiketlerinin Metin Kaydırmayı Devre Dışı Bırakmak
description: Aspose.Cells for Node.js via C++ kullanarak çizelgelerde veri etiketleri için metin kaydırmayı nasıl devre dışı bırakacağınızı öğrenin. Rehberimiz, uzun etiketlerin üst üste binmesini önlemeyi ve daha okunabilir ve net çizelge ekranları sağlamayı gösterecek.
keywords: Aspose.Cells for Node.js via C++, çizelgeleme, veri etiketleri, metin kaydırma, üst üste binme, okunabilirlik, ekranlar
type: docs
weight: 70
url: /tr/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013, kullanıcıların Grafik Veri Etiketlerinin içindeki metni kaydırıp kaydırmama seçeneğini sunar. Varsayılan olarak, Grafik Veri Etiketlerinin içindeki metin kaydırılmış durumdadır.

Aspose.Cells, [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) özelliği sağlar, böylece veri etiketlerinin metin kaydırma özelliğini aktif veya devre dışı bırakmak için true veya false olarak ayarlanabilir.

{{% /alert %}}

Aşağıdaki örnek kod, grafik veri etiketlerinin metin kaydırmasını devre dışı bırakmanın nasıl yapıldığını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
