---
title: 使用C++的JavaScript管理分页符
linktitle: 管理分页
type: docs
weight: 30
url: /zh/javascript-cpp/managing-page-breaks/
description: 本文提供示例代码，说明如何通过Aspose.Cells for JavaScript使用C++编程方式添加、清除或删除Excel工作表中的特定分页符。
keywords: 分页符JavaScript通过C++，Excel分页符JavaScript通过C++，清除分页符JavaScript通过C++，删除特定分页符JavaScript通过C++
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

分页符添加在单元格位置后，页面结束并在打印时分页符后的数据打印在下一页。简单地说，分页符根据您的设定将工作表分成多页。您还可以在运行时使用 Aspose.Cells 添加分页符。Aspose.Cells 允许开发人员添加两种分页符：

- 水平分页
- 垂直分页

在接下来的讨论中，我们将描述如何使用Aspose.Cells向工作表添加水平或垂直分页。

{{% /alert %}}

## **分页**

Aspose.Cells for JavaScript通过C++提供了一个[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类，用于表示Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供了用于管理工作表的广泛的属性和方法。

要添加分页符，使用 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类的 [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) 和 [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) 属性。

[**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) 和 [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) 属性是可能包含多个分页符的集合。每个集合都包含用于管理水平和垂直分页符的几种方法。

### **添加分页**

要在工作表中添加分页符，在指定的单元格插入水平和垂直分页符，调用 [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-) 和 [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-) 方法。每个 **add** 方法都接受要添加分页符的单元格名称。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}

### **移除特定的分页符**

要删除特定分页符，请调用[**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-)和[**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-)方法。每个**removeAt**方法都接受即将删除的分页符的索引。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **重要提示**

当你在分页设置中设置**fitToPages**属性（即[**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--)和[**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)）时，分页设置会受到影响，因此，如果你打印工作表，分页设置将不予考虑，尽管它们仍然被设置。
