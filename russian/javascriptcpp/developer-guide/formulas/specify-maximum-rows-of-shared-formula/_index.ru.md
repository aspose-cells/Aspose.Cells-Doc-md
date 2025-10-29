---
title: Задайте максимальное количество строк для разделяемой формулы с помощью JavaScript через C++
linktitle: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Узнайте, как указать максимальное количество строк для разделяемых формул с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Максимальное количество строк для общей формулы по умолчанию — 64. Оно может быть любым числом, например, 1000. Производительность общей формулы зависит от этого числа. Поэтому Aspose.Cells предоставляет свойство [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--), которое можно использовать для задания максимального количества строк. Общая формула будет разбита на несколько частей, если общее число строк превысит указанное значение, как показано на следующем скриншоте.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Укажите максимальное количество строк общей формулы**  

Следующий пример кода демонстрирует использование свойства [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). Он устанавливает максимум в 5 строк для общей формулы и добавляет общую формулу в ячейку D1 для 100 строк, сохраняет файл и выводит его как [выходной Excel-файл](61767856.xlsx). Если раскрыть содержимое файла и проверить *sheet1.xml*, увидите, что разделение общей формулы происходит каждые 5 строк, что выделено на скриншоте выше.  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
