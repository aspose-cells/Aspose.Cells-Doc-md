---
title: 在设置Style.Custom属性时检查自定义数字格式
linktitle: 在设置Style.Custom属性时检查自定义数字格式
description: Aspose.Cells 是一个用于操作电子表格文件的JavaScript库，支持在样式设置中检查自定义数字格式。本文将向你展示如何使用Aspose.Cells库检查自定义数字格式以确保样式正确。
keywords: Aspose.Cells，JavaScript库，电子表格，样式，自定义数字格式，检查，验证
type: docs
weight: 170
url: /zh/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能的使用场景**

 如果你为[**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)属性分配了无效的自定义数字格式，Aspose.Cells for JavaScript通过C++不会抛出任何异常。但如果你希望Aspose.Cells检查所分配的自定义数字格式是否有效，请将[**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-)属性设置为**true**。

## ** 设置Style.custom属性时检查自定义数字格式**

 以下示例代码为[**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)属性分配了无效的自定义数字格式。由于我们已将[**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-)属性设置为**true**，它会抛出异常，例如：无效的数字格式。请阅读代码中的注释获取更多帮助。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
