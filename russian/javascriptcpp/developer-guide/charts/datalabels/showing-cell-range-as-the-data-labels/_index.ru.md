---
title: Отображение диапазона ячеек как метки данных с помощью JavaScript через C++
linktitle: Отображение диапазона ячеек в качестве меток данных
description: Узнайте, как отображать диапазон ячеек в качестве меток данных на графиках с помощью Aspose.Cells for JavaScript через C++. Наше руководство покажет, как связать метки с источником данных и форматировать их для предоставления точной и значимой информации на ваших графиках.
keywords: Aspose.Cells for JavaScript с помощью C++, построение графиков, метки данных, диапазон ячеек, источник данных, форматирование, точность, значимая информация.
type: docs
weight: 130
url: /ru/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
В Microsoft Excel 2013 можно отображать диапазон ячеек для меток данных. Aspose.Cells for JavaScript с помощью C++ поддерживает эту функцию.
{{% /alert %}}

## **Флажок для отображения диапазона ячеек в качестве меток данных**

Чтобы показать диапазон ячеек в качестве меток данных в Microsoft Excel:

1. Выберите метки данных ряда и щелкните правой кнопкой мыши, чтобы открыть контекстное меню.  
1. Выберите **Формат меток данных**. Опции меток отображаются.  
1. Выберите или снимите флажок у опции **Метка содержит - значение из ячеек**.  

Пример кода ниже получает метки данных серии диаграммы и устанавливает свойство [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) в **true**, чтобы выбрать опцию **Label Contains - Value From Cells**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
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
