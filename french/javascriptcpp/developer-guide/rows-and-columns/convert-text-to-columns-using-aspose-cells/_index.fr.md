---
title: Convertir du texte en colonnes en utilisant Aspose.Cells for JavaScript via C++
linktitle: Convertir le texte en colonnes
type: docs
weight: 30
url: /fr/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: Apprenez comment convertir du texte en colonnes dans Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Vous pouvez convertir votre texte en colonnes en utilisant Microsoft Excel. Cette fonctionnalité est disponible dans *Outils de données* sous l'onglet *Données*. Pour diviser le contenu d'une colonne en plusieurs colonnes, les données doivent contenir un délimiteur spécifique tel qu'une virgule (ou tout autre caractère) sur la base duquel Microsoft Excel divise le contenu d'une cellule en plusieurs cellules. Aspose.Cells for JavaScript via C++ fournit également cette fonctionnalité via [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Convertir du texte en colonnes en utilisant Aspose.Cells for JavaScript via C++**  

Le code d’exemple suivant explique l’utilisation de la méthode [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). Le code commence par ajouter des noms de personnes dans la colonne A de la première feuille de calcul. Le prénom et le nom de famille sont séparés par un espace. Ensuite, il applique la méthode [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) sur la colonne A et l’enregistre en tant que fichier Excel de sortie. Si vous ouvrez le [fichier Excel de sortie](25395213.xlsx), vous verrez que les prénoms sont dans la colonne A tandis que les noms de famille sont dans la colonne B, comme illustré dans cette capture d’écran.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
