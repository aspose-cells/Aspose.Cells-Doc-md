---
title: Node.js ve C++ kullanarak PivotGrafiği ile PivotOptions yönetimi nasıl yapılır
linktitle: Pivot Seçenekleri
type: docs
weight: 10
url: /tr/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Node.js ve C++ kullanarak PivotOptions ile PivotChart nasıl yönetilir.
keywords: PivotGrafik Node.js ile C++
---
## PivotChart Nedir

Excel'de bir PivotChart, bir PivotTable'dan oluşturulan verilerin grafiksel bir temsilidir. Kullanıcılara verileri dinamik olarak görselleştirmelerine ve analiz etmelerine olanak tanır. Veriyi özetleyerek ve bilgileri grafik formunda göstererek PivotChart'lar etkileşimlidir ve verinin farklı perspektiflerini göstermek için kolayca değiştirilebilir, bu da Excel'de veri analizi ve sunum için güçlü bir araç yapar.

## PivotOptions ile PivotChart'ı Yönetme

Aspose.Cells for Node.js via C++ kullanarak, [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) kullanarak PivotChart yönetebilirsiniz.

Örnek dosya ve kod:
[Örnek Dosya](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

Yukarıdaki örnek kodla sonuç dosyasını kontrol edebilir ve aşağıdaki etkiyi gösteren sonuç dosyasını inceleyebilirsiniz:

**![Çıktı](Output.png)**
