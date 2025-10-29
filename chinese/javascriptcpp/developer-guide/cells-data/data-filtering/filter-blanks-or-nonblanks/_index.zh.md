---
title: 如何筛选空白或非空白
type: docs
weight: 85
url: /zh/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: 学习如何通过C++ API用Aspose.Cells for JavaScript筛选空白和非空白单元格。
keywords: 筛选空白，筛选非空白，工作表中筛选空白，工作表中筛选非空白，Excel中筛选空白，Excel中筛选非空白，Excel中筛选空白和非空白
---

## **可能的使用场景**
在 Excel 中对数据进行筛选是一项有价值的工具，通过使用户能够根据其条件专注于特定数据子集, 提升了数据分析、探索和演示功能, 使整体的数据处理和解释过程更加高效和有效。

## **如何在 Excel 中筛选空白或非空白**
在 Excel 中，您可以轻松地使用筛选选项来筛选空白或非空白。以下是操作步骤：

### **如何在 Excel 中筛选空白**
1. 选择范围：点击列标题的字母以选择整个列或选择要筛选空白的范围。
1. 打开筛选菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 筛选选项：单击“筛选”按钮。这将在所选范围添加筛选箭头。
1. 筛选空白：点击要筛选空白的列中的筛选箭头。取消选择除“空白”之外的所有选项，然后单击“确定”。这将仅显示该列中的空白单元格。
<br>
<image src="2.png" width="70%" />
1. 结果如下：
<br>
<image src="3.png" width="70%" />

### **如何在 Excel 中筛选非空白**
1. 选择范围：单击列标题的字母以选择整个列，或选择要筛选非空的范围。
1. 打开筛选菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 筛选选项：单击“筛选”按钮。这将在所选范围添加筛选箭头。
1. 筛选非空：单击要筛选非空的列中的筛选箭头。取消选择除“非空”或“自定义”之外的所有选项，并相应设置条件。单击“确定”。这将仅显示该列中非空的单元格。
<br>
<image src="4.png" width="70%" />
1. 结果如下：
<br>
<image src="5.png" width="70%" />

## **如何使用Aspose.Cells for JavaScript通过C++筛选空白单元格**
如果一列包含文本，以至于部分单元格为空，需要筛选只包含空白单元格的行，可以使用[**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-)和[**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-)函数，如下所示。 

请参阅以下示例代码，该代码加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)。示例代码使用三种方法来筛选空白。然后，将工作簿另存为[输出Excel文件](FilteredBlanks.xlsx)。 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **如何使用Aspose.Cells for JavaScript通过C++筛选非空白单元格**

请参阅加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)的示例代码。加载文件后，调用[AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-)函数以筛选非空数据，最后将工作簿保存为[输出Excel文件](FilteredNonBlanks.xlsx)。 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
