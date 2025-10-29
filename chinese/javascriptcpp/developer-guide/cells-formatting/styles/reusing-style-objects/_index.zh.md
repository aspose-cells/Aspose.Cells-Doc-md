---
title: 重用样式对象
linktitle: 重用样式对象
description: 通过 C++ 调用 Aspose.Cells for JavaScript ，通过创建和使用可重用的样式对象，可以简化样式管理并提高代码效率。我们的指南将帮助你利用可重用样式对象的优势，并在你的应用中实现它们。
keywords: Aspose.Cells for JavaScript 通过 C++，重用样式对象，样式管理，代码效率，可重用样式，应用开发，API 参考，示例代码，下载，支持。
type: docs
weight: 3000
url: /zh/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
重用样式对象可以节省内存并加快程序运行速度。  
{{% /alert %}}  

若要对工作表中的大范围单元格应用一些格式设置：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用于范围中的单元格。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
由于 [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) 方法使用的内存更少且效率高，因此在 Aspose.Cells 7.1.0 版本发布时，曾移除了占用大量不必要内存的旧 Cell.style 属性。  
{{% /alert %}}
