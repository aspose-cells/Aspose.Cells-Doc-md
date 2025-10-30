---
title: JavaScriptを使用してC++経由で帳票とワークシートにスコープ付きに名前付き範囲を作成
linktitle: 名前付き範囲
type: docs
weight: 40
url: /ja/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: C++を通じてAspose.Cells for JavaScriptを使用して帳票とワークシートのスコープ付き名前付き範囲の作成方法を学習 
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ワークブック（またはグローバルスコープとしても知られています）とワークシートの2つの異なるスコープで名前付き範囲を定義できます。

- ワークブックスコープの名前付き範囲は、そのワークブック内の任意のワークシートから、名前を単純に使用することでアクセスできます。
- ワークシートスコープの名前付き範囲は、それが作成された特定のワークシートの参照でアクセスされます。

Aspose.Cells for JavaScriptは、Microsoft Excelと同じ機能を持ち、帳票とワークシートのスコープ付き名前付き範囲の追加をサポートします。ワークシートスコープの名前付き範囲を作成する場合、範囲を指定するためにワークシート参照を使用してください。

{{% /alert %}} 
## **ブックスコープで名前を付けられた範囲を追加する**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>WorkbookScope Named Range Example</title>
    </head>
    <body>
        <h1>WorkbookScope Named Range Example</h1>
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

            // If a file is provided, load it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells from Cell A1 to C10
            const workbookScope = cells.createRange("A1", "C10");

            // Assign the name to workbook scope named range
            workbookScope.name = "workbookScope";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookScope.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range "workbookScope" created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
## **ワークシートスコープを持つ名前付き範囲を追加する**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Assign Range Name Example</h1>
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

            // Create new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells
            const localRange = cells.createRange("A1", "C10");

            // Assign name to range with sheet reference
            localRange.name = "Sheet1!local";

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [アクセスの作成とコピーした名前付き範囲](/cells/ja/javascript-cpp/create-access-and-copy-named-ranges/)
- [名前付き範囲の書式と変更](/cells/ja/javascript-cpp/format-and-modify-named-ranges/)
- [外部リンク付きの範囲を取得する](/cells/ja/javascript-cpp/get-range-with-external-links/)
- [非連続範囲の実装](/cells/ja/javascript-cpp/implementing-non-sequential-ranges/)
