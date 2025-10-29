---
title: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 90
url: /fr/javascript-cpp/disable-pivot-table-ribbons/
description: Comment désactiver les rubans du tableau croisé dynamique avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, JavaScript Excel via bibliothèque C++, Désactiver les rubans du tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++ Bibliothèque Excel.
---

{{% alert color="primary" %}}

Les rapports basés sur des tableaux croisés dynamiques sont utiles mais sujets à erreur si les utilisateurs cibles ne disposent pas de connaissances approfondies sur Excel pour configurer ces rapports. Dans ces circonstances, les organisations voudront limiter la capacité des utilisateurs à modifier un rapport basé sur un tableau croisé dynamique. Des fonctionnalités courantes du tableau croisé dynamique comme ajouter des filtres supplémentaires, des trancheuses, des champs, ou changer l’ordre de certains éléments dans le rapport ne sont généralement pas recommandées pour tous les utilisateurs. D’un autre côté, ces utilisateurs doivent aussi pouvoir actualiser le rapport et utiliser les filtres ou trancheuses existants. Aspose.Cells for JavaScript via C++ fournit cette capacité aux développeurs pour restreindre la modification de ces rapports lors de leur création. À cet effet, Excel offre une fonctionnalité pour désactiver le ruban du tableau croisé dynamique, ce que propose également Aspose.Cells for JavaScript via C++, permettant au développeur de désactiver le ruban contenant les contrôles pour modifier ces rapports.

{{% /alert %}}

## **Comment désactiver le ruban du tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++**

Le code suivant démontre cette fonctionnalité en accédant à un tableau croisé dynamique à partir d'une feuille, puis en définissant [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) sur **false**. Le fichier de tableau croisé dynamique d'exemple peut être téléchargé à partir de ce [lien](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
