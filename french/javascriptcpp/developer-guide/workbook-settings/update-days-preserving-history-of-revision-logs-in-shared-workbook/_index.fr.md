---
title: Mettre à jour les jours en préservant l’historique des journaux de révision dans un classeur partagé avec JavaScript via C++
linktitle: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé
type: docs
weight: 80
url: /fr/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Découvrez comment mettre à jour le nombre de jours pour préserver l’historique des journaux de révision dans les classeurs partagés en utilisant le Script Aspose.Cells for Java via C++.
---

## **Scénarios d'utilisation possibles**

Lorsque vous partagez un classeur, vous obtenez une option indiquant ***Conserver l’historique des modifications pendant N jours*** comme montré dans la capture d’écran suivante. Vous pouvez mettre à jour le nombre de jours pour préserver l’historique en utilisant le Script Aspose.Cells for Java via C++ avec la propriété [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--). 

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code d'exemple suivant crée un classeur vide, le partage, puis met à jour les journaux de révision pour conserver l'historique à 7 jours, ce qui est normalement 30 jours. Veuillez consulter le [fichier Excel de sortie](60489773.xlsx) généré par le code à titre de référence.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
