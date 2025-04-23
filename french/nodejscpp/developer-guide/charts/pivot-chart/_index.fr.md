---
title: Comment ajouter un PivotChart en utilisant Aspose.Cells for Node.js via C++
linktitle: Tableau croisé dynamique
type: docs
weight: 100
url: /fr/nodejs-cpp/how-to-add-pivot-chart/
description: Comment ajouter un PivotChart en utilisant Aspose.Cells for Node.js via C++.
keywords: PivotChart Node.js via C++
---
## Qu'est-ce qu'un tableau croisé dynamique

Un graphique croisé dynamique est une représentation visuelle des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques offrent un moyen de résumer, analyser, explorer et présenter des données résumées. Voici quelques caractéristiques clés des graphiques croisés dynamiques :

1. Représentation dynamique des données : Les graphiques croisés dynamiques se mettent à jour automatiquement pour refléter les changements dans le tableau croisé dynamique. Si vous ajoutez ou supprimez des champs dans le tableau, le graphique croisé dynamique se met à jour en conséquence.

1. Interactif : Les graphiques croisés dynamiques sont interactifs, permettant aux utilisateurs de filtrer, trier et approfondir les données. Cela facilite l'exploration de différents aspects de l'ensemble de données.

1. Mise en page flexible : Les utilisateurs peuvent modifier la mise en page du graphique croisé dynamique en déplaçant et en déposant des champs, ce qui offre une flexibilité dans la façon dont les données sont visualisées.

1. Divers types de graphiques : Les graphiques croisés dynamiques peuvent être créés à l’aide de divers types de graphiques tels que diagrammes à barres, graphiques linéaires, graphiques en secteurs, et plus encore, selon la nature des données et les insights que vous souhaitez obtenir.

1. Résumé : Les graphiques croisés dynamiques résument de grandes quantités de données et peuvent afficher des totaux, des moyennes, des comptes ou d’autres statistiques résumées.

1. Filtrage : Ils offrent des capacités de filtrage, permettant d’afficher uniquement les données qui répondent à certains critères.

<br>
Les graphiques croisés dynamiques sont couramment utilisés dans l’intelligence d’affaires et l’analyse de données pour fournir un résumé visuel clair et concis de jeux de données complexes. Ils sont un outil puissant pour prendre des décisions basées sur les données.

## Comment ajouter un PivotChart en utilisant Aspose.Cells for Node.js via C++

### **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique avec Aspose.Cells for Node.js via C++ :

1. Ajoutez des données à une feuille de calcul en utilisant la méthode `putValue` d’un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli avec des données. Les données seront utilisées comme source pour le tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille en appelant la méthode `add` de la collection `PivotTables`.
1. Accédez au nouvel objet PivotTable depuis la collection `PivotTables` en passant son index. Utilisez n’importe lequel des objets de tableau croisé dynamique encapsulés dans l’objet PivotTable pour gérer le tableau.

Des exemples de code sont donnés ci-dessous.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Ajout d'un graphique croisé dynamique**

Pour créer un PivotChart avec Aspose.Cells for Node.js via C++ :

1. Ajoutez un graphique.
1. Définissez le `PivotSource` du graphique pour référencer un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

