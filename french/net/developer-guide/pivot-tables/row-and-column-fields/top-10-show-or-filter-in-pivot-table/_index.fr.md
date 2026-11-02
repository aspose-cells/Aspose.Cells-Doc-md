---
title: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
linktitle: Afficher ou filtrer le Top 10
description: Découvrez comment afficher uniquement les éléments les mieux ou les moins bien classés d’un champ de tableau croisé dynamique dans Aspose.Cells for .NET. Cet article couvre la méthode Top10AutoShow d’Excel 97-2003, la lecture des options avec Top10AutoShowSettings ainsi que le filtre des 10 premiers éléments d’Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, 10 premiers éléments, affichage automatique, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /fr/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie chaque élément d’un champ de ligne peut être difficile à lire lorsque ce champ comporte des dizaines de membres. Un rapport sur les 10 éléments les mieux ou les moins bien classés ne conserve que ces éléments, ce qui correspond exactement aux besoins des rapports de classement — « les 5 produits générant le plus de revenus » ou « les 3 régions ayant le plus faible nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **AutoShow Excel 97-2003** — la méthode `PivotField.Top10AutoShow()`. Il s’agit du paramètre classique « Afficher les N premiers/derniers éléments », stocké directement sur le champ de tableau croisé dynamique. Il fonctionne dans toutes les versions d’Excel, anciennes et récentes, car il fait partie du format d’origine des tableaux croisés dynamiques.
- **Filtre des 10 premiers éléments Excel 2007-365** — la méthode `PivotField.FilterTop10()`. Il s’agit du filtre moderne de valeurs situé dans le menu du champ, sous « Filtres de valeurs ». Il est stocké sous forme d’objet `PivotFilter` associé au champ et propose un classement fondé sur le nombre d’éléments ou sur un pourcentage.

## **Affichage des 10 premiers éléments dans Excel 97-2003 (Top10AutoShow)**
La fonctionnalité AutoShow classique se configure avec un seul appel à `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)` :
- `isAutoShow` — active ou désactive le paramètre AutoShow sur le champ.
- `isTop` — `true` conserve les éléments les mieux classés, tandis que `false` conserve les éléments les moins bien classés.
- `count` — nombre d’éléments à conserver, par exemple 10 pour un rapport classique sur les 10 premiers éléments.
- `rankBy` — index de base zéro du **champ de données** dont les valeurs classent les éléments. Passez -1 pour classer les éléments selon le champ lui-même.
Le classement peut être effectué selon un champ de valeurs ou selon le champ lui-même. Deux variantes possibles sont présentées ci-dessous.

### **Classement par un champ de valeurs**
Classez les éléments du champ de ligne en fonction d’un champ de valeurs standard, tel que la somme des ventes. L’exemple suivant crée un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les plus performants en termes de ventes. `rankBy` vaut 0, car la somme des ventes correspond au champ de données situé à l’index 0.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Classement par le champ lui-même**
Un champ peut également servir à classer ses propres éléments — transmettez la valeur -1 comme `rankBy`. Aucun champ de données supplémentaire n’est nécessaire pour cette variante ; le champ doit simplement se trouver dans la zone des lignes ou des colonnes. L’exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lorsque ce paramètre est enregistré, l’attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut du format, et `Top10AutoShowSettings.RankBy` relit la valeur -1.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Lecture des options actuelles (Top10AutoShowSettings)**
La propriété `PivotField.Top10AutoShowSettings` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées sur le champ. Utilisez-la pour examiner la manière dont un classeur existant, ou un tableau croisé dynamique que vous venez de configurer, présente ses éléments, y compris dans le cas des classeurs chargés à partir d’un fichier.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), de sorte que les valeurs relues sont prises en compte par toutes les versions d’Excel.

## **Note**

{{% alert color="primary" %}}
- Les propriétés directes de `PivotField` (`IsAutoShow`, `IsAscendShow`, `AutoShowCount` et `AutoShowField`) sont marquées comme obsolètes. Utilisez plutôt l’objet `Top10AutoShowSettings` : `IsAutoShow` devient `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` devient `Top10AutoShowSettings.IsTop`, `AutoShowCount` devient `Top10AutoShowSettings.AutoShowCount` et `AutoShowField` devient `Top10AutoShowSettings.RankBy`. La méthode prise en charge pour modifier ces paramètres est `Top10AutoShow()`.
- `Top10AutoShow` fonctionne avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de filtre ne peut pas être classé de cette manière, car ses éléments ne figurent pas dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre des 10 premiers éléments (FilterTop10)**
Les versions modernes d’Excel proposent le filtre des 10 premiers éléments dans le menu du champ, sous « Filtres de valeurs », via l’option « 10 premiers éléments… ». Aspose.Cells le modélise avec la méthode `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — index de base zéro du champ de données dont les valeurs agrégées classent les éléments.
- `type` — signification de `itemCount`. `PivotFilterType.Count` conserve un nombre fixe d’éléments (l’option « Éléments » de la boîte de dialogue). `PivotFilterType.Percent` conserve un pourcentage des éléments ; ainsi, `itemCount` représente ce pourcentage lui-même — la valeur 30 conserve les 30 % d’éléments les mieux classés. `PivotFilterType.Sum` classe les éléments selon la couverture cumulée des valeurs.
- `isTop` — `true` conserve les éléments les mieux classés, tandis que `false` conserve les éléments les moins bien classés.
- `itemCount` — la valeur N dans le filtre des N premiers éléments ; son unité dépend de `type`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` et `FilterTop10` sont deux fonctionnalités distinctes. La fonctionnalité AutoShow écrit l’attribut classique `autoShow` sur le champ de tableau croisé dynamique et est prise en charge par toutes les versions d’Excel depuis Excel 97. `FilterTop10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version antérieure d’Excel, un tableau croisé dynamique qui utilise le filtre moderne affiche alors tous les éléments. Pour les documents qui doivent être enregistrés puis rouverts par des outils de génération antérieure, préférez `Top10AutoShow` ; pour les classeurs modernes, préférez `FilterTop10`, car cette méthode se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles associés**
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/net/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne aux tableaux croisés dynamiques](/cells/fr/net/pivot-table-add-row-and-column-fields/)
- [Regrouper les champs d’un tableau croisé dynamique](/cells/fr/net/group-pivot-fields-in-the-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/net/refresh-pivot-table/)
- [Ajouter un champ de page à un tableau croisé dynamique](/cells/fr/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}