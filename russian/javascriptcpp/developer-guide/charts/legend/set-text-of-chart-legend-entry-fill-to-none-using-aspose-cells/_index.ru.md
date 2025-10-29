---
title: Установить цвет заливки текста в пунктах легенды диаграммы в значение none с помощью Aspose.Cells for JavaScript через C++
linktitle: Установите текст заливки записи легенды диаграммы на отсутствие с использованием Aspose.Cells
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для установки заливки элемента легенды диаграммы как «Нет». Этот гайд покажет, как изменять цвет заливки элементов легенды в диаграммах Microsoft Excel для лучшей визуализации и настройки.
keywords: Aspose.Cells for JavaScript через C++, Заливка элемента легенды диаграммы, Microsoft Excel, Визуализация, Настройка.
type: docs
weight: 320
url: /ru/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Если хотите установить цвет заливки пункта легенды графика в none, чтобы он не отображался внутри легенды графика, установите [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--) в **true**.

{{% /alert %}}

В следующем образце кода устанавливается текст заливки второй записи легенды графика на никуда. Скачайте [образец excel-файла](5115219.xlsx), использованный в этом коде, и [выходной excel-файл](5115217.xlsx), который он создает, для вашего ориентира.

Следующий снимок экрана демонстрирует эффект этого кода на [пример файле Excel](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
