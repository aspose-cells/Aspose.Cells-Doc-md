---
title: Supprimer la connexion de pivot avec JavaScript via C++
linktitle: Supprimer la connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/javascript-cpp/remove-pivot-connection/
description: Apprenez comment supprimer la connexion de pivot en utilisant Aspose.Cells for JavaScript via C++.
keywords: Supprimer la connexion de pivot sans Office 2013, Office 2016, Office 2019 et Office 365 JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez dissocier un segment et un tableau croisé dynamique dans Excel, faites un clic droit sur le segment et sélectionnez "Connexions de rapport...". Dans la liste d'options, vous pouvez cocher ou décocher la case. De même, si vous souhaitez dissocier un segment et un tableau croisé dynamique en utilisant le programme API Aspose.Cells for JavaScript via C++ de manière programmatique, utilisez la méthode [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-). Cela dissociera le segment et le tableau croisé dynamique.

## **Dissocier le filtre et le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](remove-pivot-connection.xlsx) contenant un segment existant. Il accède aux segments, puis dissocie le segment du tableau croisé dynamique. Enfin, il enregistre le classeur en tant que [fichier Excel de sortie](remove-pivot-connection-out.xlsx).

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
