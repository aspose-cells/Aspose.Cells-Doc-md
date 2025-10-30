---  
title: Grafik için Veri Kaynağını Node.js kullanarak C++ ile ayarlayın  
description: Aspose.Cells for Node.js via C++ tarafından desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Kılavuzumuz, mevcut farklı veri kaynağı türlerini size gösterecek ve bunlardan veri almak ve bağlantı kurmak için nasıl yapacağınızı anlatacaktır, böylece çalışma sayfalarınızı doldurabilirsiniz.  
keywords: Aspose.Cells for Node.js via C++, grafik çizimi, veri biçimlendirme, etiketler, renkler, yazı tipleri, görünüm, kullanılabilirlik.  
linktitle: Veri Kaynağı  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/data-formatting-in-charts/  
---  

Önceki konularımızda, grafik için veri kaynağı nasıl ayarlanır gösteren birçok örnek sağladık, ancak bu konuda grafik için ayarlanabilecek veri türleri hakkında daha fazla detay vereceğiz.

## **Grafik Verisi Ayarlama**

Aspose.Cells kullanarak grafikler üzerinde çalışırken ele almanız gereken iki tür veri şunlardır:

- Grafik verisi.
- Kategori verisi.

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için kullandığımız veri kaynağıdır. [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) nesnesinin [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) yöntemini çağırarak, hücre aralığını (grafik verisi içeren) ekleyebiliriz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Kategori Verisi**

Kategori verisi, grafik verilerinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) öğesine [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--) özelliği kullanılarak eklenebilir. Aşağıda, grafik ve kategori verilerinin kullanımını göstermek için tam bir örnek verilmiştir. Yukarıdaki örnek kod çalıştırıldıktan sonra, çalışma sayfasına aşağıdaki gibi bir sütun grafiği eklenecektir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Gelişmiş Konular**  
- [Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Dinamik Grafikler Oluşturma](/cells/tr/nodejs-cpp/create-dynamic-charts/)  
- [Chart.SetChartDataRange Yöntemini Kullanarak Grafik Kurulumu için Kolay Yol](/cells/tr/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
