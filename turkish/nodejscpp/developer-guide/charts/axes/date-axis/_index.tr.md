---
title: Node.js ile C++ kullanarak Tarih Eksenini yönetme
description: Aspose.Cells for Node.js via C++ kullanarak tarih eksenini nasıl yöneteceğinizi öğrenin. Kılavuzumuz, çeşitli tarih biçimleri, zaman ölçekleri ve tick label sıklıklarıyla nasıl çalışılacağını anlatır.
keywords: Aspose.Cells for Node.js, tarih ekseni, yönetim, tarih biçimleri, zaman ölçekleri, tick label sıklıkları.
type: docs
weight: 200
url: /tr/nodejs-cpp/date-axis/
---

## **Olası Kullanım Senaryoları**
Bir çalışma sayfası verilerinden tarihleri kullanan ve bu verilerin yatay (kategori) eksende grafikte gösterildiği grafik oluşturduğunuzda, Aspose.Cells for Node.js via C++ otomatik olarak kategori eksenini tarih (zaman ölçekli) eksenine çevirir.
Tarih ekseni, çalışma sayfasındaki tarihleri belirli aralıklarda veya temel birimlerde, örneğin gün, ay veya yıl sayısını kronolojik sırada görüntüler, hatta çalışma sayfasındaki tarihler sıralı veya aynı temel birimlerde değilse bile.
Varsayılan olarak, Aspose.Cells, çalışma sayfası verilerindeki en küçük iki tarih arasındaki fark temel birimi belirler. Örneğin, hisse fiyatları verinizde tarihler arasındaki en küçük fark yedi gün ise, Excel temel birimi günü ayarlar; ancak, uzun vadeli performansı görmek istiyorsanız temel birimi ay veya yıl olarak değiştirebilirsiniz.

## **Microsoft Excel gibi Tarih Ekseni Yönetimi**
Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına yerleştiren örnek kodu aşağıda inceleyiniz. 
Ardından bir grafik ekleriz ve [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) tipini ayarlarız 
[**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) 'e ayarlar dikkate alınarak, base units için Days olarak ayarlarız.

![todo:image_alt_text](excel.png)

## **Örnek Kod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
