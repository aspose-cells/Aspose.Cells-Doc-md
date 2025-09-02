---
title: Render Custom Date Format Pattern g and ge mm dd
linktitle: Render Custom Date Format Pattern g and ge mm dd  
description: Learn how to render custom date format patterns 'g' and 'ge' in Aspose.Cells for JavaScript via C++ to control date display in spreadsheets.  
keywords: Aspose.Cells, JavaScript library, electronic spreadsheet, custom date format, rendering, pattern 'g', pattern 'ge', control display    
type: docs  
weight: 160  
url: /javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells is now able to render the custom date format patterns like g, ge.mm.dd and similar. Please check the attached [source excel file](5112361.xlsx) and the [converted PDF](5112360.pdf) by Aspose.Cells for your reference.

{{% /alert %}}  

The following sample code converts the [source excel file](5112361.xlsx) which contains date values with custom format patterns like g and ge.mm.dd into [output PDF](5112360.pdf).  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            
            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```