---  
title: Convert XLS File with Images or Charts to PDF with JavaScript via C++  
linktitle: Convert XLS File with Images or Charts to PDF  
type: docs  
weight: 50  
url: /javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/  
---  

{{% alert color="primary" %}}  

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for JavaScript via C++ can work independently to convert a spreadsheet to PDF: Aspose.PDF for JavaScript via C++ is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.  

{{% /alert %}}  

## **Sample Code**  

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
            
            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

If the spreadsheet contains formulas, it is best to call the [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) method just before rendering to PDF. Doing so ensures that formula‑dependent values are recalculated, and the correct values are rendered in the PDF.  

{{% /alert %}}