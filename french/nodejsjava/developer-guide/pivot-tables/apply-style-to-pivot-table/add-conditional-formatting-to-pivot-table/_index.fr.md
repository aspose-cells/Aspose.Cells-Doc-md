---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for Node.js via Java - ancrez une règle à la région des données avec applyTo et une portée PivotConditionFormatScopeType, ou définissez la cible avec addCellArea et getPivotAreas, puis attachez les règles et les styles via getFormatConditions().addCondition.
keywords: Aspose.Cells, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /fr/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est peinte une seule fois et conserve son style quelles que soient les valeurs. La mise en forme conditionnelle est le pendant basé sur des règles – mettre en évidence chaque montant supérieur à 200, ombrer la moitié centrale des valeurs, ou signaler les éléments les mieux classés – et la mise en surbrillance suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou actualisé.  
Dans Aspose.Cells for Node.js via Java, la mise en forme conditionnelle d'un tableau croisé dynamique réside dans la collection `pivotTable.getConditionalFormats()`. Chaque entrée est un `PivotConditionalFormat` qui répond indépendamment à deux questions :
- **Où la règle s'applique-t-elle ?** La région cible est définie soit via `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, qui reproduit le sélecteur de portée de l'interface utilisateur d'Excel, soit via `addCellArea(CellArea)` et la collection `getPivotAreas()`, qui nomment explicitement la région.
- **Que teste la règle ?** Une ou plusieurs conditions sont ajoutées à `getFormatConditions()` avec `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, et chaque condition possède son propre `getStyle()`.

{{% alert color="primary" %}}
N'appelez pas `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ni `FormatConditionCollection.addArea(CellArea)` sur l'objet `getFormatConditions()` d'un format conditionnel de tableau croisé dynamique. Ces deux surcharges proviennent de l'API de mise en forme conditionnelle d'une feuille de calcul ordinaire et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellules n'est jamais convertie en zone de tableau croisé dynamique, de sorte que la requête est silencieusement ignorée. Définissez toujours la région sur le `PivotConditionalFormat` lui‑même (`applyTo`, `addCellArea` ou `getPivotAreas()`) et ajoutez la règle avec l'une des surcharges `addCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (comme dans l'interface Excel)**
La première méthode place la règle de la même manière que l'interface utilisateur d'Excel. Une cellule du tableau croisé dynamique est identifiée par ses coordonnées de feuille de calcul à indice zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu'où la règle doit s'étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.DATA` – toutes les cellules de valeurs générées par le tableau croisé dynamique, y compris les totaux généraux.
- `PivotConditionFormatScopeType.FIELD` – les cellules de valeurs appartenant au champ identifié par la cellule, excluant les totaux généraux. La cellule doit être une cellule de champ, comme une étiquette de champ de ligne ; passer une cellule de valeur déclenche une exception.
- `PivotConditionFormatScopeType.SELECTION` – uniquement les cellules de valeurs à l'intersection sélectionnée par la cellule, généralement une seule cellule de valeur.
L'exemple ci‑dessous crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche est en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `DATA`, et met en évidence chaque montant supérieur à 200 en blanc gras sur rouge. Avec les valeurs Pomme 220, Banane 330, Cerise 200 et le total général 750, la règle colore F4, F5 et F7 – la région résolue est toute la colonne de données F4 :F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

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
// Tableau croisé dynamique avec son coin supérieur gauche en E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Ancrer le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Data
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Règle - mettre en surbrillance les montants supérieurs à 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Ancrer la même règle à l'étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `FIELD` résout à F4 :F6, à la place – la même colonne de données sans la ligne de total général – car la portée décrit maintenant le champ `Fruit` plutôt que toute la zone de valeurs. La portée `SELECTION` ancrée à F4 se résout uniquement à F4.

## **Définir la région manuellement**
La deuxième méthode ignore le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec addCellArea**
`addCellArea(CellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul à indice zéro, et la région correspond exactement au rectangle fourni – aucune expansion vers la colonne de données et aucune logique de total général. Utilisez‑le lorsque les cellules d’intérêt forment un rectangle fixe connu du rendu actuel du tableau croisé dynamique.

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
// Ciblez le rectangle F4:F6 (les cellules de valeur sans le total global)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Règle - italique sur jaune clair pour les montants compris entre 150 et 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Une région pivot sémantique avec PivotAreas**
`getPivotAreas()` utilise le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `select` ou `selectField`, puis ajoutez‑le avec `getPivotAreas().addPivotArea(PivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est actualisé et que la disposition change. La surcharge `getPivotAreas().add(PivotArea)` compile toujours mais est marquée obsolète – privilégiez `addPivotArea`.

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
// Attacher la règle au champ de données Montant en tant que région sémantique
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Règle - texte gris pour les montants inférieurs à 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `add()` sur `getConditionalFormats()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier dans l'exemple ci‑dessous montre la même règle avec son type, son opérateur et sa formule intacts, et `getCellAreas()` indique les mêmes régions. Les entrées qui n'ont jamais reçu de condition sont supprimées lors de l'enregistrement du classeur, de la même façon qu'Excel élimine une mise en forme conditionnelle dépourvue de règle.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// Ceci imprime :
// Formats conditionnels : 1
// Format 0 : CellValue GreaterThan formule1==200
//     lignes 4-7, colonnes 6-6        (F4:F7, la région de données résolue)
```

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Formater une partie du tableau croisé dynamique](/cells/fr/nodejs-java/format-part-of-pivot-table/)
- [Top 10 afficher ou filtrer dans le tableau croisé dynamique](/cells/fr/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}