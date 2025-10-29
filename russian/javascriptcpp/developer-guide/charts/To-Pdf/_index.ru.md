---
title: Преобразование диаграммы в PDF с помощью JavaScript через C++
linktitle: Диаграмма в PDF
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для преобразования диаграммы в PDF документ. В этом руководстве показано, как экспортировать диаграмму из Microsoft Excel и сохранить ее как PDF для дальнейшего распространения и архивации.
keywords: Aspose.Cells for JavaСкрипт через C++, Диаграмма в PDF, Microsoft Excel, Конвертация PDF, Экспорт, Распространение, Архивация.
type: docs
weight: 47
url: /ru/javascript-cpp/chart-to-pdf/
---

## **Отображение диаграммы в формат PDF**

Чтобы отобразить диаграмму в формате PDF, API Aspose.Cells предоставили метод [**Chart.toPdf(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toPdf-string-) с возможностью сохранить полученный PDF на диск или в поток.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart to PDF</title>
    </head>
    <body>
        <h1>Chart to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();
            // Add a new worksheet
            const sheetIndex = workbook.worksheets.add();
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);
            const chart = worksheet.charts.get(chartIndex);

            // Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Converting chart to PDF
            const outputData = chart.toPdf();
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chartPDF_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to PDF successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Создание PDF-файла диаграммы с выбранным размером страницы**  
Вы можете создать PDF диаграммы с желаемым размером страницы, используя Aspose.Cells, и указать, как вы хотите выровнять диаграмму внутри страницы: сверху, снизу, по центру, слева, справа и т.д. Также результативная диаграмма может быть создана в потоке или на диске. Ознакомьтесь с примером кода, который загружает [образец файла Excel](64716906.xlsx), получает первую диаграмму в листе и конвертирует её в [выходной PDF](64716907.pdf) с нужным размером страницы. Следующий скриншот показывает, что размер страницы в выходном PDF — 7x7, как указано в коде, а диаграмма выровнена по центру как по горизонтали, так и по вертикали.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Образец кода**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Chart PDF With Desired Page Size</title>
    </head>
    <body>
        <h1>Create Chart PDF With Desired Page Size</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet.
            const chart = worksheet.charts.get(0);

            // Create chart pdf with desired page size.
            // Note: In browser API omit file path and receive output data (Uint8Array / ArrayBuffer)
            const outputData = chart.toPdf(7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateChartPDFWithDesiredPageSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
