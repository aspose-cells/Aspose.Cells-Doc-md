---
title: JavaScript kullanarak konum, boyut ve tasarımcı grafiği ile manipulate etme C++ ile
linktitle: Pozisyon Boyutunu ve Tasarımcı Grafiğini Manipüle Edin
description: Microsoft Excel de konum, boyut ve tasarımcı grafiği etkili bir şekilde manipüle etmek için Aspose.Cells for JavaScript i C++ kullanarak nasıl kullanacağınızı öğrenin. Kılavuzumuz bu özellikleri ayarlamak ve görselleştirmeyi geliştirmek için gösterecek.
keywords: Aspose.Cells for JavaScript ile C++, Konum, Boyut, Tasarımcı Grafik, Microsoft Excel, Düzen, Görselleştirme.
type: docs
weight: 45
url: /tr/javascript-cpp/manipulate-position-size-and-designer-chart/
---

## **Grafik Pozisyonu ve Boyutu**
Bazen, çalışma sayfasındaki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek istersiniz. Aspose.Cells, bunu başarmak için [Chart.chartObject](https://reference.aspose.com/cells/javascript-cpp/chart/#chartObject--) özelliğini sağlar. Bu özellik alt özellikleri kullanılarak grafiğin yeni **yükseklik** ve **genişlik** ile yeniden boyutlandırılması veya yeni **X** ve **Y** koordinatları ile yeniden konumlandırılması mümkündür.

### **Grafiğin Konumunu ve Boyutunu Kontrol Etmek**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [Shape.x](https://reference.aspose.com/cells/javascript-cpp/shape/#x--)
1. [Shape.y](https://reference.aspose.com/cells/javascript-cpp/shape/#y--)
1. [Shape.height](https://reference.aspose.com/cells/javascript-cpp/shape/#height--)
1. [Shape.width](https://reference.aspose.com/cells/javascript-cpp/shape/#width--)

Aşağıdaki örnek yukarıdaki API'lerin kullanımını açıklar; ilk sayfasında bir grafik içeren mevcut çalışma kitabını yükler. Sonra Aspose.Cells kullanarak grafiği yeniden boyutlandırır ve yeniden konumlandırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Resize and Reposition Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the second worksheet in the Excel file (index 1)
            const worksheet = workbook.worksheets.get(1);

            // Load the chart from source worksheet (first chart)
            const chart = worksheet.charts.get(0);

            // Resize the chart
            chart.chartObject.width = 400;
            chart.chartObject.height = 300;

            // Reposition the chart
            chart.chartObject.x = 250;
            chart.chartObject.y = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart resized and repositioned successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Tasarımcı Grafikleri Manipüle Etmek**
Tasarımlı şablon dosyalarındaki grafiklerle zaman zaman manipüle etmeli veya değiştirmelisiniz. Aspose.Cells, tasarımcı grafiklerinin içeriği ve öğeleri ile manipüle edilmesini tam anlamıyla destekler. Veriler, grafik içeriği, arka plan resmi ve biçimlendirme doğrulukla korunabilir.

### **Şablon Dosyalarında Tasarımcı Grafiklerini Manipüle Etmek**
Tasarımcı grafiklerini şablon dosyalarında manipüle etmek için grafik ile ilgili API'leri kullanın. Örneğin, mevcut grafik koleksiyonunu almak için Worksheet.charts özelliğini kullanabilirsiniz.

#### **Bir Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiği oluşturmanın nasıl yapıldığını göstermektedir. Bu grafiği daha sonra manipüle edeceğiz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Pyramid Chart</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Grafiği Manipüle Etmek**
Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğimizi göstermektedir. Bu örnekte, yukarıda oluşturulan grafiği değiştireceğiz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığına dikkat edin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pie Chart Data Label Update</title>
    </head>
    <body>
        <h1>Update Pie Chart Data Label Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Get the data labels in the data series of the third data point.
            const dataLabels = chart.nSeries.get(0).points.get(2).dataLabels;

            // Change the text of the label.
            dataLabels.text = "Unided Kingdom, 400K ";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**
Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);

            // Add the third data series to it.
            chart.nSeries.add("{60, 80, 10}", true);

            // Add another data series (fourth) to it.
            chart.nSeries.add("{0.3, 0.7, 1.2}", true);

            // Plot the fourth data series on the second axis.
            chart.nSeries.get(3).plotOnSecondAxis = true;

            // Change the Border color of the second data series.
            chart.nSeries.get(1).border.color = AsposeCells.Color.Green;

            // Change the Border color of the third data series.
            chart.nSeries.get(2).border.color = AsposeCells.Color.Red;

            // Make the second value axis visible.
            chart.secondValueAxis.isVisible = true;

            // Save the excel file and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
