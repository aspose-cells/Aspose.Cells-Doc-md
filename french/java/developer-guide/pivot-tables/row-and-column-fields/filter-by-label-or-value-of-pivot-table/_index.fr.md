---
title: Filtrer les tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrer les tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for Java prend en charge des fonctionnalités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d'un tableau croisé dynamique à l'aide de filtres d'étiquettes, de filtres de dates, de filtres de valeurs, de filtres Top 10, ainsi qu'en masquant ou en affichant des éléments individuels.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, tableau croisé dynamique, filtre, filtre d'étiquette, filtre de valeur, filtre de date, filtre Top 10, élément de tableau croisé dynamique, masquer un élément
type: docs
weight: 10
url: /fr/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d'étiquettes aux champs de lignes ou de colonnes textuels, utiliser des filtres de dates lorsque le champ contient uniquement des cellules de type date-heure ou des cellules vides, appliquer des filtres de valeurs sur des nombres agrégés, utiliser des filtres Top 10 pour classer par champ de valeur, ou masquer et afficher manuellement des éléments individuels du tableau croisé dynamique à l'aide de la propriété `IsHidden`. Chaque stratégie est exposée via des API dédiées sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}
## **Introduction**
Les tableaux croisés dynamiques sont des outils d'analyse puissants, mais les résumés bruts contiennent souvent beaucoup plus d'informations qu'il n'est nécessaire de présenter. Le filtrage est le principal mécanisme permettant de réduire un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport spécifique. Aspose.Cells for Java reproduit les fonctionnalités de filtrage disponibles dans Microsoft Excel, en les exposant par programmation afin que la génération de rapports puisse être entièrement automatisée.
Les stratégies de filtrage suivantes sont couvertes dans cet article :
1. **Filtre d'étiquette** — filtre les éléments d'un champ de ligne ou de colonne en fonction de leurs étiquettes textuelles.
2. **Filtre de date** — filtre les champs de lignes ou de colonnes qui contiennent uniquement des valeurs de type date-heure (ou des cellules vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d'un champ de données.
4. **Filtre Top 10** — affiche uniquement les N éléments supérieurs ou inférieurs classés selon un champ de valeur.
5. **Masquer / Afficher des éléments du tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément individuel d'un champ.
Chaque approche utilise une méthode différente sur la classe `PivotField` ou une propriété sur la classe `PivotItem`. Après avoir appliqué un filtre, vous devez appeler `refreshData()` et `calculateData()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.
## **Filtre d'étiquette**
Un filtre d'étiquette permet de filtrer les éléments d'un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cela est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre spécifique, contiennent un mot particulier ou correspondent à un autre critère basé sur le libellé.
Aspose.Cells expose le filtrage par étiquette via la méthode `PivotField.filterByLabel(PivotFilterType, String)`. L'énumération `PivotFilterType` inclut des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. Le second argument fournit la chaîne d'étiquette utilisée pour la comparaison.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d'étiquette afin que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.
```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// Charger le classeur existant contenant un tableau croisé dynamique
Workbook workbook = new Workbook(fileName);

// Accéder à la feuille de calcul par index (première feuille de calcul)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Récupérer le premier PivotField de ligne
PivotField rowField = pivotTable.getRowFields().get(0);

// Appliquer le filtre d'étiquette - afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// Actualiser et recalculer les données du tableau croisé dynamique pour que le filtre prenne effet
pivotTable.refreshData();

// Enregistrer le classeur sur le disque
workbook.save(fileName);
```
## **Filtre de date**
Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur les dates, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le trimestre suivant ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement sur des champs stockant des informations de type date-heure.
{{% alert color="primary" %}}
Le filtre de date fonctionne uniquement lorsque la zone de lignes ou de colonnes contient exclusivement des cellules de type date-heure ou des cellules vides. Si le champ sous-jacent contient d'autres types de données tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d'appliquer ce filtre.
{{% /alert %}}
Aspose.Cells expose le filtrage par date via la méthode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, vous transmettez les dates de début et de fin).
L'exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de lignes contient un champ de date, applique un filtre de date qui limite les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// Charger le classeur existant qui contient le tableau croisé dynamique
Workbook workbook = new Workbook(inputPath);

// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Récupérer le PivotField de date depuis la zone des lignes
// (Le filtre de date ne fonctionne que lorsque la zone ligne/colonne contient uniquement des cellules date-heure ou des cellules vides)
PivotField dateField = pivotTable.getRowFields().get(0);

// Définir le critère de date pour le filtre Entre
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Appliquer le filtre de date sur le champ croisé dynamique
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
pivotTable.refreshData();

// Enregistrer le classeur
workbook.save(outputPath);
```
## **Filtre de valeur**
Les filtres de valeur opèrent sur les valeurs agrégées qu'un tableau croisé dynamique calcule dans sa zone de données. Au lieu de faire correspondre des étiquettes textuelles, ils comparent des totaux numériques à un seuil. Les cas d'utilisation typiques incluent l'affichage uniquement des produits dont la somme des ventes dépasse un montant cible ou uniquement des régions dont le nombre de transactions se situe dans une plage.
Aspose.Cells expose le filtrage par valeur via la méthode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Le paramètre `filterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Le paramètre `valueField` spécifie quel champ de données doit être évalué, et le ou les derniers arguments fournissent la ou les valeurs seuils.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// Trouver manuellement l'index du champ de données car PivotFieldCollection n'a pas de IndexOf
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

pivotTable.refreshData();

workbook.save("output.xlsx");
```
## **Filtre Top 10**
Le filtre Top 10 est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d'un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement tels que « les 10 produits par chiffre d'affaires » ou « les 5 régions les moins performantes par nombre de ventes ».
{{% alert color="primary" %}}
Le filtre Top 10 n'est efficace que lorsque le tableau croisé dynamique comporte un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n'existe aucune mesure agrégée permettant de classer les éléments, et le filtre ne peut pas être appliqué.
{{% /alert %}}
Aspose.Cells expose le filtrage Top 10 via la méthode `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. Le paramètre `itemCount` définit combien d'éléments conserver, `isTop` indique s'il faut conserver les éléments supérieurs (true) ou inférieurs (false), `valueField` référence le champ de données utilisé pour le classement, et `filterType` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`).
L'exemple suivant charge un classeur contenant un tableau croisé dynamique qui contient un champ de valeur, applique un filtre Top 10 pour ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.
```java
import com.aspose.cells.*;

// Charger le classeur existant qui contient le tableau croisé dynamique
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Vérifier qu'il y a au moins un PivotField de valeur dans la zone de données
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// Récupérer le PivotField de ligne cible (le champ auquel nous voulons appliquer Top 10)
PivotField rowField = pivotTable.getRowFields().get(0);

// Le premier (et seul) champ de données est à l'index 0 ; Top 10 classe selon celui-ci.
int valueFieldIndex = 0;

// Appliquer le filtre Top 10 sur le champ de ligne :
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (N premiers ; false signifierait N derniers)
//   - valueFieldIndex = l'index du champ de données utilisé pour classer les éléments
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// Actualiser les données du tableau croisé dynamique et le recalculer pour que le filtre prenne effet
pivotTable.refreshData();

// Enregistrer le classeur
workbook.save(outputPath);
```
## **Filtrer en masquant ou en affichant des éléments du tableau croisé dynamique**
En plus des API de filtrage structuré, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d'un `PivotField` et en activant la propriété `IsHidden`, vous pouvez supprimer sélectivement des éléments spécifiques sans appliquer de filtre basé sur une formule. Définir `IsHidden = true` masque l'élément dans le tableau croisé dynamique ; définir `IsHidden = false` l'affiche à nouveau et le rend visible.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, comme masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L'exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment l'afficher à nouveau, actualise le tableau croisé dynamique et enregistre le classeur.
```java
import com.aspose.cells.*;

// Charger un classeur existant contenant un tableau croisé dynamique
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
Worksheet sheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// Récupérer le PivotField cible (le premier champ d'étiquette de ligne dans lequel nous masquerons/affichons des éléments)
PivotField pivotField = pivotTable.getRowFields().get(0);

// Parcourir la collection PivotItems du PivotField sélectionné
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // Masquer les éléments du tableau croisé dynamique qui correspondent à un nom/critère spécifique
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // Démontrer l'affichage : ré-afficher un élément précédemment masqué du tableau croisé dynamique
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
pivotTable.refreshData();

// Enregistrer le classeur - les éléments masqués restent dans les données sous-jacentes
// mais sont exclus de l'affichage du tableau croisé dynamique en sortie
workbook.save("output_pivot_filtered.xlsx");
```
## **Résumé**
Aspose.Cells for Java fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres d'étiquette, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre Top 10 gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre un mécanisme flexible au niveau de l'élément. Combiner ces stratégies — par exemple, appliquer un filtre d'étiquette puis masquer des éléments spécifiques — permet de construire des rapports de tableaux croisés dynamiques précisément ciblés entièrement à partir du code.
{{< app/cells/assistant language="java" >}}