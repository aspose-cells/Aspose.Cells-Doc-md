---
title: C++を通じてJavaScriptを使用した範囲内のデータ検索と置換
linktitle: 範囲内のデータを検索および置換する
type: docs
weight: 170
url: /ja/javascript-cpp/search-and-replace-data-in-a-range/
description: この記事では、C++コードを使用してExcelの範囲内のデータを検索・置換する方法を説明します。
keywords: JavaScriptを使用したExcelの範囲内のデータ検索と置換、Excel内のデータ検索、範囲内のデータを検索・置換、範囲内のデータを検索、範囲内のデータ検索、Excel内のデータ検索、範囲内のデータ検索、JavaScriptを用いた範囲内のデータ検索、JavaScriptを使用した範囲内のデータ検索と置換、範囲内のデータを検索・置換
---

{{% alert color="primary" %}}

特定の範囲内のセル値を無視して検索と置換を行う必要がある場合があります。Aspose.Cells for JavaScriptをC++で使用すると、検索範囲を限定できます。この記事では、その方法について説明します。

{{% /alert %}}

C++を通じてAspose.Cells for JavaScriptは、データ検索時に範囲を指定するための[**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-)メソッドを提供します。以下のコード例は、範囲内のデータの検索と置換を行います。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
