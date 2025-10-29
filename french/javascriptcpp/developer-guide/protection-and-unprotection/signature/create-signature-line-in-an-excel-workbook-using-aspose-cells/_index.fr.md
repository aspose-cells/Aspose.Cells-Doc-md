---
title: Créer une ligne de signature dans un classeur Excel en utilisant Aspose.Cells for JavaScript via C++
linktitle: Créer une ligne de signature dans un classeur Excel en utilisant Aspose.Cells
type: docs
weight: 150
url: /fr/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Cet article décrit comment créer une ligne de signature dans un classeur Excel en utilisant du code JavaScript avec Aspose.Cells for JavaScript via C++.
keywords: Créer une ligne de signature dans un classeur Excel JavaScript via C++, comment créer une ligne de signature dans un classeur Excel, comment ajouter une ligne de signature, comment ajouter une ligne de signature au fichier Excel.
---

## **Introduction**  

Microsoft Excel permet d'ajouter une **ligne de signature** dans les classeurs Excel. Vous pouvez ajouter une ligne de signature en cliquant sur l'onglet **Insertion** puis en sélectionnant **Ligne de signature** dans le groupe **Texte**.  

## **Comment créer une ligne de signature pour Excel**  

Aspose.Cells for JavaScript via C++ offre également cette fonctionnalité et a exposé la propriété [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) à cette fin. Cet article expliquera comment utiliser cette propriété pour ajouter une ligne de signature en utilisant Aspose.Cells.  

Le code d'exemple suivant ajoute une ligne de signature en utilisant la propriété [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) et enregistre le classeur.  

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
