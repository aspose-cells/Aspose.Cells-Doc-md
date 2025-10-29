---
title: Définir une formule partagée avec JavaScript via C++
linktitle: Paramétrage de formule partagée
type: docs
weight: 10
url: /fr/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Si vous souhaitez ajouter une fonction dans une feuille de calcul qui effectuera certains calculs, cet article explique comment réaliser cette tâche en utilisant Aspose.Cells for JavaScript via C++.

{{% /alert %}}

## Définir une formule partagée en utilisant Aspose.Cells for JavaScript via C++

Supposons que vous ayez une feuille de calcul remplie de données dans le format qui ressemble à la feuille de calcul d'exemple suivante.

|**Fichier d'entrée avec une colonne de données**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Vous souhaitez ajouter une fonction en B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est: **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells.

Aspose.Cells vous permet de spécifier une formule en utilisant la propriété [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--). Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Faites soit ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0,09, A4*0,09, A5*0,09, etc.). Cela nécessite la mise à jour des références de cellule pour chaque ligne. Cela nécessite aussi que Aspose.Cells analyse chaque formule individuellement, ce qui peut prendre du temps pour de grands tableaux et des formules complexes. Cela ajoute également des lignes de code supplémentaires, bien que des boucles puissent les réduire quelque peu.

Une autre approche est d'utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne afin que la taxe soit calculée correctement. La méthode [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
