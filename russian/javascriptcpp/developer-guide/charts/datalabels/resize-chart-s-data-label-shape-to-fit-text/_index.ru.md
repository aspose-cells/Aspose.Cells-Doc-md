---
title: Изменение размера формы подписи данных диаграммы для соответствия тексту с помощью JavaScript через C++
linktitle: Изменение формы метки данных диаграммы для подгонки текста
description: Узнайте, как изменять размер формы подписи данных в диаграмме, чтобы она подходила под текст, в Aspose.Cells for JavaScript через C++. Наше руководство покажет, как настраивать размер и форму контейнера метки для правильного отображения текста без усадки или пересечения.
keywords: Aspose.Cells for JavaScript через C++, создание диаграмм, подписи данных, изменение размера формы, соответствие текста, усадка, пересечения.
type: docs
weight: 220
url: /ru/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Приложение Excel предлагает опцию **Изменить форму для подгонки текста** для подписей данных диаграммы, чтобы увеличить размер формы так, чтобы текст помещался внутри нее  
{{% /alert %}}  

## **Как изменить форму подписей данных в диаграмме, чтобы они соответствовали тексту в Microsoft Excel**  

Этот параметр можно получить в интерфейсе Excel, выбрав любую метку данных на диаграмме. Щелкните правой кнопкой мыши и выберите меню **Формат меток данных**. На вкладке **Размер и свойства** разверните раздел **Выравнивание**, чтобы открыть связанные свойства, включая опцию **Изменить форму для фиксации текста**.  

## **Как изменить размер формы подписи данных диаграммы, чтобы она соответствовала тексту, с помощью Aspose.Cells for JavaScript через C++**  

Чтобы имитировать функцию Excel по изменению размера форм меток данных для соответствия текста, API Aspose.Cells предоставил булевое свойство [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--). В следующем примере показано простое использование сценария свойства [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
