---
title: Obtenez la largeur du texte de la valeur de la cellule
type: docs
weight: 50
url: /fr/javascript-cpp/get-text-width-of-cell-value/
description: Apprenez comment obtenir la largeur du texte de la valeur d une cellule via Aspose.Cells for JavaScript en utilisant l API C++.
keywords: Obtenez la largeur du texte de la valeur d une cellule en JavaScript via C++, obtenez la largeur du texte de la valeur d une cellule en JavaScript via C++
---

## **Obtenir la largeur de texte de la valeur de la cellule**

Parfois, les développeurs peuvent avoir besoin de calculer la largeur de la valeur d'une cellule pour organiser les données dans une mise en page. Aspose.Cells for JavaScript via C++ fournit la méthode [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-), qui permet aux développeurs d'obtenir la largeur du texte de la valeur de la cellule. Le code d'exemple suivant illustre comment utiliser [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-) pour accéder à la largeur du texte de la valeur de la cellule.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier Source](96928090.xlsx)

## Code d'exemple

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Text Width Example</title>
    </head>
    <body>
        <h1>Get Text Width Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and A1 cell
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Accessing default font style
            const font = workbook.defaultStyle.font;

            // Calculating text width using CellsHelper (converted getter name to property)
            const textWidth = AsposeCells.CellsHelper.textWidth(cell.stringValue, font, 1);

            resultDiv.innerHTML = `<p style="color: green;">Text width: ${textWidth}</p>`;
        });
    </script>
</html>
```
