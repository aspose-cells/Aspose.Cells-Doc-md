---
title: En utilisant la fonction FormulaText dans Aspose.Cells for JavaScript via C++
linktitle: Utilisation de la fonction FormulaText dans Aspose.Cells
description: Cet article présente comment utiliser la fonction FormulaText dans la bibliothèque Aspose.Cells pour traiter les formules dans Microsoft Excel. Apprenez à obtenir et définir le texte de la formule des cellules et à enregistrer les fichiers Excel modifiés en utilisant JavaScript via C++.
keywords: Aspose.Cells, Excel, fonctions FormulaText JavaScript via C++
type: docs
weight: 60
url: /fr/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText est une fonction d'Excel 2013 et versions ultérieures. Elle n'est pas supportée par les versions antérieures telles qu'Excel 2010 ou 2007, etc. Comme son nom l'indique, elle affiche le texte de la formule présente dans une cellule donnée. Cet article vous montrera comment utiliser cette fonction en utilisant Aspose.Cells for JavaScript via C++.

{{% /alert %}} 

Le code d'exemple suivant illustre l'utilisation de FormulaText avec Aspose.Cells for JavaScript via C++. Le code écrit d'abord une formule dans la cellule A1 puis affiche le texte de la formule en utilisant FormulaText dans la cellule A2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **Sortie console**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
