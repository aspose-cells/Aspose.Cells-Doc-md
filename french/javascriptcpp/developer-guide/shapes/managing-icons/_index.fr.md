---
title: Ajouter des icônes à la feuille de calcul avec JavaScript via C++
linktitle: Gestion des icônes
type: docs
weight: 100
url: /fr/javascript-cpp/insert-svg-to-excel/
---

## Ajouter des icônes à la feuille de calcul dans Aspose.Cells for JavaScript via C++

Si vous avez besoin d'utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour ajouter des 'icônes' dans un fichier Excel, alors ce document peut vous aider. 

L'interface Excel correspondant à l'opération d'insertion d'icône est la suivante : 

![](1.png)

- Sélectionnez la position de l'icône à insérer dans la feuille de calcul
- Cliquez gauche sur *Insérer*->*Icônes*
- Dans la fenêtre qui s'ouvre, sélectionnez l'icône dans le rectangle rouge de la figure ci-dessus
- Clique gauche sur *Insérer*, cela sera inséré dans le fichier Excel.

L'effet est le suivant :

![](2.png)

Ici, nous avons préparé un *exemple de code* pour vous aider à insérer des icônes en utilisant [Aspose.Cells](https://products.aspose.com/cells/). Il y a aussi un [fichier d'exemple](sample.xlsx) nécessaire et un [fichier de ressources d'icônes](icon.zip). Nous avons utilisé l'interface Excel pour insérer une icône avec le même effet d'affichage que le [fichier de ressources](icon.zip) dans le [fichier d'exemple](sample.xlsx).

### JavaScript

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Lorsque vous exécutez le code ci-dessus dans votre projet, vous obtiendrez les résultats suivants :

![](3.png)
