---
title: Ajouter une connexion de tableau croisé dynamique avec JavaScript via C++
linktitle: Ajouter une connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/javascript-cpp/add-pivot-connection/
description: Apprenez comment ajouter une connexion de tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++.
keywords: Ajouter une connexion de tableau croisé dynamique sans Office 2013, Office 2016, Office 2019 et Office 365 JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez associer un segment et un tableau croisé dynamique dans Excel, vous devez faire un clic droit sur le segment et sélectionner l'option "Connexions de rapport...". Dans la liste d'options, vous pouvez agir sur la case à cocher. De même, si vous voulez associer un segment et un tableau croisé dynamique en utilisant l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-). Cela associera le segment et le tableau croisé dynamique.

## **Associer une trancheuse et un tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](add-pivot-connection.xlsx) contenant un segment existant. Il accède au segment, puis l'associe au tableau croisé dynamique. Enfin, il enregistre le classeur en tant que [fichier Excel de sortie](add-pivot-connection-out.xlsx).

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
