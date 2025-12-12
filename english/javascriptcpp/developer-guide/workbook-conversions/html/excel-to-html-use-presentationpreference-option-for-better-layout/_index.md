---  
title: Excel to HTML - Use PresentationPreference Option for Better Layout with JavaScript via C++  
linktitle: Excel to HTML - Use PresentationPreference Option for Better Layout  
type: docs  
weight: 220  
url: /javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/  
---  

{{% alert color="primary" %}}  

Aspose.Cells provides a useful **HtmlSaveOptions.presentationPreference** property for developers who need to render a better layout when saving a Microsoft Excel file to HTML or MHT format. The default value of the property is **false**. We recommend setting this property to **true** to get a more attractive presentation of Excel reports.  

{{% /alert %}}  

Please see the sample code below that demonstrates how to render an HTML file from an Excel report with **the presentation preference turned on**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Excel to HTML with Presentation Preference</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;
        
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
            
            // Instantiate the Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Create HtmlSaveOptions object
            const options = new HtmlSaveOptions();
            // Set the PresentationPreference option (converted from setPresentationPreference)
            options.presentationPreference = true;
            
            // Save the Excel file to HTML with the specified option
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPresentationlayout1.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```