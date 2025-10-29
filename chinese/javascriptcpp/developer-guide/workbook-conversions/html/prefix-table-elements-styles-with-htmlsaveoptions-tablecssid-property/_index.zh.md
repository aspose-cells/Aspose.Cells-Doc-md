---
title: 在 JavaScript 通过 C++ 使用 HtmlSaveOptions.tableCssId 属性前缀表格元素样式
linktitle: 使用 HtmlSaveOptions.tableCssId 属性前缀表格元素样式
type: docs
weight: 110
url: /zh/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 对 HTML 中的表格元素样式进行前缀。
---

## **可能的使用场景**

Aspose.Cells 允许您使用 [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) 属性为表格元素样式添加前缀。假设您将此属性设置为某个值，比如 **MyTest_TableCssId**，那么您会看到如下所示的表格元素样式：

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

以下截图显示了使用 [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) 属性对输出 HTML 产生的效果。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **使用 HtmlSaveOptions.tableCssId 属性前缀表格元素样式**

以下示例代码演示了如何使用 [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) 属性。请查看由代码生成的[输出 HTML](60489790.zip)作为参考。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Cell Style and Save as HTML with Table CSS ID</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook as in original JavaScript sample
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Access cell B5 and put value inside it
                const cell = ws.cells.get("B5");
                cell.value = "This is some text.";

                // Set the style of the cell - font color is Red
                const st = cell.style;
                st.font.color = Color.Red;
                cell.style = st;

                // Specify html save options - specify table css id
                const opts = new HtmlSaveOptions();
                opts.tableCssId = "MyTest_TableCssId";

                // Save the workbook in html
                const outputData = wb.save(SaveFormat.Html, opts);
                const blob = new Blob([outputData], { type: 'text/html' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputTableCssId.html';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download HTML File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same changes
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - specify table css id
            const opts = new HtmlSaveOptions();
            opts.tableCssId = "MyTest_TableCssId";

            // Save the workbook in html
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTableCssId.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
