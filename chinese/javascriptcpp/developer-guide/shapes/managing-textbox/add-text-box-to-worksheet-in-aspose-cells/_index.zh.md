---
title: 如何使用JavaScript通过C++在工作表中添加/插入文本框
linktitle: 在工作表中添加文本框
type: docs
weight: 10
url: /zh/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: 如何在Aspose.Cells for Java脚本中通过C++在工作表中添加/插入文本框
keywords: 通过C++在Excel工作表中添加/插入文本框
---

在Excel中的工作表中添加文本框

在Excel（版本07及以上）中，有两个地方可以插入文本框。一个是在"插入-形状"中，另一个在“插入”选项的顶端菜单右侧。

### 方法一：

![1](1.png)

### 方法二：

![2](2.png)

## 如何创建

您可以创建水平或垂直文本框。

- 选择相应的选项（横向或纵向）
- 在页面上单击左键
- 按住左键并在页面上拖动一段距离
- 释放左键

现在您可以获得一个文本框。

## 使用Aspose.Cells for Java脚本通过C++在工作表中添加文本框

当你需要批量插入文本框到工作表时，手动插入方法显然是一场灾难。如果这让你困扰，我认为这份文档会帮到你。[Aspose.Cells](https://products.aspose.com/cells/) 为你提供了一个API，便于在代码中实现批量插入。

以下示例代码创建一个文本框。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

你将获得一个类似 [结果文件](result.xlsx) 的文件。在文件中，你会看到以下内容：

![](52449.png)
