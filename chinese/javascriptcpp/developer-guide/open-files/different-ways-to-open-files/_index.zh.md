---
title: 通过C++用JavaScript打开文件的不同方法
linktitle: 打开文件的不同方式
type: docs
weight: 10
url: /zh/javascript-cpp/different-ways-to-open-files/
description: 本文介绍如何使用Aspose.Cells for JavaScript通过C++ API打开Excel文件
keywords: JavaScript在没有Excel的情况下打开Excel文件，如何用JavaScript打开Excel文件
---

{{% alert color="primary" %}}

 使用 Aspose.Cells，打开文件非常简单，例如，检索数据或使用设计器模板加快开发流程。

{{% /alert %}}

## **如何通过路径打开Excel文件**

 开发者可以通过在 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类构造函数中指定本地计算机上的文件路径，打开 Microsoft Excel 文件。只需将路径作为字符串传入构造函数。Aspose.Cells 会自动识别文件格式类型。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Open Workbook</title>
    </head>
    <body>
        <h1>Open Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook1 = new Workbook(new Uint8Array(arrayBuffer));
            console.log("Workbook opened using file successfully!");

            // Display basic info about the opened workbook
            document.getElementById('result').innerHTML = `<p style="color: green;">Workbook opened successfully! Worksheets count: ${workbook1.worksheets.count}</p>`;
        });
    </script>
</html>
```

## **如何通过流打开Excel文件**

 也可以简单地通过流的方式打开 Excel 文件。使用接受包含文件的 *Stream* 对象的重载构造函数即可。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Stream to Workbook</title>
    </head>
    <body>
        <h1>Open Excel Stream Example (Browser)</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file as an ArrayBuffer (equivalent to reading a stream in JavaScript)
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Example modification: set A1 to indicate file was loaded (demonstrates cell value setter conversion)
            const cell = worksheet.cells.get(0, 0);
            cell.value = "Loaded from stream";

            // Save the modified workbook as Excel97-2003 (.xls) since original was .xls in JavaScript example
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **如何只打开具有数据的文件**

 若只需要加载含数据的文件，可使用 [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) 和 [**LoadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadfilter) 类设置相关属性和选项，从而加载模板文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells LoadOptions Example</title>
    </head>
    <body>
        <h1>LoadOptions with LoadFilter Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Set LoadFilter property to load only data & cell formatting
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.CellData);

            // Create a Workbook object and opening the file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Indicate success
            document.getElementById('result').innerHTML = '<p style="color: green;">File data imported successfully!</p>';

            // Prepare download of the loaded workbook (optional)
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

## **如何仅加载可见工作表**

 在加载 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 时，有时只需工作簿中可见工作表中的数据。Aspose.Cells 允许在加载工作簿时跳过不可见工作表中的数据。为此，可以创建继承自 [**LoadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadfilter) 类的自定义函数，并将其实例传递给 [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) 属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create if no file selected)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, Utils } = AsposeCells;

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
            let bytes;
            let createdOutputData;

            if (fileInput.files.length) {
                // Load from user-selected file
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                bytes = new Uint8Array(arrayBuffer);
            } else {
                // Create a sample workbook in memory
                const createWorkbook = new Workbook();

                // Put some data in first cell of all 3 sheets
                createWorkbook.worksheets.get("Sheet1").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.add("Sheet2").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.add("Sheet3").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.get("Sheet3").isVisible = false;

                // Save the created workbook to bytes
                createdOutputData = createWorkbook.save(SaveFormat.Xlsx);
                bytes = createdOutputData instanceof Uint8Array ? createdOutputData : new Uint8Array(createdOutputData);

                // Provide download link for the created workbook
                const blob = new Blob([bytes]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Created Excel File';
            }

            // Prepare load options and load filter
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter();

            // Load the workbook using the bytes and load options
            const loadWorkbook = new Workbook(bytes, loadOptions);

            // Read values from A1 of Sheet1, Sheet2, Sheet3
            const sheet1A1 = loadWorkbook.worksheets.get("Sheet1").cells.get("A1").value;
            const sheet2A1 = loadWorkbook.worksheets.get("Sheet2").cells.get("A1").value;
            const sheet3A1 = loadWorkbook.worksheets.get("Sheet3").cells.get("A1").value;

            // Log to console and show in the page
            console.log(`Sheet1: A1: ${sheet1A1}`);
            console.log(`Sheet2: A1: ${sheet2A1}`);
            console.log(`Sheet3: A1: ${sheet3A1}`);

            document.getElementById('result').innerHTML =
                `<p>Sheet1: A1: ${sheet1A1}</p>
                 <p>Sheet2: A1: ${sheet2A1}</p>
                 <p>Sheet3: A1: ${sheet3A1}</p>
                 <p style="color: green;">Operation completed successfully!</p>`;
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>CustomLoad Example</h1>
        <p>Select an Excel file to evaluate sheets with CustomLoad.startSheet()</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadDataFilterOptions } = AsposeCells;

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

        class CustomLoad {
            startSheet(sheet) {
                if (sheet.isVisible()) {
                    // Load everything from visible worksheet
                    this.loadDataFilterOptions = LoadDataFilterOptions.All;
                } else {
                    // Load nothing
                    this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const custom = new CustomLoad();

            let html = '<h2>CustomLoad Results</h2>';
            html += '<ul>';

            for (let i = 0; i < workbook.worksheets.count; i++) {
                const sheet = workbook.worksheets.get(i);
                custom.startSheet(sheet);
                html += `<li><strong>${sheet.name}</strong>: loadDataFilterOptions = ${custom.loadDataFilterOptions}</li>`;
            }

            html += '</ul>';
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

{{% alert color="primary" %}}

 如果使用 Aspose.Cells 打开非本地 Excel 文件或其他文件格式（例如 PPT/PPTX，DOC/DOCX 等），会抛出异常。

{{% /alert %}} 

{{% alert color="primary" %}}

 在加载大型电子表格时，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 构造函数可能会抛出 *OutOfMemoryError*。此异常提示可用内存不足以完全加载电子表格，因此必须启用内存偏好设置来加载文件。

{{% /alert %}}
