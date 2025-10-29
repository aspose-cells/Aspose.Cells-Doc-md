---
title: 用JavaScript通过C++冻结Excel工作表的首列
linktitle: 冻结列
type: docs
weight: 190
url: /zh/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: 学习如何使用Aspose.Cells for JavaScript通过C++以编程方式冻结Excel工作表的左侧列。
keywords: 冻结左侧列，冻结首列，锁定列
---

## **介绍**  

在本文中，我们将学习如何冻结左列。当一行中有大量数据时，你可能无法在横向滚动时看到左边的列。你可以冻结并锁定首列，使其即使在滚动其他数据时仍然可见。这样可以轻松查看左列的标题。  

## **Excel中的冻结列**  

**![在Excel中冻结左侧列](freeze-columns.png)**  

1. 如果您想冻结左列，则首先选择需要冻结的列下面的列。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单上，单击“冻结第一列”
4. 滚动时，第一列始终显示在左侧视图中。

**![冻结列](frozen-columns.png)**  

如你所见，第1列已被冻结，当你横向滚动时，首列始终锁定在视图顶部。

冻结列让你无需担心，轻松查看你的长数据。

## **使用Aspose.Cells for JavaScript通过C++冻结列**  
用Aspose.Cells for JavaScript通过C++轻松冻结首列。  
请使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)方法在选定的列上冻结列。  
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.freezePanes()方法冻结第一列。
3.保存文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
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

附上[示例源Excel文件](Freeze.xlsx)。
