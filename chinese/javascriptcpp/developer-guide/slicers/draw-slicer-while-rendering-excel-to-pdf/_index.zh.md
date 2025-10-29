---
title: 在将 Excel 渲染为 PDF 时绘制分析器
type: docs
weight: 60
url: /zh/javascript-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **在将 Excel 渲染为 PDF 时绘制分析器**
如果您的Excel文件中应用了切片器，并希望导出包含切片器设置的PDF，Aspose.Cells for JavaScript通过C++现已默认支持。您只需将带切片器的Excel文件导出为PDF，生成的PDF中将显示切片器。

以下示例代码加载了包含现有切片器的[sample Excel file](94044165.xlsx)。然后将工作簿保存为[output PDF file](94044166.pdf)。以下截图比较了源Excel文件和生成的PDF文件。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as PDF</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleSlicerChart.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
