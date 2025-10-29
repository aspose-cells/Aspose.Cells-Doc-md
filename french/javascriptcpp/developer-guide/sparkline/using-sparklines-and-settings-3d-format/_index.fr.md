---
title: Utiliser les Sparklines et les paramètres de formatage 3D avec JavaScript via C++
linktitle: Utilisation de Sparklines et réglages du format 3D
type: docs
weight: 40
url: /fr/javascript-cpp/using-sparklines-and-settings-3d-format/
description: Apprenez comment utiliser les sparklines et appliquer un formatage 3D dans les fichiers Excel avec Aspose.Cells for JavaScript via C++. 
---

## **Utilisation des sparklines**
Microsoft Excel 2010 peut analyser les informations de plus de façons que jamais. Il permet aux utilisateurs de suivre et de mettre en évidence les tendances importantes des données avec de nouveaux outils d'analyse et de visualisation des données. Les sparklines sont des mini-graphiques que vous pouvez placer à l'intérieur des cellules afin de visualiser les données et le graphique sur la même table. Lorsque les sparklines sont utilisés correctement, l'analyse des données est plus rapide et plus directe. Ils offrent également une vue simple des informations, évitant les feuilles de calcul surchargées avec de nombreux graphiques complexes.

Aspose.Cells for JavaScript via C++ fournit une API pour manipuler les sparklines dans les feuilles de calcul.
### **Sparklines dans Microsoft Excel**
Pour insérer des sparklines dans Microsoft Excel 2010 :

1. Sélectionnez les cellules où vous souhaitez voir apparaître les sparklines. Pour les rendre faciles à visualiser, sélectionnez les cellules à côté des données.
1. Cliquez sur **Insérer** dans le ruban, puis choisissez **colonne** dans le groupe **Sparklines**.
1. Sélectionnez ou saisissez la plage de cellules dans la feuille de calcul contenant les données source. Les graphiques apparaîtront.

Les Sparklines vous aident à visualiser les tendances, par exemple le bilan de victoires ou de défaites pour une ligue de softball. Les Sparklines peuvent même résumer l'ensemble de la saison de chaque équipe dans la ligue.
### **Sparklines utilisant Aspose.Cells for JavaScript via C++**
Les développeurs peuvent créer, supprimer ou lire des sparklines (dans le fichier modèle) en utilisant l'API fournie par Aspose.Cells for JavaScript via C++. Les classes qui gèrent les sparklines sont contenues dans le module [SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/), vous devez donc importer ce module avant d'utiliser ces fonctionnalités.

En ajoutant des graphiques personnalisés pour une plage de données donnée, les développeurs ont la liberté d'ajouter différents types de petits graphiques à des zones de cellules sélectionnées.

L'exemple ci-dessous illustre la fonctionnalité des Sparklines. L'exemple montre comment :

1. Ouvrir un fichier modèle simple.
1. Lire les informations des sparklines pour une feuille de calcul.
1. Ajouter de nouvelles sparklines pour une plage de données donnée à une zone de cellules.
1. Enregistrez le fichier Excel sur le disque.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sparkline Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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

            // Instantiate a Workbook by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Read the Sparklines from the worksheet (if any)
            const sparklinesCount = sheet.sparklineGroups.count;
            let logHtml = '';
            for (let i = 0; i < sparklinesCount; i++) {
                const group = sheet.sparklineGroups.get(i);
                logHtml += `sparkline group: type:${group.type}, sparkline items count:${group.sparklines.count}<br/>`;
                const sparklineCount = group.sparklines.count;
                for (let j = 0; j < sparklineCount; j++) {
                    const sparkline = group.sparklines.get(j);
                    logHtml += `sparkline: row:${sparkline.row}, col:${sparkline.column}, dataRange:${sparkline.dataRange}<br/>`;
                }
            }

            // Add Sparklines
            // Define the CellArea D2:D10 (rows and columns are zero-based: D is column 4 -> index 4)
            const ca = CellArea.createCellArea(1, 4, 7, 4);
            // Add new Sparklines for a data range to a cell area
            const idx = sheet.sparklineGroups.add(SparklineType.Column, "Sheet1!B2:D8", false, ca);
            const newGroup = sheet.sparklineGroups.get(idx);
            // Create CellsColor and set color
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            newGroup.seriesColor = clr;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><div>' + logHtml + '</div>';
        });
    </script>
</html>
```
## **Réglage du format 3D**
Vous pourriez avoir besoin de styles de graphes 3D pour obtenir uniquement les résultats correspondant à votre scénario. Aspose.Cells for JavaScript via C++ fournit l'API pertinente pour appliquer le formatage 3D de Microsoft Excel 2007.

Un exemple complet est donné ci-dessous pour démontrer comment créer un graphique et appliquer le format 3D de Microsoft Excel 2007. Après l'exécution du code d'exemple, un graphique en colonnes (avec effets 3D) sera ajouté à la feuille de calcul.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>3D Chart Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, BevelPresetType, PresetMaterialType, LightRigType } = AsposeCells;

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
            // Creating a new workbook
            const book = new Workbook();

            // Add a Data Worksheet
            const dataSheet = book.worksheets.add("DataSheet");

            // Add Chart Worksheet
            const sheet = book.worksheets.add("MyChart");

            // Put some values into the cells in the data worksheet
            dataSheet.cells.get("B1").value = 1;
            dataSheet.cells.get("B2").value = 2;
            dataSheet.cells.get("B3").value = 3;
            dataSheet.cells.get("A1").value = "A";
            dataSheet.cells.get("A2").value = "B";
            dataSheet.cells.get("A3").value = "C";

            // Define the Chart Collection
            const charts = sheet.charts;
            // Add a Column chart to the Chart Worksheet
            const chartSheetIdx = charts.add(ChartType.Column, 5, 0, 25, 15);

            // Get the newly added Chart
            const chart = book.worksheets.get(2).charts.get(0);

            // Set the background/foreground color for PlotArea/ChartArea
            chart.plotArea.area.backgroundColor = Color.White;
            chart.chartArea.area.backgroundColor = Color.White;
            chart.plotArea.area.foregroundColor = Color.White;
            chart.chartArea.area.foregroundColor = Color.White;

            // Hide the Legend
            chart.showLegend = false;

            // Add Data Series for the Chart
            chart.nSeries.add("DataSheet!B1:B3", true);
            // Specify the Category Data
            chart.nSeries.categoryData = "DataSheet!A1:A3";

            // Get the Data Series
            const ser = chart.nSeries.get(0);

            // Apply the 3-D formatting
            const spPr = ser.shapeProperties;
            const fmt3d = spPr.format3D;

            // Specify Bevel with its height/width
            const bevel = fmt3d.topBevel;
            bevel.type = BevelPresetType.Circle;
            bevel.height = 2;
            bevel.width = 5;

            // Specify Surface material type
            fmt3d.surfaceMaterialType = PresetMaterialType.WarmMatte;

            // Specify surface lighting type
            fmt3d.surfaceLightingType = LightRigType.ThreePoint;

            // Specify lighting angle
            fmt3d.lightingAngle = 20;

            // Specify Series background/foreground and line color
            ser.area.backgroundColor = Color.Maroon;
            ser.area.foregroundColor = Color.Maroon;
            ser.border.color = Color.Maroon;

            // Saving the modified Excel file and providing download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = '3d_format.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
