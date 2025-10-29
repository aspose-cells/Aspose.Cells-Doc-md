---
title: 使用 Aspose.Cells for JavaScript 通过 C++ 自动刷新 OLE 对象
linktitle: 使用Aspose.Cells自动刷新OLE对象通过Microsoft Excel
type: docs
weight: 270
url: /zh/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: 了解如何使用 Aspose.Cells for JavaScript 通过 C++ 在 Excel 中自动刷新 OLE 对象。
---

{{% alert color="primary" %}}  
Aspose.Cells提供 [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--) 属性，在Microsoft Excel中打开excel文件时刷新OLE对象。由于该属性，OLE对象将显示由Microsoft Excel生成的正确OLE图像。  
{{% /alert %}}  

以下样本代码加载了包含非真实OLE图像的 [样本excel文件](5115231.xlsx)。OLE对象实际上是一个Microsoft Word文档，但样本excel文件显示的是动物图像，而不是Microsoft Word图像。但是，如果打开 [输出excel文件](5115225.xlsx)，您将看到Microsoft Excel显示了正确的OLE图像。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh OLE Objects Example</title>
    </head>
    <body>
        <h1>Refresh OLE Objects Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set auto load property of first ole object to true
            sheet.oleObjects.get(0).autoLoad = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshOLEObjects_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object autoLoad set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
