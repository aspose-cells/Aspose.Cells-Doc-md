---
title: Копирование Sparklines с указанием диапазона данных и местоположения группы Sparkline с помощью JavaScript через C++
linktitle: Копирование мини графиков, указав диапазон данных и расположение группы мини графиков
type: docs
weight: 300
url: /ru/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Узнайте, как скопировать sparklines в Excel, указав диапазон данных и расположение группы спарклайнов с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}
Microsoft Excel позволяет копировать минидиаграмму, указывая диапазон данных и местоположение группы минидиаграмм. Aspose.Cells поддерживает эту функцию.
{{% /alert %}}

Для копирования минидиаграммы в другие ячейки в Microsoft Excel:

1. Выберите ячейку, содержащую минидиаграмму.  
1. Выберите **Edit Data** в разделе **Sparkline** вкладки **Design**.  
1. Выберите **Edit Group Location & Data**.  
1. Укажите диапазон данных и местоположение.  
1. Нажмите **ОК**.

Aspose.Cells предоставляет метод `SparklineCollection.add(dataRange, row, column)` для указания диапазона данных и положения группы Sparkline. Следующий пример кода загружает исходный файл Excel, как показано на снимке выше, затем обращается к первой группе Sparkline и добавляет диапазоны данных и позиции в группу. В конце он сохраняет итоговый файл Excel на диск, как показано на снимке выше.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
