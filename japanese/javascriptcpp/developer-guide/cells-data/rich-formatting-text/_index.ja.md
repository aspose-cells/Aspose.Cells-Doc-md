---
title: セルのリッチテキストの一部をアクセスして更新する
linktitle: リッチフォーマットテキスト
type: docs
weight: 40
url: /ja/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: セルのリッチテキスト部分のアクセスと更新方法をAspose.Cells for JavaScriptはC++経由で学びます。
keywords: セルのリッチテキストへのアクセスおよび更新、セルのリッチテキストの取得、セルのリッチテキストの編集、セルのリッチテキストへのアクセス、セルのリッチテキストの更新、セルのリッチテキストの変更
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScriptはC++経由でセルのリッチテキスト部分のアクセスと更新を可能にします。その目的のために、[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)と[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)のプロパティを使用できます。これらのプロパティはフォント名、フォント色、太字などさまざまなフォントのプロパティにアクセスしたり更新したりするための[**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)オブジェクトの配列を返したり受け取ったりします。

{{% /alert %}}

## **セルのリッチテキストの部分にアクセスして更新**

以下のコードは、提供されたリンクからダウンロード可能な[ソースエクセルファイル](5112369.xlsx)を使用して、[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)と[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)のプロパティの使用例を示しています。ソースエクセルファイルのセルA1にはリッチテキストがあり、3つの部分と異なるフォントが設定されています。以下のコードスニペットはこれらの部分にアクセスし、最初の部分のフォント名を新しいものに更新し、その後ワークブックを[出力エクセルファイル](5112366.xlsx)として保存します。開くと、最初の部分のフォントが**"Arial"**に変更されているのがわかります。

### JavaScriptを用いたセルのリッチテキスト部分へのアクセスと更新のコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### サンプルコードによって生成されたコンソール出力



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
