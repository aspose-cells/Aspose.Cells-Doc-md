---
title: Get Range with External Links using JavaScript via C++
linktitle: Get Range with External Links
type: docs
weight: 120
url: /javascript-cpp/get-range-with-external-links/
description: Learn how to get ranges with external links using Aspose.Cells for JavaScript via C++. Retrieve data from different Excel files efficiently.
---

## **Get Range with External Links**

A lot of times Excel files access data from other Excel files using external links. Aspose.Cells for JavaScript via C++ provides the option to retrieve these external links by using the [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) method. The [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) method returns an array of type [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea). The [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) class provides an [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--) property which returns the name of the external file. The [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) class exposes the following members.

- [**ReferredArea.endColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endColumn--): The end column of the area
- [**ReferredArea.endRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endRow--): The end row of the area
- [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--): Get the external file name if this is an external reference
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isArea--): Indicates whether this is an area
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isExternalLink--): Indicates whether this is an external link
- [**ReferredArea.sheetName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#sheetName--): Indicates which sheet this reference is in
- [**ReferredArea.startColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startColumn--): The start column of the area
- [**ReferredArea.startRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startRow--): The start row of the area

The sample code given below demonstrates the use of the [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) method to get ranges with external links.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External References</title>
    </head>
    <body>
        <h1>Sample External References</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SampleExternalReferences.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing named ranges via worksheets.names
            const names = workbook.worksheets.names;
            const namesCount = names.count;
            const outputLines = [];
            outputLines.push(`<p>Processing file: ${file.name}</p>`);
            outputLines.push(`<p>Named Ranges Count: ${namesCount}</p>`);

            for (let i = 0; i < namesCount; i++) {
                const namedRange = names.get(i);
                outputLines.push(`<h3>Named Range ${i}: ${namedRange.name || ('Index ' + i)}</h3>`);

                // Get referred areas (including external references)
                const referredAreas = namedRange.referredAreas(true);
                if (referredAreas) {
                    referredAreas.forEach((referredArea, idx) => {
                        outputLines.push(`<h4>Referred Area ${idx}</h4>`);
                        outputLines.push(`<ul>`);
                        outputLines.push(`<li>IsExternalLink: ${referredArea.isExternalLink}</li>`);
                        outputLines.push(`<li>IsArea: ${referredArea.isArea}</li>`);
                        outputLines.push(`<li>SheetName: ${referredArea.sheetName}</li>`);
                        outputLines.push(`<li>ExternalFileName: ${referredArea.externalFileName}</li>`);
                        outputLines.push(`<li>StartColumn: ${referredArea.startColumn}</li>`);
                        outputLines.push(`<li>StartRow: ${referredArea.startRow}</li>`);
                        outputLines.push(`<li>EndColumn: ${referredArea.endColumn}</li>`);
                        outputLines.push(`<li>EndRow: ${referredArea.endRow}</li>`);
                        outputLines.push(`</ul>`);
                    });
                } else {
                    outputLines.push(`<p>No referred areas for this named range.</p>`);
                }
            }

            resultDiv.innerHTML = outputLines.join('');
        });
    </script>
</html>
```