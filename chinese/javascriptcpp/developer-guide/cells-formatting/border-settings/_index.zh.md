---
title: 边框设置
linktitle: 边框设置
description: 如何在JavaScript via C++中使用Aspose.Cells库设置单元格的边框样式和颜色。通过调整边框的宽度、样式和颜色，可以更好地控制单元格的外观和表现。
keywords: Aspose.Cells，单元格边框设置，JavaScript通过C++，边框宽度，边框样式，边框颜色
type: docs
weight: 40
url: /zh/javascript-cpp/cells-border-settings/
---

## **向单元格添加边框**

微软Excel允许用户为单元格添加边框。边框类型取决于添加的位置。例如，上边框是添加到单元格顶部的位置。用户还可以修改线条样式和颜色。

使用Aspose.Cells for JavaScript via C++，开发者可以像在Microsoft Excel中一样添加边框并自定义其外观，具有相同的灵活性。

### **向单元格添加边框**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供了[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合。[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合中的每个元素都代表一个[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的对象。

Aspose.Cells在[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类中提供了[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)属性。[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)用于设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)类提供了为单元格添加边框的属性。

#### **向单元格添加边框**

开发者可以通过使用[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)对象的[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)集合为单元格添加边框。边框类型作为索引传入[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)集合。所有边框类型都在[**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype)枚举中预定义。

**边框枚举**

|**边框类型**|**描述**|
| :- | :- |
|BottomBorder| 底部边框线|
|DiagonalDown| 从左上到右下的对角线|
|DiagonalUp| 从左下到右上的对角线|
|LeftBorder|左边框线|
|RightBorder|右边框线|
|TopBorder|顶部边框线|

[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)集合存储所有边框。[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)集合中的每个边框由[**Border**](https://reference.aspose.com/cells/javascript-cpp/border)对象表示，提供两个属性，[**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-)和[**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-)，分别设置边框的线色和线样式。

要设置边框的线条颜色，使用Color枚举（JavaScript部分）选择一种颜色，并将其赋值给Border对象的color属性。

通过从 [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) 枚举中选择线条样式来设置边框的线条样式。

**CellBorderType枚举**

|**线条样式**|**描述**|
| :- | :- |
|DashDot|细长虚点线|
|DashDotDot|细长虚点虚点线|
|Dashed|虚线|
|Dotted|点状线|
|Double|双线|
|Hair|细线|
|MediumDashDot|中等虚点线|
|MediumDashDotDot|中等虚点虚点线|
|MediumDashed|中等虚线|
|None|无线|
|Medium|中线|
|SlantedDashDot|倾斜中等虚点线|
|Thick|粗线|
|Thin|细线|
选择一种线条样式，然后将其分配给 [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) 对象的 [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) 属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
你应该同时设置线条样式和颜色。两个对角线边框线应具有相同的线条样式和颜色。
{{% /alert %}}

#### **向单元格范围添加边框**

也可以对一范围单元格添加边框，而不仅仅是单个单元格。首先，通过调用 [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合的 [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) 方法创建一个单元格范围。它接受以下参数：

- 第一行，范围的第一行。
- 第一列，表示范围的第一列。
- 行数，范围中的行数。
- 列数，范围中的列数。

[**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) 方法返回一个 [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 对象，其中包含指定范围的单元格。[**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 对象提供一个 [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) 方法，可以接受以下参数，为单元格范围添加边框：

- **边框类型**，选择自 [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) 枚举的边框类型。
- **线条样式**，选择自 [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) 枚举的边框线条样式。
- **颜色**，线条颜色，从Color枚举中选择。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
