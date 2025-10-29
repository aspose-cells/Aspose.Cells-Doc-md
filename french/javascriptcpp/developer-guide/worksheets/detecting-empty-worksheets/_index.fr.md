---
title: Détection de feuilles de calcul vides avec JavaScript via C++
linktitle: Détection de feuilles de calcul vides
type: docs
weight: 410
url: /fr/javascript-cpp/detecting-empty-worksheets/
description: Cet article vous montre un code expliquant comment détecter les feuilles de calcul vides dans les classeurs Excel de manière programmatique en utilisant l API JavaScript avec la bibliothèque C++.
keywords: détecter feuille de calcul vide JavaScript via C++, trouver feuille Excel vide JavaScript via C++
---

## **Vérifier les cellules peuplées**

Les feuilles de calcul peuvent comporter une ou plusieurs cellules remplies de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans un tel cas, il est facile de détecter si une feuille donnée est vide ou non. Tout ce que nous devons vérifier, ce sont les propriétés [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) ou [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--). Si ces propriétés retournent zéro ou des valeurs positives, cela signifie qu'une ou plusieurs cellules ont été remplies; cependant, si l'une de ces propriétés retourne -1, cela indique qu'aucune cellule n'a été remplie dans la feuille donnée.

{{% alert color="primary" %}}

Les collections de lignes et de colonnes ont des indices basés sur zéro; donc, une cellule à la ligne 0 et la colonne 0 correspond à la première cellule de la feuille, qui est A1.

{{% /alert %}}

## **Vérifier les cellules initialisées vides**

Toutes les cellules ayant des valeurs sont automatiquement initialisées; cependant, il est possible qu'une feuille de calcul ait des cellules uniquement avec une mise en forme appliquée. Dans ce cas, les propriétés [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) ou [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) retourneront -1 pour indiquer l'absence de valeurs remplies, mais les cellules initialisées en raison de la mise en forme ne peuvent pas être détectées avec cette approche. Pour vérifier si une feuille de calcul possède des cellules initialisées vides, il est conseillé d'utiliser la méthode `Enumerator.MoveNext` sur l'énumérateur obtenu à partir de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Si la méthode `Enumerator.MoveNext` retourne **true**, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille donnée.

## **Vérifier les formes**

Il est possible qu'une feuille donnée n'ait aucune cellule remplie; cependant, elle peut contenir des formes et objets tels que des contrôles, graphiques, images, etc. Si nous devons vérifier si une feuille contient une forme, nous pouvons le faire en inspectant la propriété [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--). Une valeur positive indique la présence de(s) forme(s) dans la feuille.

## **Exemple de programmation**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
