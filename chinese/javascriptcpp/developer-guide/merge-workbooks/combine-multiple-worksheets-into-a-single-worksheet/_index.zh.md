---
title: 使用JavaScript通过C++将多个工作表合并为一个工作表。
linktitle: 将多个工作表合并为单个工作表
type: docs
weight: 160
url: /zh/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: 学习如何使用8647720447Script通过C++将多个工作表合并为一个工作表。 
---

{{% alert color="primary" %}} 

有时候，您需要将多个工作表合并成一个工作表。通过使用 Aspose.Cells API，可以轻松实现这一目标。本文将展示一个代码示例，该示例读取源工作簿，并将所有源工作表的数据合并到目标工作簿中的一个工作表中。

{{% /alert %}} 

以下代码片段向您展示了如何将多个工作表合并为单个工作表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Worksheets into One Workbook</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const destWorkbook = new Workbook();
            const destSheet = destWorkbook.worksheets.get(0);

            let TotalRowCount = 0;

            for (let i = 0; i < workbook.worksheets.count; i++) {
                const sourceSheet = workbook.worksheets.get(i);

                const sourceRange = sourceSheet.cells.maxDisplayRange;
                const destRange = destSheet.cells.createRange(
                    sourceRange.firstRow + TotalRowCount,
                    sourceRange.firstColumn,
                    sourceRange.rowCount,
                    sourceRange.columnCount
                );

                destRange.copy(sourceRange);
                TotalRowCount += sourceRange.rowCount;
            }

            const outputData = destWorkbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook merged successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
