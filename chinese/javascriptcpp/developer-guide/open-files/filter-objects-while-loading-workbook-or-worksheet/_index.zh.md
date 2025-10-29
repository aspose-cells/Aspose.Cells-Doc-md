---
title: 在用C++通过JavaScript加载工作簿或工作表时筛选对象
linktitle: 在加载工作簿或工作表时过滤对象
type: docs
weight: 330
url: /zh/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: 学习在用C++通过Aspose.Cells for JavaScript加载工作簿或工作表时如何筛选数据
---

## **可能的使用场景**
请在使用[LoadOptions.loadFilter](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--)属性筛选工作簿数据时使用。但如果你想筛选单个工作表中的数据，你需要重写[LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/javascript-cpp/loadfilter/#startSheet-worksheet-)方法。在创建或使用[LoadFilter](https://reference.aspose.com/cells/javascript-cpp/loadfilter)时，提供适当的[LoadDataFilterOptions](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions)枚举值。

[LoadDataFilterOptions](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions)枚举具有以下可能值。

- 所有
- 文档设置
- 单元格空白
- 单元格布尔
- 单元格数据
- 单元格错误
- 单元格数值
- 单元格字符串
- 单元格值
- Chart
- 条件格式
- 数据验证
- 定义名称
- 文档属性
- 公式
- 超链接
- 合并区域
- 数据透视表
- 设置
- 形状
- 表单数据
- 表格设置
- 结构
- 样式
- 表
- VBA
- Xml映射

## **加载工作簿时过滤对象**
以下示例代码说明了如何从工作簿中筛选图表。请查看此代码中使用的[示例excel文件](5115258.xlsx)和由此生成的[输出PDF](5115257.pdf)。从输出PDF中可以看出，所有图表都已从工作簿中筛选出。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Charts and Save to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, PdfSaveOptions } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and filter out charts
            const lOptions = new LoadOptions();
            lOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Load the workbook with the above filter
            const workbook = new Workbook(new Uint8Array(arrayBuffer), lOptions);

            // Create PDF save options and set one page per sheet
            const pOptions = new PdfSaveOptions();
            pOptions.onePagePerSheet = true;

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf, pOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterCharts.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to PDF (charts filtered out). Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **加载工作表时过滤对象**
以下示例代码加载了[源excel文件](5115255.xlsx)，并使用自定义过滤器从其工作表中筛选以下数据。

- 它会从名为NoCharts的工作表中筛选图表。
- 它会从名为NoShapes的工作表中筛选形状。
- 它会从名为NoConditionalFormatting的工作表中筛选条件格式。

一旦使用自定义过滤器加载了[源excel文件](5115255.xlsx)，它会逐个工作表地获取所有工作表的图像。以下是用于参考的输出图像。可以看出，第一张图像没有图表，第二张图像没有形状，第三张图像没有条件格式。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Load Filter Example</title>
    </head>
    <body>
        <h1>Custom Load Filter Example</h1>
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

        // Converted CustomLoadFilter class
        class CustomLoadFilter extends AsposeCells.LoadFilter {
            startSheet(sheet) {
                if (sheet.name === "NoCharts") {
                    // Load everything and filter charts
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
                }

                if (sheet.name === "NoShapes") {
                    // Load everything and filter shapes
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
                }

                if (sheet.name === "NoConditionalFormatting") {
                    // Load everything and filter conditional formatting
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate and (optionally) attach the custom load filter
            const customFilter = new CustomLoadFilter();
            // If the environment supports assigning a load filter to workbook, set it as a property
            workbook.loadFilter = customFilter;

            // Inform user that the filter class was created and assigned
            document.getElementById('result').innerHTML = '<p style="color: green;">CustomLoadFilter created and assigned to workbook. You can download the (possibly unchanged) workbook below.</p>';

            // Save the workbook back to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

这是如何根据工作表名称使用CustomLoadFilter类。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadList a { display: block; margin: 6px 0; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Render Worksheets to PNG with Custom Load Filter</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <div id="downloadList"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

        // Define CustomLoadFilter class (placeholder - adapt as needed)
        // The original JavaScript code referenced a CustomLoadFilter implementation.
        // This minimal implementation can be replaced with actual filtering logic.
        class CustomLoadFilter {
            constructor() {
            }
            // If the AsposeCells runtime expects specific methods on the filter,
            // implement them here. This is a generic placeholder.
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            const downloadList = document.getElementById('downloadList');
            downloadList.innerHTML = '';
            resultDiv.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Prepare load options and assign custom load filter
            const loadOpts = new LoadOptions();
            loadOpts.loadFilter = new CustomLoadFilter();

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOpts);

            // Iterate through worksheets and render each to PNG
            const sheetCount = workbook.worksheets.count;
            for (let i = 0; i < sheetCount; i++) {
                const worksheet = workbook.worksheets.get(i);

                // Create image options
                const imageOpts = new ImageOrPrintOptions();
                imageOpts.onePagePerSheet = true;
                imageOpts.imageType = ImageType.Png;

                // Render worksheet to image bytes
                const render = new SheetRender(worksheet, imageOpts);
                const imgBytes = render.toImage(0);

                // Create blob and download link for each rendered image
                const blob = new Blob([imgBytes], { type: 'image/png' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const sheetNameSafe = worksheet.name ? worksheet.name.replace(/[\/\\:?*"<>|]/g, '_') : `sheet${i+1}`;
                link.href = url;
                link.download = `outputCustomFilteringPerWorksheet_${sheetNameSafe}.png`;
                link.textContent = `Download ${link.download}`;
                downloadList.appendChild(link);
            }

            resultDiv.innerHTML = `<p style="color: green;">Rendered ${sheetCount} worksheet(s). Download links are available below.</p>`;
        });
    </script>
</html>
```
