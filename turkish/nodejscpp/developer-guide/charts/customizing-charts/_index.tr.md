---  
title: Node.js kullanarak C++ ile Grafikler Özelleştirme  
linktitle: Grafikleri Özelleştirme  
description: Aspose.Cells for Node.js via C++ te grafiklerin nasıl özelleştirileceğini öğrenin. Kılavuzumuz, grafik düzenlerinin nasıl değiştirileceğini, veri serilerinin nasıl eklenip biçimlendirileceğini, eksenlerin nasıl ayarlanacağını ve çeşitli biçimlendirme seçeneklerinin nasıl uygulanacağını gösterecek.  
keywords: Aspose.Cells for Node.js via C++, grafik oluşturma, özelleştirme, düzenler, veri serileri, eksenler, biçimlendirme, görünüm, kullanılabilirlik.  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/customizing-charts/  
---  


## **Özel Grafikler Oluşturma**  

Şimdiye kadar, grafikler hakkında konuşurken, standart biçimlendirme ayarlarına sahip olan temel grafiklere baktık. Sadece veri kaynağını tanımlar, birkaç özelliği ayarlar ve grafik varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilerin kendi biçimlendirme ayarlarıyla grafikler oluşturmasına izin veren özel grafikler oluşturmayı da destekler.  

Geliştiriciler, Aspose.Cells kullanarak çalışma zamanında özel grafikler oluşturabilirler.  

Bir grafik, bir veri serisinden oluşur. Aspose.Cells'te her veri serisi, bir [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) nesnesiyle temsil edilir, oysa [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) nesnesi, [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) nesnelerinin bir koleksiyonudur. Özel grafik oluştururken, geliştiriciler [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) nesnesinde toplanan farklı veri serileri için farklı grafik türleri kullanma özgürlüğüne sahiptir.  

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

 Şu anda, Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığın grafiklerini birleştiren özel grafiklere destek sağlar. Ancak, gelecekteki sürümlerde daha fazla grafik desteklenecektir.  

{{% /alert %}}  

