---
title: 加载或导入带有公式的CSV文件 via JavaScript
linktitle: 加载或导入具有公式的CSV文件
type: docs
weight: 350
url: /zh/javascript-cpp/load-or-import-csv-file-with-formulas/
description: 学习如何使用Aspose.Cells for JavaScript通过C++加载和导入包含公式的CSV文件。
---

{{% alert color="primary" %}}

CSV文件通常包含文本数据，它们不包含任何公式。然而，有时CSV文件也会包含公式。此类CSV文件应通过将[TxtLoadOptions.hasFormula](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#hasFormula--)设置为**true**来加载。一旦将此属性设置为**true**，Aspose.Cells将不把公式视为简单文本，而会将其作为公式处理，Aspose.Cells的公式计算引擎将按常规处理它们。

{{% /alert %}}

以下代码演示了如何加载以及导入带公式的 CSV 文件。你可以使用任何 CSV 文件。为了示例，我们使用包含此数据的【简单 CSV 文件】（5115034.csv），如你所见，它包含一个公式。

{{< highlight javascript >}}
<!DOCTYPE html>
<html>
    <head>
        <title>Load CSV with Formulas and Save as XLSX</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="convertToXlsx">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download XLSX</a>
        <div id="result"></div>

        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, TxtLoadOptions, SaveFormat } = AsposeCells;

            AsposeCells.onReady().then(() => {
                console.log("Aspose.Cells initialized");
            });

            document.getElementById('convertToXlsx').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                const loadOptions = new TxtLoadOptions();
                loadOptions.hasFormula = true;

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = file.name.replace(/\.csv$/i, '.xlsx');
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download XLSX File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the XLSX file.</p>';
            });
        </script>
    </body>
</html>
{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Load Example</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const bytes = new Uint8Array(arrayBuffer);

            // TxtLoadOptions configuration
            const opts = new TxtLoadOptions();
            opts.separator = ',';
            opts.hasFormula = true;

            // Load your CSV file with formulas in a Workbook object
            const workbook = new Workbook(bytes, opts);

            // You can also import your CSV file like this
            // The code below is importing CSV file starting from cell D4 (rowIndex=3, colIndex=3)
            const worksheet = workbook.worksheets.get(0);
            worksheet.cells.importCSV(bytes, opts, 3, 3);

            // Save your workbook in Xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

代码首先加载CSV文件，然后在单元格D4处重新导入，并最终将工作簿保存为XLSX格式。输出的 XLSX 文件（[链接](5115052.xlsx)）如下所示。你可以看到，单元格C3和F4包含公式，其结果为800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |
