---
title: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/javascript-cpp/get-html5-string-from-cell/
description: 学习如何通过Aspose.Cells for JavaScript通过C++ API从单元格获取HTML5字符串。
keywords: 从单元格获取HTML5字符串 JavaScript via C++，从单元格获取HTML5字符串 JavaScript，通过C++管理单元格的HTML5字符串
---

## **可能的使用场景**

Aspose.Cells 使用 [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) 方法返回单元格的HTML字符串，该方法接受一个布尔参数。如果传递 **false**，将返回普通HTML；如果传递 **true**，将返回HTML5字符串。

## **从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后，它通过 [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) 方法获取A1单元格的普通HTML和HTML5字符串，并在控制台打印它们。

## **示例代码**

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


## **控制台输出**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
