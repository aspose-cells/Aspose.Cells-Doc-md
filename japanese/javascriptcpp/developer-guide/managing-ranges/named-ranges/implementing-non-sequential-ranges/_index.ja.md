---
title: JavaScriptとC++を使用して非連続範囲を実装する
linktitle: 非連続範囲の実装
type: docs
weight: 700
url: /ja/javascript-cpp/implementing-non-sequential-ranges/
description: Aspose.Cells for JavaScriptを用いて非連続範囲の作成方法を学び、非隣接セル範囲を効果的に利用しましょう。
---

{{% alert color="primary" %}} 

通常、名前付範囲は連続した矩形でセルが隣接しています。しかし、時にはセルが隣接しない非連続のセル範囲を使用する必要があります。Aspose.Cells for JavaScriptは非隣接セルを持つ範囲を作成することもサポートしています。

{{% /alert %}} 

以下のコードサンプルは、Aspose.Cells for JavaScriptを用いて非連続範囲の名前付範囲を作成する方法を示しています。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add NonSequenced Range Name</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a Name for non sequenced range
            const index = workbook.worksheets.names.add("NonSequencedRange");

            const name = workbook.worksheets.names.get(index);

            // Creating a non sequence range of cells
            name.refersTo = "=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6";

            // Saving the workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and name added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
