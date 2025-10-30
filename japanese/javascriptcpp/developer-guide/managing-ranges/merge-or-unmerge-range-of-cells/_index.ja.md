---
title: JavaScriptを使用してセル範囲の結合または結合解除（C++経由）
linktitle: セル範囲の結合または解除
type: docs
weight: 190
url: /ja/javascript-cpp/merge-or-unmerge-range-of-cells/
description: ExcelでC++コードを使用して範囲内のセルの結合と解除
keywords: JavaScriptを使用した範囲内のセルの結合と解除、範囲内のセルをJavaScriptで結合・解除、ExcelでJavaScriptを使ったセルの結合と解除、JavaScriptでExcelのセルを結合および解除、JavaScriptでExcelのセルを結合・解除、ExcelのセルをJavaScriptで結合・解除、ExcelのセルをJavaScriptで結合・解除、JavaScriptでExcelのセルを結合、JavaScriptでExcelのセルの結合解除、JavaScriptを使用した範囲内のセルを結合
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してセルの範囲を結合または分割できます。 Aspose.Cellsはこの目的のための[**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--)および[**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--)メソッドを提供します。この記事では、セルの範囲を単一のセルに結合する方法について説明します。

{{% /alert %}}

## **例**

以下のサンプルコードは、最初に範囲（A1:D4）を作成し、その範囲内のセルを[**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--)メソッドを使って1つのセルにマージします。同様に、範囲を作成し、[**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--)メソッドを呼び出すことでセルを分割できます。

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
