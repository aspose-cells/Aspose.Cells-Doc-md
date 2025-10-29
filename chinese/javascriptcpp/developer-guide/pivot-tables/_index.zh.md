---
title: 插入数据透视表
linktitle: 数据透视表
type: docs
weight: 160
url: /zh/javascript-cpp/create-pivot-table/
description: 创建和格式化Excel电子表格文件的数据透视表。
---

## **创建数据透视表**

可以使用Aspose.Cells for JavaScript通过C++以编程方式为电子表格添加数据透视表。

### **数据透视表对象模型**

Aspose.Cells for JavaScript通过C++提供了一套特殊的类，用于创建和控制数据透视表。这些类用于创建和设置[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)对象，数据透视表的基本构件。这些对象包括：

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) 代表 [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) 中的一个字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) 代表 [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) 中的所有 [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) 代表工作表上的数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) 代表工作表上的所有 [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) 对象的集合。

### **使用 Aspose.Cells 创建一个简单的数据透视表**

1. 使用 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 对象的 [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) 方法向工作表添加数据。
   这些数据将被用作数据透视表的数据源。
1. 通过调用 [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) 集合的 [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) 方法（封装在工作表对象中）向工作表添加一个数据透视表。
1. 通过传递数据透视表索引从 [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) 集合中访问新的 [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) 对象。
1. 使用上面解释的任何 [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) 对象来管理数据透视表。

执行示例代码后，数据透视表将被添加到工作表中。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

当将一系列单元格指定为数据源时，该范围必须从左上到右下。例如，“A1:C3”是有效的，但“C3:A1”是无效的。

{{% /alert %}}
