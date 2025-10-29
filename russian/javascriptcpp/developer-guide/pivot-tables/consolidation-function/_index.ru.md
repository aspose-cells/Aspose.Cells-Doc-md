---
title: Функция консолидации
type: docs
weight: 20
url: /ru/javascript-cpp/consolidation-function/
description: Как применить функцию объединения (ConsolidationFunction) к полям данных сводной таблицы с помощью Aspose.Cells for JavaScript на C++.
keywords: Aspose.Cells for JavaScript для Excel на C++, библиотека Excel JavaScript, использование функции объединения (ConsolidationFunction) к полям данных сводной таблицы с помощью Aspose.Cells for JavaScript для Excel на C++.
---

## **Функция консолидации**

Aspose.Cells for JavaScript на C++ можно использовать для применения функции объединения (ConsolidationFunction) к полям данных (или значений) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши по полю значений и выбрать опцию **Настройка поля значения...**, затем перейти на вкладку **Сводка значений по**. Там вы можете выбрать любую функцию объединения по вашему выбору, например Sum, Count, Average, Max, Min, Product, Distinct Count и др.

Aspose.Cells for JavaScript на C++ предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/), поддерживающее следующие функции объединения.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Как применить функцию объединения к полям данных сводной таблицы с помощью Aspose.Cells for JavaScript на C++**

Следующий код применяет функцию объединения **Среднее** к первому полю данных (или значению) и функцию объединения **Уникальное количество** ко второму полю данных (или значению).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Функция консолидации УНИКАЛЬНОЕ_КОЛИЧЕСТВО поддерживается только в Microsoft Excel 2013.

{{% /alert %}}
