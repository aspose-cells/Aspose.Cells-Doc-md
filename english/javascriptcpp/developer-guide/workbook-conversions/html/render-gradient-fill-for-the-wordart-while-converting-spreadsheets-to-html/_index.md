---  
title: Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML with JavaScript via C++  
linktitle: Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML  
type: docs  
weight: 90  
url: /javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Learn how to render gradient fill for WordArt when converting spreadsheets to HTML using Aspose.Cells for JavaScript via C++.  
---  

## **Possible Usage Scenarios**  
Before Aspose.Cells 17.1, Aspose.Cells did not render the gradient fill of WordArt when the Excel file was converted to HTML format. Since the release of Aspose.Cells 17.1, WordArt gradient fill is supported. The following screenshot compares the effect of the gradient fill when converting the Excel file using Aspose.Cells 17.1 and an older version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML**  
The following sample code converts the [source Excel file](22774111.xlsx) into the [output HTML format](22774109.zip). The source Excel file contains a WordArt object with gradient fill as shown in the above screenshot.  

## **Sample Code**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```