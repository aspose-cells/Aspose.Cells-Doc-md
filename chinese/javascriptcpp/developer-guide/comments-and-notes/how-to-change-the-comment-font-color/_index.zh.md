---
title: 如何用 JavaScript 通过 C++ 改变评论的字体颜色
linktitle: 如何更改评论字体颜色
type: docs
weight: 180
url: /zh/javascript-cpp/how-to-change-the-comment-font-color/
---

{{% alert color="primary" %}}  
Microsoft Excel 允许用户在单元格中添加评论以提供额外信息和突出显示数据。开发者可能需要自定义评论以指定对齐设置、文本方向、字体颜色等。通过 C++ 使用脚本提供的 API 可以实现这些功能。  
{{% /alert %}}  

通过 C++ 使用脚本提供的 [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--) 属性设置评论的字体颜色。以下示例代码演示如何使用 [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--) 属性设置评论的文本方向。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Comment Font Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, StyleFlag } = AsposeCells;

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

            // Instantiate a new Workbook (if a file is provided, open it; otherwise create a new workbook)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add some text in cell A1
            worksheet.cells.get("A1").putValue("Here");

            // Add a comment to A1 cell
            const commentIndex = worksheet.comments.add("A1");
            const comment = worksheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is Test.";

            const shape = worksheet.comments.get("A1").commentShape;

            shape.fill.solidFill.color = Color.Black;
            const font = shape.font;
            font.color = Color.White;
            const styleFlag = new StyleFlag();
            styleFlag.fontColor = true;
            shape.textBody.format(0, shape.text.length, font, styleFlag);

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCommentFontColor.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上述代码生成的[输出文件](102662195.xlsx)附在此供您参考。
