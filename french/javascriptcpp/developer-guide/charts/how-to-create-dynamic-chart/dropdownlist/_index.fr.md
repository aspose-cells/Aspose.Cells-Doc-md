---
title: Comment créer un graphique dynamique avec une liste déroulante en utilisant JavaScript via C++
linktitle: Comment créer un graphique dynamique avec liste déroulante
description: Découvrez comment créer un graphique dynamique qui se met à jour en fonction de la sélection dans une liste déroulante en utilisant Aspose.Cells for JavaScript via C++. Notre guide étape par étape vous montrera comment intégrer une liste déroulante dans votre graphique pour une visualisation des données flexible.
keywords: Aspose.Cells for JavaScript via C++, graphique dynamique, liste déroulante, visualisation des données, intégration, visualisation flexible.
type: docs
weight: 76
url: /fr/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique avec liste déroulante dans Excel est un outil puissant qui permet aux utilisateurs de créer des graphiques interactifs qui peuvent se mettre à jour dynamiquement en fonction des données sélectionnées. Cette fonctionnalité est particulièrement utile dans les situations où il est nécessaire d'analyser de multiples ensembles de données ou de comparer divers scénarios.

Une application courante d'un graphique dynamique avec liste déroulante est l'analyse financière. Par exemple, une entreprise peut avoir plusieurs ensembles de données financières pour différentes années ou départements. En utilisant une liste déroulante, les utilisateurs peuvent sélectionner l'ensemble de données spécifique qu'ils souhaitent analyser, et le graphique se mettra automatiquement à jour pour afficher les informations correspondantes. Cela permet de comparer facilement et d'identifier les tendances ou schémas.

Une autre application se trouve dans les ventes et le marketing. Une entreprise peut avoir des données de vente pour différents produits ou régions. Avec un graphique dynamique avec liste déroulante, les utilisateurs peuvent choisir un produit ou une région spécifique dans la liste déroulante, et le graphique se mettra à jour dynamiquement pour afficher les performances de vente pour l'option sélectionnée. Cela aide à identifier les zones ou produits les plus performants et à prendre des décisions basées sur les données.

En résumé, un graphique dynamique avec liste déroulante dans Excel offre un moyen flexible et interactif de visualiser et d'analyser les données. Il est précieux dans les situations où il est nécessaire de comparer plusieurs ensembles de données ou d'explorer différents scénarios, ce qui en fait un outil polyvalent pour l'analyse financière, les ventes et le marketing, et de nombreuses autres applications.

## **Utilisez Aspose Cells pour créer un graphique dynamique avec liste déroulante**
Dans les paragraphes suivants, nous vous expliquerons comment créer un graphique dynamique avec une liste déroulante en utilisant Aspose.Cells for JavaScript via C++. Nous partagerons le code de l’exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Chart with Dropdownlist](DynamicChartWithDropdownlist.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Remarques**
Dans le fichier généré, le graphique comptera dynamiquement les données pour le mois sélectionné. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :
