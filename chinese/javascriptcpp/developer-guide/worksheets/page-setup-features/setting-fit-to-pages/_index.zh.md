---
title: 如何用JavaScript通过C++将Excel打印为宽度和高度适合的页面
linktitle: 如何将Excel打印为宽度和高度适应的页面
type: docs
weight: 200
url: /zh/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: 本文展示了使用C++的Script设置FitToPagesWide和FitToPagesTall的代码示例
keywords: 通过 C++ 使用 JavaScript 设置 FitToPagesWide 和 FitToPagesTall，如何在 JavaScript 中添加 FitToPagesWide 和 FitToPagesTall，如何在 Excel 中设置 FitToPagesWide 和 FitToPagesTall，如何清除 Excel 中的 FitToPagesWide 和 FitToPagesTall，如何将 Excel 打印为适合宽度和高度的页面，如何将工作表作为一页打印，如何在一页中打印工作表的所有列。
---

## **介绍**

FitToPagesWide和FitToPagesTall设置用于电子表格应用（如Microsoft Excel），用于控制打印时电子表格的缩放方式。这些设置确保你的打印输出在水平和垂直方向上都在指定的页数内。以下是每个设置的详细说明：

1. FitToPagesWide：此设置指定打印输出应适合的页宽。例如，将FitToPagesWide设置为1，表示内容缩放至适合一页宽，无论电子表格有多宽。
2. FitToPagesTall：该设置指定打印输出应适合的页数高。例如，将 FitToPagesTall 设置为 1，意味着内容将缩放以适应单页的高度，无论行数多少。

## **为什么使用适合页面宽度和高度**
以下是设置适合页面宽度和高度的一些原因：
1. 控制打印布局：通过指定页面宽度和高度的页数，可以确保打印的文档易于阅读且布局合理，没有列或行被尴尬地拆分到不同的页面上。
2. 一致性：如果你要打印多个工作表或报告，使用这些设置有助于保持格式一致，便于比较和分析打印的文档。
3. 专业呈现：正确缩放和适应内容到指定的页数可以使你的数据展示更专业、更有条理。

## **如何在Excel中将文件打印为宽度和高度都适合的页面**

要在Microsoft Excel中设置适合页面宽度和高度的设置，请按照以下步骤操作：

1. 打开你的Excel工作簿，转到你想打印的工作表。
2. 转到功能区的页面布局选项卡。
3. 在页面设置组中，点击右下角的小箭头打开页面设置对话框。
4. 在页面设置对话框中，切换到页面标签。
5. 在缩放下，选择“适合”选项，然后指定你希望的宽和高的页数：在第一个框输入你希望的宽页面数（“适合 x 页宽”），在第二个框输入你希望的高页面数（“适合 y 页高”）。
<br>
<img src="2.png" width=60% />

6. 点击确定应用设置。

## **如何使用 Aspose.Cells for JavaScript 通过 C++ 将 Excel 打印为适合宽度和高度的页面**

要在指定工作表中设置 FitToPagesWide 和 FitToPagesTall：首先，加载【示例文件】(input.xlsx)，然后需要修改 [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) 对象的 [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) 和 [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) 属性以适应目标工作表。以下是 JavaScript 示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

输出结果：
<br>
<img src="1.png" width=60% />

## **如何使用 Aspose.Cells for JavaScript 通过 C++ 将工作表作为一页打印**

要将工作表作为一页打印：首先，加载【示例文件】(sample.xlsx)，然后需要设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/) 对象的 [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) 属性。以下是 JavaScript 示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

输出结果：
<br>
<img src="3.png" width=60% />

## **如何使用 Aspose.Cells for JavaScript 通过 C++ 在一页中打印工作表的所有列**

要在一页中打印工作表的所有列：首先，加载【示例文件】(sample.xlsx)，然后需要设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/) 对象的 [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) 属性。以下是 JavaScript 示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

输出结果：
<br>
<img src="4.png" width=60% />
