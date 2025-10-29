---
title: 数据排序
type: docs
weight: 130
url: /zh/javascript-cpp/sort-data-of-excel/
description: 学习如何使用Aspose.Cells for JavaScript通过C++ API对数据进行排序。
keywords: 按升序或降序对数据进行排序，根据背景颜色对数据进行排序
---

{{% alert color="primary" %}}

数据排序是微软Excel的许多实用功能之一。它允许用户排列数据，使其更易扫描。Aspose.Cells for JavaScript通过C++允许开发者按字母顺序或数字顺序排序工作表数据，其方式与微软Excel排序数据相同。

{{% /alert %}}

## **在 Microsoft Excel 中排序数据**

要在 Microsoft Excel 中排序数据：

1. 从“排序”菜单中选择“数据”。将显示“排序”对话框。
1. 选择排序选项。

通常，排序是针对一个列表执行的 - 定义为一组连续的数据，数据以列显示。

## **使用 Aspose.Cells 进行数据排序**

Aspose.Cells for JavaScript通过C++提供了用于以升序或降序排序数据的[**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter)类，该类具有一些重要成员，例如Key1 ... Key3和Order1 ... Order3属性，这些成员用于定义排序的关键字和指定排序顺序。

在执行数据排序之前，您必须定义关键字并设置排序顺序。该类提供了 [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) 方法，用于根据工作表中的单元格数据执行数据排序。

[**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) 方法接受以下参数：

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)，基础工作表的单元格。
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)，单元格范围。在应用数据排序前定义单元格区域。

此示例使用在Microsoft Excel中创建的模板文件"Book1.xls"。在执行下面的代码后，数据将被适当地排序。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

如果要进行*由左至右*的排序，请使用[**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-)属性。

{{% /alert %}}

### **以背景颜色排序数据**

Excel提供了根据背景色排序数据的功能。使用Aspose.Cells for JavaScript通过C++的DataSorter，可以使用[**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor在[**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-)中根据背景色排序数据。所有包含指定颜色的单元格在[**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-)中的函数会根据SortOrder设置放在顶部或底部，其余单元格顺序不变。

以下是可以下载以进行此功能测试的样本文件：

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [使用自定义排序列表对列中的数据进行排序](/cells/zh/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [在对数据进行排序时指定排序警告](/cells/zh/javascript-cpp/specifying-sort-warning-while-sorting-data/)
