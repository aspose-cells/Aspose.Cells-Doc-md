---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++, ancrer une règle à la région de données avec applyTo et un scope PivotConditionFormatScopeType, ou définir la cible avec addCellArea et pivotAreas, puis attacher les règles et les styles via formatConditions.addCondition.
keywords: Aspose.Cells for JavaScript via C++, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /fr/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est peinte une fois et conserve son style quels que soient les valeurs. La mise en forme conditionnelle est le pendant basé sur des règles – mettre en surbrillance chaque montant supérieur à 200, ombrer les cinquante pour cent du milieu, ou signaler les éléments les mieux classés – et la mise en surbrillance suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou rafraîchi.  
Dans Aspose.Cells, la mise en forme conditionnelle d'un tableau croisé dynamique se trouve dans la collection `pivotTable.conditionalFormats`. Chaque entrée est un `PivotConditionalFormat` qui répond à deux questions de manière indépendante :
- **Où la règle s'applique-t-elle ?** La région cible est définie soit via `applyTo(row, column, scope)`, qui reproduit le sélecteur de portée de l'interface utilisateur Excel, soit via `addCellArea(cellArea)` et la collection `pivotAreas`, qui nomment explicitement la région.
- **Que teste la règle ?** Une ou plusieurs conditions sont ajoutées à `formatConditions` avec `addCondition(type, operatorType, formula1, formula2)`, et chaque condition possède son propre `style`.

{{% alert color="primary" %}}
N'appelez pas `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` ou `formatConditions.addArea(cellArea)` sur l'objet `formatConditions` d'un format conditionnel de tableau croisé dynamique. Ces deux surcharges sont héritées de l'API de mise en forme conditionnelle ordinaire des feuilles de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellules n'est jamais convertie en zone de tableau croisé dynamique, de sorte que la requête est silencieusement ignorée. Définissez toujours la région sur le `PivotConditionalFormat` lui‑même (`applyTo`, `addCellArea` ou `pivotAreas`) et ajoutez la règle avec l'une des surcharges `addCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l'interface Excel)**
La première méthode positionne la règle comme le fait l'interface utilisateur d'Excel. Une cellule du tableau croisé dynamique est nommée par ses coordonnées de feuille de calcul basées sur zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu'où la règle doit s'étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.Data` – toutes les cellules de valeurs que le tableau croisé dynamique produit, y compris les totaux généraux.
- `PivotConditionFormatScopeType.Field` – les cellules de valeurs qui appartiennent au champ identifié par la cellule, excluant les totaux généraux. La cellule doit être une cellule de champ, telle qu'une étiquette de champ de ligne ; passer une cellule de valeur lève une exception.
- `PivotConditionFormatScopeType.Selection` – uniquement les cellules de valeurs à l'intersection que la cellule sélectionne, généralement une seule cellule de valeur.
L'exemple ci‑dessus crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `Data`, et met en évidence chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Apple 220, Banana 330, Cherry 200 et le total général 750, la règle colore F4, F5 et F7 – la région résolue est toute la colonne de données F4 : F7, et seules les cellules dont la valeur satisfait la règle s'illuminent.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Ancrer le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Data
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Règle - mettre en évidence les montants supérieurs à 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) renvoie le fichier sous forme d'octets
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Ancrer la même règle à l’étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `Field` se résout en F4 : F6 – la même colonne de données sans la ligne de total général – car la portée décrit maintenant le champ `Fruit` plutôt que la totalité de la zone de valeurs. La portée `Selection` ancrée à F4 se résout uniquement à F4.

## **Définir la région manuellement**
La deuxième méthode ignore le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec addCellArea**
`addCellArea(cellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul basées sur zéro, et la région correspond exactement au rectangle fourni – aucune extension à la colonne de données et aucune logique de total général. Utilisez‑le lorsque les cellules d’intérêt forment un rectangle fixe connu du présent agencement du tableau croisé dynamique.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Cibler le rectangle F4:F6 (les cellules de valeur sans le total général)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Règle - italique en jaune clair pour les montants entre 150 et 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **Une région pivot sémantique avec pivotAreas**
`pivotAreas` est le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `select` ou `selectField`, puis ajoutez‑le avec `pivotAreas.addPivotArea(pivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est rafraîchi et que la disposition change. La surcharge `pivotAreas.add(pivotArea)` fonctionne toujours mais est marquée comme obsolète – privilégiez `addPivotArea`.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Attacher la règle au champ de données Montant en tant que région sémantique
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Règle - texte gris pour les montants inférieurs à 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `conditionalFormats.add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier sauvegardé par le premier exemple dans Node montre la même règle avec son type, son opérateur et sa formule intacts, et `getCellAreas()` indique la même région. Sur cette plateforme, les propriétés `type` et `operator` d’une condition apparaissent sous forme de valeurs numériques d’énumération. Les entrées qui n’ont jamais reçu de condition sont éliminées lors de l’enregistrement du classeur, de la même façon qu’Excel supprime une mise en forme conditionnelle dépourvue de règle.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Recharger le fichier écrit par le premier exemple
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // Cela affiche :
    // Formats conditionnels : 1
    // Format 0 : 1 2 formula1==200   (type 1 = CellValue, opérateur 2 = GreaterThan)
    //     lignes 4-7, colonnes 6-6        (F4:F7, la région de données résolue)
    process.exit(0);
});
```

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)
- [Formater une partie du tableau croisé dynamique](/cells/fr/javascript-cpp/format-part-of-pivot-table/)
- [Afficher ou filtrer le Top 10 dans le tableau croisé dynamique](/cells/fr/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}