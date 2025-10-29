---
title: Установка разделяемой формулы с помощью JavaScript через C++
linktitle: Настройка общих формул
type: docs
weight: 10
url: /ru/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Если вы хотите добавить функцию в лист, которая будет выполнять некоторые вычисления, эта статья объясняет, как это сделать с помощью Aspose.Cells for JavaScript через C++.

{{% /alert %}}

## Установка разделяемой формулы с помощью Aspose.Cells for JavaScript через C++

Предположим, у вас есть лист с данными в формате, который выглядит как приведенный ниже образец листа.

|**Входной файл с одним столбцом данных**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Вы хотите добавить функцию в B2, которая будет вычислять налог с продаж для первой строки данных. Налог составляет **9%**. Формула, вычисляющая налог с продаж, такова: **"=A2*0.09"**. В этой статье объясняется, как применить эту формулу с помощью Aspose.Cells.

Aspose.Cells позволяет указывать формулу, используя свойство [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--). Для других ячеек (B3, B4, B5 и так далее) в столбце есть два варианта добавления формул.

Либо выполните то, что вы делали для первой ячейки, фактически устанавливая формулу для каждой ячейки, соответствующим образом обновляя ссылку на ячейку (A3*0.09, A4*0.09, A5*0.09 и так далее). Это требует обновления ссылок на ячейки для каждой строки. Также необходимо, чтобы Aspose.Cells анализировал каждую формулу отдельно, что может быть затратным по времени для больших таблиц и сложных формул. Кроме того, это требует дополнительных строк кода, хотя циклы могут немного сократить их.

Другой подход - использовать **общую формулу**. С общей формулой формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы налог был рассчитан правильно. Метод [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) более эффективен, чем первый метод.

Приведенный ниже пример демонстрирует, как его использовать.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
