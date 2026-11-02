---
title: Afficher ou filtrer le Top 10 dans un tableau croisé dynamique
linktitle: Afficher ou filtrer le Top 10 dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux classés ou les moins bien classés d’un champ de tableau croisé dynamique dans Aspose.Cells for Java. Cet article couvre la méthode Top10AutoShow d’Excel 97-2003, la lecture des options avec Top10AutoShowSettings et le filtre Top 10 d’Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Java, tableau croisé dynamique, 10 premiers éléments, affichage automatique, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /fr/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie tous les éléments d’un champ de ligne peut être difficile à lire lorsque ce champ comporte des dizaines de membres. Un rapport Top 10 ne conserve que les éléments les mieux classés ou les moins bien classés, ce qui répond exactement aux besoins des rapports de classement — « 5 premiers produits par chiffre d’affaires » ou « 3 dernières régions par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **AutoShow d’Excel 97-2003** — la méthode `PivotField.top10AutoShow()`. Cette méthode configure le paramètre classique « Afficher les N premiers/derniers éléments », stocké directement sur le champ de tableau croisé dynamique. Elle fonctionne dans toutes les versions d’Excel, anciennes et récentes, car elle fait partie du format d’origine des tableaux croisés dynamiques.
- **Filtre Top 10 d’Excel 2007-365** — la méthode `PivotField.filterTop10()`. Ce filtre de valeurs Top 10 moderne est accessible dans le menu du champ, sous « Filtres de valeurs ». Il est stocké sous forme d’un objet `PivotFilter` attaché au champ et propose un classement par nombre d’éléments ou par pourcentage.

## **Affichage du Top 10 dans Excel 97-2003 (top10AutoShow)**
Le paramètre AutoShow classique se configure par un seul appel à `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` :
- `isAutoShow` — active ou désactive le paramètre AutoShow sur le champ.
- `isTop` — `true` conserve les éléments les mieux classés (« Haut »), `false` conserve les moins bien classés (« Bas »).
- `count` — le nombre d’éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `rankBy` — l’index de base zéro du **champ de données** dont les valeurs servent à classer les éléments. Transmettez la valeur -1 pour classer les éléments selon le champ lui-même.
Le classement peut être effectué selon un champ de valeurs ou selon le champ lui-même. Deux cas d’usage sont présentés ci-dessous.

### **Classement selon un champ de valeurs**
Classez les éléments du champ de ligne en fonction d’un champ de valeurs ordinaire, tel que Sum of Sales. L’exemple suivant crée un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les mieux classés selon les ventes. `rankBy` vaut 0, car « Sum of Sales » est le champ de données situé à l’index 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Afficher les 2 premiers éléments classés par « Sum of Sales » (index du champ de données 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Classement selon le champ lui-même**
Un champ peut également être classé selon lui-même : transmettez la valeur -1 comme `rankBy`. Aucun champ de données supplémentaire n’est nécessaire pour cette variante ; le champ doit simplement figurer dans la zone de ligne (ou de colonne). L’exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lorsque ce paramètre est enregistré, l’attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut du format. `Top10AutoShowSettings.getRankBy()` relit alors la valeur -1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Afficher les 3 derniers éléments classés par le champ lui-même (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Lecture des options actuelles (Top10AutoShowSettings)**
La méthode `PivotField.getTop10AutoShowSettings()` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées sur le champ. Utilisez-le pour inspecter la manière dont les éléments seront affichés dans un classeur existant ou dans un tableau croisé dynamique que vous venez de configurer, y compris lorsque le classeur a été chargé à partir d’un fichier.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), de sorte que les valeurs relues sont prises en compte par toutes les versions d’Excel.

## **Remarque**

{{% alert color="primary" %}}
- Les propriétés directes de `PivotField` exposées par `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` et `getAutoShowField()` sont marquées comme obsolètes. Utilisez plutôt l’objet `Top10AutoShowSettings` : `Top10AutoShowSettings.isAutoShow()` remplace `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` remplace `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` remplace `PivotField.getAutoShowCount()` et `Top10AutoShowSettings.getRankBy()` remplace `PivotField.getAutoShowField()`. Pour modifier les paramètres, utilisez la méthode `PivotField.top10AutoShow()`.
- `top10AutoShow` fonctionne avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne figurent pas dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre Top 10 (filterTop10)**
Les versions modernes d’Excel proposent le filtre de valeurs Top 10 dans le menu du champ (« Filtres de valeurs », « Top 10 »...). Aspose.Cells modélise ce filtre à l’aide de la méthode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — l’index de base zéro du champ de données dont les valeurs agrégées servent à classer les éléments.
- `type` — indique ce que représente `itemCount`. `PivotFilterType.COUNT` conserve un nombre fixe d’éléments (option « Éléments » de la boîte de dialogue). `PivotFilterType.PERCENT` conserve un pourcentage des éléments ; ainsi, `itemCount` représente lui-même ce pourcentage : la valeur 30 conserve les 30 % d’éléments les mieux classés. `PivotFilterType.SUM` classe les éléments en fonction du cumul de leurs valeurs.
- `isTop` — `true` pour « Haut », `false` pour « Bas ».
- `itemCount` — le N dans l’expression « Top N » ; son unité dépend de `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Filtre Top 10 - garder les 2 premiers éléments par « Sum of Sales » (index du champ de données 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// Pour un filtre basé sur un pourcentage, garder plutôt les 30 % premiers éléments :
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` et `filterTop10` sont deux fonctionnalités distinctes. AutoShow écrit l’attribut classique `autoShow` défini sur le champ de tableau croisé dynamique et est pris en compte par toutes les versions d’Excel, depuis Excel 97. `filterTop10` écrit une entrée `PivotFilter` moderne, qui requiert Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version plus ancienne d’Excel, un tableau croisé dynamique qui utilise le filtre moderne revient à afficher tous les éléments. Pour les documents qui doivent faire l’objet d’un aller-retour au moyen d’outils hérités, privilégiez `top10AutoShow` ; pour les classeurs modernes, privilégiez `filterTop10`, car cette méthode se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles associés**
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/java/pivot-table-add-row-and-column-fields/)
- [Regrouper les champs dans un tableau croisé dynamique](/cells/fr/java/group-pivot-fields-in-the-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/)
- [Ajouter un champ de page à un tableau croisé dynamique](/cells/fr/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}