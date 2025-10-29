---
title: 通过C++的JavaScript实现工作表视图
linktitle: 工作表视图
type: docs
weight: 40
url: /zh/javascript-cpp/worksheet-views/
description: 本文将介绍如何使用JavaScript和JavaScript API与Excel工作簿和工作表的分页预览交互。包括拆分窗格、冻结窗格和缩放比例的操作。
---

## **分页预览**

所有工作表都可以以两种模式查看：

- 普通视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种显示工作表为打印格式的编辑视图。分页预览显示每个页面将显示哪些数据，以便您调整打印区域和分页。通过C++的Aspose.Cells for JavaScript，开发者可以启用普通视图或分页预览模式。

### **控制视图模式**

Aspose.Cells提供了一个代表Microsoft Excel文件的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 班。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 班包含一个 [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，允许访问Excel文件中的每个工作表。

一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班提供了各种属性和方法，用于管理工作表。为了启用普通或页面分页预览模式，使用 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班的 [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) 属性。[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) 是一个布尔属性，只能存储 **true** 或 **false** 值。

#### **启用普通视图**

通过将 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班的 [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) 属性设置为 **false**，将工作表设置为普通视图。

#### **启用分页预览**

通过将 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班的 [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) 属性设置为 **true**，将任何工作表设为页面分页预览。这样做将工作表从普通视图切换到页面分页预览。

下面给出一个完整的示例，演示了如何使用 [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) 属性为Excel文件的第一个工作表启用页面分页预览模式。

通过创建 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 班的实例打开book1.xls文件。通过将 [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) 属性设置为 **true**，将视图切换为页面分页预览第一个工作表。修改后的文件被保存为output.xls。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **缩放因子**

### **使用Microsoft Excel**

Microsoft Excel提供了一个功能，允许用户设置工作表的缩放比例。此功能帮助用户以更大或更小的视图查看工作表内容。用户可以将缩放因子设置为任何值。

### **Aspose.Cells和缩放因子**

Aspose.Cells允许开发人员设置工作表的缩放因子。
Aspose.Cells提供了一个代表Microsoft Excel文件的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 班。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 班包含一个 [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，允许访问Excel文件中的每个工作表。

一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班提供了各种属性和方法，用于管理工作表。为了设置工作表的缩放因子，使用 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 班的 [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) 属性。通过将数字（整数）值分配给 [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) 属性，设置缩放因子。

下面提供一个完整示例，演示如何使用 [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) 属性设置 Excel 文件第一个工作表的缩放比例。

通过创建一个[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类的实例来打开book1.xls文件。将第一个工作表的缩放比例设置为75，并将修改后的文件保存为output.xls。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **冻结窗格**

### **使用Microsoft Excel**

冻结窗格是Microsoft Excel提供的一个功能。冻结窗格允许您在工作表中滚动时选择要保持可见的数据。

### **Aspose.Cells 和 冻结窗格**

Aspose.Cells允许开发人员在运行时将冻结窗格应用于工作表。

Aspose.Cells提供一个代表Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供了管理工作表的多种属性和方法。若要配置冻结窗格，请调用 Worksheet 类的 [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) 方法。[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) 方法包含以下参数：

- **行**，冻结将从该行开始。
- **列**，冻结将从该列开始。
- **冻结行**，顶部窗格中可见的行数。
- **冻结列**，左侧窗格中可见列的数量。

通过在实例化时调用[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类的构造函数来打开book1.xls文件，并在第一个工作表中冻结了一些行和列。修改后的文件保存为output.xls。

下面给出了一个完整示例，展示如何使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)方法来冻结第一个工作表（从C4开始，由第4行和第3列表示，其中行和列从0索引开始）的行和列。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **拆分窗格**

如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请使用拆分窗格。Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并且您可以独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您在一个窗格中进行更改，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。

### **应用和移除拆分窗格**

#### **拆分窗格**

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类提供了一系列用于管理Excel文件的属性和方法。要实现分割视图，请使用[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类的[**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)。要移除分割窗格，请使用[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--)方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用拆分窗格功能到第一个工作表的一个单元格上。然后保存更新后的文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

运行以上代码后，生成的文件将具有分割视图。

#### **移除窗格**

使用 [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) 方法来删除分割窗格。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [隐藏工作表中零值的显示](/cells/zh/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表标签颜色](/cells/zh/javascript-cpp/set-worksheet-tab-color/)
- [显示和隐藏网格线以及行列标题](/cells/zh/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [显示和隐藏行、列和滚动条](/cells/zh/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [显示和隐藏工作表和标签](/cells/zh/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [在工作表中显示公式而非数值](/cells/zh/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/javascript-cpp/use-error-checking-options/)
