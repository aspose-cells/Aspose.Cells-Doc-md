---
title: Libérer le gel des lignes ou colonnes avec JavaScript via C++
linktitle: Décongeler les volets
type: docs
weight: 190
url: /fr/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez à débloquer (désépingler) les lignes, colonnes ou volets des feuilles de calcul Excel de manière programmatique en utilisant l API JavaScript avec C++.
keywords: Débloquer les volets, lignes, colonnes, débloquer la fenêtre JavaScript via C++.
---

## **Introduction**

Dans cet article, nous apprendrons comment délier les lignes, les colonnes et les volets. Si les feuilles de calcul dans les fichiers Excel sont gelées, il arrive que nous souhaitions déverrouiller la feuille ou ajuster les lignes, colonnes ou volets gelés.


## **Dans Excel**

1. Cliquez sur l'onglet Affichage > Immobiliser les volets > Débloquer les volets.

**![débloquer les volets dans Excel](Unfreeze-Panes.png)**




## **Débloquer les lignes, colonnes ou volets avec Aspose.Cells for JavaScript via C++**
Il est simple de débloquer les volets avec Aspose.Cells for JavaScript via C++. Veuillez utiliser la méthode [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) pour débloquer les volets.

1. Construisez le classeur pour ouvrir le fichier gelé.
2. Débloquer les volets avec la méthode Worksheet.unFreezePanes().
3. Enregistrez le fichier.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Fichier Excel source joint (Frozen.xlsx).
