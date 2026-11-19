---
title: Filtrage des Tableaux Croisés Dynamiques par libellé ou valeur
description: Aspose.Cells for Java prend en charge des capacités de filtrage exhaustives des Tableaux Croisés Dynamiques. Cet article explique comment filtrer les données d’un Tableau Croisé Dynamique à l’aide de filtres par libellé, de filtres par date, de filtres par valeur, de filtres des 10 premiers et en masquant ou en réaffichant des éléments du Tableau Croisé Dynamique.
linktitle: Filtrage par libellé ou valeur
keywords: Aspose.Cells, bibliothèque Java, tableur, Tableau Croisé Dynamique, filtre, filtre par libellé, filtre par valeur, filtre par date, filtre des 10 premiers, élément de Tableau Croisé Dynamique, masquage d’un élément de Tableau Croisé Dynamique
type: docs
weight: 10
url: /fr/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un Tableau Croisé Dynamique. Vous pouvez appliquer des filtres par libellé aux champs de ligne ou de colonne contenant du texte, utiliser des filtres par date lorsque le champ contient uniquement des cellules de date et d’heure ou des cellules vides, appliquer des filtres par valeur aux nombres agrégés, utiliser des filtres des 10 premiers pour classer les éléments selon un champ de valeur, ou masquer et réafficher manuellement des éléments individuels du Tableau Croisé Dynamique à l’aide de la propriété `IsHidden`. Chaque stratégie est exposée via des API dédiées sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les Tableaux Croisés Dynamiques sont de puissants outils d’analyse, mais les synthèses brutes contiennent souvent bien plus d’informations que vous n’avez besoin de présenter. Le filtrage est le principal mécanisme permettant de réduire un Tableau Croisé Dynamique aux lignes, aux colonnes ou aux valeurs utiles pour un rapport donné. Aspose.Cells for Java reproduit les capacités de filtrage disponibles dans Microsoft Excel et les expose de manière programmatique afin que la génération des rapports puisse être entièrement automatisée.
Les stratégies de filtrage suivantes sont abordées dans cet article :
1. **Filtre par libellé** — filtre les éléments d’un champ de ligne ou de colonne en fonction de leurs libellés textuels.
2. **Filtre par date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de date et d’heure, ou des valeurs vides.
3. **Filtre par valeur** — filtre les éléments en fonction des valeurs agrégées d’un champ de données.
4. **Filtre des 10 premiers** — affiche uniquement les N éléments les plus élevés ou les plus bas, classés selon un champ de valeur.
5. **Masquer / Réafficher les éléments du Tableau Croisé Dynamique** — contrôle manuellement la visibilité de chaque élément individuel d’un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après l’application de n’importe quel filtre, vous devez appeler `getPivotCache().refresh()` sur le Tableau Croisé Dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre par libellé**
Un filtre par libellé permet de filtrer les éléments d’un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cette opération est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre donnée, contiennent un mot particulier ou correspondent à un autre critère fondé sur les libellés.
Aspose.Cells expose le filtrage par libellé par l’intermédiaire de la méthode `PivotField.filterByLabel(PivotFilterType, String)`. L’énumération `PivotFilterType` contient des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. Le second argument fournit la chaîne de libellé utilisée pour la comparaison.
L’exemple suivant charge un classeur contenant un Tableau Croisé Dynamique existant, applique un filtre par libellé afin que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le Tableau Croisé Dynamique et enregistre le résultat.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Filtre par date**
Les filtres par date permettent de restreindre un Tableau Croisé Dynamique à l’aide de critères fondés sur les dates, tels qu’aujourd’hui, la semaine dernière, ce mois-ci, le trimestre suivant ou une plage de dates donnée. Ce sont des filtres spécialisés qui ne fonctionnent qu’avec des champs stockant des informations de date et d’heure.

{{% alert color="primary" %}}
Le filtre par date ne fonctionne que lorsque la zone des lignes ou des colonnes contient uniquement des cellules de date et d’heure ou des valeurs vides. Si le champ sous-jacent contient d’autres types de données, tels que des nombres ou du texte, le filtre par date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté comme une date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d’appliquer ce filtre.
Aspose.Cells expose le filtrage par date par l’intermédiaire de la méthode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L’énumération `PivotFilterType` contient des valeurs spécifiques aux dates, telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. En fonction du type de filtre sélectionné, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, vous transmettez les dates de début et de fin).
L’exemple suivant charge un classeur contenant un Tableau Croisé Dynamique dont la zone des lignes contient un champ de date, applique un filtre par date qui limite les éléments visibles à une plage de dates donnée, actualise le Tableau Croisé Dynamique et enregistre le classeur.
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Filtre par valeur**
Les filtres par valeur opèrent sur les valeurs agrégées qu’un Tableau Croisé Dynamique calcule dans sa zone de données. Au lieu de comparer des libellés textuels, ils comparent des totaux numériques à un seuil. Les cas d’utilisation typiques consistent à afficher uniquement les produits dont la somme des ventes dépasse un montant cible, ou uniquement les régions dont le nombre de transactions se situe dans une plage donnée.
Aspose.Cells expose le filtrage par valeur par l’intermédiaire de la méthode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Le paramètre `filterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Le paramètre `valueField` indique le champ de données à évaluer, et le ou les derniers arguments fournissent la ou les valeurs de seuil.
L’exemple suivant charge un classeur contenant un Tableau Croisé Dynamique, applique un filtre par valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le Tableau Croisé Dynamique et enregistre le classeur.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Filtre des 10 premiers**
Le filtre des 10 premiers est une forme spécialisée de filtre par valeur qui ne conserve que les N éléments les plus élevés ou les plus bas selon un champ de valeur choisi. Il est couramment utilisé pour classer des rapports tels que « 10 premiers produits par chiffre d’affaires » ou « 5 dernières régions par nombre de ventes ».

{{% alert color="primary" %}}
Le filtre des 10 premiers n’est efficace que lorsque le Tableau Croisé Dynamique contient un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n’existe aucune mesure agrégée permettant de classer les éléments, et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtrage des 10 premiers par l’intermédiaire de la méthode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)`. Le paramètre `valueFieldIndex` est l’index du champ de données dont les valeurs agrégées servent à classer les éléments, `filterType` sélectionne l’unité de `itemCount` (`PivotFilterType.COUNT` conserve un nombre fixe d’éléments, `PivotFilterType.PERCENT` conserve un pourcentage des éléments, de sorte que `itemCount` correspond lui-même au pourcentage), `isTop` indique s’il faut conserver les éléments les plus élevés (`true`) ou les plus bas (`false`), et `itemCount` définit le nombre d’éléments, ou le pourcentage, à conserver.
L’exemple suivant charge un classeur contenant un Tableau Croisé Dynamique qui possède un champ de valeur, applique un filtre des 10 premiers afin de ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le Tableau Croisé Dynamique et enregistre le classeur.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrage par masquage ou réaffichage des éléments du Tableau Croisé Dynamique**
En plus des API de filtrage structuré, Aspose.Cells permet de contrôler directement la visibilité de chaque élément du Tableau Croisé Dynamique. En parcourant la collection `PivotItems` d’un `PivotField` et en basculant la propriété `IsHidden`, vous pouvez masquer sélectivement des éléments spécifiques sans appliquer de filtre fondé sur une formule. L’affectation de `IsHidden = true` masque l’élément du Tableau Croisé Dynamique ; l’affectation de `IsHidden = false` l’affiche à nouveau et le rend visible.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à certains éléments, par exemple pour masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport donné. L’exemple ci-dessous charge un Tableau Croisé Dynamique, masque un élément spécifique par son nom, montre comment l’afficher à nouveau, actualise le Tableau Croisé Dynamique et enregistre le classeur.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Résumé**
Aspose.Cells for Java fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres par libellé, par date et par valeur couvrent les scénarios d’analyse les plus courants, tandis que le filtre des 10 premiers gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre une solution de repli flexible au niveau de l’élément. La combinaison de ces stratégies — par exemple, l’application d’un filtre par libellé suivie du masquage d’éléments spécifiques — permet de créer des rapports de Tableaux Croisés Dynamiques précisément ciblés entièrement à partir du code.

## Articles associés
- [Insérer un Tableau Croisé Dynamique](/cells/fr/java/create-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un Tableau Croisé Dynamique dans Aspose.Cells for Java](/cells/fr/java/pivot-table-add-row-and-column-fields/)
- [Ajouter des champs de filtre à un Tableau Croisé Dynamique dans Aspose.Cells for Java](/cells/fr/java/add-page-field-in-pivot-table/)
- [Gérer les champs de valeur d’un Tableau Croisé Dynamique dans Aspose.Cells for Java](/cells/fr/java/manage-value-fields/)
- [Actualiser les Tableaux Croisés Dynamiques et les caches de Tableau Croisé Dynamique dans Aspose.Cells for Java](/cells/fr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}