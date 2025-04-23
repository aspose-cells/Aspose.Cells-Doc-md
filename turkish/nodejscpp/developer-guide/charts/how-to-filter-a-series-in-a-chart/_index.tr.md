---
title: Node.js ve C++ kullanarak Grafik Verilerini filtreleme için Üç Yöntem
linktitle: Grafik Verisini Filtreleme İçin Üç Yöntem
description: Excel de grafikleri filtrelemeyi, Aspose.Cells for Node.js via C++ kullanarak öğrenin. Kapsamlı rehberimiz, grafiklere filtre uygulama, grafik elemanlarını özelleştirme ve daha iyi içgörüler ve bilinçli kararlar için veri analizi araçlarını kullanma yollarını gösterecek.
keywords: Aspose.Cells for Node.js via C++, Excel de Grafik Filtreleme, Veri Analizi, Karar Verme, Görselleştirme.
type: docs
weight: 2210
url: /tr/nodejs-cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Bir grafik oluşturmak için serileri filtreleme**

### **Excel'de bir grafikten serileri filtreleme adımları**
Excel'de, belirli serileri grafikten çıkarabiliriz, bu da o serilerin grafikte gösterilmeyeceği anlamına gelir. Orijinal grafiği **Şekil 1**'de gösterilmiştir. Ancak, **Testserisi2** ve **Testserisi4**'ü filtrelediğimizde, grafik aşağıdaki gibi görünecektir, **Şekil 2**.

Aspose.Cells for Node.js via C++'te benzer işlemi yapabiliriz. Böyle bir örnek ([sample](seriesFiltered.xlsx)) dosyada, **Testseries2** ve **Testseries4**'ü filtrelemek istiyorsak, aşağıdaki kodu çalıştırabiliriz. Ayrıca, iki liste tutacağız: biri ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) tüm seçilen serileri depolamak için.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Örnek Kod**
Aşağıdaki örnek kodu [örnek Excel dosyasını](seriesFiltered.xlsx) yükler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. Veriyi filtrele ve grafiği değiştirmesine izin ver**

Verilerinizi filtrelemek, çok fazla veri ile grafik filtreleriyle başa çıkmanın mükemmel bir yoludur. Verileri filtrelediğinizde, grafik değişecektir. Çözmemiz gereken önemli bir konu, grafiğin ekranda kalmasını sağlamaktır. Filtre uyguladığınızda, gizli satırlar oluşur ve zaman zaman grafik bu gizli satırlarda olur.

![todo:image_alt_text](Figure3.png)

### **Excel'de Grafikteki Değişikliği Uygulamak İçin Veri Filtrelerini Kullanma Adımları**

1. Veri aralığınızın içine tıklayın.
2. **Veri** sekmesine tıklayın ve Filtreleri açmak için Filtreleri tıklayın. Başlık satırınızın açılır oklarının olması gerekecektir.
3. **Ekle** sekmesine giderek sütun grafiği seçerek bir grafik oluşturun.
4. Verilerinizi veri içindeki açılır oklar kullanarak filtreleyin. Grafik Filtreleri kullanmayın.

### **Örnek Kod**
Aşağıdaki örnek kod, aynı özelliği Aspose.Cells kullanarak gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. Verileri bir Tablo kullanarak filtreleyin ve grafiği değiştirin**

Tablo kullanımı, bir aralık kullanmakla bir yöntem 2'ye benzer, ancak tabloların aralıklara göre avantajları vardır. Aralığınızı bir Tablo'ya değiştirip veri eklediğinizde, grafik otomatik olarak güncellenir. Bir aralıkta veri kaynağını değiştirmeniz gerekecektir.

### **Excel'de tablo olarak biçimlendir**

Veri içine tıklayın ve **CTRL + T** kullanın veya Ana sekme, **Tablo Olarak Biçimlendir**i kullanın

![todo:image_alt_text](Figure4.png)

### **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](TableFilters.xlsx) yükler ve Aspose.Cells kullanarak aynı özelliği gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
