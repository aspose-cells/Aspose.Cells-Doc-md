---
title: JavaScript ile C++ üzerinden Grafik Görünümünü Ayarlama
description: Grafiklerin görünümünü nasıl yapılandıracağınızı öğrenin. Kılavuzumuz, grafik düzenlerini, renkleri, yazı tiplerini ve efektleri istediğiniz görsel stile ulaşmak ve çalışma sayfelerinizi geliştirmek için nasıl değiştireceğinizi gösterecektir.
keywords: Aspose.Cells for JavaC++ ile Komut Dosyası, grafik çizimi, grafik görünümü, düzenler, renkler, yazı tipleri, efektler, çalışma sayfaları.
linktitle: Grafik Formatı
type: docs
weight: 20
url: /tr/javascript-cpp/setting-chart-appearance/
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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 60;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = new AsposeCells.Color(0, 0, 255);

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = new AsposeCells.Color(255, 255, 0);

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(255, 0, 0);

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = new AsposeCells.Color(0, 255, 255);

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **Grafik Çizgilerini Ayarlama**
Geliştiriciler ayrıca [Seri Koleksiyonu](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) üzerindeki çizgi veya veri işaretçileri üzerine farklı stil türleri uygulayabilir. Aşağıdaki kod örneği Aspose.Cells API kullanarak grafik çizgilerini nasıl ayarlayacağınızı gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Applying a dotted line style on the lines of a SeriesCollection
            chart.nSeries.get(0).border.style = AsposeCells.LineType.Dot;

            // Applying a triangular marker style on the data markers of a SeriesCollection
            chart.nSeries.get(0).marker.markerStyle = AsposeCells.ChartMarkerType.Triangle;

            // Setting the weight of all lines in a SeriesCollection to medium
            chart.nSeries.get(1).border.weight = AsposeCells.WeightType.MediumLine;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
Geliştiriciler, aşağıdaki örnekte gösterildiği gibi, [Seri Koleksiyonu](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) veya diğer grafik nesnelerine farklı Microsoft Excel temaları/renkleri uygulayabilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Chart Series Fill Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FillType, ThemeColor, ThemeColorType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook containing the chart
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first chart in the sheet
            const chart = worksheet.charts.get(0);

            // Specify the FillFormat's type to Solid Fill of the first series
            const series = chart.nSeries.get(0);
            series.area.fillFormat.fillType = FillType.Solid;

            // Get the CellsColor of SolidFill
            const cc = series.area.fillFormat.solidFill.cellsColor;

            // Create a theme in Accent style
            cc.themeColor = new ThemeColor(ThemeColorType.Accent6, 0.6);

            // Apply the theme to the series
            series.area.fillFormat.solidFill.cellsColor = cc;

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart series fill updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**
Microsoft Excel kullanarak bir grafiğin ve eksenlerinin başlıklarını WYSIWYG ortamında ayarlayabilirsiniz. Aspose.Cells ayrıca, çalışma zamanında bir grafik ve eksenlerinin başlıklarını ayarlamanıza olanak tanır. Tüm grafikler ve eksenler, aşağıdaki örnekte gösterildiği gibi başlıklarını ayarlamak için kullanılabilen [Başlık](https://reference.aspose.com/cells/javascript-cpp/title/) özelliğine sahiptir.

Aşağıdaki kod örneği, grafik ve eksenlere başlık ayarlamanın yolunu gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, GradientStyleType, Color } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [Color.Lime, 1, GradientStyleType.Horizontal, 1];

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Büyük Izgaralarla Çalışma**
Büyük ızgaraların görünümünü özelleştirmek mümkündür. Izgaraları gizlemek veya göstermek, renk ve diğer ayarları tanımlamak vb. aşağıda, ızgaraların nasıl gizleneceğini ve renginin nasıl değiştirileceğini gösteriyoruz.

#### **Büyük Izgaraları Gizleme**
Geliştiriciler, [Line](https://reference.aspose.com/cells/javascript-cpp/line/) nesnesinin [isVisible()](https://reference.aspose.com/cells/javascript-cpp/line/#isVisible--) özelliğini **true** veya **false** olarak ayarlayarak ana ızgara çizgilerinin görünürlüğünü kontrol edebilir.

Aşağıdaki kod parçacığı, ana ızgara çizgilerinin nasıl gizleneceğini gösterir. Ana ızgara çizgileri gizlendikten sonra çalışma sayfasına bir sütun grafik eklenecek ve ızgara çizgileri olmayacaktır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Hiding the major gridlines of Category Axis
            chart.categoryAxis.majorGridLines.isVisible = false;

            // Hiding the major gridlines of Value Axis
            chart.valueAxis.majorGridLines.isVisible = false;

            // Saving the Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Büyük Izgaraların Ayarlarını Değiştirme**
Geliştiriciler, yalnızca büyük ızgaraların görünürlüğünü değil, aynı zamanda rengi gibi diğer özelliklerini de kontrol edebilirler.

Aşağıdaki kod parçacığı, ana ızgara çizgilerinin rengini nasıl değiştireceğinizi gösterir. Renk ayarlandıktan sonra, çalışma sayfasına ayarlanmış ızgara çizgileri ile bir sütun grafik eklenecek.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                // Creating a new Workbook object
                const workbook = new Workbook();

                // Adding a new worksheet to the Workbook object
                const sheetIndex = workbook.worksheets.add();

                // Obtaining the reference of the newly added worksheet by passing its sheet index
                const worksheet = workbook.worksheets.get(sheetIndex);

                // Adding sample values to cells
                worksheet.cells.get("A1").value = 50;
                worksheet.cells.get("A2").value = 100;
                worksheet.cells.get("A3").value = 150;
                worksheet.cells.get("B1").value = 60;
                worksheet.cells.get("B2").value = 32;
                worksheet.cells.get("B3").value = 50;

                // Adding a chart to the worksheet
                const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

                // Accessing the instance of the newly added chart
                const chart = worksheet.charts.get(chartIndex);

                // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
                chart.nSeries.add("A1:B3", true);

                // Setting the foreground color of the plot area
                chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

                // Setting the foreground color of the chart area
                chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

                // Setting the foreground color of the 1st SeriesCollection area
                chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

                // Setting the foreground color of the area of the 1st SeriesCollection point
                chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

                // Filling the area of the 2nd SeriesCollection with a gradient
                chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

                // Setting the color of Category Axis' major gridlines to silver
                chart.categoryAxis.majorGridLines.color = AsposeCells.Color.Silver;

                // Setting the color of Value Axis' major gridlines to red
                chart.valueAxis.majorGridLines.color = AsposeCells.Color.Red;

                // Saving the Excel file and creating download link
                const outputData = workbook.save(SaveFormat.Excel97To2003);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'book1.out.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
            });
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/javascript-cpp/set-the-values-format-code-of-chart-series/)
- [Grafikte Arka Plan Doldurma Olarak Resim Ayarlama](/cells/tr/javascript-cpp/set-picture-as-background-fill-in-the-chart/)
