---
title: 使用JavaScript通过C++在渲染Excel到PDF时忽略错误
linktitle: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 80
url: /zh/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: 学习在使用Aspose.Cells for Java脚本通过C++将Excel文件转换为PDF的过程中，如何忽略错误。
---

## **可能的使用场景**  

有时候在将Excel文件转换为PDF时会出现错误或异常，导致转换过程终止。您可以使用[**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--)属性在转换过程中忽略所有此类错误。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会丢失部分数据。因此，仅在数据丢失对您不重要的情况下使用此属性。  

## **在将Excel渲染为PDF时忽略错误**  

以下代码加载了[示例Excel文件](55541778.xlsx)，但该示例Excel文件在[转换为PDF](55541779.pdf)时出现错误，发生在17.11版本中，但由于使用[**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--)属性，不会抛出错误。不过截图中显示的一个*圆角红箭头形状*会丢失。  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
