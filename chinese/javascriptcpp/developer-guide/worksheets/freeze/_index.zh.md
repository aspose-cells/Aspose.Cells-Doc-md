---
title: 用 JavaScript 通过 C++ 冻结 Excel 工作表的窗格
linktitle: 冻结窗格
type: docs
weight: 190
url: /zh/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: 在本文中，你将学习如何使用 Aspose.Cells for JavaScript 通过 C++ 编程方式冻结 Excel 工作表的窗格。
keywords: 冻结窗格，冻结窗口。
---

## **介绍**  

 本文介绍如何冻结窗格。当你有大量数据在共同标题下时，滚动后无法看到标题行，且每条记录包含许多数据。通过冻结窗格，可以在滚动时仍然看到冻结的部分。你可以方便地看到顶部行或首列的标题。冻结和取消冻结窗格只会改变数据的视图，不会改变数据本身。  

## **在Excel中**  

**![Excel中的冻结窗格](Freeze-panes.png)**  

 1. 若要冻结窗格、冻结行列，先选中一个单元格（如B2）。  
2. 单击“查看”>“冻结窗格”  
3. 在下拉菜单上，单击“冻结窗格”  
 4. 向下或向右滚动时，第一行和第一列会被冻结。  

**![冻结窗格](Frozen-Panes.png)**  

如图所示，第1行和列A被冻结，第2行是第三行，第2个可见列是D。  

冻结窗格使您可以在查看大量数据时不必跟踪行或列标签。  

## **使用C++的Aspose.Cells for JavaScript冻结窗格**  
使用C++的Aspose.Cells for JavaScript轻松冻结窗格。请使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)方法在选定的单元格中冻结窗格。  
1.构建工作簿以打开文件或创建一个空文件。  
2. 使用Worksheet.freezePanes()方法冻结窗格。  
3.保存文件。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

附上[示例源Excel文件](Freeze.xlsx)。
