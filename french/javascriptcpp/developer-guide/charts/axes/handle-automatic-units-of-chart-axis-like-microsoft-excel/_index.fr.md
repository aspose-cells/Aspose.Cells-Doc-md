---
title: Gérez les unités automatiques de l axe du graphique comme Microsoft Excel avec JavaScript via C++
linktitle: Gérer les Unités Automatiques de l Axe du Graphique comme Microsoft Excel
description: Apprenez comment gérer les unités automatiques sur les axes du graphique dans Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment configurer et personnaliser les unités automatiques sur un axe de graphique, y compris l affichage en notation scientifique et le réglage de l échelle.
keywords: Aspose.Cells for JavaScript via C++, axes du graphique, unités automatiques, Microsoft Excel, configuration, personnalisation, notation scientifique, mise à l échelle.
type: docs
weight: 120
url: /fr/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Scénarios d'utilisation possibles**  
Les premières versions de Aspose.Cells for JavaScript via C++ n'étaient pas capables de gérer correctement les unités automatiques de l'axe du graphique lors de la rendu en image ou PDF. Maintenant, Aspose.Cells for JavaScript via C++ supporte la gestion des unités automatiques de l'axe du graphique. Aucun changement de code nécessaire. Il suffit de convertir votre graphique en image ou PDF, et il affichera l'axe du graphique comme Microsoft Excel le fait.  

## **Gérer les unités automatiques de l'axe du graphique comme dans Microsoft Excel**  
Le code d’exemple suivant charge le [fichier Excel d’exemple](61767755.xlsx) et génère le [graphique PDF de sortie](61767752.pdf). La capture d'écran montre les unités automatiques de l’axe du graphique encadrées en rouge et compare également le graphique du fichier Excel d’origine avec le graphique PDF de sortie. Les deux sont exactement identiques.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Code d'exemple**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
