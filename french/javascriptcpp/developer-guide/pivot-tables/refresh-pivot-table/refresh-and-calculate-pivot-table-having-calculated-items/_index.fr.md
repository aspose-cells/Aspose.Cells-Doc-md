---
title: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 40
url: /fr/javascript-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ supporte désormais le rafraîchissement et le calcul des tableaux croisés dynamiques contenant des éléments calculés. Veuillez utiliser [**PivotTable.refreshData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshdata--) et [**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--) comme d'habitude pour effectuer cette fonction.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

Le code d'exemple suivant charge le [fichier source Excel](5115238.xlsx) contenant un tableau croisé dynamique comprenant trois éléments calculés tels que "add", "div", "div2". Nous modifions d'abord la valeur de la cellule D2 en 20, puis rafraîchissons et calculons le tableau croisé dynamique en utilisant les API Aspose.Cells for JavaScript via C++ et enregistrons le classeur au format PDF. Les résultats dans le [PDF de sortie](5115229.pdf) montrent que Aspose.Cells for JavaScript via C++ a rafraîchi et calculé avec succès le tableau croisé dynamique contenant des éléments calculés. Vous pouvez le vérifier en utilisant Microsoft Excel en mettant manuellement la valeur 20 dans la cellule D2, puis en rafraîchissant le tableau croisé dynamique avec le raccourci Alt+F5 ou en cliquant sur le bouton de rafraîchissement du tableau croisé dynamique.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh and Calculate Pivot Table Items</title>
    </head>
    <body>
        <h1>Refresh and Calculate Pivot Table Items</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Change the value of cell D2
            const cell = sheet.cells.get("D2");
            cell.value = 20;

            // Refresh and calculate all the pivot tables inside this sheet
            sheet.refreshPivotTables();

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshAndCalculateItems_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            result.innerHTML = '<p style="color: green;">Pivot tables refreshed and calculated. Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
