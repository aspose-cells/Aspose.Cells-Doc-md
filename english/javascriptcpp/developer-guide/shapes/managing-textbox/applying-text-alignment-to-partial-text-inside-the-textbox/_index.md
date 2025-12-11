---
title: How to apply/set text alignment to TextBox with JavaScript via C++
linktitle: Apply/Set text alignment to TextBox
type: docs
weight: 20
url: /javascript-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: How to apply/set text alignment to TextBox in Aspose.Cells for JavaScript via C++.
keywords: apply/set alignment TextBox Worksheet Excel Aspose JavaScript via C++
---

TextBoxes can improve the expressiveness of our documents and diagrams, and applying different alignments to different parts of a TextBox can help highlight points of interest to readers. However, the default alignment of a TextBox does not meet all our needs. For this, you may need to adjust each TextBox to meet your target requirements. If you don't have many TextBox objects to tweak, you're in luck. If there are many TextBoxes to adjust, you will be in trouble. Don't worry, [Aspose.Cells](https://products.aspose.com/cells/) provides an API interface to help you do just that.

The following sample code applies text alignment to a TextBox.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add TextBox Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const shapes = worksheet.shapes;

            // add a TextBox
            const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
            shape.text = "This is a test.";

            // set alignment
            shape.textHorizontalAlignment = AsposeCells.TextAlignmentType.Center;
            shape.textVerticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

You can also change the text alignment of some text inside a TextBox shape with the appropriate HTML text. The following sample code applies text alignment to partial text inside the TextBox.

[source file](SampleTextboxExcel2016.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox HTML Transfer Example</title>
    </head>
    <body>
        <h1>TextBox HTML Transfer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MsoDrawingType, Utils } = AsposeCells;
        
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

            // Load source workbook from the selected file
            const sourceWb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the source TextBox whose text is to be aligned
            const sourceTextBox = sourceWb.worksheets.get(0).shapes.get(0);

            // Create an object of the destination workbook
            const destWb = new Workbook();

            // Access the first worksheet from the collection
            const _sheet = destWb.worksheets.get(0);

            // Create a new TextBox
            const _textBox = _sheet.shapes.addShape(MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

            // Use the HTML string from a template file's TextBox
            _textBox.htmlText = sourceTextBox.htmlText;

            // Save the workbook and provide a download link
            const outputData = destWb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Text box HTML copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```