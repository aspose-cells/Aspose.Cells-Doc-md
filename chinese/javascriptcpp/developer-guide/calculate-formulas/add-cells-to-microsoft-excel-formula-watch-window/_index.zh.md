---
title: 通过 C++ 使用 JavaScript 添加单元格到 Microsoft Excel 的公式观察窗口
linktitle: 将单元格添加到Microsoft Excel公式监视窗口
description: 如何使用 Aspose.Cells 库通过 JavaScript 和 C++ 将单元格添加到 Excel 的公式观察窗口。通过加载现有的 Excel 文件或创建新文件，我们可以操作其中的单元格并设置公式。最后，将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells，Excel，公式观察窗口，单元格，添加，JavaScript via C++
type: docs
weight: 60
url: /zh/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel的监控窗口是一个方便的工具，可在窗口中观察单元格值及其公式。你可以通过点击*公式 > 监控窗口*在Microsoft Excel中打开*监控窗口*。它有*添加监控*按钮，用于添加待检查的单元格。同样，你可以使用[**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-)方法通过Aspose.Cells API将单元格添加到*监控窗口*。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了单元格C1和E1的公式，并将它们添加到监控窗口。然后将工作簿保存为[输出Excel文件](67338481.xlsx)。如果你打开输出Excel文件并查看*监控窗口*，你将看到两个单元格，如截图所示。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
