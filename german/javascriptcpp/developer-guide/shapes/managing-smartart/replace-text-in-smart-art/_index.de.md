---
title: Text in Smart Art mit JavaScript via C++ ersetzen
linktitle: Ersetzen Sie Text in SmartArt
type: docs
weight: 1200
url: /de/javascript-cpp/replace-text-in-smart-art/
description: Lernen Sie, wie Sie Text in Smart Art mit Aspose.Cells for JavaScript via C++ ersetzen.
---

## **Mögliche Verwendungsszenarien**  

Smart Art ist eines der wichtigsten Objekte in einer Arbeitsmappe. Oft besteht Bedarf, den Text in Smart Art zu aktualisieren. Aspose.Cells for JavaScript via C++ bietet diese Funktion, indem es die [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--)-Eigenschaft setzt.  

Die Beispielquelle kann von folgendem Link heruntergeladen werden:  

[SmartArt.xlsx](77496338.xlsx)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells SmartArt Example</title>
    </head>
    <body>
        <h1>SmartArt Replacement Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlSaveOptions } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const worksheets = workbook.worksheets;
            for (let i = 0; i < worksheets.count; i++) {
                const worksheet = worksheets.get(i);
                const shapes = worksheet.shapes;
                for (let j = 0; j < shapes.count; j++) {
                    const shape = shapes.get(j);
                    // Set alternative text using property assignment
                    shape.alternativeText = "ReplacedAlternativeText";
                    if (shape.isSmartArt()) {
                        // Access smart art grouped shapes via properties
                        const smartArtShapes = shape.resultOfSmartArt.groupedShapes;
                        for (let k = 0; k < smartArtShapes.length; k++) {
                            const smartart = smartArtShapes[k];
                            // Set text using property assignment
                            smartart.text = "ReplacedText";
                        }
                    }
                }
            }

            // Configure save options and enable SmartArt update
            const options = new OoxmlSaveOptions();
            options.updateSmartArt = true;

            // Save workbook to XLSX format with options and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSmartArt.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">SmartArt updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
