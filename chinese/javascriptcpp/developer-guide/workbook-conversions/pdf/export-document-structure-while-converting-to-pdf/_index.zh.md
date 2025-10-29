---
title: 在使用JavaScript通过C++转换为PDF时导出文档结构
linktitle: 在将其转换为PDF时导出文档结构
type: docs
weight: 360
url: /zh/javascript-cpp/export-document-structure-while-converting-to-pdf/
description: 学习如何在使用Aspose.Cells for Java脚本通过C++将Excel文件转换为带标签的PDF时导出文档结构。
---

PDF的逻辑结构功能提供了一种将关于文档内容结构的信息集成到PDF文件中的机制。Aspose.Cells for Java脚本通过C++保留了Microsoft Excel文档中的结构信息，如单元格、行、表格、工作表、图片、形状、页眉/页脚等。

使用[PdfSaveOptions.exportDocumentStructure()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#exportDocumentStructure--)选项可以导出结构信息的带标签PDF。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export PDF with Document Structure</title>
    </head>
    <body>
        <h1>Export PDF with Document Structure</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set to export document structure.
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.exportDocumentStructure = true;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF exported successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
