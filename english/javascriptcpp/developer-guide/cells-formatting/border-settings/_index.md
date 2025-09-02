---
title: Border Settings
linktitle: Border Settings
description: How to use the Aspose.Cells library in JavaScript via C++ to set the border style and color of cells. By adjusting the width, style, and color of the border, you have more control over how cells look and appear.
keywords: Aspose.Cells, Cell Border Settings, JavaScript via C++, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /javascript-cpp/cells-border-settings/
---

## **Adding Borders to Cells**

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells for JavaScript via C++, developers can add borders and customize what they look like in the same flexible way as in Microsoft Excel.

### **Adding Borders to Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides the [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection. Each item in the [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class.

Aspose.Cells provides the [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) property in the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class. The [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) is used to set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) class provides properties for adding borders to cells.

#### **Adding Borders to a Cell**

Developers can add borders to a cell by using the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object's [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) collection. The border type is passed as an index to the [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) collection. All border types are pre-defined in the [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) enumeration.

**Border enumeration**

|**Border Types**|**Description**|
| :- | :- |
|BottomBorder|A bottom border line|
|DiagonalDown|A diagonal line from top left to right bottom|
|DiagonalUp|A diagonal line from bottom left to right top|
|LeftBorder|A left border line|
|RightBorder|A right border line|
|TopBorder|A top border line|

The [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) collection stores all borders. Each border in the [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) collection is represented by a [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) and [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) to set a border's line color and style respectively.

To set a border's line color, select a color using the Color enumeration (part of JavaScript) and assign it to the Border object's color property.

The border's line style is set by selecting a line style from the [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) enumeration.

**CellBorderType enumeration**

|**Line Styles**|**Description**|
| :- | :- |
|DashDot|Thin dash-dotted line|
|DashDotDot|Thin dash-dot-dotted line|
|Dashed|Dashed line|
|Dotted|Dotted line|
|Double|Double line|
|Hair|Hairline|
|MediumDashDot|Medium dash-dotted line|
|MediumDashDotDot|Medium dash-dot-dotted line|
|MediumDashed|Medium dashed line|
|None|No line|
|Medium|Medium line|
|SlantedDashDot|Slanted medium dash-dotted line|
|Thick|Thick line|
|Thin|Thin line|
Select one of the line styles and then assign it to the [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) object's [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) property.

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
You should set both line style and color at the same time. The two diagonal border lines should have the same line style and color.
{{% /alert %}}

#### **Adding Borders to a Range of Cells**

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first, create a range of cells by calling the [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection's [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) method. It takes the following parameters:

- First Row, the first row of the range.
- First Column, represents the first column of the range.
- Number of Rows, the number of rows in the range.
- Number of Columns, the number of columns in the range.

The [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) method returns a [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) object, which contains the specified range of cells. The [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) object provides a [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) method that takes the following parameters to add a border to the range of cells:

- **Border Type**, the border type, selected from the [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) enumeration.
- **Line Style**, the border line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) enumeration.
- **Color**, the line color, selected from the Color enumeration.

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