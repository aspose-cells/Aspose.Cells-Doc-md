---
title: Managing TextBox with JavaScript via C++
linktitle: Managing TextBox
type: docs
weight: 50
url: /javascript-cpp/managing-textbox-of-excel/
description: Learn how to manage TextBox in Excel using Aspose.Cells for JavaScript via C++. 
keywords: Manage TextBox in Excel JavaScript via C++
---

## **Possible Usage Scenarios**
There are scenarios where you might need to add, update, or manipulate TextBox objects within an Excel worksheet. This can be useful for adding annotations, guiding texts, or any supplementary information that assists in data presentation. Aspose.Cells for JavaScript via C++ provides robust functionality to manage TextBox in Excel documents. 

## **Managing TextBox using Aspose.Cells for JavaScript via C++**
This example shows how to:

1. Create a new workbook.
2. Add a TextBox shape.
3. Modify properties of the TextBox as needed.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

This code demonstrates how to create and configure a TextBox within an Excel worksheet, showing how to adjust its size, position, and format it according to your requirements.

Keep in mind that interactions with text boxes may vary based on specific use cases, so refer to the Aspose.Cells for JavaScript via C++ documentation for additional methods and properties.