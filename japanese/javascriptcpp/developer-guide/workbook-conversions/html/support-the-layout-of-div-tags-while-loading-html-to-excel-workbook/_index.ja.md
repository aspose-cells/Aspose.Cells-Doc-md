---
title: JavaScriptを使用してC++でHTMLをExcelのワークブックにロードするとき、DIVタグのレイアウトをサポートします
linktitle: HTMLをExcelワークブックに読み込む際に、DIVタグのレイアウトをサポートします。
type: docs
weight: 50
url: /ja/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}}
通常、HTMLをExcelワークブックオブジェクトに読み込む際に、divタグのレイアウトは無視されます。ただし、divタグのレイアウトを無視しないようにしたい場合は、[HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--)プロパティを **true** に設定してください。このプロパティのデフォルト値は **false**です。
{{% /alert %}}

以下のサンプルコードは、[HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--)プロパティの使用例を示しています。入力HTML内で使用されるAsposeロゴ（5115218.png）と、コードによって生成された出力Excelファイル（5115220.xlsx）をダウンロードしてください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat, Utils } = AsposeCells;

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
            const exportHtml = `
<html>
<body>
<table>
<tr>
<td>
<div>This is some Text.</div>
<div>
<div>
<span>This is some more Text</span>
</div>
<div>
<span>abc@abc.com</span>
</div>
<div>
<span>1234567890</span>
</div>
<div>
<span>ABC DEF</span>
</div>
</div>
<div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
</td>
<td>
<img src="ASpose_logo_100x100.png" />
</td>
</tr>
</table>
</body>
</html>`;

            // Encode HTML string to Uint8Array
            const encoder = new TextEncoder();
            const ms = encoder.encode(exportHtml);

            // Specify HTML load options, support div tag layouts
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.supportDivTag = true;

            // Create workbook object from the html using load options
            const wb = new Workbook(ms, loadOptions);

            // Auto fit rows and columns of first worksheet
            const ws = wb.worksheets.get(0);
            ws.autoFitRows();
            ws.autoFitColumns();

            // Save the workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DivTagsLayout_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
