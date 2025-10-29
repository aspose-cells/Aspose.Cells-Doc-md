---
title: 使用JavaScript通过C++检测工作表中的合并单元格
linktitle: 检测工作表中的合并单元
description: 了解如何使用Aspose.Cells for JavaScript通过C++检测工作表中的合并单元格。本文将向你展示如何使用库来识别和操作合并单元格。
keywords: Aspose.Cells，工作表，合并单元格，检测，识别，操作JavaScript通过C++
type: docs
weight: 80
url: /zh/javascript-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

本文介绍如何在工作表中获取合并的单元区域。

Aspose.Cells for JavaScript通过C++允许你获取工作表中的合并区域。你也可以取消合并（拆分）它们。本文展示了使用**Aspose.Cells API**完成此任务的最简代码。

{{% /alert %}}

该组件提供 [**Cells.mergedAreas**](https://reference.aspose.com/cells/javascript-cpp/cells/#mergedAreas--) 方法，可以获取所有合并单元格。以下示例代码演示如何在工作表中检测合并单元格。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unmerge Areas</title>
    </head>
    <body>
        <h1>Unmerge Merged Areas Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook by opening the uploaded excel file
            const wkBook = new Workbook(new Uint8Array(arrayBuffer));

            // Get a worksheet in the workbook
            const wkSheet = wkBook.worksheets.get("Sheet2");

            // Clear its contents
            wkSheet.cells.clear();

            // Get merged areas
            const areas = wkSheet.cells.mergedAreas;

            // Check if areas is null or not
            if (!areas || areas.length === 0) {
                console.warn("No merged areas to unmerge.");
                resultDiv.innerHTML = '<p style="color: orange;">No merged areas to unmerge.</p>';
                return;
            }

            // Define some variables
            let frow, fcol, erow, ecol, trows, tcols;
            // Loop through the arraylist and get each cellarea
            // To unmerge it
            for (let i = 0; i < areas.length; i++) {
                frow = areas[i].startRow;
                fcol = areas[i].startColumn;
                erow = areas[i].endRow;
                ecol = areas[i].endColumn;

                trows = erow - frow + 1;
                tcols = ecol - fcol + 1;
                wkSheet.cells.unMerge(frow, fcol, trows, tcols);
            }

            // Saving the modified Excel file and provide download link
            const outputData = wkBook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MergeTrial.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Merged areas unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
