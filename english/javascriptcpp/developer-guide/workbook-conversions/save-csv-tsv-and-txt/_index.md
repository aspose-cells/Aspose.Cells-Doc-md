---  
title: Convert Excel to CSV, TSV and Txt with JavaScript via C++  
linktitle: Save as CSV, TSV and Txt  
type: docs  
weight: 40  
url: /javascript-cpp/convert-excel-to-csv-tsv-and-txt/  
description: Learn how to convert Excel files to CSV, TSV, and TXT formats using Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells makes it possible to convert Excel, ODS, JSON, and other format files to CSV, TSV, and TXT.  

{{% /alert %}}  

## **Saving Workbook to Text or CSV Format**  

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default, both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.  

The following code example explains how to save an entire workbook into text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS, and so on) with any number of worksheets.  

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.  

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) is a comma, so do not specify a separator if saving to CSV format.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Txt Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Txt Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator.
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (as text)
            const outputData = workbook.save(SaveFormat.Txt, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as text. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Saving Text Files with Custom Separator**  

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Workbook to TXT/CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions, SaveFormat } = AsposeCells;
        
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

            // Create a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Optionally specify CSV save format if required by the API
            options.saveFormat = SaveFormat.CSV;

            // Save the workbook to CSV/TXT using the options
            const outputData = wb.save(SaveFormat.CSV, options);
            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```  


## **Advanced topics**  
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](/cells/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)  
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)