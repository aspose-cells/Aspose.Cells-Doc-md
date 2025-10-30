---
title: Node.js ile C++ kullanarak Tornado Grafiği nasıl oluşturulur
linktitle: Tornado grafiği nasıl oluşturulur.
type: docs
weight: 73
url: /tr/nodejs-cpp/create-tornado-chart/
description: Aspose.Cells for Node.js via C++ API kullanarak tornado grafik oluşturmayı öğrenin.
keywords: Node.js ile dönüm grafiği oluştur, dönüm grafiği ekle, dönüm grafiği yerleştir
---

## **Giriş**
Tufan grafiği, aynı zamanda tufan diyagramı veya tufan grafiği olarak da bilinen, Excel'de duyarlılık analizi için sıklıkla kullanılan bir veri görselleştirme türüdür. Belirli bir sonuç veya çıktı üzerinde değişkenlerin etkisini anlamanıza yardımcı olur.

## **Excel'de Bir Tufan Grafiği Nasıl Oluşturulur**
Excel'de bir tufan grafiği oluşturmak için şu adımları izleyebilirsiniz:
1. Verileri seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafiği Ekle --> Yığılmış Çubuk Grafiği'ne tıklayın.
<br>
<img src="1.png" width=70% />
2. Y-eksenini değiştirin: Y-eksenine sağ tıklayın. Biçim eksenine tıklayın. Etiketlerde, etiket konumu açılır menüsüne tıklayın ve Düşük öğesini seçin.
<br>
<img src="2.png" width=70% />
3. Herhangi bir sütunu seçin ve biçimlendirmeye gidin. Uygun bir boşluk genişliği ayarlayın.
<br>
<img src="3.png" width=70% />
4. Tufan grafiğinden eksi işaretini (-) çıkaralım. X-eksenini seçin. Biçimlendirmeye gidin. Eksen seçeneklerinde, sayıya tıklayın. Kategoride, özel seçin. Biçim koduna ###0,###0 yazın. Ekle'ye tıklayın.
<br>
<img src="4.png" width=70% />
5. Y-eksenine tıklayın ve eksen seçeneklerine gidin. Eksen seçeneklerinde kategorileri ters sırada işaretleyin.
<br>
<img src="5.png" width=70% />

## **Aspose.Cells for Node.js via C++'te Dönüm Grafiği Eklemeyi Nasıl Yapılır**
Lütfen aşağıdaki örnek kodu inceleyin. İçinde bazı örnek veriler içeren [örnek Excel dosyası](sample.xlsx) yükler. Ardından, başlangıç verilerine dayalı olarak yığılmış sütun grafiği oluşturur ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını [çıkış XLSX formatına](out.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından çıkış Excel dosyasında oluşturulan tufan grafiğini göstermektedir.
<br>
<img src="6.png" width=70% />

### **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
