---
title: Перенос строк и перенос текста
linktitle: Перенос строк и перенос текста
description: Как реализовать перенос текста и автоматический перенос слов с помощью библиотеки Aspose.Cells в JavaScript через C++. Используя библиотеку Aspose.Cells, вы можете легко вставлять текст в ячейки и настраивать методы переноса текста, такие как ручной перенос, автоматический перенос и т.д. В этом документе подробно описывается, как реализовать эти функции, и приводится пример кода для справки.
keywords: Aspose.Cells, перенос строк, перенос текста, макет текста JavaScript через C++
type: docs
weight: 60
url: /ru/javascript-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}
Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.
{{% /alert %}}

## **Перенос текста в ячейке**
Чтобы переносить текст внутри ячейки, используйте метод [**Aspose.Cells.Style.isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook
            }

            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cell = ws.cells;

            // Increase the width of First Column Width
            cell.columns.get(0).width = 35;

            // Increase the height of first row
            cell.rows.get(0).height = 36;

            // Add Text to the First Cell
            const firstCell = cell.checkCell(0, 0);
            firstCell.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Использование явных переносов строк**
Вы можете использовать '\n' в JavaScript для вставки явных переносов строк в ячейке.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // No file selected - create a new workbook
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 65;

            // Add Text to the First Cell with Explicit Line Breaks
            const firstCell = cells.checkCell(0, 0);
            firstCell.putValue("I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
