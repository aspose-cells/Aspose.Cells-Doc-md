---
title: Filtrage des tableaux croisés dynamiques par libellé ou par valeur
linktitle: Filtrage des tableaux croisés dynamiques par libellé ou par valeur
description: Aspose.Cells for Node.js via C++ prend en charge une gamme complète de filtres pour les tableaux croisés dynamiques. Cet article explique comment filtrer les données d’un tableau croisé dynamique à l’aide de filtres de libellé, de date, de valeur et top 10, ainsi que comment masquer ou réafficher ses éléments.
keywords: Aspose.Cells, bibliothèque Node.js via C++, feuille de calcul, tableau croisé dynamique, filtre, filtre de libellé, filtre de valeur, filtre de date, filtre top 10, élément de tableau croisé dynamique, masquage d’un élément de tableau croisé dynamique
type: docs
weight: 10
url: /fr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres de libellé aux champs de ligne ou de colonne contenant du texte, utiliser des filtres de date lorsque le champ contient uniquement des cellules contenant des dates et des heures ou des cellules vides, appliquer des filtres de valeur aux valeurs numériques agrégées, utiliser des filtres top 10 pour classer les éléments selon un champ de valeur, ou masquer et réafficher manuellement des éléments de tableau croisé dynamique à l’aide de la propriété `IsHidden`. Chaque stratégie est disponible via les API dédiées des classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les tableaux croisés dynamiques sont de puissants outils d’analyse, mais les synthèses brutes contiennent souvent bien plus d’informations qu’il n’est nécessaire d’en présenter. Le filtrage est le principal mécanisme permettant de limiter un tableau croisé dynamique aux lignes, aux colonnes ou aux valeurs pertinentes pour un rapport donné. Aspose.Cells for Node.js via C++ reproduit les capacités de filtrage disponibles dans Microsoft Excel et les expose de manière programmatique afin d’automatiser entièrement la génération de rapports.
Les stratégies de filtrage suivantes sont abordées dans cet article :
1. **Filtre de libellé** — filtre les éléments d’un champ de ligne ou de colonne en fonction de leurs libellés.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de date et d’heure ou des valeurs vides.
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d’un champ de données.
4. **Filtre top 10** — affiche uniquement les N éléments les plus élevés ou les plus bas, classés selon un champ de valeur.
5. **Masquage / réaffichage des éléments d’un tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément dans un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après l’application de n’importe quel filtre, vous devez appeler `refreshData()` et `calculateData()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre de libellé**
Un filtre de libellé permet de filtrer les éléments d’un champ de ligne ou de colonne en comparant leurs libellés à un motif. Cette méthode est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre donnée, contiennent un mot particulier ou satisfont à un autre critère fondé sur le libellé.
Aspose.Cells expose le filtrage par libellé au moyen de la méthode `PivotField.filterByLabel(PivotFilterType, string)`. L’énumération `PivotFilterType` comprend notamment des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank` et `CaptionIsBlank`. Le deuxième argument fournit la chaîne de libellé utilisée pour la comparaison.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre de libellé de sorte que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

```javascript
const AsposeCells = require("aspose.cells.node");
let fileName = "sample.xlsx";
let prefix = "B";
// Charger le classeur existant contenant un tableau croisé dynamique
let workbook = new AsposeCells.Workbook(fileName);
// Accéder à la feuille de calcul par index (première feuille)
let worksheet = workbook.getWorksheets().get(0);
// Accéder au tableau croisé dynamique par index
let pivotTable = worksheet.getPivotTables().get(0);
// Récupérer le premier champ de ligne
let rowField = pivotTable.getRowFields().get(0);
// Appliquer le filtre d’étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");
// Actualiser et recalculer les données du tableau croisé dynamique afin que le filtre prenne effet
pivotTable.getPivotCache().refresh();
// Enregistrer le classeur sur le disque
workbook.save(fileName);
```

## **Filtre de date**
Les filtres de date permettent de limiter un tableau croisé dynamique à l’aide de critères fondés sur des dates, tels qu’aujourd’hui, la semaine dernière, ce mois-ci, le trimestre suivant ou une plage de dates spécifique. Il s’agit de filtres spécialisés qui ne s’appliquent qu’aux champs stockant des informations de date et d’heure.

{{% alert color="primary" %}}
Le filtre de date ne fonctionne que si la zone des lignes ou des colonnes contient uniquement des cellules contenant des dates et des heures ou des cellules vides. Si le champ source contient d’autres types de données, tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Vérifiez que le champ est formaté comme une date et que toutes les valeurs sont des instances `DateTime` valides ou que les cellules correspondantes sont vides avant d’appliquer ce filtre.
Aspose.Cells expose le filtrage par date au moyen de la méthode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L’énumération `PivotFilterType` contient des valeurs dédiées aux dates telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, vous transmettez les dates de début et de fin).
L’exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui limite les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}
// Charger le classeur existant qui contient le tableau croisé dynamique
const workbook = new AsposeCells.Workbook(inputPath);
// Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
const worksheet = workbook.getWorksheets().get(0);
// Accéder au tableau croisé dynamique par index
const pivotTable = worksheet.getPivotTables().get(0);
// Récupérer le champ PivotField de date de la zone de lignes
// (Le filtre de date fonctionne uniquement lorsque la zone de lignes/colonnes contient uniquement des cellules de date-heure ou des cellules vides)
const dateField = pivotTable.getRowFields().get(0);
// Définir le critère de date pour le filtre Entre
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);
// Appliquer le filtre de date au champ du tableau croisé dynamique
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
// Actualiser et recalculer le tableau croisé dynamique afin que le filtre soit effectif
pivotTable.getPivotCache().refresh();
// Enregistrer le classeur
workbook.save(outputPath);
```

## **Filtre de valeur**
Les filtres de valeur agissent sur les valeurs agrégées qu’un tableau croisé dynamique calcule dans sa zone de données. Au lieu de comparer des libellés, ils comparent des totaux numériques à un seuil. Les scénarios courants comprennent l’affichage des seuls produits dont la somme des ventes dépasse un montant cible ou des seules régions dont le nombre de transactions est compris dans une plage.
Aspose.Cells expose le filtrage par valeur au moyen de la méthode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Le paramètre `filterType` peut prendre des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Le paramètre `valueField` spécifie le champ de données à évaluer, et le ou les derniers arguments fournissent la ou les valeurs de seuil.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
const AsposeCells = require("aspose.cells.node");
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Filtre top 10**
Le filtre top 10 est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d’un champ de valeur choisi. Il est couramment utilisé pour établir des rapports de classement tels que « 10 principaux produits par chiffre d’affaires » ou « 5 régions ayant le nombre de transactions le plus faible ».

{{% alert color="primary" %}}
Le filtre top 10 n’est efficace que si le tableau croisé dynamique contient un ou plusieurs champs de valeur dans la zone de données. En l’absence d’au moins un champ de valeur, aucune mesure agrégée ne permet de classer les éléments et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtrage top 10 au moyen de la méthode `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Le paramètre `itemCount` définit le nombre d’éléments à conserver, `isTop` indique s’il faut conserver les éléments les plus élevés (true) ou les plus bas (false), `valueField` désigne le champ de données utilisé pour le classement et `filterType` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`).
L’exemple suivant charge un classeur contenant un tableau croisé dynamique avec un champ de valeur, applique un filtre top 10 afin de ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Load the existing workbook that contains the pivot table
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
const rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
const valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Sum, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrage par masquage ou réaffichage des éléments d’un tableau croisé dynamique**
Outre les API de filtrage, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément d’un tableau croisé dynamique. En parcourant la collection `PivotItems` d’un `PivotField` et en basculant la propriété `IsHidden`, vous pouvez masquer sélectivement certains éléments sans appliquer de filtre fondé sur une formule. Définir `IsHidden = true` masque l’élément du tableau croisé dynamique ; définir `IsHidden = false` le réaffiche et le rend à nouveau visible.
Cette méthode est utile lorsque la règle de filtrage est irrégulière ou spécifique à certains éléments, par exemple pour masquer quelques catégories désignées par leur nom qui ne doivent pas apparaître dans un rapport particulier. L’exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment le réafficher, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
const AsposeCells = require("aspose.cells.node");
// Charger un classeur existant contenant un tableau croisé dynamique
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
const sheet = workbook.getWorksheets().get(0);
// Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
const pivotTable = sheet.getPivotTables().get(0);
// Récupérer le champ PivotField cible (le premier champ de ligne dont nous masquerons ou afficherons des éléments)
const pivotField = pivotTable.getRowFields().get(0);
// Parcourir la collection PivotItems du PivotField sélectionné
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);
    // Masquer les éléments du tableau croisé dynamique correspondant à un nom ou critère spécifique
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }
    // Démontrer comment afficher de nouveau un élément du tableau croisé dynamique précédemment masqué
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}
// Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
pivotTable.getPivotCache().refresh();
// Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
// mais sont exclus du résultat affiché du tableau croisé dynamique
workbook.save("output_pivot_filtered.xlsx");
```

## **Résumé**
Aspose.Cells for Node.js via C++ fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres de libellé, de date et de valeur couvrent les scénarios d’analyse les plus courants, tandis que le filtre top 10 permet d’établir des classements. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre une solution de repli flexible, au niveau de chaque élément. La combinaison de ces stratégies — par exemple, l’application d’un filtre de libellé suivie du masquage de certains éléments — permet de créer, entièrement à l’aide de code, des rapports de tableaux croisés dynamiques ciblés avec précision.

## Articles connexes
- [Insérer un tableau croisé dynamique](/cells/fr/nodejs-cpp/create-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Gérer les champs de valeur d’un tableau croisé dynamique dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/manage-value-fields/)
- [Actualiser les tableaux croisés dynamiques et leurs caches dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}