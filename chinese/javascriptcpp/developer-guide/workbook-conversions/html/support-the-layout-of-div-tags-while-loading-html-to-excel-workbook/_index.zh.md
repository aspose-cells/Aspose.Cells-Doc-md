---
title: 支持在加载 HTML 到 Excel 工作簿时布置 DIV 标签的布局，使用 JavaScript 通过 C++
linktitle: 支持在加载 HTML 到 Excel 工作簿时布局 DIV 标签
type: docs
weight: 50
url: /zh/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}}
通常在将 HTML 加载到 Excel 工作簿对象时，会忽略 div 标签的布局。但是，如果你希望不忽略 div 标签的布局，请设置 [HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--) 属性为 **true**。该属性的默认值为 **false**。
{{% /alert %}}

以下示例代码展示了 [HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--) 属性的用法。请下载示例中的 [Aspose Logo](5115218.png) 和由代码生成的 [输出Excel文件](5115220.xlsx)。

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
