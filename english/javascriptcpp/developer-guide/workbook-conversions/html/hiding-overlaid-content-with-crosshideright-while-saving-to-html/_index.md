---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML with JavaScript via C++
linktitle: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel, but when you change the cross type to **CrossHideRight**, it hides all the strings on the right side of a cell that are overlaid or overlapping with the cell's string.

## **Hiding Overlaid Content with CrossHideRight while saving to HTML**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) to **CrossHideRight**. The screenshot explains how **CrossHideRight** affects the output HTML compared with the default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To HTML</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To HTML</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            
            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to HTML
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;
            
            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```