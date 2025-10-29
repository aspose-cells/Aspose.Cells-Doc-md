---
title: Lire et manipuler les graphiques Excel 2016 avec JavaScript via C++
linktitle: Lire et Manipuler les Graphiques Excel 2016
description: Apprenez comment lire et manipuler les graphiques Excel 2016 en utilisant Aspose.Cells for JavaScript via C++. Ce guide vous montrera comment accéder et modifier diverses propriétés de graphique.
keywords: Aspose.Cells for JavaScript via C++, graphiques Excel 2016, lecture, manipulation, étiquettes de données, couleurs des séries, mise en page, graphique hiérarchique, graphique circulaire.
type: docs
weight: 48
url: /fr/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Scénarios d'utilisation possibles**  
Aspose.Cells prend désormais en charge la lecture et la manipulation des graphiques Microsoft Excel 2016 qui ne sont pas présents dans Microsoft Excel 2013 ou les versions antérieures.  
## **Lire et manipuler les graphiques Excel 2016**  
Le code d'exemple suivant charge le fichier Excel source (22774101.xlsx) contenant des graphiques Excel 2016 dans la première feuille. Il lit tous les graphiques un par un et modifie leur titre en fonction de leur type de graphique. La capture d'écran suivante montre le fichier Excel source avant l'exécution du code. Comme vous pouvez le voir, le titre du graphique est identique pour tous.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

La capture d'écran suivante montre le [fichier Excel de sortie](22774104.xlsx) après l'exécution du code. Comme vous pouvez le voir, le titre du graphique est modifié en fonction de son type de graphique.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Code d'exemple**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Sortie console**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Sujets avancés**  
- [Création de Graphique en Cascade](/cells/fr/javascript-cpp/creating-waterfall-chart/)  
- [Création de Graphique TreeMap](/cells/fr/javascript-cpp/creating-treemap-chart/)  
- [Création de Graphique Sunburst](/cells/fr/javascript-cpp/creating-sunburst-chart/)
