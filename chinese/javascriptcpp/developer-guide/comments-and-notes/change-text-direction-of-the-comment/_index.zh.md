---
title: 通过 C++ 使用 JavaScript 改变评论的文本方向
linktitle: 更改评论的文本方向
type: docs
weight: 10
url: /zh/javascript-cpp/change-text-direction-of-the-comment/
description: 学习如何使用 C++ 通过脚本改变评论的文本方向。有效自定义评论对齐设置。
---

{{% alert color="primary" %}}

Microsoft Excel 允许用户向单元格添加评论，以提供额外信息和突出数据。开发者可能需要自定义评论以指定对齐设置和文本方向。通过 C++ 使用脚本提供的 API 可以完成此任务。

{{% /alert %}}

通过 C++ 使用脚本提供的 [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) 属性设置评论的文本方向。以下示例代码演示如何使用 [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) 属性设置评论的文本方向。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment Shape</title>
    </head>
    <body>
        <h1>Add Comment Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, TextDirectionType } = AsposeCells;

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
            // Instantiate a new Workbook
            const wb = new Workbook();

            // Get the first worksheet
            const sheet = wb.worksheets.get(0);

            // Add a comment to A1 cell
            const commentIndex = sheet.comments.add("A1");
            const comment = sheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set its horizontal alignment setting
            comment.commentShape.textHorizontalAlignment = TextAlignmentType.Right;

            // Set the Text Direction - Right-to-Left
            comment.commentShape.textOrientationType = TextDirectionType.RightToLeft;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is test";

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutCommentShape.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
