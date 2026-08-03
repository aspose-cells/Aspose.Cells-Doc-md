---
title: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for .NET prend en charge des fonctionnalités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d'un tableau croisé dynamique à l'aide de filtres d'étiquettes, de filtres de dates, de filtres de valeurs, de filtres des 10 premiers et en masquant ou affichant des éléments du tableau croisé dynamique.
keywords: Aspose.Cells, bibliothèque .NET, tableur, tableau croisé dynamique, filtre, filtre d'étiquette, filtre de valeur, filtre de date, filtre des 10 premiers, élément de tableau croisé dynamique, masquer un élément
type: docs
weight: 10
url: /fr/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d'étiquettes aux champs de lignes ou de colonnes textuels, utiliser des filtres de dates lorsque le champ ne contient que des cellules de type date-heure ou des cellules vides, appliquer des filtres de valeurs sur les nombres agrégés, utiliser les filtres des 10 premiers pour classer selon un champ de valeur, ou masquer et afficher manuellement des éléments individuels du tableau croisé dynamique à l'aide de la propriété `IsHidden`. Chaque stratégie est exposée via des API dédiées sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}
## **Introduction**
Les tableaux croisés dynamiques sont des outils d'analyse puissants, mais les résumés bruts contiennent souvent beaucoup plus d'informations que ce dont vous avez besoin pour une présentation. Le filtrage est le principal mécanisme permettant de restreindre un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport spécifique. Aspose.Cells for .NET reproduit les fonctionnalités de filtrage disponibles dans Microsoft Excel, en les exposant par programmation afin que la génération de rapports puisse être entièrement automatisée.
Les stratégies de filtrage suivantes sont abordées dans cet article :
1. **Filtre d'étiquette** — filtre les éléments des champs de lignes ou de colonnes en fonction de leurs étiquettes textuelles.
2. **Filtre de date** — filtre les champs de lignes ou de colonnes qui contiennent uniquement des valeurs de type date-heure (ou des cellules vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d'un champ de données.
4. **Filtre des 10 premiers** — affiche uniquement les N éléments les plus élevés ou les plus bas, classés selon un champ de valeur.
5. **Masquer / Afficher des éléments du tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément individuel d'un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après avoir appliqué un filtre, vous devez appeler `PivotCache.Refresh()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.
## **Filtre d'étiquette**
Un filtre d'étiquette vous permet de filtrer les éléments d'un champ de ligne ou de colonne en comparant leurs légendes textuelles à un modèle. Cela est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre spécifique, contiennent un mot particulier ou correspondent à un autre critère basé sur la légende.
Aspose.Cells expose le filtrage par étiquette via la méthode `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. L'argument `filterType` sélectionne le mode de comparaison (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc.). Les arguments `label1` et `label2` fournissent le texte de comparaison — passez `string.Empty` pour `label2` lorsque vous n'avez besoin que d'une correspondance sur une seule valeur, par exemple « commence par » ou « contient ».
L'exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d'étiquette afin que seuls les éléments dont les légendes commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// Charger le classeur existant contenant un tableau croisé dynamique
Workbook workbook = new Workbook(fileName);

// Accéder à la feuille de calcul par index (première feuille de calcul)
Worksheet worksheet = workbook.Worksheets[0];

// Accéder au tableau croisé dynamique par index
PivotTable pivotTable = worksheet.PivotTables[0];

// Récupérer le premier PivotField de ligne
PivotField rowField = pivotTable.RowFields[0];

// Appliquer le filtre d'étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// Actualiser et recalculer les données du tableau croisé dynamique pour que le filtre prenne effet
pivotTable.PivotCache.Refresh();

// Enregistrer le classeur sur le disque
workbook.Save(fileName);
```
## **Filtre de date**
Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur les dates, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le prochain trimestre ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement sur les champs stockant des informations de type date-heure.
{{% alert color="primary" %}}
Le filtre de date ne fonctionne que lorsque la zone de lignes ou de colonnes contient uniquement des cellules de type date-heure ou des cellules vides. Si le champ sous-jacent contient d'autres types de données tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d'appliquer ce filtre.
{{% /alert %}}
Aspose.Cells expose le filtrage par date via la méthode `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous passez une ou deux valeurs `DateTime` (pour `Between`, vous passez les dates de début et de fin).
L'exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de lignes contient un champ de date, applique un filtre de date qui limite les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";

if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}

// Charger le classeur existant qui contient le tableau croisé dynamique
var workbook = new Workbook(inputPath);

// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
var worksheet = workbook.Worksheets[0];

// Accéder au tableau croisé dynamique par index
var pivotTable = worksheet.PivotTables[0];

// Récupérer le PivotField de date depuis la zone des lignes
// (Le filtre de date ne fonctionne que lorsque la zone ligne/colonne contient uniquement des cellules date-heure ou des cellules vides)
PivotField dateField = pivotTable.RowFields[0];

// Définir le critère de date pour le filtre Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Appliquer le filtre de date sur le champ pivot
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
pivotTable.PivotCache.Refresh();

// Enregistrer le classeur
workbook.Save(outputPath);
```
## **Filtre de valeur**
Les filtres de valeur opèrent sur les valeurs agrégées qu'un tableau croisé dynamique calcule dans sa zone de données. Au lieu de comparer des étiquettes textuelles, ils comparent des totaux numériques à un seuil. Les cas d'utilisation typiques consistent à afficher uniquement les produits dont la somme des ventes dépasse un montant cible, ou uniquement les régions dont le nombre de transactions se situe dans une plage.
Aspose.Cells expose le filtrage par valeur via la méthode `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Le paramètre `valueFieldIndex` indique le champ de données à évaluer ; déterminez sa position avec `pivotTable.DataFields.IndexOf(dataField)` ou en parcourant la collection. Le paramètre `filterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Les deux arguments `double` fournissent la ou les valeurs seuils.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.
```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// Trouver l'index du champ de données manuellement car PivotFieldCollection n'a pas IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}

pivotTable.PivotCache.Refresh();

workbook.Save("output.xlsx");
```
## **Filtre des 10 premiers**
Le filtre des 10 premiers est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d'un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement tels que « les 10 meilleurs produits par chiffre d'affaires » ou « les 5 pires régions par nombre de ventes ».
{{% alert color="primary" %}}
Le filtre des 10 premiers n'est efficace que lorsque le tableau croisé dynamique possède un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n'y a aucune mesure agrégée permettant de classer les éléments, et le filtre ne peut pas être appliqué.
{{% /alert %}}
Aspose.Cells expose le filtrage des 10 premiers via la méthode `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`. Le paramètre `itemCount` définit le nombre d'éléments à conserver, `filterType` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`), `isTop` indique s'il faut conserver les éléments supérieurs (`true`) ou inférieurs (`false`), et `valueFieldIndex` est l'index du champ de données utilisé pour classer les éléments.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique qui contient un champ de valeur, applique un filtre des 10 premiers pour ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Charger le classeur existant qui contient le tableau croisé dynamique
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (index 0)
Worksheet worksheet = workbook.Worksheets[0];

// Accéder au tableau croisé dynamique par index
PivotTable pivotTable = worksheet.PivotTables[0];

// Vérifier qu'il y a au moins un PivotField de valeur dans la zone de données
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// Récupérer le PivotField de ligne cible (le champ auquel nous voulons appliquer Top 10)
PivotField rowField = pivotTable.RowFields[0];

// Le premier (et unique) champ de données est à l'index 0 ; Top 10 classe par celui-ci.
int valueFieldIndex = 0;

// Appliquer le filtre Top 10 sur le champ de ligne :
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N ; false signifierait bottom N)
//   - valueFieldIndex = l'index du champ de données utilisé pour classer les éléments
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// Actualiser les données du tableau croisé dynamique et le recalculer pour que le filtre prenne effet
pivotTable.PivotCache.Refresh();

// Enregistrer le classeur
workbook.Save(outputPath);
```
## **Filtrage en masquant ou affichant des éléments du tableau croisé dynamique**
En plus des API de filtrage structurées, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d'un `PivotField` et en basculant la propriété `IsHidden`, vous pouvez supprimer sélectivement des éléments spécifiques sans appliquer un filtre basé sur une formule. Définir `IsHidden = true` masque l'élément dans le tableau croisé dynamique ; définir `IsHidden = false` l'affiche à nouveau et le rend visible.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, comme le masquage d'un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L'exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment l'afficher à nouveau, actualise le tableau croisé dynamique et enregistre le classeur.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Charger un classeur existant contenant un tableau croisé dynamique
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
Worksheet sheet = workbook.Worksheets[0];

// Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
PivotTable pivotTable = sheet.PivotTables[0];

// Récupérer le PivotField cible (le premier champ d'étiquette de ligne dans lequel nous masquerons/afficherons des éléments)
PivotField pivotField = pivotTable.RowFields[0];

// Parcourir la collection PivotItems du PivotField sélectionné
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // Masquer les éléments du tableau croisé dynamique qui correspondent à un nom/un critère spécifique
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // Démontrer l'affichage : ré-afficher un élément précédemment masqué du tableau croisé dynamique
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
pivotTable.PivotCache.Refresh();

// Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
// mais sont exclus de l'affichage du tableau croisé dynamique en sortie
workbook.Save("output_pivot_filtered.xlsx");
```
## **Résumé**
Aspose.Cells for .NET fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres d'étiquettes, de dates et de valeurs couvrent les scénarios analytiques les plus courants, tandis que le filtre des 10 premiers gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre une alternative flexible au niveau de l'élément. La combinaison de ces stratégies — par exemple, l'application d'un filtre d'étiquette suivie du masquage d'éléments spécifiques — vous permet de créer des rapports de tableaux croisés dynamiques précisément ciblés entièrement à partir du code.
{{< app/cells/assistant language="csharp" >}}