---  
title: Créer des graphiques dynamiques avec Node.js via C++  
linktitle: Créer des graphiques dynamiques  
description: Apprenez comment créer des graphiques dynamiques dans Aspose.Cells for Node.js via C++. Ce guide vous montrera comment mettre à jour dynamiquement les données, séries et formats de vos graphiques en fonction de vos besoins, pour présenter visuellement des données changeantes dans vos feuilles de calcul.  
keywords: Aspose.Cells pour Node.js, création de graphiques, graphiques dynamiques, données, séries, mise en forme, feuilles de calcul, mise à jour.  
type: docs  
weight: 240  
url: /fr/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
Les graphiques dynamiques (ou interactifs) ont la capacité de changer lorsque vous modifiez la portée des données. En d'autres termes, les graphiques dynamiques peuvent refléter automatiquement les modifications lorsque la source de données est modifiée. Pour déclencher le changement de la source de données, on peut utiliser l'option de filtrage des tables Excel ou utiliser un contrôle tel qu'une liste déroulante ou une liste déroulante.

Cet article démontre l’utilisation des API Aspose.Cells for Node.js via C++ pour créer des graphiques dynamiques en utilisant les deux approches mentionnées.  
{{% /alert %}}  

## **Utilisation des tables Excel**  

{{% alert color="primary" %}}  
Les tables Excel sont désignées comme ListObjects dans la perspective d'Aspose.Cells, par conséquent, nous utiliserons le terme "ListObject" au lieu de "Table" pour plus de clarté. Veuillez lire en détail comment [créer des ListObjects](/cells/fr/nodejs-cpp/create-and-format-table/) avec Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

ListObjects offre la fonctionnalité intégrée pour trier et filtrer les données via l'interaction de l'utilisateur. Les deux options de tri et de filtrage sont proposées par des listes déroulantes ajoutées automatiquement à la ligne d'en-tête de [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject). Grâce à ces fonctionnalités (tri et filtrage), [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) semble être le candidat idéal pour servir de source de données à un graphique dynamique, car lorsqu'un tri ou un filtrage est modifié, la représentation des données dans le graphique sera changée pour refléter l'état actuel de [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).

Afin de garder la démonstration simple à comprendre, nous créerons le [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) à partir de zéro et avancerons étape par étape comme indiqué ci-dessous.

1. Créez un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) vide.
1. Accéder au [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) du premier [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dans le [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Insérez des données dans les cellules.
1. Créer [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) basé sur les données insérées.
1. Créer [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) en fonction de la plage de données de [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
1. Enregistrez le résultat sur le disque.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Utilisation de Formules Dynamiques**  

Si vous ne souhaitez pas utiliser le [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) comme source de données pour le graphique dynamique, l'autre option consiste à utiliser des fonctions Excel (ou formules) pour créer une plage de données dynamique, et un contrôle (tel que ComboBox) pour déclencher le changement de données. Dans ce scénario, nous utiliserons la fonction VLOOKUP pour récupérer les valeurs appropriées en fonction de la sélection dans le ComboBox. Lorsque la sélection change, la fonction VLOOKUP actualisera la valeur de la cellule. Si une plage de cellules utilise la fonction VLOOKUP, toute la plage peut être actualisée lors de l'interaction de l'utilisateur, elle peut donc être utilisée comme source pour le graphique dynamique.

Afin de simplifier la démonstration et de la rendre compréhensible, nous créerons le classeur à partir de zéro et avancerons étape par étape comme décrit ci-dessous.

1. Créez un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) vide.
1. Accéder au [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) du premier [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dans le [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Insérez des données dans les cellules en créant une plage nommée. Ces données serviront de série pour le graphique dynamique.
1. Créer [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) basé sur la plage nommée créée à l'étape précédente.
1. Insérez quelques autres données dans les cellules qui serviront de source à la fonction VLOOKUP.
1. Insérez la fonction VLOOKUP (avec les paramètres appropriés) dans une plage de cellules. Cette plage servira de source pour le graphique dynamique.
1. Créer [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) basé sur la plage créée à l'étape précédente.
1. Enregistrez le résultat sur le disque.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

