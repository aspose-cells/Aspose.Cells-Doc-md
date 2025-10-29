---
title: 使用C++通过JavaScript将表格转换为ODS
linktitle: 将表格转换为ODS
type: docs
weight: 70
url: /zh/javascript-cpp/convert-table-to-ods/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将带有表格的Excel文件转换为ODS格式。
---

Aspose.Cells支持将含有表格的Excel文件转换为ODS文件。只需将文件保存为ODS格式，生成的ODS文件内将包含可用的表格。

## 示例代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Table to ODS Example</title>
    </head>
    <body>
        <h1>Convert Table to ODS Example</h1>
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

            // Opening the Excel file from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the file to ODS format and providing download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertTableToOds_out.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the ODS file.</p>';
        });
    </script>
</html>
```

示例代码生成的输出ODS文件已附上供您参考。

[**Output ODS File**](ConvertTableToOds_out.ods)
