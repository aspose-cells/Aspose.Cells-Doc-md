---
title: Calcul de la formule matricielle des tables de données avec JavaScript via C++
linktitle: Calcul de la formule de tableau de données
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer des formules matricielles pour une table de données dans Microsoft Excel avec JavaScript via C++. Charger ou créer un fichier Excel, calculer la formule matricielle, et enregistrer le fichier modifié.
keywords: Aspose.Cells, Excel, tables de données, formules matricielles, calculs JavaScript via C++
type: docs
weight: 70
url: /fr/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Vous pouvez créer une table de données dans Microsoft Excel en utilisant Données > Analyse hypothèse > Table de données.... Aspose.Cells vous permet maintenant de calculer la formule matricielle d’une table de données. Veuillez utiliser [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) normalement pour calculer tout type de formules.

{{% /alert %}}

Dans le code d'exemple suivant, nous avons utilisé le [fichier Excel source](5115535.xlsx). Si vous changez la valeur de la cellule B1 à 100, les valeurs du tableau de données qui sont remplies de couleur jaune deviendront 120 comme indiqué dans les images suivantes. Le code d'exemple génère le [PDF de sortie](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
