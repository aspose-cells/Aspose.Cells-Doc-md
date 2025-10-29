---
title: Скрытие отображения нулевых значений в листе с помощью JavaScript через C++
linktitle: Скрытие отображения нулевых значений в таблице
type: docs
weight: 50
url: /ru/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: В этой статье приведён пример кода, объясняющий, как программно скрыть нулевые значения в таблице Excel с помощью библиотеки JavaScript через C++.
keywords: скрыть нулевые значения листа Excel с помощью JavaScript через C++
---

{{% alert color="primary" %}} 

Иногда вам нужно скрывать нулевые значения в электронной таблице. Это может быть личным предпочтением или стандартом форматирования.

{{% /alert %}} 

Чтобы скрыть нулевые значения в таблице Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Инструменты** выберите **Параметры**, затем выберите вкладку **Вид**.
1. Отмените выбор опции **Нулевые значения**.
1. Нажмите **ОК**.

Пожалуйста, ознакомьтесь с примером кода ниже, демонстрирующим скрытие нулей с помощью Aspose.Cells for JavaScript через C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
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

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
