---
title: Node.js kullanarak C++ ile Grafik Görünümünü Ayarlama
description: Aspose.Cells for Node.js via C++ te grafiklerin görünümünü nasıl yapılandıracağınızı öğrenin. Kılavuzumuz, grafik düzenlerini, renkleri, yazı tiplerini ve efektleri istediğiniz görsel stili elde etmek ve çalışma sayfelerinizi geliştirmek için nasıl değiştireceğinizi gösterecek.
keywords: Aspose.Cells for Node.js via C++, grafik oluşturma, grafik görünümü, düzenler, renkler, yazı tipleri, efektler, çalışma sayfaları.
linktitle: Grafik Formatı
type: docs
weight: 20
url: /tr/nodejs-cpp/setting-chart-appearance/
---

## **Grafik Görünümünü Ayarlama**
Bir Grafik Oluşturma Nasıl Konusunda Aspose.Cells tarafından sunulan grafik türleri ve grafik nesnelerinin kısa bir tanıtımını ve bir tanesini nasıl oluşturacağınızı açıklamıştık. Bu makale, özelliklerini ayarlayarak grafiklerin görünümünü özelleştirmenin nasıl yapılacağını tartışıyor:

- Grafik alanını ayarlama.
- Grafik çizgilerini ayarlama.
- Temalar uygulama.
- Grafiklere ve eksenlere başlıklar eklemek.
- Izgaralarla çalışma.

### **Grafik Alanını Ayarlama**
Bir grafikte farklı türde alanlar bulunmakta ve Aspose.Cells her bir alanın görünümünü değiştirme esnekliği sağlar. Geliştiriciler, bir alan üzerinde farklı biçimlendirme ayarları uygulayarak ön plan rengi, arka plan rengi ve doldurma biçimi gibi farklı biçimlendirme ayarlarını uygulayabilir.

Aşağıdaki örnekte, bir grafikte farklı türde alanlara farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Plot alanı
- Grafik alanı
- Seri koleksiyonu alanı
- Bir Seri Koleksiyonu içindeki tek bir noktanın alanı

Aşağıdaki kod parçası, grafik alanını nasıl ayarlayacağınızı göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(new AsposeCells.Color(0, 0, 255));

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(new AsposeCells.Color(255, 255, 0));

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(255, 0, 0));

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 255, 255));

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Grafik Çizgilerini Ayarlama**
Geliştiriciler, [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) üzerindeki çizgi veya veri belirteçlerine farklı tarzlar uygulayabilir. Aşağıdaki kod parçacığı, Aspose.Cells API'sini kullanarak grafik çizgilerini nasıl ayarlayacağınızı gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Applying a dotted line style on the lines of a SeriesCollection
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Dot);

// Applying a triangular marker style on the data markers of a SeriesCollection
chart.getNSeries().get(0).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Triangle);

// Setting the weight of all lines in a SeriesCollection to medium
chart.getNSeries().get(1).getBorder().setWeight(AsposeCells.WeightType.MediumLine);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
Geliştiriciler, aşağıdaki örnekte gösterildiği gibi Microsoft Excel temaları/rengi uygulayabilir ve bu sayede [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) veya diğer grafik nesnelerini özelleştirebilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");

// Loads the workbook containing the chart
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first chart in the sheet
const chart = worksheet.getCharts().get(0);

// Specify the FillFormat's type to Solid Fill of the first series
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.Solid);

// Get the CellsColor of SolidFill
const cc = chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().getCellsColor();

// Create a theme in Accent style
cc.setThemeColor(new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent6, 0.6));

// Apply the theme to the series
chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().setCellsColor(cc);

// Save the Excel file
workbook.save(path.join(dataDir, "output.out.xlsx"));
```

### **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**
Microsoft Excel kullanarak, bir grafiğin ve eksenlerin başlıklarını WYSIWYG ortamında ayarlayabilirsiniz. Aspose.Cells sayesinde, geliştiriciler grafik ve eksen başlıklarını çalışma zamanında ayarlayabilir. Tüm grafikler ve eksenler, aşağıdaki örnekte gösterildiği gibi başlıklar içeren [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) özelliğine sahiptir.

Aşağıdaki kod örneği, grafik ve eksenlere başlık ayarlamanın yolunu gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Büyük Izgaralarla Çalışma**
Büyük ızgaraların görünümünü özelleştirmek mümkündür. Izgaraları gizlemek veya göstermek, renk ve diğer ayarları tanımlamak vb. aşağıda, ızgaraların nasıl gizleneceğini ve renginin nasıl değiştirileceğini gösteriyoruz.

#### **Büyük Izgaraları Gizleme**
Geliştiriciler, [Line](https://reference.aspose.com/cells/nodejs-cpp/line/) nesnesinin [isVisible()](https://reference.aspose.com/cells/nodejs-cpp/line/#isVisible--) özelliğini **true** veya **false** olarak ayarlayarak ana ızgara çizgilerinin görünürlüğünü kontrol edebilir.

Aşağıdaki kod parçacığı, ana ızgara çizgilerinin nasıl gizleneceğini gösterir. Ana ızgara çizgileri gizlendikten sonra çalışma sayfasına bir sütun grafik eklenecek ve ızgara çizgileri olmayacaktır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Hiding the major gridlines of Category Axis
chart.getCategoryAxis().getMajorGridLines().setIsVisible(false);

// Hiding the major gridlines of Value Axis
chart.getValueAxis().getMajorGridLines().setIsVisible(false);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Büyük Izgaraların Ayarlarını Değiştirme**
Geliştiriciler, yalnızca büyük ızgaraların görünürlüğünü değil, aynı zamanda rengi gibi diğer özelliklerini de kontrol edebilirler.

Aşağıdaki kod parçacığı, ana ızgara çizgilerinin rengini nasıl değiştireceğinizi gösterir. Renk ayarlandıktan sonra, çalışma sayfasına ayarlanmış ızgara çizgileri ile bir sütun grafik eklenecek.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the color of Category Axis' major gridlines to silver
chart.getCategoryAxis().getMajorGridLines().setColor(AsposeCells.Color.Silver);

// Setting the color of Value Axis' major gridlines to red
chart.getValueAxis().getMajorGridLines().setColor(AsposeCells.Color.Red);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Gelişmiş Konular**
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/nodejs-cpp/set-the-values-format-code-of-chart-series/)
- [Grafikte Arka Plan Doldurma Olarak Resim Ayarlama](/cells/tr/nodejs-cpp/set-picture-as-background-fill-in-the-chart/)


