---  
title: How to Use Color Palette  
linktitle: How to Use Color Palette  
type: docs  
weight: 80  
url: /javascript-cpp/excel-color-palette/  
description: JavaScript code to add custom colors to the palette and use Excel color palette with Aspose.Cells for JavaScript via C++.  
keywords: JavaScript add custom colors to the palette, JavaScript programmatically excel color palette, programmatically how to use color palette in workbook, JavaScript how to use color palette in excel  
---  

## **Colors and Palette**  

A palette is the set of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97‑2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.  

With Aspose.Cells for JavaScript via C++, it is possible not only to use the palette's existing colors, but also to use custom colors. Before using a custom color, add it to the palette first.  

This topic discusses how to add custom colors to the palette.  

## **Add Custom Colors to Palette**  

Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) class provides a [**changePalette(Color, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) method that takes the following parameters to modify the palette by adding a custom color:  

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
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;
        
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            const isInPaletteBefore = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteBefore);
            resultDiv.innerHTML = `<p>Is Orchid in palette before change: ${isInPaletteBefore}</p>`;

            // Adding Orchid color to the palette at the 55th index
            workbook.changePalette(Color.Orchid, 55);

            const isInPaletteAfter = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteAfter);
            resultDiv.innerHTML += `<p>Is Orchid in palette after change: ${isInPaletteAfter}</p>`;

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding a value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining a new Style object
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
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

The palette holds only 56 colors. When you add a custom color, the palette is changed, and any element in the file formatted with the previous color is also changed. Therefore, when you modify the palette, please be very careful. Moreover, this limitation applies only to the XLS (Excel 97‑2003) file format; there is no such limitation for XLSX or other newer Excel (2007, 2010, 2013, etc.) file formats.  

{{% /alert %}}  