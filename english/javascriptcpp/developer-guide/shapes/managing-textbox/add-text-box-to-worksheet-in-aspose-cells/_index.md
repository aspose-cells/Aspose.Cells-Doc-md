---
title: How to add/insert TextBox to Worksheet with JavaScript via C++
linktitle: Add Text Box to Worksheet
type: docs
weight: 10
url: /javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: How to add/insert Text Box to Worksheet in Aspose.Cells for JavaScript via C++.
keywords: add/insert Text Box TextBox Worksheet Excel Aspose JavaScript via C++
---

## Add Text Box to Worksheet in Excel

In Excel (version 2007 and above), there are two places where you can insert text boxes: one in **Insert → Shapes**, and the other on the right side of the top menu under the **Insert** tab.

### Method one:

![1](1.png)

### Method two:

![2](2.png)

## How to create

You can create text boxes with horizontal or vertical text.

- Select the corresponding option (horizontal or vertical)  
- Left‑click on the page  
- Hold down the left button and drag a distance on the page  
- Release the left button  

Now you get a text box.

## Add Text Box to Worksheet in Aspose.Cells for JavaScript via C++

When you need to bulk‑insert TextBox objects into the worksheet, the manual insertion method is obviously impractical. If this bothers you, this document will help. [Aspose.Cells](https://products.aspose.com/cells/) provides an API to easily perform bulk inserts in your code.

The following sample code creates a text box.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

You will get a file similar to the [result file](result.xlsx). In the file, you will see the following:

![](52449.png)