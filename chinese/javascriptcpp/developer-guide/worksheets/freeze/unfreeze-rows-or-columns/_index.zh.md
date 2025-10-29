---
title: 使用JavaScript通过C++解除冻结行或列
linktitle: 取消冻结窗格
type: docs
weight: 190
url: /zh/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用C++中的JavaScript API以编程方式解除Excel工作表的行、列或窗格的冻结。
keywords: 通过C++使用JavaScript解除窗格、解除行冻结、解除列冻结、解除窗口冻结
---

## **介绍**

在本文中，我们将学习如何取消冻结行、列和窗格。如果Excel文件中的工作表被冻结，有时我们希望取消冻结或调整冻结的行、列或窗格。


## **在Excel中**

1. 单击“查看”选项卡 > 冻结窗格 > 取消冻结窗格。

**![在Excel中取消冻结窗格](Unfreeze-Panes.png)**




## **通过Aspose.Cells for JavaScript和C++解除冻结行、列或窗格**
使用Aspose.Cells for JavaScript通过C++轻松解除窗格冻结。请使用[**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--)方法解除窗格。

1. 构造工作簿以打开冻结文件。
2. 使用Worksheet.unFreezePanes()方法解除窗格冻结。
3.保存文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

附有【示例源Excel文件】(Frozen.xlsx)。
