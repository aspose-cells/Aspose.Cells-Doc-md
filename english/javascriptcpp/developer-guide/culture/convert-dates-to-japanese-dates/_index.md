---
title: Convert Dates to Japanese Dates with JavaScript via C++
linktitle: Convert Dates to Japanese Dates
type: docs
weight: 350
url: /javascript-cpp/convert-dates-to-japanese-dates/
description: Learn how to convert Gregorian dates to Japanese dates using Aspose.Cells for JavaScript via C++.
---  

{{% alert color="primary" %}}  

In the Japanese Calendar, a new era begins with the reign of a new emperor. On 1 May 2019, a new emperor came into power, which marked the end of the Heisei era and the beginning of the Reiwa era.  

{{% /alert %}}  

Aspose.Cells provides a way to convert Gregorian dates to Japanese dates. During this conversion, the changes in the era are also considered. The following code snippet converts the [source Excel](90112015.xlsx) file containing Gregorian dates to the [output PDF](90112016.pdf) with Japanese dates as shown in the image below.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel with Japanese Dates to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, CountryCode } = AsposeCells;
        
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

            // Create LoadOptions for XLSX and set language/region to Japan
            const options = new LoadOptions(LoadFormat.Xlsx);
            options.languageCode = CountryCode.Japan;
            options.region = CountryCode.Japan;

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'JapaneseDates.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```