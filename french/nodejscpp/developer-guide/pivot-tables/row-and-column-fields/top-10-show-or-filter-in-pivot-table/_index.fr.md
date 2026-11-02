---
title: Afficher ou filtrer le Top 10 dans un tableau croisé dynamique
linktitle: Afficher ou filtrer le Top 10 dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux ou les moins bien classés d'un champ de tableau croisé dynamique dans Aspose.Cells for Node.js via C++. Cet article présente la méthode Top10AutoShow d'Excel 97-2003, la lecture des options avec Top10AutoShowSettings et le filtre Top 10 d'Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Node.js via C++, tableau croisé dynamique, top 10, affichage automatique, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /fr/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique qui répertorie chaque élément d'un champ de ligne peut être difficile à lire lorsque ce champ contient des dizaines de membres. Un rapport Top 10 ne conserve que les éléments les mieux classés ou les moins bien classés, ce qui répond précisément aux besoins des rapports de classement : « les 5 premiers produits par chiffre d'affaires » ou « les 3 régions les moins bien classées selon le nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **Excel 97-2003 AutoShow** — la méthode `pivotField.top10AutoShow()`. Il s'agit du paramètre classique « Afficher les N premiers/derniers éléments », stocké directement sur le champ du tableau croisé dynamique. Il fonctionne dans toutes les versions d'Excel, anciennes et récentes, car il fait partie du format d'origine des tableaux croisés dynamiques.
- **Filtre Top 10 Excel 2007-365** — la méthode `pivotField.filterTop10()`. Il s'agit du filtre de valeurs Top 10 moderne disponible dans le menu du champ, sous Filtres de valeurs. Il est stocké sous forme d'objet `PivotFilter` attaché au champ et propose un classement basé sur le nombre d'éléments ou sur un pourcentage.

## **Afficher le Top 10 dans Excel 97-2003 (top10AutoShow)**
L'AutoShow classique se configure par un seul appel à `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)` :
- `isAutoShow` — active ou désactive le paramètre AutoShow sur le champ.
- `isTop` — `true` conserve les éléments les mieux classés (Haut), `false` conserve les moins bien classés (Bas).
- `count` — le nombre d'éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `rankBy` — l'index, compté à partir de 0, du **champ de données** dont les valeurs classent les éléments. Transmettez la valeur -1 pour classer les éléments selon le champ lui-même.
Le classement peut être fondé sur un champ de valeurs ou sur le champ lui-même. Deux variantes pertinentes sont présentées ci-dessous.

### **Classer selon un champ de valeurs**
Classez les éléments du champ de ligne en fonction d'un champ de valeurs standard, tel que Sum of Sales. L'exemple suivant crée un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les plus vendus. `rankBy` vaut 0, car « Sum of Sales » est le champ de données situé à l'index 0.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Classer selon le champ lui-même**
Un champ peut également être classé selon lui-même : transmettez la valeur -1 à `rankBy`. Aucun champ de données supplémentaire n'est nécessaire pour cette variante ; le champ doit simplement se trouver dans la zone des lignes (ou des colonnes). L'exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lorsque ce paramètre est enregistré, l'attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut de ce format. La méthode `top10AutoShowSettings.getRankBy()` renvoie ensuite la valeur -1.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Lire les options actuelles (Top10AutoShowSettings)**
La méthode `pivotField.getTop10AutoShowSettings()` retourne un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées sur le champ. Utilisez-le pour examiner la manière dont un classeur existant ou un tableau croisé dynamique que vous venez de configurer affiche ses éléments, notamment lorsque le classeur a été chargé à partir d'un fichier.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Les valeurs relues sont donc celles qui seront prises en compte par toutes les versions d'Excel.

## **Remarque**

{{% alert color="primary" %}}
- Les méthodes directes de `PivotField`, à savoir `isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` et `getAutoShowField()`, sont marquées comme obsolètes. Utilisez plutôt l'objet `Top10AutoShowSettings` : `pivotField.isAutoShow` devient `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` devient `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` devient `top10AutoShowSettings.getAutoShowCount()` et `pivotField.getAutoShowField()` devient `top10AutoShowSettings.getRankBy()`. La modification des paramètres est prise en charge par la méthode `pivotField.top10AutoShow()`.
- `top10AutoShow()` fonctionne avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre Top 10 (filterTop10)**
Dans les versions modernes d'Excel, Top 10 est disponible sous forme de filtre de valeurs dans le menu du champ (Filtres de valeurs, Top 10...). Dans Aspose.Cells, ce filtre est implémenté par la méthode `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)`, qui retourne le `PivotFilter` créé :
- `valueFieldIndex` — l'index, compté à partir de 0, du champ de données dont les valeurs agrégées classent les éléments.
- `type` — détermine la signification de `itemCount`. `PivotFilterType.Count` conserve un nombre fixe d'éléments (l'option « Éléments » de la boîte de dialogue). `PivotFilterType.Percent` conserve un pourcentage des éléments ; `itemCount` correspond donc directement à ce pourcentage — la valeur 30 conserve les 30 % des éléments les mieux classés. `PivotFilterType.SUM` classe les éléments en fonction de la couverture cumulée des valeurs.
- `isTop` — `true` pour Haut, `false` pour Bas.
- `itemCount` — le nombre N dans « Top N » ; son unité dépend de `type`.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` et `filterTop10` sont deux fonctionnalités distinctes. AutoShow écrit l'attribut classique `autoShow` et les attributs associés sur le champ du tableau croisé dynamique. Il est pris en charge par toutes les versions d'Excel, depuis Excel 97. `filterTop10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu'un classeur est ouvert dans une version plus ancienne d'Excel, un tableau croisé dynamique qui utilise le filtre moderne recourt alors à l'affichage de tous les éléments. Pour les documents qui doivent faire l'aller-retour avec des outils hérités, préférez `top10AutoShow` ; pour les classeurs modernes, préférez `filterTop10`, car il peut être utilisé avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles connexes**
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Regrouper les champs du tableau croisé dynamique](/cells/fr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}