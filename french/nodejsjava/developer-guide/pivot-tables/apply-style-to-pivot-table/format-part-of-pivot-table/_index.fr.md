---
title: Formater une partie d'un tableau croisé dynamique
description: Formater une partie d'un tableau croisé dynamique dans Aspose.Cells for Node.js via Java en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.format, les formats étant stockés dans PivotTable.getPivotFormats() et conservés lors du rafraîchissement du tableau croisé dynamique.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Node.js via Java, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /fr/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.formatAll` applique un style unique à l'ensemble du tableau croisé dynamique et est décrit sur la page parente. Il ne fait pas de distinction entre les libellés, les valeurs, les totaux ou les régions particulières du rapport.  
En pratique, seule une partie d'un tableau croisé dynamique doit généralement ressortir. Les cibles courantes incluent les libellés appartenant à un champ de ligne, les cellules de valeur générées par un champ, la ligne du total général, ou un rectangle arbitraire tel que les deux premières lignes d'éléments.  
Appliquer un style directement aux cellules de la feuille de calcul d’un tableau croisé dynamique n’est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les libellés d’un champ ou les valeurs de données, et il est résolu à nouveau lorsque le tableau croisé dynamique est recalculé, rafraîchi ou développé. En revanche, un style écrit directement sur une cellule appartient à cette position de cellule et n’est pas suivi par le modèle de tableau croisé dynamique.  
Aspose.Cells expose la famille complète de surcharges `PivotTable.format` afin que les deux types de mise en forme soient disponibles :
- `format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.select` ou `PivotArea.selectField`.
- `format(CellArea, Style)` ancre un style à un rectangle de la feuille de calcul à l’intérieur du tableau croisé dynamique.
- `format(int row, int column, Style)` cible une seule cellule.
- `formatAll(Style)` formate l’ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l'approche recommandée lorsqu’une mise en évidence doit suivre un champ ou une région du rapport.
1. Créez une `PivotArea` avec `new PivotArea(pivotTable)`. L'objet décrit une région sémantique qui appartient à ce tableau croisé dynamique spécifique.  
2. Sélectionnez un champ par sa position indexée à partir de zéro sur un axe donné avec `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DATA_AND_LABEL` sélectionne à la fois les libellés et les données du champ.  
   - `PivotTableSelectionType.LABEL_ONLY` sélectionne uniquement les libellés du champ.  
   - `PivotTableSelectionType.DATA_ONLY` sélectionne uniquement les cellules de données du champ.  
3. Sélectionnez un champ par son nom avec `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Lorsqu’un champ de ligne est sélectionné par son nom, la région se résout aux cellules de valeur générées par les éléments de ce champ.  
4. Créez un `Style` avec `Workbook.createStyle()`, configurez sa police, sa couleur de premier plan et son motif d’arrière-plan plein, puis transmettez le style à `PivotTable.format(area, style)`.  
5. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.getPivotFormats()`.  
6. Les formats ancrés aux champs sont appliqués lorsque les données du tableau croisé dynamique sont calculées. Ainsi, appelez `PivotTable.calculateData()` après l’application des formats afin que les styles deviennent visibles.  
L'exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux libellés de ligne `Fruit` avec `PivotArea.select` et `PivotTableSelectionType.LABEL_ONLY`, applique un style aux cellules de valeur générées par ce même champ de ligne avec `PivotArea.selectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.format(CellArea, Style)` lorsque la région d’intérêt est un simple rectangle de feuille de calcul plutôt qu’une région pivot sémantique.  
Une `CellArea` est décrite par les champs publics `StartRow`, `StartColumn`, `EndRow` et `EndColumn`. Les valeurs sont des coordonnées de feuille de calcul indexées à partir de zéro, et les coordonnées de fin identifient la dernière ligne et colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu’à la position de fin incluse.  
Contrairement à un format ancré à un champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `calculateData()` n’est pas nécessaire pour que le style apparaisse.  
Un rectangle `CellArea` peut contenir à la fois des cellules de libellé et des cellules de valeur. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.  
L'exemple suivant formate le rectangle `E4:F5` du tableau croisé dynamique avec un style italique, bleu clair, et enregistre le classeur sans aucun recalcul supplémentaire.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Comment les zones Pivot et les zones CellArea se correspondent**
Excel stocke la mise en forme des tableaux croisés dynamiques sous forme d’enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu’une requête de mise en forme est traduite en zones pivot lors de son enregistrement.  
La relation entre la `CellArea` fournie par l’utilisateur et les zones pivot stockées en interne est de type plusieurs-à-plusieurs dans les deux sens.  
- Une `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules de libellé et des cellules de valeur, il est décomposé en règles distinctes pour les libellés et les données, car le modèle pivot traite la mise en forme des libellés et des données indépendamment.  
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu’une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C’est pourquoi `PivotArea.getCellAreas()` renvoie une collection plutôt qu’un seul rectangle.  
Chaque opération de mise en forme effectuée via `PivotTable.format` est enregistrée dans `PivotTable.getPivotFormats()`. Chaque entrée `PivotTableFormat` expose la `PivotArea` associée et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu’une `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.  
Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `getOnlyLabel()` et `getOnlyData()`. L’exemple ci‑dessous formate un unique rectangle couvrant à la fois les libellés et les valeurs, inspecte `PivotTable.getPivotFormats()` et affiche les coordonnées `CellArea` que chaque zone pivot stockée résout.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
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
Parce que les formats sont stockés en tant que zones pivot plutôt qu’en tant que styles de cellule ordinaires, ils survivent aux recalculs et aux rafraîchissements. Lorsque le tableau croisé dynamique est rafraîchi avec `PivotTable.refreshData()`, recalculé avec `calculateData()`, ou enregistré puis rechargé, chaque zone pivot stockée se résout de nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez une `PivotArea` construite avec `select` ou `selectField` lorsqu’une mise en évidence doit rester attachée à un champ ou à une région sémantique lors des rafraîchissements, et utilisez une `CellArea` lorsque le formatage d’un rectangle fixe dans la mise en page actuelle du tableau croisé dynamique suffit. La surcharge `format(int row, int column, Style)` à cellule unique cible une cellule individuelle. Utilisez `formatAll`, décrit sur la page parente, lorsque l’ensemble du tableau croisé dynamique doit être restylé en une fois.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Ajouter des champs de ligne et de colonne au tableau croisé dynamique](/cells/fr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/nodejs-java/manage-value-fields/)
- [Rafraîchir le tableau croisé dynamique](/cells/fr/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}