---
title: 在Excel或OpenOffice中插入超链接
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/javascript-cpp/insert-hyperlinks-to-excel/
description: 如何在使用C++的JavaScript中，用Aspose.Cells库在Excel文件插入超链接而无需MS Excel。
keywords: 在 JavaScript 通过 C++ 插入超链接到 Excel，添加或插入超链接，插入到 URL 链接，插入到单元格，插入到外部文件
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用Aspose.Cells，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}} 

## **添加超链接**
Aspose.Cells允许开发者使用API或设计表格（手动创建超链接并由Aspose.Cells导入到其他表格中）向Excel文件中添加超链接。

Aspose.Cells 提供了一个类 [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个 Microsoft Excel 文件。 [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)，可以访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。 [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供了不同的方法，用于在 Excel 文件中添加超链接。
## **添加指向URL的链接**
[Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类包含一个 [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) 集合。每个项代表一个 [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink)。通过调用 [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) 集合的 [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) 方法为 URL 添加超链接。该方法接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，URL地址。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

在上述示例中，在空单元格**A1**中添加了一个超链接。在这种情况下，如果单元格为空，则URL地址也会作为其值添加到该空单元格。如果单元格不为空并添加了超链接，则单元格的值看起来像普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 
## **将链接添加到同一文件中的单元格**
可以通过调用 [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) 集合的 [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) 方法，为同一 Excel 文件中的单元格添加超链接。该方法支持内部和外部超链接。重载方法之一接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **向外部文件添加链接**
可以通过调用 [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) 集合的 [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) 方法为外部的 Excel 文件添加超链接。该方法接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **高级主题**
- [添加图像超链接](/cells/zh/javascript-cpp/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/javascript-cpp/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/javascript-cpp/get-hyperlinks-in-range/)
