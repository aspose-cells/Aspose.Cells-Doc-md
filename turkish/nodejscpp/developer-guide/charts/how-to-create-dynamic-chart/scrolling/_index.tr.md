---
title: Node.js ile Dinamik Kaydırmalı Grafik nasıl oluşturulur?
linktitle: Dinamik Kaydırmalı Grafik Nasıl Oluşturulur
description: Aspose.Cells for Node.js via C++ kullanarak dinamik kaydırmalı grafik oluşturma adımlarını öğrenin. Adım adım kılavuzumuz, pürüzsüz veri geçişleri ve otomatik kaydırma ile grafiklerinizi sürekli ve güncel tutacak nasıl yapılacağını gösterecek.
keywords: Aspose.Cells for Node.js, Dinamik Kaydırmalı Grafik, Veri Geçişleri, Pürüzsüz Kaydırma, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 75
url: /tr/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik kaydırma grafiği, zamanla değişen verileri göstermek için kullanılan bir grafiksel temsil türüdür. Gerçek zamanlı veri görünümü sağlamak üzere tasarlanmıştır ve kullanıcılara sürekli güncellemeleri ve trendleri takip etme imkanı tanır. Grafik, yeni veri ekledikçe sürekli güncellenir ve en güncel bilgileri göstermek üzere otomatik olarak kaydırılır.

Dinamik kaydırma grafikleri genellikle finans, hisse senedi piyasası analizi, hava durumu takibi ve sosyal medya analitiği gibi çeşitli endüstrilerde kullanılır. Kullanıcıların veri desenlerini görselleştirmelerine ve analiz etmelerine olanak tanır ve gerçek zamanlı bilgilere dayalı bilinçli kararlar almalarını sağlar.

Bu grafikler genellikle etkileşimli olarak tasarlanır, kullanıcının yakınlaştırma yapmasına, tarihli veriler arasında kaydırmasına ve zaman aralıklarını ayarlamasına olanak tanır. Genellikle birden fazla veri serisini destekler, farklı metriklerin ve ilişkilerinin kapsamlı bir görünümünü sunar.

Genel olarak, dinamik kaydırma grafikleri, zaman serisi verilerinin izlenmesi ve analiz edilmesi için değerli araçlardır, gerçek zamanlı karar alma ve veri görselleştirme kapasitelerini geliştirmeye yardımcı olurlar.

## **Aspose.Cells kullanarak Dinamik Kaydırmalı Grafik oluşturun**
Aşağıdaki paragraflarda, Aspose.Cells for Node.js via C++ kullanarak Dinamik Kaydırmalı Grafik nasıl oluşturulacağını göstereceğiz. Örnek kod ve bu kod ile oluşturulan Excel dosyasını da göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Kaydırma Grafik Dosyasını](DynamicScrollingChart.xlsx) oluşturacaktır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Notlar**
Oluşturulan dosyada, kaydırma çubuğunu kullanabilir ve grafik dinamik olarak en son 10 veri kümesini sayar. Bu, örnek kod içinde "OFFSET" formülü kullanılarak yapılır:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

"Sheet1!$H$20" hücresinde "10" sayısını "15" yapmayı deneyebilirsiniz, ve dinamik grafik en son 15 veri kümesini sayacaktır. Artık Aspose.Cells for Node.js via C++ kullanarak başarılı bir şekilde dinamik kaydırmalı grafik oluşturduk.
