---
title: 使用JavaScript通过C++创建和管理Microsoft Excel文件中的表格
linktitle: 表格
type: docs
weight: 150
url: /zh/javascript-cpp/create-and-format-table/
description: 使用Aspose.Cells for JavaScript via C++插入、调整大小、编辑、删除和格式化Excel文件中的表格。
---

## **创建表**

电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。

### **列表对象的优点**

当您将数据列表转换为实际列表对象时，会有相当多的优点

- 新行和列会自动包括在内。
- 列表底部可以轻松添加总计行来显示求和、平均、计数等信息。
- 添加在右侧的列会自动并入列表对象中。
- 基于行和列的图表会自动扩展。
- 分配给行和列的命名范围将自动扩展。
列表受到意外行和列删除的保护。

### **在 Microsoft Excel 中创建列表对象**

- 选择用于创建列表对象的数据范围
- 这将显示创建列表对话框。
- 实现数据的列表对象并指定汇总行（选择 **数据**，然后 **列表**，接着 **总行**）。

### **使用 Aspose.Cells API**

Aspose.Cells 提供了代表 Microsoft Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，允许访问 Excel 文件中的每个工作表。

工作表由 {0} 类表示。{1} 类提供了管理工作表的丰富属性和方法。要在工作表中创建 {2}，使用 {3} 集合属性来自 {4} 类。每个 {5} 实际上是 {6} 类的对象，它还提供用于添加列表对象和指定范围的 {7} 方法。根据指定的单元格范围，Aspose.Cells 会在工作表中创建 {8}，使用 {9} 属性格式化表格以满足您的需求。

在下例中，我们在工作表中添加示例数据，添加一个 [**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--) 并应用默认样式。 [**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--) 样式受到 Microsoft Excel 2007/2010 的支持。

在下面的示例中，我们使用Aspose.Cells API创建了与上节Microsoft Excel中相同的[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **格式化表**

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表格）。 表格是包含相关数据的一系列行和列，独立于其他行和列中的数据。 默认情况下，表中的每一列都在标题行中启用了过滤器，这样您就可以快速过滤或排序列表对象数据。 您可以向列表对象添加一个总行（列表中的特殊行，为使用数字数据工作提供了一系列有用的聚合函数）。 Aspose.Cells提供了创建和管理列表（或表格）的选项。

### **格式化列表对象**

Aspose.Cells 提供了代表 Microsoft Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，允许访问 Excel 文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供了管理工作表的各种属性和方法。要在工作表中创建[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)，使用[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类的[**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--)集合属性。每个[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)实际上是[**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/)类的对象，进而提供[**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-)方法以添加列表对象并指定其涵盖的单元格范围。根据指定的范围，Aspose.Cells会在工作表中创建[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)。使用[**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/)（例如[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)类的属性来格式化表格以满足您的需求。

下例为工作表添加示例数据，添加一个[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)并应用默认样式。[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)样式支持Microsoft Excel 2007/2010。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [将表格转换为ODS](/cells/zh/javascript-cpp/convert-table-to-ods/)
- [查找与外部数据连接相关的查询表和列表对象](/cells/zh/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [读取和写入带有查询表数据源的表格](/cells/zh/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [设置工作表内表格或列表对象的批注](/cells/zh/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表格和区域](/cells/zh/javascript-cpp/tables-and-ranges/)
