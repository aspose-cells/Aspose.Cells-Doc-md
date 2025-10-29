---
title: Définir le code de format des valeurs de la série de graphique avec JavaScript via C++
description: Apprenez comment définir le code de format des valeurs de la série de graphique dans Aspose.Cells for JavaScript via C++. Ce guide vous aidera à comprendre comment formater vos données de série de graphique en utilisant le code de format approprié, vous permettant de présenter vos données avec précision et professionnalisme.
keywords: Aspose.Cells for JavaScript via C++, série de graphiques, code de format des valeurs, mise en forme, présentation des données, précision, professionnalisme.
linktitle: Format numérique
type: docs
weight: 100
url: /fr/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs de la série de graphique en utilisant la propriété [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--). Cette propriété est utile non seulement pour la série basée sur la plage à l’intérieur de la feuille de calcul, mais fonctionne également bien pour la série créée avec un tableau de valeurs.

## **Définir le code de format des valeurs de la série du graphique**
Le code d’exemple suivant ajoute une série dans un graphique vide qui n'avait pas de série auparavant. Il ajoute la série en utilisant un tableau de valeurs. Une fois la série ajoutée, il la formate avec le code $#,##0 en utilisant la propriété [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--), et le nombre 10000 devient $10 000. La capture d'écran montre l'effet du code sur le [fichier Excel d'exemple](51740712.xlsx) et le [fichier Excel de sortie](51740713.xlsx) après exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Code d'exemple**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
