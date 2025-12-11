---  
title: Load or Import CSV file with Formulas via JavaScript  
linktitle: Load or Import CSV file with Formulas  
type: docs  
weight: 350  
url: /javascript-cpp/load-or-import-csv-file-with-formulas/  
description: Learn how to load and import CSV files containing formulas using Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}

CSV files mostly contain textual data and do not contain any formulas. However, sometimes CSV files contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.hasFormula](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#hasFormula--) as **true**. Once this property is set to **true**, Aspose.Cells will not treat formulas as simple text. They will be treated as formulas, and the Aspose.Cells formula calculation engine will process them as usual.  

{{% /alert %}}

The following code illustrates how you can load as well as import a CSV file with formulas. You can use any CSV file. For illustration purposes, we use the [simple csv file](5115034.csv) which contains this data. As you can see, it contains a formula.  

{{< highlight javascript >}}  
<!DOCTYPE html>  
<html>  
    <head>  
        <title>Load CSV with Formulas and Save as XLSX</title>  
    </head>  
    <body>  
        <h1>Load CSV with Formulas and Save as XLSX</h1>  
        <input type="file" id="fileInput" accept=".csv" />  
        <button id="convertToXlsx">Convert to XLSX</button>  
        <a id="downloadLink" style="display: none;">Download XLSX</a>  
        <div id="result"></div>  

        <script src="aspose.cells.js.min.js"></script>  
        <script type="text/javascript">  
            const { Workbook, TxtLoadOptions, SaveFormat } = AsposeCells;  

            AsposeCells.onReady().then(() => {  
                console.log("Aspose.Cells initialized");  
            });  

            document.getElementById('convertToXlsx').addEventListener('click', async () => {  
                const fileInput = document.getElementById('fileInput');  
                if (!fileInput.files.length) {  
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';  
                    return;  
                }  

                const file = fileInput.files[0];  
                const arrayBuffer = await file.arrayBuffer();  

                const loadOptions = new TxtLoadOptions();  
                loadOptions.hasFormula = true;  

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);  

                const outputData = workbook.save(SaveFormat.Xlsx);  
                const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });  
                const downloadLink = document.getElementById('downloadLink');  
                downloadLink.href = URL.createObjectURL(blob);  
                downloadLink.download = file.name.replace(/\.csv$/i, '.xlsx');  
                downloadLink.style.display = 'block';  
                downloadLink.textContent = 'Download XLSX File';  

                document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the XLSX file.</p>';  
            });  
        </script>  
    </body>  
</html>  
{{< /highlight >}}  

```html  
<!DOCTYPE html>  
<html>  
    <head>  
        <title>Aspose.Cells CSV Load Example</title>  
    </head>  
    <body>  
        <h1>Load CSV with Formulas and Save as XLSX</h1>  
        <input type="file" id="fileInput" accept=".csv" />  
        <button id="runExample">Run Example</button>  
        <a id="downloadLink" style="display: none;">Download Result</a>  
        <div id="result"></div>  
    </body>  

    <script src="aspose.cells.js.min.js"></script>  
    <script type="text/javascript">  
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;  
        
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';  
                return;  
            }  

            const file = fileInput.files[0];  
            const arrayBuffer = await file.arrayBuffer();  
            const bytes = new Uint8Array(arrayBuffer);  

            // TxtLoadOptions configuration  
            const opts = new TxtLoadOptions();  
            opts.separator = ',';  
            opts.hasFormula = true;  

            // Load your CSV file with formulas in a Workbook object  
            const workbook = new Workbook(bytes, opts);  

            // You can also import your CSV file like this  
            // The code below is importing CSV file starting from cell D4 (rowIndex=3, colIndex=3)  
            const worksheet = workbook.worksheets.get(0);  
            worksheet.cells.importCSV(bytes, opts, 3, 3);  

            // Save your workbook in Xlsx format  
            const outputData = workbook.save(SaveFormat.Xlsx);  
            const blob = new Blob([outputData]);  
            const downloadLink = document.getElementById('downloadLink');  
            downloadLink.href = URL.createObjectURL(blob);  
            downloadLink.download = 'output_out.xlsx';  
            downloadLink.style.display = 'block';  
            downloadLink.textContent = 'Download Excel File';  

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';  
        });  
    </script>  
</html>  
```  

The code first loads the CSV file, then imports it again at cell D4. Finally, it saves the workbook object in XLSX format. The [output XLSX file](5115052.xlsx) looks like this. As you can see, cells C3 and F4 contain formulas, and their result is 800.  

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |