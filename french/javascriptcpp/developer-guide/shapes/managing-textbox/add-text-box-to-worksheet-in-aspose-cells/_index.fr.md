---
title: Comment ajouter/inserer une zone de texte dans la feuille de calcul avec JavaScript via C++
linktitle: Ajouter une zone de texte à une feuille de calcul
type: docs
weight: 10
url: /fr/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Comment ajouter/inserer une zone de texte dans la feuille de calcul en Aspose.Cells for JavaScript via C++.
keywords: ajouter/inserer du texte dans une zone de texte, zone de texte, feuille de calcul Excel Aspose JavaScript via C++
---

## Ajouter une zone de texte à une feuille de calcul dans Excel

Dans le programme Excel (version 07 et supérieure), il y a deux endroits où vous pouvez insérer des zones de texte. L'un dans "insert-shapes", l'autre en haut à droite du menu "Insert".

### méthode un :

![1](1.png)

### méthode deux :

![2](2.png)

## Comment créer

Vous pouvez créer des zones de texte à texte horizontal ou vertical.

- Sélectionner l'option correspondant (horizontal ou vertical)
- Cliquez sur la page avec le bouton gauche de la souris
- Maintenez le bouton gauche enfoncé et faites glisser une distance sur la page
- Relâchez le bouton gauche

Maintenant, vous avez une zone de texte.

## Ajouter une zone de texte à la feuille de calcul en Aspose.Cells for JavaScript via C++

Lorsque vous devez insérer en masse des zones de texte dans la feuille de calcul, la méthode d'insertion manuelle est évidemment une catastrophe. Si cela vous dérange, je pense que ce document vous aidera. [Aspose.Cells](https://products.aspose.com/cells/) fournit une API pour effectuer facilement des insertions en masse dans votre code.

Le code d'exemple suivant crée une zone de texte.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Vous obtiendrez un fichier similaire à [fichier résultat](result.xlsx). Dans ce fichier, vous verrez ce qui suit :

![](52449.png)
