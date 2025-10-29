---
title: 使用JavaScript通过C++更改HTML链接目标类型
linktitle: 更改HTML链接的目标类型
type: docs
weight: 320
url: /zh/javascript-cpp/change-the-html-link-target-type/
description: 学习如何使用Aspose.Cells for JavaScript通过C++更改HTML链接目标类型，控制HTML链接中的target属性。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接的目标类型。 HTML 链接看起来像这样

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如你所见，上述HTML链接中的target属性是**_self**。你可以使用[**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--)属性控制这个target属性。此属性接受具有以下值的[**HtmlLinkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmllinktargettype)枚举。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

以下代码说明了[**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--)属性的用法。它将链接目标类型更改为**blank**。默认值是**parent**。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlLinkTargetType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HTML save options and set link target type
            const opts = new HtmlSaveOptions();
            opts.linkTargetType = HtmlLinkTargetType.Self;

            // Save the workbook to HTML using the save options
            const outputData = workbook.save(SaveFormat.Html, opts);

            // Create a downloadable blob for the resulting HTML
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = `<p style="color: green;">File converted and ready for download: ${downloadLink.download}</p>`;
        });
    </script>
</html>
```
