---
title: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for Node.js via Java prend en charge des fonctionnalités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d'un tableau croisé dynamique à l'aide de filtres d'étiquettes, de filtres de dates, de filtres de valeurs, de filtres des 10 premiers, et en masquant ou affichant des éléments individuels.
keywords: Aspose.Cells, bibliothèque Node.js via Java, feuille de calcul, tableau croisé dynamique, filtre, filtre d'étiquette, filtre de valeur, filtre de date, filtre des 10 premiers, élément de tableau croisé dynamique, masquer un élément
type: docs
weight: 10
url: /fr/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d'étiquettes aux champs de ligne ou de colonne textuels, utiliser des filtres de dates lorsque le champ ne contient que des cellules de type date-heure ou des cellules vides, appliquer des filtres de valeurs sur les nombres agrégés, utiliser des filtres des 10 premiers pour classer les données selon un champ de valeur, ou masquer et afficher manuellement des éléments individuels du tableau croisé dynamique à l'aide de la propriété `IsHidden`. Chaque stratégie est exposée par des API dédiées sur les classes `PivotField` et `PivotItem`.

{{% /alert %}}

## **Introduction**

Les tableaux croisés dynamiques sont des outils d'analyse puissants, mais les résumés bruts contiennent souvent beaucoup plus d'informations que ce dont vous avez besoin pour une présentation. Le filtrage est le principal mécanisme permettant de restreindre un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport spécifique. Aspose.Cells for Node.js via Java reproduit les capacités de filtrage disponibles dans Microsoft Excel, en les exposant par programmation afin que la génération de rapports puisse être entièrement automatisée.

Les stratégies de filtrage suivantes sont traitées dans cet article :

1. **Filtre d'étiquette** — filtre les éléments d'un champ de ligne ou de colonne en fonction de leurs étiquettes textuelles.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de type date-heure (ou des cellules vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d'un champ de données.
4. **Filtre des 10 premiers** — affiche uniquement les N premiers ou N derniers éléments classés selon un champ de valeur.
5. **Masquer / Afficher des éléments** — contrôle manuellement la visibilité de chaque élément individuel dans un champ.

Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après l'application de tout filtre, vous devez appeler `refreshData()` et `calculateData()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre d'étiquette**

Un filtre d'étiquette vous permet de filtrer les éléments d'un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cela est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre spécifique, contiennent un mot particulier ou correspondent à un autre critère basé sur le libellé.

Aspose.Cells expose le filtrage par étiquette via la méthode `PivotField.filterByLabel(PivotFilterType, string)`. L'énumération `PivotFilterType` inclut des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. Le second argument fournit la chaîne d'étiquette utilisée pour la comparaison.

L'exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d'étiquette afin que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Charger le classeur existant contenant un tableau croisé dynamique
let workbook = new AsposeCells.Workbook(fileName);

// Accéder à la feuille de calcul par index (première feuille)
let worksheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index
let pivotTable = worksheet.getPivotTables().get(0);

// Récupérer le premier PivotField de ligne
let rowField = pivotTable.getRowFields().get(0);

// Appliquer le filtre d'étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Actualiser et recalculer les données du tableau croisé dynamique pour que le filtre prenne effet
pivotTable.getPivotCache().refresh();

// Enregistrer le classeur sur le disque
workbook.save(fileName);
```

## **Filtre de date**

Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur les dates, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le trimestre suivant, ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement sur les champs stockant des informations de type date-heure.

{{% alert color="primary" %}}

Le filtre de date ne fonctionne que lorsque la zone de ligne ou de colonne contient uniquement des cellules de type date-heure ou des valeurs vides. Si le champ sous-jacent contient d'autres types de données, tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d'appliquer ce filtre.

{{% /alert %}}

Aspose.Cells expose le filtrage par date via la méthode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, et `Between`. Selon le type de filtre choisi, vous passez une ou deux valeurs `DateTime` (pour `Between`, vous passez les dates de début et de fin).

L'exemple suivant charge un classeur avec un tableau croisé dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui restreint les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// Charger le classeur existant qui contient le tableau croisé dynamique
var workbook = new AsposeCells.Workbook(inputPath);

// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
var worksheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index
var pivotTable = worksheet.getPivotTables().get(0);

// Récupérer le PivotField de date depuis la zone des lignes
// (Le filtre de date ne fonctionne que lorsque la zone des lignes/colonnes contient uniquement des cellules date-heure ou des cellules vides)
let dateField = pivotTable.getRowFields().get(0);

// Définir le critère de date pour le filtre Between
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// Appliquer le filtre de date sur le champ croisé dynamique
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
pivotTable.getPivotCache().refresh();

// Enregistrer le classeur
workbook.save(outputPath);
```

## **Filtre de valeur**

Les filtres de valeur opèrent sur les valeurs agrégées qu'un tableau croisé dynamique calcule dans sa zone de données. Au lieu de faire correspondre des étiquettes textuelles, ils comparent les totaux numériques à un seuil. Les cas d'utilisation typiques incluent l'affichage uniquement des produits dont la somme des ventes dépasse un montant cible, ou uniquement des régions dont le nombre de transactions se situe dans une plage.

Aspose.Cells expose le filtrage par valeur via la méthode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Le paramètre `filterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, et `ValueLessThanOrEqual`. Le paramètre `valueField` spécifie le champ de données à évaluer, et le ou les derniers arguments fournissent la ou les valeurs seuils.

L'exemple suivant charge un classeur avec un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// Trouver l'index du champ de données manuellement car PivotFieldCollection n'a pas de méthode IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```

## **Filtre des 10 premiers**

Le filtre des 10 premiers est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d'un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement, tels que « les 10 meilleurs produits par chiffre d'affaires » ou « les 5 pires régions par nombre de ventes ».

{{% alert color="primary" %}}

Le filtre des 10 premiers n'est efficace que lorsque le tableau croisé dynamique possède un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n'y a pas de mesure agrégée pour classer les éléments, et le filtre ne peut pas être appliqué.

{{% /alert %}}

Aspose.Cells expose le filtrage des 10 premiers via la méthode `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Le paramètre `itemCount` définit combien d'éléments conserver, `isTop` indique s'il faut conserver les éléments du haut (true) ou du bas (false), `valueField` référence le champ de données utilisé pour le classement, et `filterType` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`).

L'exemple suivant charge un classeur avec un tableau croisé dynamique contenant un champ de valeur, applique un filtre des 10 premiers pour ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (index 0)
let worksheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index
let pivotTable = worksheet.getPivotTables().get(0);

// Confirmer qu'il y a au moins un PivotField de valeur dans la zone de données
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);

// Récupérer le PivotField de ligne cible (le champ sur lequel nous voulons appliquer Top 10)
let rowField = pivotTable.getRowFields().get(0);

// Le premier (et seul) champ de données est à l'index 0 ; Top 10 classe selon lui.
let valueFieldIndex = 0;

// Appliquer le filtre Top 10 sur le champ de ligne :
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N ; false signifierait bottom N)
//   - valueFieldIndex = l'index du champ de données utilisé pour classer les éléments
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Actualiser les données du tableau croisé dynamique et les recalculer pour que le filtre prenne effet
pivotTable.getPivotCache().refresh();

// Enregistrer le classeur
workbook.save(outputPath);
```

## **Filtrage par masquage ou affichage d'éléments**

En plus des API de filtrage structuré, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d'un `PivotField` et en basculant la propriété `IsHidden`, vous pouvez supprimer sélectivement des éléments spécifiques sans appliquer de filtre basé sur une formule. Définir `IsHidden = true` masque l'élément du tableau croisé dynamique ; définir `IsHidden = false` l'affiche à nouveau et le rend visible.

Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, par exemple masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L'exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment l'afficher à nouveau, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
let sheet = workbook.getWorksheets().get(0);

// Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
let pivotTable = sheet.getPivotTables().get(0);

// Récupérer le PivotField cible (le premier champ d'étiquette de ligne dans lequel nous masquerons/afficherons des éléments)
let pivotField = pivotTable.getRowFields().get(0);

// Parcourir la collection PivotItems du PivotField sélectionné
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // Masquer les éléments du tableau croisé dynamique qui correspondent à un nom/critère spécifique
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // Démontrer le réaffichage : ré-afficher un élément précédemment masqué du tableau croisé dynamique
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
pivotTable.getPivotCache().refreshData();

// Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
// mais sont exclus de l'affichage du tableau croisé dynamique
workbook.save("output_pivot_filtered.xlsx");
```

## **Résumé**

Aspose.Cells for Node.js via Java fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres d'étiquette, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre des 10 premiers gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre une alternative flexible au niveau de l'élément. Combiner ces stratégies — par exemple, appliquer un filtre d'étiquette puis masquer des éléments spécifiques — vous permet de créer des rapports de tableau croisé dynamique ciblés avec précision entièrement à partir du code.
{{< app/cells/assistant language="nodejs-java" >}}