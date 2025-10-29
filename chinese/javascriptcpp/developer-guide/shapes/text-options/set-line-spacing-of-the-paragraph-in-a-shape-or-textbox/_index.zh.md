---
title: 设置形状或文本框中文本段落的行距
linktitle: 设置形状或文本框中段落的行间距
type: docs
weight: 290
url: /zh/javascript-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/
description: 学习如何使用Aspose.Cells for JavaScript通过C++设置形状或文本框中段落的行距
---

{{% alert color="primary" %}}

你可以使用[**TextParagraph.lineSpace**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#lineSpace--)、[**TextParagraph.spaceBefore**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#spaceBefore--)和[**TextParagraph.spaceAfter**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#spaceAfter--)属性设置段落的行间距、前间距和后间距，这些都属于[**TextParagraph**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/)类。

{{% /alert %}}

以下示例代码解释了所述属性的用法。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells TextBox Paragraph Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            const ws = wb.worksheets.get(0);

            ws.shapes.addTextBox(2, 0, 2, 0, 100, 200);

            const shape = ws.shapes.get(0);
            shape.text = "Sign up for your free phone number.\nCall and text online for free.";

            const p = shape.textBody.textParagraphs.get(1);

            p.lineSpaceSizeType = AsposeCells.LineSpaceSizeType.Points;
            p.lineSpace = 20;

            p.spaceAfterSizeType = AsposeCells.LineSpaceSizeType.Points;
            p.spaceAfter = 10;

            p.spaceBeforeSizeType = AsposeCells.LineSpaceSizeType.Points;
            p.spaceBefore = 10;

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
