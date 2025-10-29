---
title: 使用 JavaScript via C++ 计算 Excel 2016 的 MINIFS 和 MAXIFS 函数
description: 本文介绍如何使用 Aspose.Cells 库在 JavaScript via C++ 中计算 Microsoft Excel 2016 的 MINIFS 和 MAXIFS 函数。加载已有的 Excel 文件或创建新文件，然后使用 Aspose.Cells 方法计算这些函数并将结果保存到磁盘。
keywords: Aspose.Cells，Excel，2016，MINIFS 函数，MAXIFS 函数，计算，JavaScript via C++
type: docs
weight: 300
url: /zh/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能的使用场景**
Microsoft Excel 2016 支持 MINIFS 和 MAXIFS 函数。这些函数在 Excel 2013 或更早版本中不支持。 Aspose.Cells for JavaScript 通过 C++ 也支持这些函数的计算。以下截图展示了这些函数的用法。请阅读截图中的红色注释以了解这些函数的工作原理。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **计算Excel 2016的MINIFS和MAXIFS函数**
以下示例代码加载[示例Excel文件](5115149.xlsx)，调用[Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)方法，通过Aspose.Cells for JavaScript用C++实现公式计算，然后将结果保存到[输出PDF](5115154.pdf)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
