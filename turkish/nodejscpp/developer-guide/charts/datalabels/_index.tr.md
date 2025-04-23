---  
title: Node.js ile C++ kullanarak Excel Grafiklerinin Veri Etiketlerini Yönetme  
description: Aspose.Cells for Node.js via C++ kullanarak Excel grafiklerindeki veri etiketlerini etkili bir şekilde nasıl yöneteceğinizi öğrenin. Bu kapsamlı kılavuz, etiketleri ekleme, kaldırma ve değiştirme gibi çeşitli yönetim görevlerini kapsar ve grafik okunabilirliğini ve kullanılabilirliğini artırır.  
keywords: Aspose.Cells for Node.js, Excel grafikler, veri etiketleri, yönetim, okunabilirlik, kullanılabilirlik, ekleme, kaldırma, değiştirme.  
linktitle: VeriEtiketleri  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

VeriEtiketleri, bir grafikte önemli bir parçadır.  
Her seri için değeri, yüzdeyi vb. kolayca öğrenebiliriz  

{{% /alert %}}  

## **VeriEtiketleri Seçenekleri**  
Aspose.Cells for Node.js via C++, çalışma zamanında grafiklerin veri etiketlerini yönetmenize izin verir, [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/) nesnesi ile grafiğin veri etiketlerini hareket ettirmek, güncellemek ve biçimlendirmek oldukça basittir.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Grafiğin VeriEtiketlerini Yönetme**  
Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/) ile grafiğin veri etiketlerini yönetmek oldukça basittir.  

Aşağıdaki kod parçacığı, Veri Etiketlerini nasıl yöneteceğinizi gösterir:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Gelişmiş Konular**  
- [Grafiğin Serisinde Veri Noktalarına Özel Etiketler Ekleme](/cells/tr/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Grafiklerin Veri Etiketlerinde Metin Kırpmayı Devre Dışı Bırak](/cells/tr/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Veri Etiket Şeklini Metne Sığacak Şekilde Yeniden Boyutlandır](/cells/tr/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Grafik Noktasının Zengin Metin Özel Veri Etiketi](/cells/tr/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama](/cells/tr/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Veri Etiketleri Olarak Hücre Aralığını Gösterme](/cells/tr/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

