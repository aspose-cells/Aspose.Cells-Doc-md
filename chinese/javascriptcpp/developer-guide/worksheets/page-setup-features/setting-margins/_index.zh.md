---
title: 使用 JavaScript 通过 C++ 设置边距
linktitle: 设置边距
type: docs
weight: 20
url: /zh/javascript-cpp/setting-margins/
description: 在本文中，您将学习如何使用示例代码设置 Excel 工作表的边距，也学习如何通过 JavaScript API 通过 C++ 编程设置页面中心、页眉和页脚的边距。
keywords: 用 JavaScript 通过 C++ 设置 Excel 工作表的边距，设置工作表页眉和页脚边距
---

{{% alert color="primary" %}}

Aspose.Cells 完全支持微软 Excel 的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells 配置页面边距。

{{% /alert %}}

## **设置页边距**

Aspose.Cells for JavaScript 通过 C++ 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含 [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。

[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 属性用于设置工作表的页面设置选项。[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 属性是 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 类的对象，使开发者能够为打印的工作表设置不同的页面布局选项。[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 类提供了多种属性和方法，用于设置页面布局。

### **页面边距**

使用 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 类成员设置页面边距（左、右、上、下）。以下列出几个用于指定页面边距的成员：

- [**PageSetup.leftMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#leftMargin--)
- [**PageSetup.rightMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#rightMargin--)
- [**PageSetup.topMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#topMargin--)
- [**PageSetup.bottomMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#bottomMargin--)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Page Margins Example</title>
    </head>
    <body>
        <h1>Set Page Margins Example</h1>
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
                // Proceed with a new empty workbook if no file selected
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            pageSetup.bottomMargin = 2;
            pageSetup.leftMargin = 1;
            pageSetup.rightMargin = 1;
            pageSetup.topMargin = 3;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetMargins_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page margins set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **页面居中**

可以在页面上水平和垂直居中某个内容。为此，有一些有用的 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 类成员，如 [**PageSetup.centerHorizontally**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerHorizontally--) 和 [**PageSetup.centerVertically**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerVertically--)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Center On Page</title>
    </head>
    <body>
        <h1>Center On Page Example</h1>
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
            // Create a workbook object (blank workbook)
            const workbook = new Workbook();

            // Get the worksheets in the workbook
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pagesetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Center on page Horizontally and Vertically
            pageSetup.centerHorizontally = true;
            pageSetup.centerVertically = true;

            // Save the Workbook in Excel 97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **页眉和页脚边距**

使用 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 类成员（如 [**PageSetup.headerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerMargin--) 和 [**PageSetup.footerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerMargin--)）设置页眉和页脚边距。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Header/Footer Margins</title>
    </head>
    <body>
        <h1>Set Header/Footer Margins Example</h1>
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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Get the worksheets collection
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pageSetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Header / Footer margins (converted from setHeaderMargin/setFooterMargin)
            pageSetup.headerMargin = 2;
            pageSetup.footerMargin = 2;

            // Save the Workbook as Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
