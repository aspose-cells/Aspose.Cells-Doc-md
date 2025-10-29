---
title: Remplacer le texte dans l art intelligent avec JavaScript via C++
linktitle: Remplacer le texte dans l art intelligent
type: docs
weight: 1200
url: /fr/javascript-cpp/replace-text-in-smart-art/
description: Apprenez à remplacer le texte dans l art intelligent en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

L'art intelligent est l'un des principaux objets dans un classeur. Il est souvent nécessaire de mettre à jour le texte dans l'art intelligent. Aspose.Cells for JavaScript via C++ offre cette fonctionnalité en définissant la propriété [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--).  

Le fichier source d'exemple peut être téléchargé à partir du lien suivant :  

[SmartArt.xlsx](77496338.xlsx)  

## **Code d'exemple**  

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
