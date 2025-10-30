---
title: Node.js ve C++ kullanarak Seriyi görünmez yapma nasıl yapılır
linktitle: Seriyi görünmez yapma
description: Excel grafiğinde seriyi görünmez yapmayı Aspose.Cells for Node.js via C++ kullanarak öğrenin. 
keywords: Excel grafik, Seri, Görünmez, IsFiltered Node.js ve C++ kullanımı.
type: docs
weight: 74
url: /tr/nodejs-cpp/how-to-set-series-invisible/
---

## Excel Grafiğinde Seriyi görünmez yapma

Excel grafiğinde, bir grafiğe sağ tıklayın, "Veri Seç"e tıklayın ve açılan pencerede, seriyi görünür olup olmadığını işaretleyerek veya işareti kaldırarak ayarlayabilirsiniz. Aşağıdaki [örnek dosyayı](SeriesFiltered.xlsx) indirebilir ve figürde gösterildiği gibi Excel'de kullanarak bu fonksiyonu gerçekleştirebilirsiniz. Şimdi, bunu Aspose.Cells kütüphanesini kullanarak nasıl yapacağınızı anlatacağız.

![todo:image_alt_text](series-invisible.png)

## Aspose.Cells kullanarak seriyi görünmez yapma 

Aspose.Cells kullanarak seriyi görünmez yapmak için aşağıdaki kodu kullanıyoruz:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Aşağıdaki [girdi dosyasını](SeriesFiltered.xlsx) ve [çıktı dosyasını](output.xlsx) edinebilirsiniz.

Aşağıdaki şekilde gösterildiği gibi, orijinalde görünür olan ilk iki seri, çıktı dosyasında görünmez hale geldi.
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
