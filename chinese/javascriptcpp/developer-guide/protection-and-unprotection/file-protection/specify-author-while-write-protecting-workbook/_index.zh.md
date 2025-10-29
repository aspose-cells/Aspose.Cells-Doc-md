---
title: 使用 C++ 通过 JavaScript 指定作者在保护工作簿时
linktitle: 在写保护工作簿时指定作者
type: docs
weight: 40
url: /zh/javascript-cpp/specify-author-while-write-protecting-workbook/
description: 使用 C++ 通过 Aspose.Cells for JavaScript 在保护工作簿时指定作者姓名
---

## **可能的使用场景**

 您可以在使用Aspose.Cells API写保护工作簿时指定作者姓名。请使用[**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--)属性完成此操作。

## **在保护工作簿时指定作者**

 以下示例代码说明了[**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--)属性的用法。该代码创建一个空白工作簿，用密码进行写保护，指定作者姓名，并保存为[输出Excel文件](67338582.xlsx)。下图展示了示例代码对输出Excel文件的效果，供您参考。

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
