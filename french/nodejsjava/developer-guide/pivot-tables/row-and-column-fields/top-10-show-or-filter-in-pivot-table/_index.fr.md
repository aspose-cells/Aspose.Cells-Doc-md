---
title: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
linktitle: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux classés ou les moins bien classés d’un champ de tableau croisé dynamique dans Aspose.Cells for Node.js via Java. Cet article présente la méthode Top10AutoShow d’Excel 97-2003, la lecture des options avec Top10AutoShowSettings et le filtre des 10 premiers éléments d’Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Node.js via Java, tableau croisé dynamique, 10 premiers, affichage auto, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /fr/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie chaque élément d’un champ de ligne peut être difficile à lire lorsque ce champ comporte des dizaines de membres. Un rapport des 10 premiers éléments ne conserve que les éléments les mieux classés ou les moins bien classés, ce qui répond exactement aux besoins des rapports de classement — « 5 principaux produits par chiffre d’affaires » ou « 3 dernières régions par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **AutoShow Excel 97-2003** — la méthode `PivotField.top10AutoShow()`. Il s’agit du paramètre classique « Afficher les N éléments supérieurs/inférieurs » stocké directement sur le champ du tableau croisé dynamique. Il fonctionne dans toutes les versions d’Excel, anciennes et récentes, car il fait partie du format d’origine des tableaux croisés dynamiques.
- **Filtre des 10 premiers éléments Excel 2007-365** — la méthode `PivotField.filterTop10()`. Il s’agit du filtre moderne des 10 premiers éléments disponible dans le menu du champ, sous Filtres de valeurs. Il est stocké sous forme d’objet `PivotFilter` associé au champ et propose un classement fondé sur le nombre d’éléments ou sur un pourcentage.

## **Affichage des 10 premiers éléments dans Excel 97-2003 (Top10AutoShow)**
La fonctionnalité AutoShow classique se configure avec un seul appel à `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` :
- `isAutoShow` — active ou désactive le paramètre AutoShow sur le champ.
- `isTop` — `true` conserve les éléments les mieux classés, `false` conserve les éléments les moins bien classés.
- `count` — le nombre d’éléments à conserver, par exemple 10 pour un rapport classique des 10 premiers éléments.
- `rankBy` — l’index du **champ de données** dont les valeurs servent à classer les éléments ; la numérotation des index commence à zéro. Transmettez -1 pour classer les éléments selon le champ lui-même.
Le classement peut reposer sur un champ de valeurs ou sur le champ lui-même. Deux variantes courantes sont présentées ci-dessous.

### **Classement par un champ de valeurs**
Classez les éléments du champ de ligne en fonction d’un champ de valeurs classique, tel que « Somme des ventes ». L’exemple suivant construit un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les mieux classés par chiffre d’affaires. La valeur de `rankBy` est 0, car « Somme des ventes » est le champ de données situé à l’index 0.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Classement par le champ lui-même**
Un champ peut également être classé par lui-même : transmettez -1 comme `rankBy`. Aucun champ de données supplémentaire n’est nécessaire pour cette variante ; le champ doit simplement se trouver dans la zone des lignes ou des colonnes. L’exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lorsque ce paramètre est enregistré, l’attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut du format. À la lecture, `getTop10AutoShowSettings().getRankBy()` renvoie -1.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Lecture des options actuelles (Top10AutoShowSettings)**
La méthode `PivotField.getTop10AutoShowSettings()` retourne un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées sur le champ. Utilisez-le pour examiner la manière dont un classeur existant ou un tableau croisé dynamique que vous venez de configurer affichera ses éléments, y compris dans le cas des classeurs chargés à partir d’un fichier.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Les accesseurs `isAutoShow()`, `isTop()`, `getAutoShowCount()` et `getRankBy()` correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Par conséquent, les valeurs relues sont celles prises en compte par toutes les versions d’Excel.

## **Remarque**

{{% alert color="primary" %}}
- Les accesseurs directs de `PivotField`, à savoir `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` et `getAutoShowField()`, sont marqués comme obsolètes. Utilisez plutôt l’objet `getTop10AutoShowSettings()` : `isAutoShow()` devient `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` devient `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` devient `getTop10AutoShowSettings().getAutoShowCount()` et `getAutoShowField()` devient `getTop10AutoShowSettings().getRankBy()`. La méthode `top10AutoShow()` elle-même reste le moyen pris en charge de modifier les paramètres.
- `top10AutoShow()` fonctionne avec les champs de ligne et de colonne. Un champ placé uniquement dans la zone de filtre (ou de page) ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre des 10 premiers éléments (FilterTop10)**
Les versions modernes d’Excel proposent le filtre des 10 premiers éléments dans le menu du champ, sous Filtres de valeurs. Aspose.Cells le modélise avec la méthode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, qui retourne le `PivotFilter` créé :
- `valueFieldIndex` — l’index du champ de données dont les valeurs agrégées servent à classer les éléments ; la numérotation des index commence à zéro.
- `type` — détermine la signification de `itemCount`. `PivotFilterType.COUNT` conserve un nombre fixe d’éléments, correspondant à l’option Éléments de la boîte de dialogue. `PivotFilterType.PERCENT` conserve un pourcentage des éléments ; `itemCount` représente alors le pourcentage lui-même — la valeur 30 conserve les 30 % des éléments les mieux classés. `PivotFilterType.SUM` effectue le classement selon la couverture cumulée des valeurs.
- `isTop` — `true` pour les éléments les mieux classés, `false` pour les éléments les moins bien classés.
- `itemCount` — le N de « N premiers » ; son unité dépend de `type`.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` et `filterTop10()` sont deux fonctionnalités distinctes. AutoShow écrit l’ensemble classique d’attributs `autoShow` sur le champ du tableau croisé dynamique. Ces attributs sont pris en charge par toutes les versions d’Excel depuis Excel 97. `filterTop10()` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version antérieure d’Excel, un tableau croisé dynamique qui utilise le filtre moderne revient à afficher tous les éléments. Pour les documents destinés à un aller-retour avec des outils hérités, préférez `top10AutoShow()` ; pour les classeurs modernes, préférez `filterTop10()`, car il se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles connexes**
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Regrouper les champs du tableau croisé dynamique](/cells/fr/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/nodejs-java/refresh-pivot-table/)
- [Ajouter un champ de page à un tableau croisé dynamique](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}