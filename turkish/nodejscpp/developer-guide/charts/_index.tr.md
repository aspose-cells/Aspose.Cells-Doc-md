---
title: Node.js ile C++ üzerinden Grafik Oluşturma ve Yönetme
linktitle: Grafikler
description: Aspose.Cells for Node.js kullanarak Microsoft Excel de grafiklerin nasıl oluşturulacağını öğrenin. Kılavuzumuz çeşitli grafik türlerini ve görünüm ile biçimlendirmelerini nasıl özelleştireceğinizi gösterecek.
keywords: Aspose.Cells for Node.js, Grafik Oluşturma, Microsoft Excel, Grafik Türleri, Özelleştirme, Görünüm, Biçimlendirme.
type: docs
weight: 130
url: /tr/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells çok esnek grafik nesneleri sağlar. Bu konu, Aspose.Cells'in grafik nesnelerini tartışmaktadır.

{{% /alert %}}

## **Grafikler Oluşturma**

### **Basitçe bir Grafik Oluşturma**
Aşağıdaki örnek kodlarla Aspose.Cells ile bir grafik oluşturmak oldukça basittir:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Bir Grafik Oluşturmak için Bilinmesi Gerekenler**

Grafik oluşturulmadan önce, Aspose.Cells kullanarak grafik oluştururken yardımcı olacak bazı temel kavramları anlamak önemlidir.

#### **Grafikleme Nesneleri**

Grafik nesneleri aşağıda listelenmiştir:

- Seri, bir grafikte tek veri serisi.
- Eksen, bir grafik eksenleri.
- Grafik, tek bir Excel grafiği.
- GrafikAlanı, çalışma sayfasındaki grafik alanı.
- GrafikVeriTablosu, bir grafik veri tablosu.
- GrafikÇerçeve, bir grafikteki çerçeve nesnesi.
- GrafikNokta, bir grafikteki seri içindeki tek bir nokta.
- GrafikNoktaKoleksiyonu, bir serideki tüm noktaları içeren bir koleksiyon.
- Grafikler, Grafik nesnelerinin bir koleksiyonu.
- VeriEtiketleri, belirtilen seri için tüm VeriEtiketi nesnelerinin bir koleksiyonu.
- DoldurBiçimi, bir şeklin doldurulma biçimi.
- Zemin, 3B bir grafik zemini.
- Efsane, grafik efsanesi.
- Çizgi, grafik çizgisi.
- SeriKoleksiyonu, Seri nesnelerinin bir koleksiyonu.
- İşaretEtiketleri, bir grafik eksenindeki işaret etiketleri ile ilişkili olan işaret etiketi etiketleri.
- Başlık, bir grafik veya eksenin başlığı.
- Trend Çizgisi, bir grafikteki bir trend çizgisi.
- Trend Çizgisi Koleksiyonu, belirtilen veri serisi için tüm Trend Çizgisi nesnelerinin bir koleksiyonu.
- Duvarlar, 3D bir grafikte duvarlar.

#### **Grafik Nesneleri Kullanma**

Yukarıda belirtildiği gibi, tüm grafik nesneleri, ilgili sınıfların örnekleridir ve belirli görevleri yerine getirmek için belirli özellikler ve metotlar sağlar. Grafik nesnelerini kullanarak grafikler oluşturun.

Bir çalışma sayfasına herhangi bir grafik eklemek için [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) koleksiyonunu kullanın. [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) koleksiyonundaki her öğe bir [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) nesnesini temsil eder. Bir [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) nesnesi, grafiğin görünümünü özelleştirmek için gereken diğer tüm grafik nesnelerini kapsar. Birkaç temel grafik nesnesi kullanarak basit bir grafik yaratmanın yolu aşağıda gösterilmektedir.

### **Aspose.Cells Kullanarak Grafik Oluşturma**

**Adımlar:**

1. [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/) nesnesinin [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-) metodunu kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin.
   Bu, grafik veri kaynağı olarak kullanılacaktır.
1. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) nesnesiyle kapsüllenmiş [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) koleksiyonunun [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) metodunu çağırarak çalışma sayfasına grafik ekleyin.
1. [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) sıralamasıyla grafik türünü belirtin.
   Örneğin, aşağıdaki örnek [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) değeri grafiğin türü olarak kullanır.
1. Yeni [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) nesnesine, indeksini geçirerek [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) koleksiyonundan erişin.
1. Grafik yönetimi için [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) nesnesine kapsüllenmiş herhangi bir grafik nesnesini kullanın.
   Aşağıdaki örnek, [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) grafik nesnesini kullanarak grafiğin veri kaynağını belirtir.

Grafiğe kaynak veri eklerken, veri kaynağı hücre aralığı (örneğin "A1:C3"), ardışık olmayan hücre dizisi (örneğin "A1, A3, A5") veya değer dizisi (örneğin "1,2,3") olabilir.

Bu genel adımlar, herhangi bir türde bir grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesnelerini kullanın.

Aspose.Cells ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) olarak adlandırılan bir numaralandırmada önceden tanımlanmıştır.

Önceden tanımlanmış grafik tipleri:

|**Grafik Tipleri**|**Açıklama**|
| :- | :- |
|Column|Temsil Edilen Kümeleme Sutun Grafiği|
|ColumnStacked|Tasvir Yığılmış Sutun Grafiği|
|Column100PercentStacked|Tasvir 100% Yığılmış Sutun Grafiği|
|Column3DClustered|Tasvir 3D Küme Sutun Grafiği|
|Column3DStacked|Tasvir 3D Yığılmış Sutun Grafiği|
|Column3D100PercentStacked|Tasvir 3D 100% Yığılmış Sutun Grafiği|
|Column3D|Tasvir 3D Sutun Grafiği|
|Bar|Tasvir Kümeleme Çubuk Grafiği|
|BarStacked|Yığın Çubuk Grafiğini Temsil Eder|
|Bar100PercentStacked|100% Yığılmış Çubuk Grafiğini Temsil Eder|
|Bar3DClustered|3D Küme Çubuk Grafiğini Temsil Eder|
|Bar3DStacked|3D Yığılmış Çubuk Grafiğini Temsil Eder|
|Bar3D100PercentStacked|3D 100% Yığılmış Çubuk Grafiğini Temsil Eder|
|Line|Çizgi Grafiğini Temsil Eder|
|LineStacked|Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentStacked|100% Yığılmış Çizgi Grafiğini Temsil Eder|
|LineWithDataMarkers|Veri İşaretleri Bulunan Çizgi Grafiğini Temsil Eder|
|LineStackedWithDataMarkers|Veri İşaretleri Bulunan Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentStackedWithDataMarkers|100% Yığılmış Veri İşaretleri Bulunan Çizgi Grafiğini Temsil Eder|
|Line3D|3D Çizgi Grafiğini Temsil Eder|
|Pie|Pasta Grafiğini Temsil Eder|
|Pie3D|3D Pasta Grafiğini Temsil Eder|
|PiePie|Pasta Grafiğinde Pasta Temsil Eder|
|PieExploded|Patlamış Pasta Grafiğini Temsil Eder|
|Pie3DExploded|3D Patlamış Pasta Grafiğini Temsil Eder|
|PieBar|Pasta Grafiğinde Çubuk Temsil Eder|
|Scatter|Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByCurvesWithDataMarker|Eğrilerle Bağlı Veri İşaretleri Bulunan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByCurvesWithoutDataMarker|Eğrilerle Bağlı Veri İşaretleri Bulunmayan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByLinesWithDataMarker|Çizgilerle Bağlı Veri İşaretleri Bulunan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByLinesWithoutDataMarker|Çizgilerle Bağlı Veri İşaretleri Bulunmayan Saçılma Grafiğini Temsil Eder|
|Area|Alan Grafiğini Temsil Eder|
|AreaStacked|Yığılmış Alan Grafiğini Temsil Eder|
|Area100PercentStacked|100% Yığılmış Alan Grafiğini Temsil Eder|
|Area3D|3D Alan Grafiğini Temsil Eder|
|Area3DStacked|3D Yığılmış Alan Grafiğini Temsil Eder|
|Area3D100PercentStacked|3D 100% Yığılmış Alan Grafiğini Temsil Eder|
|Doughnut|Donut Grafiğini Temsil Eder|
|DoughnutExploded|Exploded Doughnut Chartını Temsil Ediyor|
|Radar|Radar Grafiğini Temsil Ediyor|
|RadarWithDataMarkers|Veri İşaretçileri olan Radar Grafiğini Temsil Ediyor|
|RadarFilled|Dolu Radar Grafiğini Temsil Ediyor|
|Surface3D|3 boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceWireframe3D|Tel Kafesli 3 Boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceContour|Kontur Grafiğini Temsil Ediyor|
|SurfaceContourWireframe|Tel Kafesli Kontur Grafiğini Temsil Ediyor|
|Bubble|Balon Grafiğini Temsil Ediyor|
|Bubble3D|3 Boyutlu Balon Grafiğini Temsil Ediyor|
|Cylinder|Silindir Grafiğini Temsil Ediyor|
|CylinderStacked|Yığılmış Silindir Grafiğini Temsil Ediyor|
|Cylinder100PercentStacked|100% Yığılmış Silindir Grafiğini Temsil Ediyor|
|CylindericalBar|Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalBarStacked|Yığılmış Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalBar100PercentStacked|100% Yığılmış Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalColumn3D|3 Boyutlu Silindirik Sütun Grafiğini Temsil Ediyor|
|Cone|Konik Grafiğini Temsil Ediyor|
|ConeStacked|Yığılmış Konik Grafiğini Temsil Ediyor|
|Cone100PercentStacked|100% Yığılmış Konik Grafiğini Temsil Ediyor|
|ConicalBar|Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalBarStackedStacked Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalBar100PercentStacked|100% Yığılmış Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalColumn3D|3 Boyutlu Konik Sütun Grafiğini Temsil Ediyor|
|Pyramid|Piramit Grafiğini Temsil Ediyor|
|PyramidStacked|Yığılmış Piramit Grafiğini Temsil Ediyor|
|Pyramid100PercentStacked|100% Yığılmış Piramit Grafiğini Temsil Ediyor|
|PyramidBar|Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBarStacked|Stacked Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBar100PercentStacked|100% Yığılmış Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidColumn3D| 3D Piramit Sutun Grafiğini Temsil Eder|
{{% alert color="primary" %}}

Hücre aralığını veri kaynağı olarak atadığınızda, yalnızca sol üstten sağ alta doğru aralığı belirleyebilirsiniz. Örneğin, "A1:C3" geçerli iken "C3:A1" geçersizdir.

{{% /alert %}}

#### **Piramit Grafiği**

Örnek kod çalıştırıldığında, bir piramit grafiği çalışma sayfasına eklenir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Çizgi Grafiği**

Yukarıdaki örnekte, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) yerine *Line* yazarak bir çizgi grafiği oluşturulur. Tam kaynak aşağıda sağlanmıştır. Kod çalıştırıldığında, çalışma sayfasına bir çizgi grafiği eklenir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Kabarcık Grafiği**

Bir balon grafiği oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) değeri [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) olarak ayarlanmalı ve BubbleSizes, Values ve XValues gibi birkaç ek özellik uygun şekilde ayarlanmalıdır. Aşağıdaki kod çalıştırıldığında, çalışma sayfasına bir balon grafiği eklenir.

#### **Veri İşaretçisi ile Çizgi Grafiği**

Veri işaretçili çizgi grafik oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) değeri *ChartType.LineWithDataMarkers* olarak ayarlanmalı ve arka plan alanı, Seriler İşaretçileri, Değerler ve XValues gibi birkaç ek özellik uygun şekilde ayarlanmalıdır. Aşağıdaki kod çalıştırıldığında, çalışma sayfasına veri işaretçili çizgi grafik eklenir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Gelişmiş Konular**
- [Excel 2016 Grafiklerini Okuma ve Değiştirme](/cells/tr/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Excel Grafik Eksenlerini Yönetme](/cells/tr/nodejs-cpp/chart-axes/)
- [Grafik Görünümünü Ayarlama](/cells/tr/nodejs-cpp/setting-chart-appearance/)
- [Grafik Türleri](/cells/tr/nodejs-cpp/chart-types/)
- [Grafikleri Özelleştirme](/cells/tr/nodejs-cpp/customizing-charts/)
- [Grafiğin Veri Kaynağını Ayarlama](/cells/tr/nodejs-cpp/data-formatting-in-charts/)
- [Excel Grafik Veri Etiketlerini Yönetme](/cells/tr/nodejs-cpp/insert-datalabels-to-chart/)
- [Grafiğin Çalışma Sayfasını Alma](/cells/tr/nodejs-cpp/get-worksheet-of-the-chart/)
- [Excel Grafiklerinin Açıklamasını Yönetme](/cells/tr/nodejs-cpp/chart-legend/)
- [Pozisyon Boyutunu ve Tasarımcı Grafiği Yönetme](/cells/tr/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Lider Çizgili Pasta Grafiği Oluşturma](/cells/tr/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Grafiplerde Şekiller](/cells/tr/nodejs-cpp/controls-in-charts/)
- [Excel Grafik Başlıklarını Yönetme](/cells/tr/nodejs-cpp/chart-and-axis-titles/)
- [Grafik Rendeleme](/cells/tr/nodejs-cpp/chart-rendering/)
- [Grafik Eğrisi Trend Çizgisinin Denklem Metnini Alma](/cells/tr/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
