---
title: 在共享工作簿中更新保留修订日志的天数，使用 JavaScript 通过 C++
linktitle: 在共享工作簿中保留修订日志的更新日志
type: docs
weight: 80
url: /zh/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 在共享工作簿中更新保存修订日志的天数。
---

## **可能的使用场景**

当你共享一个工作簿时，会出现一个选项“***保留更改历史N天***”，如下图所示。你可以使用 Aspose.Cells for JavaScript 通过 C++ 的 [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--) 属性来更新保留历史的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **在共享工作簿中保留修订日志的更新日志**

以下示例代码创建一个空白工作簿，然后共享它并将修订日志天数修改为7天，通常是30天。请参考代码生成的[输出Excel文件](60489773.xlsx)。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
