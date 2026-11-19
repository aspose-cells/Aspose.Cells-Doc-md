---
title: Filtrage des tableaux croisés dynamiques par libellé ou par valeur
linktitle: Filtrage des tableaux croisés dynamiques par libellé ou par valeur
description: Aspose.Cells for C++ prend en charge des fonctionnalités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d’un tableau croisé dynamique à l’aide de filtres par libellé, de filtres par date, de filtres par valeur et de filtres Top 10, ainsi que comment masquer ou réafficher des éléments de tableau croisé dynamique.
keywords: Aspose.Cells, bibliothèque C++, tableur, tableau croisé dynamique, filtre, filtre par libellé, filtre par valeur, filtre par date, filtre Top 10, élément de tableau croisé dynamique, masquage d’un élément de tableau croisé dynamique
type: docs
weight: 10
url: /fr/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose cinq stratégies pratiques de filtrage des données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres par libellé aux champs de ligne ou de colonne contenant du texte, utiliser des filtres par date lorsque le champ contient uniquement des cellules contenant des dates et des heures ou des cellules vides, appliquer des filtres par valeur aux valeurs numériques agrégées, utiliser des filtres Top 10 pour classer les éléments selon un champ de valeur, ou masquer et réafficher manuellement des éléments individuels du tableau croisé dynamique à l’aide de la propriété `IsHidden`. Chaque stratégie est accessible par des API dédiées sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les tableaux croisés dynamiques sont de puissants outils d’analyse, mais les synthèses brutes contiennent souvent davantage d’informations que nécessaire pour un rapport donné. Le filtrage constitue le principal mécanisme permettant de restreindre un tableau croisé dynamique aux lignes, aux colonnes ou aux valeurs utiles à un rapport donné. Aspose.Cells for C++ reprend les fonctionnalités de filtrage disponibles dans Microsoft Excel et les expose de manière programmatique, ce qui permet d’automatiser entièrement la génération des rapports.
Les stratégies de filtrage suivantes sont abordées dans cet article :
1. **Filtre par libellé** — filtre les éléments d’un champ de ligne ou de colonne en fonction de leurs libellés textuels.
2. **Filtre par date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de date et d’heure (ou des cellules vides).
3. **Filtre par valeur** — filtre les éléments en fonction des valeurs agrégées d’un champ de données.
4. **Filtre Top 10** — affiche uniquement les N éléments en tête ou en fin de classement selon un champ de valeur.
5. **Masquage / réaffichage d’éléments de tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément individuel d’un champ.
Chaque approche recourt à une méthode différente définie sur la classe `PivotField` ou à une propriété de la classe `PivotItem`. Après avoir appliqué un filtre, vous devez appeler `GetPivotCache().Refresh()` sur le tableau croisé dynamique afin que les données en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre par libellé**
Un filtre par libellé permet de filtrer les éléments d’un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cette fonctionnalité est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre donnée, contiennent un mot particulier ou respectent un autre critère fondé sur les libellés.
Aspose.Cells expose le filtrage par libellé au moyen de la méthode `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. L’énumération `PivotFilterType` comprend des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank` et `CaptionIsBlank`, ainsi que d’autres valeurs. Le second argument fournit la chaîne de libellé à comparer.
L’exemple ci-dessous charge un classeur contenant un tableau croisé dynamique déjà présent, applique un filtre par libellé de sorte que seuls les éléments dont les libellés commencent par le préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtre par date**
Les filtres par date permettent de filtrer un tableau croisé dynamique selon des critères fondés sur les dates, tels qu’aujourd’hui, la semaine dernière, ce mois-ci, le prochain trimestre ou une plage de dates spécifique. Ce sont des filtres spécialisés qui ne s’appliquent qu’aux champs stockant des informations de date et d’heure.

{{% alert color="primary" %}}
Le filtre par date ne fonctionne que si la zone des lignes ou des colonnes contient uniquement des cellules contenant des dates et des heures ou des valeurs vides. Si le champ sous-jacent contient d’autres types de données, tels que des nombres ou du texte, le filtre par date ne produira pas le résultat attendu. Vérifiez que le champ est mis en forme comme une date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d’appliquer ce filtre.
Aspose.Cells expose le filtrage par date au moyen de la méthode `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. L’énumération `PivotFilterType` contient des valeurs spécifiques aux dates telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre sélectionné, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, vous transmettez la date de début et la date de fin).
L’exemple ci-dessous charge un classeur dont la zone des lignes du tableau croisé dynamique contient un champ de date, applique un filtre par date qui limite les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtre par valeur**
Les filtres par valeur portent sur les valeurs agrégées qu’un tableau croisé dynamique calcule dans sa zone de données. Contrairement aux filtres par libellé, ils comparent des totaux numériques à un seuil. Parmi les cas d’utilisation courants figurent l’affichage des seuls produits dont la somme des ventes dépasse un montant cible, ou des seules régions dont le nombre de transactions se situe dans une plage donnée.
Aspose.Cells expose le filtrage par valeur au moyen de la méthode `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Le paramètre `filterType` peut prendre des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Le paramètre `valueField` indique le champ de données à évaluer, tandis que les arguments finaux fournissent la ou les valeurs de seuil.
L’exemple ci-dessous charge un classeur contenant un tableau croisé dynamique, applique un filtre par valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtre Top 10**
Le filtre Top 10 est une forme spécialisée de filtre par valeur qui ne conserve que les N éléments dont la valeur est la plus élevée ou la plus faible, selon le champ de valeur choisi. Il est couramment utilisé pour établir des classements tels que « 10 premiers produits par chiffre d’affaires » ou « 5 régions les moins bien classées par nombre de ventes ».

{{% alert color="primary" %}}
Le filtre Top 10 n’est efficace que si le tableau croisé dynamique contient un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n’existe aucune mesure agrégée permettant de classer les éléments et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtre Top 10 au moyen de la méthode `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`. Le paramètre `valueFieldIndex` est l’index du champ de données dont les valeurs agrégées déterminent le classement des éléments, `type` sélectionne l’unité d’expression de `itemCount` (`PivotFilterType::Count` conserve un nombre fixe d’éléments, tandis que `PivotFilterType::Percent` conserve un pourcentage des éléments ; dans ce cas, `itemCount` correspond directement au pourcentage), `isTop` indique s’il faut conserver les éléments en tête de classement (`true`) ou en bas de classement (`false`), et `itemCount` définit le nombre d’éléments ou le pourcentage à conserver.
L’exemple ci-dessous charge un classeur contenant un tableau croisé dynamique avec un champ de valeur, applique un filtre Top 10 pour ne conserver que les 10 éléments dont la somme des ventes est la plus élevée, actualise le tableau croisé dynamique et enregistre le classeur.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrage par masquage ou réaffichage d’éléments de tableau croisé dynamique**
Outre les API de filtrage structuré, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d’un `PivotField` et en modifiant la valeur de la propriété `IsHidden`, vous pouvez masquer sélectivement des éléments spécifiques sans appliquer de filtre fondé sur une formule. La définition de `IsHidden = true` masque l’élément du tableau croisé dynamique ; celle de `IsHidden = false` l’affiche à nouveau.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou propre à un élément, par exemple pour masquer quelques catégories nommées qui ne doivent pas apparaître dans un rapport donné. L’exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment le réafficher, actualise le tableau croisé dynamique et enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Résumé**
Aspose.Cells for C++ fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres par libellé, par date et par valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre Top 10 permet de gérer les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre une solution de repli flexible, au niveau de chaque élément. Combiner ces stratégies — par exemple, appliquer un filtre par libellé, puis masquer des éléments spécifiques — vous permet de créer entièrement par code des rapports de tableau croisé dynamique ciblés avec précision.

## Articles connexes
- [Insérer un tableau croisé dynamique](/cells/fr/cpp/create-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for C++](/cells/fr/cpp/pivot-table-add-row-and-column-fields/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for C++](/cells/fr/cpp/add-page-field-in-pivot-table/)
- [Gérer les champs de valeur d’un tableau croisé dynamique dans Aspose.Cells for C++](/cells/fr/cpp/manage-value-fields/)
- [Actualiser les tableaux croisés dynamiques et les caches de tableau croisé dynamique dans Aspose.Cells for C++](/cells/fr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}