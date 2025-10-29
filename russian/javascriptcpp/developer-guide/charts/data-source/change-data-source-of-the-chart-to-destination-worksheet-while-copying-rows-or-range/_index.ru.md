---
title: Изменение источника данных графика на рабочий лист назначения при копировании строк или диапазона с помощью JavaScript через C++
linktitle: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона
description: Узнайте, как изменить источник данных графика на рабочий лист назначения при копировании строк или диапазона в Aspose.Cells for JavaScript через C++. Это руководство показывает, как обновить диапазон данных графика и связать его с рабочим листом назначения.
keywords: Aspose.Cells for JavaScript через C++, построение графиков, источник данных, рабочий лист назначения, строки, диапазон, копирование, обновление, диапазон данных, связь.
type: docs
weight: 440
url: /ru/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Возможные сценарии использования**

Когда вы копируете строки или диапазон, содержащий диаграммы, на новый лист, источник данных диаграммы не изменяется. Например, если источник данных диаграммы `=Sheet1!$A$1:$B$4`, то после копирования строк или диапазона на новый лист, источник данных останется таким же - `=Sheet1!$A$1:$B$4`. Он по-прежнему ссылается на старый лист, то есть Sheet1. Это поведение также в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый целевой лист, используйте свойство [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) и задайте его значение **true** при вызове метода [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-). Например, если ваш целевой лист DestSheet, источник данных диаграммы изменится с `=Sheet1!$A$1:$B$4` на `=DestSheet!$A$1:$B$4`.

## **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**

Следующий пример кода объясняет использование свойства [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) при копировании строк или диапазона с диаграммами на новый лист. Код использует [образец файла Excel](5113699.xlsx) и создает [выходной файл Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
