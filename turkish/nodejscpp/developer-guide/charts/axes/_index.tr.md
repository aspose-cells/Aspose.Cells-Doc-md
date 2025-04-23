---  
title: Excel Grafiklerinin Eksenlerini Node.js ve C++ ile Yönetin  
description: Aspose.Cells for Node.js via C++ kullanarak grafik eksenlerini nasıl yapılandıracağınızı öğrenin. Bu kılavuz, ana ve ikincil eksenlerin ayarlanmasını, alanlarının belirlenmesini ve özelliklerinin değiştirilmesini gösterecek.  
keywords: Aspose.Cells for Node.js via C++, grafik eksenleri, yapılandırma, ana eksenler, ikincil eksenler, aralık, özellikler.  
linktitle: Eksenler  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

Excel grafiklerinde 3 çeşit eksen bulunmaktadır:  
1. Yatay(Kategori) Eksen: X Eksen  
1. Dikey(Değer) Ekseni: Y Ekseni  
1. Derinlik(Seriler) Ekseni: Z Ekseni  

{{% /alert %}}  

## **Eksen Seçenekleri**  
Aspose.Cells for Node.js via C++, grafiklerin eksenlerini çalışırken yönetmenizi sağlar. [Eksen](https://reference.aspose.com/cells/nodejs-cpp/axis/) nesnesi ile, Excel'de yapıldığı gibi Eksenin tüm seçeneklerini değiştirebilirsiniz.  

|![todo:image_alt_text](chart_axes.png)|  

## **X ve Y Eksenlerini Yönetme**  
Excel grafikte, yatay ve dikey eksenler en popüler iki eksendir.  

Aşağıdaki kod parçacığı, X ve Y eksenlerinin ayarlarını nasıl yapacağınızı gösterir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Gelişmiş Konular**  
- [Tick Etiketi Yönünü Değiştirme](/cells/tr/nodejs-cpp/change-tick-label-direction/)  
- [Grafikte Hangi Eksenin Var Olduğunu Belirleme](/cells/tr/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Grafik Ekseni Otomatik Birimleri ile Başa Çık](/cells/tr/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma](/cells/tr/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Excel Grafikte Kategori Eksenini Nasıl Ayarlayacağınız](/cells/tr/nodejs-cpp/how-to-set-category-axis/)  

