---
title: Сначала заполните данные по строкам, а затем по столбцам
type: docs
weight: 1000
url: /ru/javascript-cpp/populate-data-first-by-row-then-by-column/
description: Изучите, как сначала заполнить данными по строкам, а затем по столбцам с помощью API Aspose.Cells for JavaScript через C++.
keywords: Заполнение данных сначала по строкам, затем по столбцам через JavaScript с использованием C++, вставка данных сначала по строкам, затем по столбцам через JavaScript с использованием C++, добавление данных сначала по строкам, затем по столбцам через JavaScript с использованием C++, высокопроизводительная вставка данных через JavaScript через C++, высокопроизводительное добавление данных через JavaScript с использованием C++
---

{{% alert color="primary" %}}  

Заполнение электронной таблицы данными сначала по строкам, а затем по столбцам улучшает общую производительность.  

{{% /alert %}}  

Размещение данных в последовательности A1, B1, A2, B2 быстрее, чем A1, A2, B1, B2. Если в листе большое количество ячеек и вы следуете второй последовательности, то есть заполняете данные строка за строкой, этот совет может значительно ускорить программу.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
