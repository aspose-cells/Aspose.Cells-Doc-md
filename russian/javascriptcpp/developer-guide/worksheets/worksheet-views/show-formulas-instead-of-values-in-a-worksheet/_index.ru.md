---
title: Показать формулы вместо значений в листе с помощью JavaScript через C++
linktitle: Показать формулы вместо значений в рабочем листе
type: docs
weight: 20
url: /ru/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: В этой статье представлен пример кода для использования API JavaScript через C++ для программного отображения формул, а не значений, в листе или таблице Excel.
---

{{% alert color="primary" %}}

Возможно показывать формулы вместо вычисленных значений в Microsoft Excel с помощью опции «Показать формулы» на ленте «Формулы». При отображении формул Microsoft Excel показывает формулы в листе. Вы можете добиться того же с помощью Aspose.Cells for JavaScript через C++.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--). Установите его в **true**, чтобы задать отображение формул в Microsoft Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
