---
title: Comment vérifier l état figé sans Excel en utilisant JavaScript via C++
linktitle: État figé
type: docs
weight: 190
url: /fr/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: Dans cet article, vous apprendrez comment vérifier l état figé d une feuille Excel de manière programmatique en utilisant la bibliothèque JavaScript avec C++.
---

## **Introduction**

Dans cet article, nous apprendrons comment vérifier l'état figé d'une feuille Excel de manière programmatique. Nous pouvons simplement déterminer si la feuille est figée ou divisée dans MS Excel. Mais existe-t-il une méthode pour savoir si elle est figée ou divisée avec JavaScript ? Nous pouvons le faire simplement avec Aspose.Cells for JavaScript via C++.

## **Les volets de fenêtre sont-ils gelés**
Avec Aspose.Cells for JavaScript via C++, nous pouvons vérifier si la fenêtre est figée et combien de lignes et colonnes sont verrouillées.

Veuillez utiliser la propriété [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) pour vérifier l'état des volets de la fenêtre et obtenir les lignes et colonnes verrouillées avec la propriété [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. Construisez un classeur pour ouvrir le fichier.
2. Vérifiez si la feuille de calcul est gelée.
3. Obtenez les lignes et colonnes verrouillées.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
