---
title: Mesurer la largeur et la hauteur de la valeur de la cellule en pixels.
linktitle: Mesurer la taille.
type: docs
weight: 260
url: /fr/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Apprenez à mesurer la largeur et la hauteur de la valeur de la cellule en unité de pixels via Aspose.Cells for JavaScript en C++.
keywords: Mesurer la largeur de la valeur de la cellule en unité de pixels en JavaScript via C++, Mesurer la hauteur de la valeur de la cellule en unité de pixels en JavaScript via C++, Obtenir la largeur de la valeur de la cellule en unité de pixels en JavaScript via C++, Obtenir la hauteur de la valeur de la cellule en unité de pixels en JavaScript via C++
---

{{% alert color="primary" %}}  

Parfois, vous devez calculer la largeur et la hauteur de la valeur de la cellule pour adapter la valeur de la cellule à l'intérieur de la cellule. Aspose.Cells fournit des méthodes [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) et [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) à cet effet. En utilisant ces méthodes, vous pouvez calculer la largeur et la hauteur de la valeur de la cellule, puis définir respectivement la largeur de la colonne et la hauteur de la ligne de cette cellule, ce qui ajustera ou adaptera la valeur de la cellule à l'intérieur de la cellule.  

Alternativement, vous pouvez également [ajuster automatiquement la hauteur des lignes et la largeur des colonnes de votre cellule ou plage de cellules](/cells/fr/javascript-cpp/autofit-rows-and-columns/) en utilisant les API Aspose.Cells.  

{{% /alert %}}  

Le code suivant explique l’utilisation des méthodes [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) et [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Sujets avancés**  
- [Obtenir la largeur de texte de la valeur de la cellule](/cells/fr/javascript-cpp/get-text-width-of-cell-value/)
