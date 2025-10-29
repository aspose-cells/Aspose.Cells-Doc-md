---
title: 使用CellsFactory类创建样式对象
linktitle: 使用CellsFactory类创建样式对象
description: 了解如何使用Aspose.Cells for JavaScript通过C++中的CellsFactory类创建单元格样式对象。根据需要定制电子表格单元格的外观。
keywords: Aspose.Cells，JavaScript via C++，电子表格，样式对象，单元格样式，定制化
type: docs
weight: 70
url: /zh/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **使用CellsFactory类创建Style对象**
以下示例代码通过CellsFactory类创建[样式](https://reference.aspose.com/cells/javascript-cpp/style)对象，然后设置工作簿的默认样式。请下载[输出Excel文件](5115153.xlsx)查看此代码的效果。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;

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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
