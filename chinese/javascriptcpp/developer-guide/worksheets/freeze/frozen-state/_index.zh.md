---
title: 如何在没有Excel的情况下检查冻结状态，使用JavaScript通过C++
linktitle: 冻结状态
type: docs
weight: 190
url: /zh/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: 在这篇文章中，您将学习如何使用JavaScript结合C++库以编程方式检查Excel工作表的冻结状态。
---

## **介绍**

在本文中，我们将学习如何以编程方式检查Excel工作表的冻结状态。我们可以简单地在MS Excel中查找工作表是否被冻结或拆分。但有没有办法用JavaScript查找是否被冻结或拆分？我们可以用Aspose.Cells for JavaScript通过C++轻松实现。

## **窗格是否冻结**
使用Aspose.Cells for JavaScript通过C++，我们可以检查窗口是否被冻结，以及锁定了多少行和列。

请使用[**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--)属性来检查窗口窗格的状态，并使用[**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--)属性获取锁定的行和列。
1.构建工作簿以打开文件。
2.检查工作表是否被冻结。
3. 获取锁定的行和列。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
