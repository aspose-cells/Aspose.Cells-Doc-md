---
title: Modify an Existing Style
linktitle: Modify an Existing Style
description: Aspose.Cells is a JavaScript via C++ library for working with spreadsheet files that allows users to modify existing cell styles. This article introduces how to modify an existing cell style with the Aspose.Cells library so that users can change the appearance of the cells as they need.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

To apply the same formatting options to cells, create a new formatting style object. A formatting style object is a combination of formatting characteristics, such as font, font size, indentation, number, border, patterns, etc., named and stored as a set. When applied, all of the formatting in that style is applied.

You can also use an existing style, save it with the workbook, and use it to format information with the same attributes.

When cells aren't explicitly formatted, the **Normal** style (the workbook's default style) is applied. Microsoft Excel predefines several styles in addition to the Normal style, including Comma, Currency, and Percent.

Aspose.Cells allows modifying any of these styles or any other style that you define with your desired attributes.

{{% /alert %}}

## **Using Microsoft Excel**

To update a style in Microsoft Excel 97-2003:

1. On the **Format** menu, click **Style**.  
2. Select the style you want to modify from the **Style name** list.  
3. Click **Modify**.  
4. Select the style options that you want using the tabs in the **Format Cells** dialog.  
5. Click **OK**.  
6. Under **Style includes**, specify the style features you want.  
7. Click **OK** to save the style and apply it to the selected range.

## **Using Aspose.Cells for JavaScript via C++**

The following examples demonstrate how to use the [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--) method.

### **Creating and Modifying a Style**

This example creates a [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object, applies it to a range of cells, and modifies the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object. The modifications are automatically applied to the cell and the range the style was applied to.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the cells of the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Apply the style (described above) to cell A1.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize a StyleFlag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and a range,
            // the change is reflected (the new modification is implemented) to cell A1 and
            // range B1:D1.
            style.update();

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Modifying an Existing Style**

This example uses a simple template Excel file in which a style called **Percent** has already been applied to a range. The example:

1. Gets the style.  
2. (Optionally) creates a style object.  
3. Modifies the style formatting.

The modifications are automatically applied to the range the style was applied to.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;
        
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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```