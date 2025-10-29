---
title: Обработка автоматических единиц оси графика, как в Microsoft Excel, с помощью JavaScript через C++
linktitle: Обработка автоматических единиц оси диаграммы, как в Microsoft Excel
description: Узнайте, как управлять автоматическими единицами на осях графика с помощью Aspose.Cells for JavaScript через C++. Наш гид покажет, как настроить и адаптировать автоматические единицы на оси графика, включая отображение научной нотации и изменение масштаба.
keywords: Aspose.Cells for JavaScript через C++, оси графика, автоматические единицы, Microsoft Excel, настройка, кастомизация, научная нотация, масштабирование.
type: docs
weight: 120
url: /ru/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Возможные сценарии использования**  
Ранние версии Aspose.Cells for JavaScript через C++, не могли правильно обрабатывать автоматические единицы оси графика при выводе его в изображение или PDF. Сейчас, Aspose.Cells for JavaScript через C++ поддерживает обработку автоматических единиц оси графика. Никаких изменений в коде не требуется. Просто преобразуйте график в изображение или PDF, и он будет отображать ось так же, как это делает Microsoft Excel.  

## **Обработка автоматических единиц оси диаграммы, как в Microsoft Excel**  
Следующий пример кода загружает [образец Excel файла](61767755.xlsx) и создает [выходной PDF с диаграммой](61767752.pdf). Скриншот показывает автоматические единицы оси диаграммы в красных прямоугольниках и сравнивает диаграмму из файла Excel с PDF-выводом. Оба точно совпадают.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Образец кода**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
