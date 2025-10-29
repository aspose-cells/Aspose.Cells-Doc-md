---
title: 用JavaScript通过C++冻结Excel工作表的顶部行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: 本文将介绍如何使用JavaScript库结合C++ API以编程方式冻结Excel工作表的顶部行。
keywords: 用C++的JavaScript冻结顶部行。
---

## **介绍**

在本文中，我们将学习如何冻结顶部行。当您有大量数据在共同标题下时，在向下滚动工作表时无法看到标题。您可以冻结顶部行，以便即使在滚动其他数据时也能看到冻结部分。您可以轻松识别顶部的标题行。

## **在Excel中冻结行**

**![在Excel中冻结顶部行](Freeze-Rows.png)**

1. 如果您想冻结顶部行，则首先选择需要冻结的行以下的行。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单中，单击“冻结顶部行”。
4. 滚动时，第一行始终显示在顶部视图中。

**![冻结行](Frozen-Row.png)**

如您所见，第一行已被冻结；当您向下滚动时，第一行始终保持在视图顶部。

冻结行让您在查看大量数据时无需关注行标签。

## **使用Aspose.Cells for JavaScript通过C++冻结行**
用Aspose.Cells for JavaScript通过C++轻松冻结行。 
请使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)方法在所选行处冻结行。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.freezePanes()方法冻结第一行。
3.保存文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

附有[示例源Excel文件](../Freeze.xlsx)。
