---
title: 如何用 JavaScript 通过 C++ 改变 Excel 中评论的背景
linktitle: 评论背景
type: docs
weight: 190
url: /zh/javascript-cpp/how-to-set-comment-background/
description: 使用 C++ 通过脚本改变 Excel 中评论的背景色，并插入图片或图像。
keywords: 用 C++ 通过 JavaScript 添加插入图片的颜色评论背景到 Excel
---

{{% alert color="primary" %}}
 评论被添加到单元格以记录评论内容，从细节如公式的工作方式、数据来源到审阅者的问题。在多个人在不同时间讨论或审查同一文档时，评论扮演着极其重要的角色。如何区分不同人的评论？是的，我们可以为每个评论设置不同的背景颜色。但当需要处理大量文档和评论时，手动操作是个灾难。幸运的是，[**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) 提供了一个 API，可以让你在代码中实现此功能。
{{% /alert %}}

## **如何在Excel中更改评论的颜色**

当你不需要批注的默认背景色时，可以用自己关注的颜色替换它。如何更改 Excel 中批注框的背景色？

以下代码将指导你如何使用[**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/)为你自己选择的评论添加喜欢的背景颜色。

这里我们为你准备了一个[示例文件](exmaple.xlsx)。该文件用于初始化下面的代码中的 Workbook 对象。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change Comment Background Color Example</title>
    </head>
    <body>
        <h1>Change Comment Background Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Initialize a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the newly added comment
            const comment = workbook.worksheets.get(0).comments.get(0);

            // change background color
            const shape = comment.commentShape;
            shape.fill.solidFill.color = AsposeCells.Color.Red;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment background color changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

执行上述代码，你将得到一个[输出文件](result.xlsx)。

## **如何在Excel中评论中插入图片或图像**

Microsoft Excel 允许用户极大程度地自定义电子表格的外观和感觉。甚至可以在评论中添加背景图片。添加背景图片可以是美观的选择，也可以用来强化品牌。

以下示例代码使用 [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) API 从零开始创建一个 XLSX 文件，并在单元格 A1 添加带有图片背景的评论。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Comment with Picture Example</h1>
        <p>
            Select an existing Excel file (optional) and an image file to attach to a comment in cell A1.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert in comment (required):</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the comment.</p>';
                return;
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get comments collection for the first sheet
            const comments = worksheet.comments;

            // Add a comment to cell A1 (row 0, column 0)
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set comment text and font name (converted from setters to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load the selected image file and set it to the comment's shape fill imageData
            const imageFile = imageInput.files[0];
            const imgArrayBuffer = await imageFile.arrayBuffer();
            const imageData = new Uint8Array(imgArrayBuffer);

            comment.commentShape.fill.imageData = imageData;

            // Save the workbook to a blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'commentwithpicture1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Comment with picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</body>
</html>
```
