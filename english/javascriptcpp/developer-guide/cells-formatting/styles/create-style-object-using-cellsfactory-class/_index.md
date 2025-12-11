---
title: Create Style object using CellsFactory class
linktitle: Create Style object using CellsFactory class
description: Learn how to create a cell style object using the CellsFactory class in Aspose.Cells for JavaScript via C++. Customize the appearance of spreadsheet cells as needed.
keywords: Aspose.Cells, JavaScript via C++, electronic spreadsheet, style object, cell style, customization
type: docs
weight: 70
url: /javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **Create Style object using CellsFactory class**
The following sample code creates a [Style](https://reference.aspose.com/cells/javascript-cpp/style) object using the [CellsFactory](https://reference.aspose.com/cells/javascript-cpp/cellsfactory) class and then sets the Default Style of the workbook. Please download the [output Excel file](5115153.xlsx) to see the results of this code for your reference.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;
        
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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```