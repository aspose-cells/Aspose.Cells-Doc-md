---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for Node.js via C++ - ancrer une règle sur la région de données avec applyTo et une portée PivotConditionFormatScopeType, ou définir la cible avec addCellArea et pivotAreas, puis attacher les règles et les styles via formatConditions.addCondition.
keywords: Aspose.Cells for Node.js via C++, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /fr/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est colorée une fois et conserve son style quelles que soient les valeurs.  
La mise en forme conditionnelle est la contrepartie basée sur des règles – mettre en surbrillance chaque montant supérieur à 200, ombrer les cinquante pour cent du milieu, ou signaler les éléments les mieux classés – et la mise en surbrillance suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou actualisé.  
Dans Aspose.Cells, la mise en forme conditionnelle du tableau croisé dynamique se trouve dans la collection `pivotTable.getConditionalFormats()`.  
Chaque entrée est un `PivotConditionalFormat` qui répond à deux questions indépendamment :
- **Où la règle s'applique-t-elle ?** La région cible est définie soit via `applyTo(row, column, scope)`, qui reflète le sélecteur de portée de l'interface utilisateur Excel, soit via `addCellArea(cellArea)` et la collection `pivotConditionalFormat.getPivotAreas()`, qui nomment explicitement la région.  
- **Que teste la règle ?** Une ou plusieurs conditions sont ajoutées à `formatConditions`, obtenues via `pivotConditionalFormat.getFormatConditions()`, avec `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, et chaque condition possède son propre style via `getStyle()`.

{{% alert color="primary" %}}
N'appelez pas `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` ou `formatConditions.addArea(cellArea)` sur l'objet `formatConditions` d'un format conditionnel de tableau croisé dynamique. Ces deux surcharges sont héritées de l'API de mise en forme conditionnelle ordinaire de la feuille de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellules n'est jamais convertie en zone de tableau croisé dynamique, ainsi la requête est ignorée silencieusement. Définissez toujours la région sur l'objet `pivotConditionalFormat` lui‑même (`applyTo`, `addCellArea` ou `getPivotAreas()`) et ajoutez la règle avec l'une des surcharges `addCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (la façon de l'interface Excel)**
La première méthode positionne la règle comme le fait l'interface utilisateur Excel. Une cellule du tableau croisé dynamique est nommée par ses coordonnées de feuille de calcul indexées à zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu'où la règle doit s'étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.DATA` – toutes les cellules de valeur produites par le tableau croisé dynamique, y compris les totaux généraux.  
- `PivotConditionFormatScopeType.FIELD` – les cellules de valeur appartenant au champ identifié par la cellule, à l'exclusion des totaux généraux. La cellule doit être une cellule de champ, par exemple une étiquette de champ de ligne ; fournir une cellule de valeur déclenche une exception.  
- `PivotConditionFormatScopeType.SELECTION` – uniquement les cellules de valeur à l'intersection que la cellule sélectionne, généralement une seule cellule de valeur.  
L'exemple ci‑dessous crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche est en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `DATA`, et met en surbrillance chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Pomme 220, Banane 330, Cerise 200 et le total général 750, la règle colore F4, F5 et F7 — la région résolue est la totalité de la colonne de données de F4 à F7, et seules les cellules dont la valeur satisfait la règle sont mises en surbrillance.

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
// Tableau croisé dynamique avec son coin supérieur gauche à E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Ancrer le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Données
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Règle - mettre en surbrillance les montants supérieurs à 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Ancrer la même règle à l'étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `FIELD` se résout en F4 : F6 à la place – la même colonne de données sans la ligne de total général – car la portée décrit maintenant le champ `Fruit` plutôt que l'ensemble de la zone de valeurs. La portée `SELECTION` ancrée à F4 se résout uniquement à F4.

## **Définir la région manuellement**
La deuxième méthode ignore le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec addCellArea**
`addCellArea(cellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul indexées à zéro, et la région correspond exactement au rectangle fourni — aucune extension vers la colonne de données et aucune logique de total général. Utilisez‑la lorsque les cellules d'intérêt forment un rectangle fixe connu de la disposition actuelle du tableau croisé dynamique.

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
// Cible le rectangle F4:F6 (les cellules de valeur sans le total général)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Règle - italique sur jaune clair pour les montants entre 150 et 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Une région pivot sémantique avec getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` est le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `select` ou `selectField`, et ajoutez‑le avec `pivotAreas.addPivotArea(pivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est actualisé et que la disposition change. La surcharge `pivotAreas.add(pivotArea)` compile toujours mais est marquée comme obsolète — privilégiez `addPivotArea`.

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
// Attacher la règle au champ de données Amount en tant que région sémantique
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Règle - texte gris pour les montants inférieurs à 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel à `conditionalFormats.add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur — réouvrir le fichier dans l'exemple ci‑dessous montre la même règle avec son type, son opérateur et sa formule intacts, et `getCellAreas()` indique les mêmes régions. Les entrées qui n'ont jamais reçu de condition sont supprimées lors de l'enregistrement du classeur, de la même manière qu'Excel élimine une mise en forme conditionnelle dépourvue de règle.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// Ceci imprime :
// Formats conditionnels : 1
// Format 0 : CellValue GreaterThan formula1==200
//     lignes 4-7, colonnes 6-6        (F4:F7, la région de données résolue)
```

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)
- [Formater une partie du tableau croisé dynamique](/cells/fr/nodejs-cpp/format-part-of-pivot-table/)
- [Afficher ou filtrer le top 10 dans le tableau croisé dynamique](/cells/fr/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}