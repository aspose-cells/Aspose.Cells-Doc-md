---
title: Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties with JavaScript via C++
linktitle: Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties
type: docs
weight: 320
url: /javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Learn how to set ScaleCrop and LinksUpToDate properties of built-in document properties using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) and [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) are two extended built-in document properties defined inside the OpenXml format. The purpose of these properties is as follows.

## **1) ScaleCrop**
This element indicates the display mode of the document thumbnail. Set this element to **TRUE** to enable scaling of the document thumbnail to the display. Set this element to **FALSE** to enable cropping of the document thumbnail to show only sections that fit the display.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **2) LinksUpToDate**
This element indicates whether hyperlinks in a document are up‑to‑date. Set this element to **TRUE** to indicate that hyperlinks are updated. Set this element to **FALSE** to indicate that hyperlinks are outdated.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **Screenshot showing these properties inside the app.xml file**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties**
The following sample code sets the [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) and [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) extended built-in document properties of the workbook. Please check the [output excel file](5115500.xlsx) generated with this code, change its extension to .zip, extract its contents, and view the app.xml as shown in the screenshot above.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
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

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```