---
title: Formater une partie d’un tableau croisé dynamique
description: Formater une partie d’un tableau croisé dynamique dans Aspose.Cells for Node.js via C++ en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.format, les formats étant stockés dans PivotTable.getPivotFormats() et conservés lorsque le tableau croisé dynamique est actualisé.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Node.js via C++, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /fr/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
`PivotTable.formatAll` applique un style unique à l’ensemble du tableau croisé dynamique et est expliqué sur la page parente. Il ne fait pas de distinction entre les étiquettes, les valeurs, les totaux ou des zones particulières du rapport.  
En pratique, seule une partie d’un tableau croisé dynamique doit généralement ressortir. Les cibles courantes incluent les étiquettes appartenant à un champ de ligne, les cellules de valeur générées par un champ, la ligne de total général, ou un rectangle arbitraire tel que les deux premières lignes d’éléments.  
Appliquer un style directement aux cellules de feuille de calcul d’un tableau croisé dynamique n’est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les étiquettes d’un champ ou les valeurs de données, et il est résolu de nouveau lorsque le tableau croisé dynamique est recalculé, actualisé ou développé. En revanche, un style écrit directement dans une cellule appartient à cette position de cellule et n’est pas suivi par le modèle pivot.  
Aspose.Cells expose la famille complète de surcharges `PivotTable.format` afin que les deux types de mise en forme soient disponibles :
- `format(PivotArea, Style)` attache un style à une région sémantique construite avec `PivotArea.select` ou `PivotArea.selectField`.
- `format(CellArea, Style)` attache un style à un rectangle de feuille de calcul à l’intérieur du tableau croisé dynamique.
- `format(number row, number column, Style)` cible une cellule unique.
- `formatAll(Style)` met en forme l’ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l’approche recommandée lorsqu’une mise en évidence doit suivre un champ ou une région du rapport.  
1. Créez un `PivotArea` avec `new PivotArea(pivotTable)`. L’objet décrit une région sémantique appartenant à ce tableau croisé dynamique précis.  
1. Sélectionnez un champ par sa position indice zéro sur un axe donné avec `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DataAndLabel` sélectionne à la fois les étiquettes et les données du champ.  
   - `PivotTableSelectionType.LabelOnly` sélectionne uniquement les étiquettes du champ.  
   - `PivotTableSelectionType.DataOnly` sélectionne uniquement les cellules de données du champ.  
1. Sélectionnez un champ par son nom avec `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Lorsqu’un champ de ligne est sélectionné par son nom, la région se résout aux cellules de valeur générées par les éléments de ce champ.  
1. Créez un `Style` avec `workbook.createStyle()`, configurez sa police, sa couleur de premier plan et son motif de remplissage plein, puis transmettez le style à `pivotTable.format(area, style)`.  
1. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `pivotTable.getPivotFormats()`.  
1. Les formats attachés aux champs sont appliqués lorsque les données du pivot sont calculées. Par conséquent, appelez `pivotTable.calculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.  
L’exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux étiquettes de ligne `Fruit` avec `PivotArea.select` et `PivotTableSelectionType.LabelOnly`, applique un style aux cellules de valeur générées par le même champ de ligne avec `PivotArea.selectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient rendus.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formater une zone Cell du tableau croisé dynamique**
Utilisez `PivotTable.format(CellArea, Style)` lorsque la zone d’intérêt est un simple rectangle de feuille de calcul plutôt qu’une région pivot sémantique.  
Un `CellArea` est décrit par ses propriétés `startRow`, `startColumn`, `endRow` et `endColumn`. Les valeurs sont des coordonnées de feuille de calcul à indice zéro, et les coordonnées de fin identifient la dernière ligne et la dernière colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu’à la position de fin, incluses.  
Contrairement à un format ancré sur un champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `pivotTable.calculateData()` n’est pas nécessaire pour que le style apparaisse.  
Un rectangle `CellArea` peut contenir à la fois des cellules d’étiquette et des cellules de valeur. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.  
L’exemple suivant met en forme le rectangle `E4:F5` du tableau croisé dynamique avec un style italique bleu clair et enregistre le classeur sans recalcul supplémentaire.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Correspondance entre les zones Pivot et les zones Cell**
Excel stocke la mise en forme du tableau croisé dynamique sous forme d’enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu’une demande de mise en forme est traduite en zones pivot lorsqu’elle est enregistrée.  
La relation entre le `CellArea` fourni par l’utilisateur et les zones pivot stockées en interne est de plusieurs à plusieurs dans les deux sens.  
- Un `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules d’étiquette et des cellules de valeur, il est décomposé en règles distinctes d’étiquette et de données, car le modèle pivot traite séparément la mise en forme des étiquettes et celle des données.  
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu’une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C’est pourquoi `PivotArea.getCellAreas()` renvoie une collection plutôt qu’un seul rectangle.  
Chaque opération de mise en forme effectuée via `pivotTable.format()` est enregistrée dans `pivotTable.getPivotFormats()`. Chaque entrée `PivotTableFormat` expose le `PivotArea` associé et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu’un `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.  
Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `getOnlyLabel()` et `getOnlyData()`. L’exemple ci‑dessous met en forme un seul rectangle couvrant à la fois les étiquettes et les valeurs, inspecte `pivotTable.getPivotFormats()`, et affiche les coordonnées `CellArea` que chaque zone pivot stockée résout.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Parce que les formats sont stockés sous forme de zones pivot plutôt que comme des styles de cellule ordinaires, ils survivent aux recalculs et aux actualisations. Lorsque le tableau croisé dynamique est actualisé avec `pivotTable.refreshData()`, recalculé avec `pivotTable.calculateData()`, ou enregistré puis rechargé, chaque zone pivot stockée se résout à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez un `PivotArea` construit avec `select` ou `selectField` lorsqu’une mise en évidence doit rester attachée à un champ ou à une région sémantique à travers les actualisations, et utilisez un `CellArea` lorsque la mise en forme d’un rectangle fixe dans la disposition actuelle du tableau croisé dynamique est suffisante. La surcharge `format(number row, number column, Style)` cible une cellule individuelle. Utilisez `formatAll`, expliqué sur la page parente, lorsque l’ensemble du tableau croisé dynamique doit être restylé en une fois.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)
- [Ajouter des champs de ligne et de colonne au tableau croisé dynamique](/cells/fr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Gérer les champs de valeur dans le tableau croisé dynamique](/cells/fr/nodejs-cpp/manage-value-fields/)
- [Actualiser le tableau croisé dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}