---
title: Lire le sous titre du graphique à partir d un fichier ODS en JavaScript via C++
linktitle: Lire le sous titre du graphique à partir du fichier ODS
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour lire le sous titre du graphique à partir d un fichier OpenDocument Spreadsheet (ODS). Notre guide montrera comment extraire et accéder au sous titre d un graphique pour une analyse ou une affichage ultérieur.
keywords: Aspose.Cells for JavaScript via C++, Lecture du sous titre du graphique, Fichier OpenDocument Spreadsheet, Fichier ODS, Extraction de graphique, Analyse des données.
type: docs
weight: 160
url: /fr/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **Lire le sous-titre du graphique à partir du fichier ODS**

Aspose.Cells vous permet de lire les sous-titres des graphiques dans les fichiers ODS en utilisant la propriété [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--). Le code d'exemple suivant charge le [fichier ODS d'exemple](89620481.ods) et lit le sous-titre du graphique en utilisant la propriété [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) et l'affiche dans la fenêtre Console. Veuillez consulter la sortie de la console du code ci-dessous comme référence.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **Sortie console**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
