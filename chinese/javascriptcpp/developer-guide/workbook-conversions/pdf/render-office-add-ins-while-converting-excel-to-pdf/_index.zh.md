---
title: 在通过 C++ 采用 JavaScript 转换 Excel 为 PDF 时渲染 Office 插件
linktitle: 转换Excel为PDF时呈现Office加载项
type: docs
weight: 100
url: /zh/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能的使用场景**

早期，Aspose.Cells 在将 Excel 文件保存为 PDF 格式时无法渲染 Office 插件。现在 Aspose.Cells 可以正常渲染。您无需使用任何特殊方法或属性来在输出 PDF 中渲染 Office 插件。只需将您的 Excel 文件保存为 PDF 格式，它将自动渲染 Office 插件。

## **在将Excel转换为PDF时呈现Office加载项**

以下示例代码保存了包含Office加载项的[示例Excel文件](60489769.xlsx)。请查看[之前版本（即17.11）生成的输出PDF](60489770.pdf)和[较新版本（即17.12及之后版本）生成的输出PDF](60489771.pdf)。之前版本的输出PDF为空白，但较新版本的输出PDF显示了Office加载项。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
