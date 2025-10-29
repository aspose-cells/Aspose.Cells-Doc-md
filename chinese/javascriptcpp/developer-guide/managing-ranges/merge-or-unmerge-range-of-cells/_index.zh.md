---
title: 使用JavaScript via C++合并或取消合并单元格区域
linktitle: 合并或取消合并单元格范围
type: docs
weight: 190
url: /zh/javascript-cpp/merge-or-unmerge-range-of-cells/
description: 使用C++的JavaScript在Excel中合并和取消合并范围内的单元格。
keywords: 使用JavaScript在Excel中合并和取消合并单元格，使用JavaScript在范围内合并和取消合并单元格，使用JavaScript在Excel中合并和取消合并单元格，使用JavaScript在范围内合并和取消合并单元格，使用JavaScript在Excel中合并和取消合并单元格，使用JavaScript在Excel中合并和取消合并单元格，JavaScript在Excel中合并和取消合并单元格，JavaScript在Excel中合并单元格，JavaScript在Excel中取消合并单元格，用JavaScript在范围内合并单元格
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 来合并或拆分一系列单元格。Aspose.Cells 为此提供了 [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) 和 [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) 方法。本文解释了如何将一系列单元格合并为单个单元格。

{{% /alert %}}

## **示例**

以下示例代码首先创建一个范围 — A1:D4 — 然后使用[**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--)方法将该范围中的单元格合并成一个单元格。类似地，你也可以通过创建范围并调用[**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--)方法来拆分单元格。

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
