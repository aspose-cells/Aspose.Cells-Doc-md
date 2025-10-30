---
title: Node.js kullanarak C++ ile Konum, Boyut ve Tasarımcı Grafiklerini Manipüle Etmek
linktitle: Pozisyon Boyutunu ve Tasarımcı Grafiğini Manipüle Edin
description: Microsoft Excel de konum, boyut ve tasarımcı grafiği etkin bir şekilde manipüle etmek için Aspose.Cells for Node.js via C++ ü nasıl kullanacağınızı öğrenin. Rehberimiz, bu özellikleri iyileştirilmiş düzen ve görselleştirme için nasıl ayarlayacağınızı gösterecek.
keywords: Aspose.Cells for Node.js via C++, Konum, Boyut, Tasarımcı Grafik, Microsoft Excel, Düzen, Görselleştirme.
type: docs
weight: 45
url: /tr/nodejs-cpp/manipulate-position-size-and-designer-chart/
---

## **Grafik Pozisyonu ve Boyutu**
Bazen, çalışma sayfası içindeki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek istersiniz. Aspose.Cells, bunu başarmak için [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) özelliği sağlar. Bu özelliğin alt özelliklerini kullanarak grafiği yeni **yükseklik** ve **genişlik** ile yeniden boyutlandırabilir veya yeni **X** ve **Y** koordinatlarıyla yeniden konumlandırabilirsiniz.

### **Grafiğin Konumunu ve Boyutunu Kontrol Etmek**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
1. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
1. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
1. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

Aşağıdaki örnek yukarıdaki API'lerin kullanımını açıklar; ilk sayfasında bir grafik içeren mevcut çalışma kitabını yükler. Sonra Aspose.Cells kullanarak grafiği yeniden boyutlandırır ve yeniden konumlandırır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Tasarımcı Grafikleri Manipüle Etmek**
Tasarımlı şablon dosyalarındaki grafiklerle zaman zaman manipüle etmeli veya değiştirmelisiniz. Aspose.Cells, tasarımcı grafiklerinin içeriği ve öğeleri ile manipüle edilmesini tam anlamıyla destekler. Veriler, grafik içeriği, arka plan resmi ve biçimlendirme doğrulukla korunabilir.

### **Şablon Dosyalarında Tasarımcı Grafiklerini Manipüle Etmek**
Tasarımcı grafiklerini şablon dosyalarında manipüle etmek için grafik ile ilgili API'leri kullanın. Örneğin, mevcut grafik koleksiyonunu almak için Worksheet.charts özelliğini kullanabilirsiniz.

#### **Bir Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiği oluşturmanın nasıl yapıldığını göstermektedir. Bu grafiği daha sonra manipüle edeceğiz.

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
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Grafiği Manipüle Etmek**
Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğimizi göstermektedir. Bu örnekte, yukarıda oluşturulan grafiği değiştireceğiz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığına dikkat edin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("Unided Kingdom, 400K ");

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**
Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the Border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the Border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
