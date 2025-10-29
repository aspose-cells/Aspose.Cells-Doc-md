---
title: Obtenir l adresse, le nombre de cellules, le décalage de l ensemble de la colonne et de la ligne entière de la plage avec JavaScript via C++
linktitle: Obtenir le décalage du nombre de cellules d adresse de la colonne entière et de la ligne entière de la plage
type: docs
weight: 330
url: /fr/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for JavaScript via C++ fournit l'objet Range qui dispose de diverses méthodes utilitaires permettant à l'utilisateur de travailler facilement avec les plages Excel. Cet article illustre l'utilisation des méthodes ou propriétés suivantes de l'objet Range.

- **Adresse**

Obtient l'adresse de la plage.

- **Nombre de cellules**

Obtient le nombre de cellules dans la plage.

- **Décalage**

Obtient la plage par décalage.

- **Colonne entière**

Obtient un objet Range qui représente la colonne entière (ou les colonnes) contenant la plage spécifiée.

- **Ligne entière**

Obtient un objet Range qui représente la ligne entière (ou les lignes) contenant la plage spécifiée.

## **Obtenez l'adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière de la plage.**
Le code d'exemple suivant explique l'utilisation des méthodes et propriétés comme discuté ci-dessus. Veuillez consulter la sortie de la console du code ci-dessous pour référence.

## **Code d'exemple**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **Sortie console**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
