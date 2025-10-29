---
title: Accéder à une Table depuis une cellule et ajouter des valeurs à l intérieur en utilisant des décalages de ligne et de colonne avec JavaScript via C++
linktitle: Accéder à un tableau depuis une cellule et ajouter des valeurs à l intérieur en utilisant des décalages de ligne et de colonne
type: docs
weight: 230
url: /fr/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

Normalement, vous ajoutez des valeurs à l'intérieur de l'objet Table ou Liste en utilisant la méthode [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-). Mais parfois, vous pourriez avoir besoin d'ajouter des valeurs à l'intérieur de l'objet Table ou Liste en utilisant les décalages de ligne et de colonne.  

Pour accéder à une Table ou un Object de liste à partir d'une cellule, utilisez la propriété [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--). Pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne, utilisez la méthode [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

La capture d'écran suivante montre le fichier Excel source utilisé dans le code. Il contient le tableau vide et met en évidence la cellule D5 qui se trouve à l'intérieur du tableau. Nous accéderons à ce tableau depuis la cellule D5 en utilisant la propriété [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) puis ajouterons les valeurs à l'intérieur en utilisant à la fois [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) et [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) méthodes.  

## Exemple  

### Captures d'écran comparant les fichiers source et de sortie  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

La capture d'écran suivante montre le fichier Excel de sortie généré par le code. Comme vous pouvez le voir, la cellule D5 a une valeur et la cellule F6, qui est située à l'emplacement 2,2 du tableau, a une valeur.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Code JavaScript pour accéder au tableau depuis la cellule et ajouter des valeurs à l'intérieur en utilisant des décalages de rangée et de colonne  

Le code d'exemple suivant charge le fichier Excel source tel que montré dans la capture d'écran ci-dessus et ajoute des valeurs à l'intérieur du tableau, puis génère le fichier Excel de sortie tel qu'indiqué ci-dessus.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
