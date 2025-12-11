---  
title: Read Chart Subtitle from ODS File using JavaScript via C++  
linktitle: Read Chart Subtitle from ODS File  
description: Learn how to use Aspose.Cells for JavaScript via C++ to read the chart subtitle from an OpenDocument Spreadsheet (ODS) file. Our guide will demonstrate how to extract and access the subtitle of a chart for further analysis or display.  
keywords: Aspose.Cells for JavaScript via C++, Read Chart Subtitle, OpenDocument Spreadsheet, ODS File, Chart Extraction, Data Analysis.  
type: docs  
weight: 160  
url: /javascript-cpp/read-chart-subtitle-from-ods-file/  
---  

## **Read Chart Subtitle from ODS File**

Aspose.Cells provides the ability to read chart subtitles in ODS files by using the [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) property. The following sample code loads the [sample ODS file](89620481.ods) and reads the chart subtitle using the [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) property and prints it in the console window. Please see the console output from the code given below for reference.  

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```  

## **Console Output**

{{< highlight javascript >}}  
Chart Subtitle: Sample Chart Subtitle  
{{< /highlight >}}