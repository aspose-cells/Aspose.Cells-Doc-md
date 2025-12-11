---
title: Fill Settings
linktitle: Fill Settings
description: Learn how to customize the fill settings, background, and style of cells using the Aspose.Cells library for JavaScript via C++.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style, JavaScript via C++
type: docs
weight: 50
url: /javascript-cpp/cells-fill-settings/
---

## **Colors and Background Patterns**

Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.

Aspose.Cells also supports these features in a flexible manner. In this topic, we learn to use these features using Aspose.Cells.

### **Setting Colors and Background Patterns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection. Each item in the [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class.

The [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) has the [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) property that is used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells provides a [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) enumeration that contains a set of pre‑defined types of background patterns, which are given below.

|**Background Patterns**|**Description**|
| :- | :- |
|DiagonalCrosshatch|Represents diagonal crosshatch pattern|
|DiagonalStripe|Represents diagonal stripe pattern|
|Gray6|Represents 6.25% gray pattern|
|Gray12|Represents 12.5% gray pattern|
|Gray25|Represents 25% gray pattern|
|Gray50|Represents 50% gray pattern|
|Gray75|Represents 75% gray pattern|
|HorizontalStripe|Represents horizontal stripe pattern|
|None|Represents no background|
|ReverseDiagonalStripe|Represents reverse diagonal stripe pattern|
|Solid|Represents solid pattern|
|ThickDiagonalCrosshatch|Represents thick diagonal crosshatch pattern|
|ThinDiagonalCrosshatch|Represents thin diagonal crosshatch pattern|
|ThinDiagonalStripe|Represents thin diagonal stripe pattern|
|ThinHorizontalCrosshatch|Represents thin horizontal crosshatch pattern|
|ThinHorizontalStripe|Represents thin horizontal stripe pattern|
|ThinReverseDiagonalStripe|Represents thin reverse diagonal stripe pattern|
|ThinVerticalStripe|Represents thin vertical stripe pattern|
|VerticalStripe|Represents vertical stripe pattern|

In the example below, the foreground color of the A1 cell is set, but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **Important to Know**

{{% alert color="primary" %}}

- To set a cell's foreground or background color, use the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object's [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) or [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) properties. Both will take effect only if the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object's [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) property is configured.
- The [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) property sets the cell's shade color. The [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), that contains a set of pre‑defined types of background patterns.
- If you select *BackgroundType.None* value from the [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) enumeration, the foreground color is not applied. Likewise, the background color is not applied if you select the *BackgroundType.None* or *BackgroundType.Solid* values.
- When retrieving a cell's shading/fill color, if [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) is *BackgroundType.None*, [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) will return *Color.Empty*.

{{% /alert %}}

### **Applying Gradient Fill Effects**

To apply your desired gradient fill effects to the cell, use the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object's [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) property accordingly.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;
        
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Colors and Palette**

A palette is the set of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97‑2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

### **Adding Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class provides a [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) method that takes the following parameters to add a custom color to the palette:

- **Custom Color** – the custom color to be added.  
- **Index** – the index of the color in the palette that the custom color will replace. Should be between 0‑55.

The example below adds a custom color (Orchid) to the palette before applying it to a font.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this limitation applies only to the XLS (Excel 97‑2003) file format; there is no such limitation for XLSX or other advanced MS Excel (2007/2010/2013) file formats.

{{% /alert %}}