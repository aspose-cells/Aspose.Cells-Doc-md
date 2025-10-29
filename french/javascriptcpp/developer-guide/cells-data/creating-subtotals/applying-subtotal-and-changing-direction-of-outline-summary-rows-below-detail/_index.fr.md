---
title: Appliquer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
type: docs
weight: 100
url: /fr/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Apprenez comment appliquer un sous total et changer la direction des lignes de résumé du contour sous Détail en utilisant le script Aspose.Cells for Java via API C++.
keywords: Appliquer un sous total, ajouter un sous total, changer la direction des lignes de synthèse du contour en dessous du détail, changer la direction des colonnes de synthèse du contour à droite du détail, créer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
---

{{% alert color="primary" %}}

Cet article expliquera comment appliquer un sous-total aux données et changer la direction des lignes de synthèse du contour en dessous du détail.

Vous pouvez appliquer un sous-total aux données en utilisant la méthode [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-). Elle prend les paramètres suivants.

- **CellArea** - la plage sur laquelle appliquer le sous-total
- **GroupBy** - le champ à regrouper, en tant que décalage entier indexé à partir de zéro
- **Function** - la fonction de sous-total
- **TotalList** - un tableau de décalages de champ indexés à partir de zéro, indiquant les champs auxquels les sous-totaux sont ajoutés
- **Replace** - Indique s'il faut remplacer les sous-totaux actuels
- **SautsDePage** - Indique s'il faut ajouter un saut de page entre les groupes
- **RésuméSousDonnées** - Indique s'il faut ajouter un résumé sous les données.

De plus, vous pouvez contrôler la direction des lignes de résumé avec détail **ci-dessous** comme indiqué dans la capture d'écran suivante en utilisant la propriété Worksheet.Outline.SummaryRowBelow. Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant **Données > Plan > Paramètres**

![todo:image_alt_text](1.png)

{{% /alert %}}

## Images des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous, qui contient des données dans les colonnes A et B.

![todo:image_alt_text](2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par le code d'exemple. Comme vous pouvez le constater, un sous-total a été appliqué à la plage A2:B11 et la direction de la synthèse est les lignes de résumé ci-dessous le détail.

![todo:image_alt_text](3.png)

## JavaScript pour appliquer un sous-total et changer la direction des lignes de résumé du contour



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
