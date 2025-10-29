---
title: Gestion des TextBox avec JavaScript via C++
linktitle: Gestion des zones de texte
type: docs
weight: 50
url: /fr/javascript-cpp/managing-textbox-of-excel/
description: Apprenez à gérer les TextBox dans Excel en utilisant Aspose.Cells for JavaScript via C++. 
keywords: Gérer les TextBox dans Excel JavaScript via C++
---

## **Scénarios d'utilisation possibles**
Il peut y avoir des scénarios où vous devrez ajouter, mettre à jour ou manipuler des objets TextBox dans une feuille Excel. Cela peut être utile pour ajouter des annotations, des textes d'accompagnement ou toute information complémentaire facilitant la présentation des données. Aspose.Cells for JavaScript via C++ offre une fonctionnalité robuste pour gérer les TextBox dans les documents Excel. 

## **Gestion des TextBox avec Aspose.Cells for JavaScript via C++**
Cet exemple montre comment :

1. Créez un nouveau classeur.
2. Ajouter une forme TextBox.
3. Modifier les propriétés du TextBox selon les besoins.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Ce code montre comment créer et configurer un TextBox dans une feuille Excel, en ajustant sa taille, sa position et en le formatant selon vos exigences.

 Gardez à l'esprit que les interactions avec les zones de texte peuvent varier en fonction des cas d'utilisation spécifiques, donc consultez la documentation de Aspose.Cells for JavaScript via C++ pour d'autres méthodes et propriétés.
