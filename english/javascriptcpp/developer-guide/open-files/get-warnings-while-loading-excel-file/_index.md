---
title: Get Warnings while Loading Excel File with JavaScript via C++
linktitle: Get Warnings while Loading Excel File
type: docs
weight: 110
url: /javascript-cpp/get-warnings-while-loading-excel-file/
description: Learn how to capture warnings while loading an Excel file using Aspose.Cells for JavaScript via C++. Handle corrupt but loadable workbooks effectively.
---

## **Possible Usage Scenarios**

Sometimes the user tries to load a workbook which is somewhat corrupt but loadable. In such cases, Aspose.Cells throws warnings while loading the workbook. You can catch these warnings by implementing the [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) interface and setting the [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--) property.

## **Get Warnings while Loading Excel File**

The following sample code explains how to get warnings while loading an Excel file. The code loads the [sample Excel file](sampleDuplicateDefinedName.xlsx) which throws a [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) warning on loading. This warning is then caught by the [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) method that prints the warning messages on the console. The code then saves the workbook as the [output Excel file](outputDuplicateDefinedName.xlsx). If you open the sample Excel file in Microsoft Excel, it will also display this warning, as shown in the screenshot. Please also check the console output of the code shown below for better understanding.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;
        
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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **Console Output**

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}