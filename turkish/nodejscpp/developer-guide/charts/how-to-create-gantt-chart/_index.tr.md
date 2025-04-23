---
title: Node.js ile C++ kullanarak Gantt Çizelgesi nasıl oluşturulur
linktitle: Gantt grafiği nasıl oluşturulur?
type: docs
weight: 72
url: /tr/nodejs-cpp/how-to-create-gantt-chart/
description: Aspose.Cells for Node.js via C++ API ile Gantt Çizelgesi oluşturmayı öğrenin.
keywords: Node.js ile Gantt Çizelgesi oluşturma, Gantt çizelgesi ekleme, Gantt çizelgesi yerleştirme
---

## **Gantt grafiği nedir?**

Gantt grafiği, bir proje takvimini anlatan bir tür çubuk grafik türüdür. Bir projenin çeşitli unsurlarının başlangıç ve bitiş tarihlerini gösterir. Her görev veya etkinlik, süresine karşılık gelen bir çubukla temsil edilir. Gantt grafikleri ayrıca görevler arasındaki bağımlılıkları gösterir, böylece proje yöneticileri görevlerin tamamlanması gereken sıralamayı görselleştirebilir. Bunlar, proje yönetiminde projeleri etkin şekilde planlamak, zamanlamak ve izlemek için yaygın olarak kullanılır.

## **Excel'de Gantt Grafiği Nasıl Oluşturulur?**

Excel'de Gantt grafiği oluşturmak için aşağıdaki adımları izleyebilirsiniz:
1. Gantt grafiği için bazı veri ekleyin. 
<br>
<img src="00.png" width=50% />
1. Veriyi seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafik Ekle --> Katlı Çubuk Grafik seçeneklerini kullanın. Örneğimizde, B1:B7, ve ardından **Katlı Çubuk** grafiği ekleyin.
<br>
<img src="1.png" width=50% />

1. Grafiği seçin, **Veri Ekle** -> **Ekle**, **Seri adı** ve **Seri değerleri** ayarlarını aşağıdaki gibi yapın.
<br>
<img src="2.png" width=50% />

1. Grafiği seçin, **Yatay (Kategori) Eksen Etiketleri** düzenleyin.
<br>
<img src="3.png" width=50% />

1. **Eksen Biçimlendir** seçeneğiyle Y Ekseni, **Kategorileri ters sırada** seçin.
1. **Mavi Seri**yi seçin ve **Doldur -> Doldurmasız** seçeneğini ayarlayın.
1. **Eksen Formatı**nı açın, X Eksenini ayarlayın ve **En düşük ve en yüksek** değerleri belirleyin (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. Grafik için **Veri Etiketleri Ekle**, şimdi bir Gantt grafiği elde edeceksiniz.
<br>
<img src="0.png" width=50% />


## **Aspose.Cells'te Gantt Çizelgesi Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, bazı örnek veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Ardından, başlangıç verilerine dayanarak yığılmış çubuk grafiği oluşturur ve ilgili özellikleri belirler. Son olarak, çalışma kitabını [çıkış XLSX formatında](result.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan Gantt çizelgesini gösterir.
<br>
<img src="5.png" width=60% />

### **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

