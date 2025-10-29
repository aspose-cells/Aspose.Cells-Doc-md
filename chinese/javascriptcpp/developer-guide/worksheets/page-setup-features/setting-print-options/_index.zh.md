---
title: 使用C++的JavaScript设置打印选项
linktitle: 设置打印选项
type: docs
weight: 40
url: /zh/javascript-cpp/setting-print-options/
description: 本文演示了如何使用JavaScript API和C++库以编程方式设置Excel工作表页面设置功能的打印选项。您可以设置打印区域、打印标题和页面顺序。
keywords: 用C++的JavaScript设置Excel打印区域，用JavaScript设置打印标题，设置和清除打印标题，用JavaScript清除打印标题，用JavaScript添加打印标题，用JavaScript移除打印标题，在Excel中设置打印标题，在Excel中清除打印标题。
---

{{% alert color="primary" %}}

Microsoft Excel的页面设置提供了几个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。

{{% /alert %}}

## **设置打印选项**

这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

Aspose.Cells for JavaScript通过C++支持所有由Microsoft Excel提供的打印选项，开发者可以使用[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)类提供的属性轻松配置这些选项。关于如何使用这些属性将在下面详细讨论。

### **设置打印区域**

默认情况下，打印区域包括包含数据的工作表的所有区域。开发人员可以为工作表确定特定的打印区域。

要选择特定的打印区域，请使用 [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) 类的 [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) 属性。将定义打印区域的单元范围分配给此属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **设置打印标题**

Aspose.Cells 允许您指定行列标题在打印工作表的所有页面上重复显示。要这样做，请使用 [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) 类的 [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) 和 [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) 属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) 类还提供了几个其他属性来设置常规打印选项如下：

 - [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--)：一个布尔属性，定义是否打印网格线。
 - [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--)：一个布尔属性，定义是否打印行和列标题。
 - [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--)：一个布尔属性，定义是否以黑白模式打印工作表。
 - [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--)：定义是否在工作表上或在工作表末尾显示打印注释。
 - [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--)：一个布尔属性，定义是否无图形打印工作表。
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--)：定义是否按显示的方式、空白、短横线或N/A打印单元格错误。

要设置[**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--)和[**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--)属性，Aspose.Cells for JavaScript通过C++还提供了两个枚举[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)和[**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype)，它们包含预定义的值，分别赋值给[**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--)和[**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--)属性。

 [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)枚举中的预定义值及其描述如下。

|**打印备注类型**|**描述**|
| :- | :- |
|PrintInPlace|指定将批注打印为显示在工作表上的形式。
|PrintNoComments|指定不打印批注。
|PrintSheetEnd|指定将批注打印在工作表末尾。

 [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype)枚举的预定义值及其描述如下。

|**打印错误类型**|**描述**|
| :- | :- |
|PrintErrorsBlank|指定不打印错误。|
|PrintErrorsDash|指定打印错误为"--"。|
|PrintErrorsDisplayed|指定打印错误为显示的形式。|
|PrintErrorsNA|指定打印错误为"#N/A"。|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **设置页面顺序**

 [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)类提供了[**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--)属性，用于排序工作表的多个页面以进行打印。主要有两种页面排序方式。

- 打印所有页面，然后再打印任何页面到右侧。
- 先从左到右打印页面，然后打印下面的页面。

 Aspose.Cells 提供了包含所有预定义排序类型的枚举[**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype)。

 [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype)枚举的预定义值及其描述如下。

|**打印顺序类型**|**描述**|
| :- | :- |
|DownThenOver|表示打印顺序为先向下再向右。|
|OverThenDown|表示打印顺序为先向右再向下。|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
