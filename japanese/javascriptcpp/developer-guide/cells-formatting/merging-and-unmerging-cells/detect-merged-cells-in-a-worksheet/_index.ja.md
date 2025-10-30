---
title: ワークシート内のマージセルを検出する方法をC++経由のJavaScriptで学びます。
linktitle: ワークシート内の結合セルを検出
description: Aspose.Cells for JavaScript経由でC++を使用して、マージセルを検出する方法を学びます。ライブラリを使用してマージセルを特定・操作するテクニックを紹介します。
keywords: Aspose.Cells、ワークシート、セルのマージ、検出、識別、操作JavaScript via C++
type: docs
weight: 80
url: /ja/javascript-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

この記事では、ワークシート内の結合セル領域を取得する方法について説明しています。

Aspose.Cells for Javaスクリプト（C++経由）は、ワークシートのセル結合範囲を取得することを可能にします。解除（分割）も可能です。この記事では、**Aspose.Cells API**を使用してこの作業を行う最も簡単なコード例を示します。

{{% /alert %}}

このコンポーネントは、すべての結合セルを取得できる [**Cells.mergedAreas**](https://reference.aspose.com/cells/javascript-cpp/cells/#mergedAreas--) メソッドを提供します。以下のコード例はワークシート内の結合セルを検出する方法を示しています。

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
