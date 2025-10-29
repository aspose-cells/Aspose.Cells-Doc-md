---
title: 管理Excel文件的数据
linktitle: 单元格数据
type: docs
weight: 110
url: /zh/javascript-cpp/view-and-edit-excel-data/
description: 本文介绍如何使用Aspose.Cells库通过JavaScript调用C++的方式查看和编辑Excel文件的数据。
keywords: Aspose.Cells JavaScript通过C++管理Excel文件数据，添加数据到Excel文件，从Excel文件获取数据，如何提高添加数据的效率，管理和更新单元格数据，获取单元格数据，插入单元格数据
---

{{% alert color="primary" %}}

在[访问工作表单元格](/cells/zh/javascript-cpp/accessing-cells-of-a-worksheet/)中，我们讨论了访问工作表单元格的基本方法。本文使用其中一种方法向单元格添加不同类型的数据。

{{% /alert %}}

## **如何向单元格添加数据**

Aspose.Cells for Java通过C++脚本提供了一个类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可以访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供一个[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合，集合中的每个项目代表一个[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的对象。

Aspose.Cells允许开发者通过调用[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)方法向工作表中的单元格添加数据。Aspose.Cells提供了[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)方法的重载版本，允许开发者向单元格添加不同类型的数据。使用这些重载版本的[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)方法，可以向单元格添加布尔值、字符串、双精度、整数或日期/时间等值。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **如何提高效率**

如果你使用[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)方法将大量数据放入工作表，应该先按行、再按列向单元格添加值。这种方法极大地提高了应用程序的效率。

## **如何从单元格中检索数据**

Aspose.Cells for JavaScript通过C++提供一个类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个微软Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可以访问文件中的工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供一个[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合中的每个项目代表一个[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类提供了多个属性，允许开发者根据数据类型从单元格中检索值。这些属性包括：

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--)：返回单元格的字符串值。
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--)：返回单元格的双精度值。
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--)：返回单元格的布尔值。
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--)：返回单元格的日期/时间值。
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--)：返回单元格的浮点值。
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--)：返回单元格的整数值。

当字段未填写时，包含[**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--)或[**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--)的单元格会抛出异常。

还可以通过使用[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)方法检查单元格中包含的数据类型。实际上，[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)方法基于以下列出的一组预定义值的[**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype)枚举：

|**单元格值类型**|**描述**|
| :- | :- |
|IsBool|指定单元格值为布尔类型。|
|IsDateTime|指定单元格值为日期/时间类型。|
|IsNull|表示空白单元格。|
|IsNumeric|指定单元格值为数值类型。|
|IsString|指定单元格值为字符串类型。|
|IsUnknown|指定单元格值为未知类型。|

你还可以使用上面预定义的单元格值类型与每个单元格中实际数据的类型进行比较。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

在操作工作表时，用户可能在单元格中添加不同类型的数据。这些数据类型可能包括布尔值、整数、浮点数、文本或日期/时间值。使用Aspose.Cells，可以根据数据类型获取相应的单元格值。

{{% /alert %}}

## **高级主题**
- [访问工作表的单元格](/cells/zh/javascript-cpp/accessing-cells-of-a-worksheet/)
- [将文本数值数据转换为数字](/cells/zh/javascript-cpp/convert-text-numeric-data-to-number/)
- [创建小计](/cells/zh/javascript-cpp/creating-subtotals/)
- [数据筛选](/cells/zh/javascript-cpp/data-filtering/)
- [数据排序](/cells/zh/javascript-cpp/sort-data-of-excel/)
- [数据有效性](/cells/zh/javascript-cpp/data-validation/)
- [查找或搜索数据](/cells/zh/javascript-cpp/find-or-search-data/)
- [获取有格式和无格式的单元格字符串值](/cells/zh/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [在单元格内添加HTML富文本](/cells/zh/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [在Excel或OpenOffice中插入超链接](/cells/zh/javascript-cpp/insert-hyperlinks-to-excel/)
- [如何在何处使用枚举器](/cells/zh/javascript-cpp/how-and-where-to-use-enumerators/)
- [以像素为单位测量单元格值的宽度和高度](/cells/zh/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [同时读取多个线程中的单元格值](/cells/zh/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [单元格名称和行/列索引之间的转换](/cells/zh/javascript-cpp/names-and-indices/)
- [首先按行，然后按列填充数据](/cells/zh/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [保留单引号前缀的单元格值或范围](/cells/zh/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [访问和更新单元格的富文本部分](/cells/zh/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
