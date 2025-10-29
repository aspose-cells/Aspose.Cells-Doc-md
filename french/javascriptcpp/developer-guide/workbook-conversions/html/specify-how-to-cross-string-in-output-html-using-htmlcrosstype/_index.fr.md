---
title: Spécifier comment croiser une chaîne dans le HTML de sortie en utilisant HtmlCrossType avec JavaScript via C++
linktitle: Définir comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType
type: docs
weight: 140
url: /fr/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Apprenez comment contrôler le débordement de chaîne dans la sortie HTML en spécifiant HtmlCrossType dans Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu’elle dépasse la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez contrôler ce débordement en spécifiant le type de croisement à l’aide de l’énumération [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Elle possède les valeurs suivantes :

- **HtmlCrossType.Default** : Affichage comme MS Excel ; dépend de la prochaine cellule. Si la cellule suivante est nulle, la chaîne passera ou sera tronquée.

- **HtmlCrossType.MSExport** : Affiche la chaîne comme dans MS Excel exportant HTML.

- **HtmlCrossType.Cross**: Afficher la chaîne HTML croisée; la performance pour la création de grands fichiers HTML sera plus de dix fois plus rapide que de définir la valeur sur Default ou FitToCell.

- **HtmlCrossType.FitToCell** : affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType**

 Le code exemple suivant charge le [fichier Excel d'exemple](51740732.xlsx) et le sauvegarde au format HTML en spécifiant différents [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Veuillez télécharger les [HTMLs de sortie](51740734.zip) générés avec ce code. Le fichier Excel exemple contient une image bordée en rouge comme montré dans cette capture d'écran, illustrant l'effet des valeurs [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) sur le HTML de sortie.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
