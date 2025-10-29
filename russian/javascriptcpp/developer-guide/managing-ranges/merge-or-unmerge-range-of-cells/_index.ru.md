---
title: Объединение или отмена объединения диапазона ячеек с помощью JavaScript через C++
linktitle: Объединение или разъединение диапазона ячеек
type: docs
weight: 190
url: /ru/javascript-cpp/merge-or-unmerge-range-of-cells/
description: Объединение и разъединение ячеек в диапазоне в Excel с помощью JavaScript через C++ код.
keywords: Объединение и разъединение ячеек в диапазоне с помощью JavaScript, объединение и разъединение ячеек в диапазоне, объединять и разъединять ячейки с помощью JavaScript, использовать JavaScript для объединения и разъединения ячеек, объединять и разъединять ячейки в Excel с помощью JavaScript, объединять и разъединять ячейки в Excel с помощью JavaScript, объединение и разъединение ячеек в Excel с помощью JavaScript, объединение ячеек в Excel, разъединение ячеек в Excel, объединение ячеек в диапазоне с помощью JavaScript
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для объединения или разделения диапазона ячеек. Aspose.Cells предоставляет методы [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) и [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) для этой цели. В этой статье объясняется, как объединить диапазон ячеек в одну ячейку.

{{% /alert %}}

## **Пример**

Следующий пример кода сначала создает диапазон - A1:D4 - затем объединяет ячейки в диапазоне в одну с помощью метода [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--). Аналогично, можно разбить ячейки, создав диапазон и вызвав метод [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create and Merge Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeInitialized = false;
        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeInitialized = true;
            runButton.disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait.</p>';
                return;
            }

            // Creating a workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range
            const range = worksheet.cells.createRange("A1:D4");

            // Merge range into a single cell
            range.merge();

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range merged successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
