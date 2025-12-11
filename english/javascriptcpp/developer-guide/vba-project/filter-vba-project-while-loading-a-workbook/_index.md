---  
title: Filter VBA Project while loading a workbook with JavaScript via C++  
linktitle: Filter VBA Project while loading a workbook  
type: docs  
weight: 140  
url: /javascript-cpp/filter-vba-project-while-loading-a-workbook/  
description: Learn how to filter VBA projects while loading Excel workbooks using Aspose.Cells for JavaScript via C++.  
---  

## **Filter VBA Project while loading an Excel workbook in JavaScript via C++**  

Some .xlsm/.xlsb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells for JavaScript via C++ will unconditionally load this (meta) data when opening such workbooks. You may need to control this though [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) when you really only need to extract sheet names for a large number of workbooks, thus skipping over such unneeded content. This filter is provided by introducing a new option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions).  

## **Sample Code**  

The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:  

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;
        
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```