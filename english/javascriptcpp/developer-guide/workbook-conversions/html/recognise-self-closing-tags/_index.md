---  
title: Recognise Self Closing Tags with JavaScript via C++  
linktitle: Recognise Self Closing Tags  
type: docs  
weight: 120  
url: /javascript-cpp/recognise-self-closing-tags/  
---  

HTML can have a variety of tag formatting for empty tags like `<td></td>` or `<td/>`. Aspose.Cells for JavaScript via C++ supports both formats now, whereas earlier it only supported `<td></td>`-like tags. This feature can be tested by converting the attached sample HTML file to an Excel file. The sample HTML file and output Excel file can be downloaded from the following links for testing.  

[sampleSelfClosingTags.html](sampleSelfClosingTags)  

[outsampleSelfClosingTags.xlsx](73990156.xlsx)  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert HTML to Excel Example</h1>
        <input type="file" id="fileInput" accept=".html,.htm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat, Utils } = AsposeCells;
        
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an HTML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set HTML load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);

            // Instantiating a Workbook object by loading the HTML file stream with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the workbook to XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleSelfClosingTags.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the XLSX file.</p>';
        });
    </script>
</html>
```