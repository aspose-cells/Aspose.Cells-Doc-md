---
title: Create Signature Line in an Excel Workbook using Aspose.Cells for JavaScript via C++
linktitle: Create Signature Line in an Excel Workbook using Aspose.Cells
type: docs
weight: 150
url: /javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: This article describes how to create a Signature Line in an Excel Workbook using JavaScript code with Aspose.Cells for JavaScript via C++.
keywords: Create Signature Line in an Excel Workbook JavaScript via C++, How to Create Signature Line in an Excel Workbook, How to Add Signature Line, How to Add Signature Line to Excel file.
---

## **Introduction**  

Microsoft Excel provides a feature to add a **Signature Line** in Excel workbooks. You can add a Signature Line by clicking the **Insert** tab and then selecting **Signature Line** from the **Text** group.  

## **How to Create Signature Line for Excel**  

Aspose.Cells for JavaScript via C++ also provides this feature and exposes the [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) property for this purpose. This article will explain how to use this property to add a Signature Line using Aspose.Cells.  

The following sample code adds a Signature Line using the [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) property and saves the workbook.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;
        
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```