---  
title: Grafikten PDF ye Dönüştürme ile Node.js ve C++  
linktitle: Grafikten PDF ye  
description: Aspose.Cells for Node.js via C++ kullanarak bir grafiği PDF dökümanına dönüştürmeyi nasıl yapacağınızı öğrenin. Rehberimiz, Microsoft Excel den grafik çıkartma ve PDF olarak kaydetme ve dağıtım amacıyla nasıl kullanılacağını gösterir.  
keywords: Aspose.Cells for Node.js via C++, Grafikden PDF ye, Microsoft Excel, PDF Dönüşüm, Dışa Aktar, Dağıtım, Arşivleme.  
type: docs  
weight: 47  
url: /tr/nodejs-cpp/chart-to-pdf/  
---  

## **Grafiği PDF'ye Dönüştürme**

Grafiği PDF formatına dönüştürmek için Aspose.Cells API'leri, sonucu PDF'nin disk yoluna veya akışa kaydetme yeteneğiyle [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) metodunu açığa çıkardı.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **İstenen Sayfa Boyutunda Grafik PDF Oluşturma**  
Aspose.Cells kullanarak istediğiniz sayfa boyutuyla grafik PDF oluşturabilir ve grafiği sayfa içinde nasıl hizalayacağınızı üst, alt, ortala, sol, sağ gibi belirtebilirsiniz. Ayrıca, çıktı grafiği akışta veya diske kaydedilebilir. Aşağıdaki örnek kod, [örnek Excel dosyası](64716906.xlsx) yükler, çalışma sayfasındaki ilk grafiğe erişir ve ardından istenilen sayfa boyutuyla [çıktı Pdf'sine](64716907.pdf) dönüştürür. Aşağıdaki ekran görüntüsü, çıktı Pdf'sinde sayfa boyutunun kodda belirtildiği gibi 7x7 olduğunu ve grafiğin hem yatay hem dikey olarak ortalanmış olduğunu gösterir.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
