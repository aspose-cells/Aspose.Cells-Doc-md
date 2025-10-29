---
title: 在数据透视表中添加计算字段
type: docs
weight: 130
url: /zh/javascript-cpp/add-calculated-field-in-pivot-table/
description: 如何在使用Aspose.Cells for JavaScript通过C++时为数据透视表添加计算字段。
keywords: 使用Aspose.Cells for JavaScript通过C++，在Excel中使用JavaScript库，为数据透视表添加计算字段。
---

## **可能的使用场景**
当您基于已知数据创建数据透视表时，您会发现其中的数据不是您想要的。您想要的数据是这些原始数据的组合。例如，您需要在希望获取数据之前对原始数据进行加法、减法、乘法和除法。这时，您需要构建一个计算字段并设置相应的计算公式。然后对计算字段执行一些统计和其他操作。 

## **如何在Excel中的数据透视表中添加计算字段**
在Excel中的数据透视表中插入计算字段，请按照以下步骤进行：

1. 选择要向其添加计算字段的数据透视表。 
2. 转到功能区中的数据透视表分析选项卡。
3. 单击“字段、项和集” ，然后从下拉菜单中选择“计算字段”。
4. 在“名称”字段中输入计算字段的名称。
5. 在"公式"字段中，输入要使用适当的数据透视表字段名称和数学运算符进行计算的公式。 
<br>
<img src="1.png" width=80% />
6. 单击"确定"创建计算字段。
7. 新的计算字段将出现在数据透视表字段列表中的值部分。
8. 将计算字段拖动到数据透视表的值部分中，以显示计算值。
<br>
<img src="2.png" width=80% />

## **如何使用Aspose.Cells for Java脚本通过C++库在数据透视表中添加计算字段**
使用Aspose.Cells for Java脚本通过C++向Excel文件添加计算字段。请查看以下示例代码。执行示例代码后，将在工作表中添加带有计算字段的透视表。
1. 设置原始数据并创建数据透视表。 
2. 根据数据透视表中现有的PivotField创建计算字段。
3. 将计算字段添加到数据区。 
4. 最后，以[out.xlsx]格式保存工作簿。 

## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
