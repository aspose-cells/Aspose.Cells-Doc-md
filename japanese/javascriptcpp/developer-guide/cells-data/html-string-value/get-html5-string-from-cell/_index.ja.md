---
title: セルから HTML5 文字列を取得
type: docs
weight: 90
url: /ja/javascript-cpp/get-html5-string-from-cell/
description: CellからHTML5文字列を取得する方法をAspose.Cells for JavaScript経由でC++ APIを通じて学びます。
keywords: セルからHTML5文字列を取得、JavaScript経由でセルのHTML5文字列を取得、C++でセルのHTML5文字列を管理します。
---

## **可能な使用シナリオ**

Aspose.Cellsは、ブールパラメータを受け取る[**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-)メソッドを使用してセルのHTML文字列を返します。パラメータに**false**を渡すと通常のHTMLを返し、**true**を渡すとHTML5文字列を返します。

## **セルからHTML5文字列を取得**

次のサンプルコードはワークブックオブジェクトを作成し、最初のシートのセルA1にいくつかのテキストを追加します。その後、セルA1から通常のHTMLとHTML5文字列を[**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-)メソッドを使って取得し、コンソールに出力します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Get HTML String from Cell</h1>
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
            // This example creates a new workbook, writes text to A1 and retrieves HTML strings.
            const wb = new Workbook();

            const ws = wb.worksheets.get(0);

            const cell = ws.cells.get("A1");
            cell.value = "This is some text.";

            const strNormal = cell.htmlString;
            const strHtml5 = cell.htmlString;

            console.log("Normal:\r\n" + strNormal);
            console.log();
            console.log("Html5:\r\n" + strHtml5);

            document.getElementById('result').innerHTML =
                '<h2>Results</h2>' +
                '<p><strong>Normal:</strong></p><pre>' + escapeHtml(strNormal) + '</pre>' +
                '<p><strong>Html5:</strong></p><pre>' + escapeHtml(strHtml5) + '</pre>' +
                '<p style="color: green;">Operation completed successfully!</p>';
        });

        function escapeHtml(text) {
            if (text === null || text === undefined) return "";
            return String(text)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }
    </script>
</html>
```


## **コンソール出力**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
