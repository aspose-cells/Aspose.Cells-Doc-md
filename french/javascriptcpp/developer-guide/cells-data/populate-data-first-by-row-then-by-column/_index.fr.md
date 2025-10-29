---
title: Remplir d abord les données par ligne puis par colonne
type: docs
weight: 1000
url: /fr/javascript-cpp/populate-data-first-by-row-then-by-column/
description: Apprenez comment remplir d abord les données par ligne puis par colonne via l API Aspose.Cells for JavaScript via C++.
keywords: Remplir d abord les données par ligne puis par colonne JavaScript via C++, insérer des données par ligne puis par colonne JavaScript via C++, ajouter des données par ligne puis par colonne JavaScript via C++, insertion de données haute performance JavaScript via C++, ajout de données haute performance JavaScript via C++
---

{{% alert color="primary" %}}  

Remplir une feuille de calcul avec des données d'abord par ligne puis par colonne améliore les performances globales.  

{{% /alert %}}  

Placer les données dans la séquence A1, B1, A2, B2 est plus rapide que A1, A2, B1, B2. S'il y a de nombreuses cellules dans une feuille de calcul et que vous suivez la deuxième séquence, c'est-à-dire que vous remplissez les données ligne par ligne, ce conseil peut rendre le programme beaucoup plus rapide.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
