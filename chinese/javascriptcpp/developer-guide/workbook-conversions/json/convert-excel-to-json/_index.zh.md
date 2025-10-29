---
title: 使用JavaScript通过C++将Excel导出为JSON
linktitle: 转换Excel为JSON
type: docs
weight: 300
url: /zh/javascript-cpp/convert-excel-to-json/
description: 学习如何使用C++和Aspose.Cells for JavaScript将Excel文件转换为JSON。
keywords: 通过C++将工作簿导出为JSON，使用JavaScript将Excel转换为JSON
---

{{% alert color="primary" %}}  
Aspose.Cells 支持将工作簿转换为 JSON（JavaScript 对象表示法）文件。  
{{% /alert %}}  

## **将Excel工作簿转换为JSON**  

无需担心如何将Excel工作簿转换为JSON，因为Aspose.Cells for JavaScript通过C++的库提供了最佳解决方案。Aspose.Cells API支持将电子表格转换为JSON格式。要导出工作簿为JSON，将[**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/)作为[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)方法的第二个参数传递。您也可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/)类来设置导出工作表到JSON的其他参数。  

以下代码示例演示了导出 Excel 工作簿为 JSON。请查看此代码，将【源文件】(sample.xlsx) 转换为由代码生成的 JSON 文件。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
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

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

以下代码示例使用 JsonSaveOptions 类来指定额外设置，并演示将Excel工作簿导出为JSON。请参考代码，将【源文件】(sample.xlsx) 转换为由代码生成的JSON文件。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```
