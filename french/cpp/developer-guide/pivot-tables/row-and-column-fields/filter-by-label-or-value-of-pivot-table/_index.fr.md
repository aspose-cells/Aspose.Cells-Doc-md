---
title: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for C++ offre des capacités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d'un tableau croisé dynamique à l'aide de filtres d'étiquettes, de filtres de dates, de filtres de valeurs, de filtres des 10 premiers, et en masquant ou affichant des éléments dynamiques.
keywords: Aspose.Cells, bibliothèque C++, tableur, tableau croisé dynamique, filtre, filtre d'étiquette, filtre de valeur, filtre de date, filtre des 10 premiers, élément dynamique, masquer élément dynamique
type: docs
weight: 10
url: /fr/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d'étiquettes aux champs de ligne ou de colonne textuels, utiliser des filtres de dates lorsque le champ ne contient que des cellules de type date-heure ou des cellules vides, appliquer des filtres de valeurs sur les nombres agrégés, utiliser des filtres des 10 premiers pour classer selon un champ de valeur, ou encore masquer et afficher manuellement des éléments dynamiques individuels à l'aide de la propriété `IsHidden`. Chaque stratégie est exposée via des API dédiées sur les classes `PivotField` et `PivotItem`.

{{% /alert %}}

## **Introduction**

Les tableaux croisés dynamiques sont des outils d'analyse puissants, mais les résumés bruts contiennent souvent bien plus d'informations que ce dont vous avez besoin pour une présentation. Le filtrage est le principal mécanisme permettant de restreindre un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport spécifique. Aspose.Cells for C++ reproduit les capacités de filtrage disponibles dans Microsoft Excel, en les exposant par programmation afin que la génération de rapports puisse être entièrement automatisée.

Les stratégies de filtrage suivantes sont traitées dans cet article :

1. **Filtre d'étiquette** — filtre les éléments des champs de ligne ou de colonne en fonction de leurs étiquettes textuelles.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de type date-heure (ou des cellules vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d'un champ de données.
4. **Filtre des 10 premiers** — affiche uniquement les N éléments supérieurs ou inférieurs classés selon un champ de valeur.
5. **Masquer / afficher des éléments dynamiques** — contrôle manuellement la visibilité de chaque élément individuel d'un champ.

Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après avoir appliqué un filtre, vous devez appeler `RefreshData()` et `CalculateData()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre d'étiquette**

Un filtre d'étiquette vous permet de filtrer les éléments d'un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cela est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre spécifique, contiennent un mot particulier, ou correspondent à un autre critère basé sur le libellé.

Aspose.Cells expose le filtrage par étiquettes via la méthode `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. L'énumération `PivotFilterType` comprend des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. Le second argument fournit la chaîne d'étiquette utilisée pour la comparaison.

L'exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d'étiquette afin que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

```cpp
namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Charger le classeur existant contenant un tableau croisé dynamique
    Workbook wb(fileName);

    // Accéder à la feuille de calcul par index (première feuille de calcul)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Accéder au tableau croisé dynamique par index
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Récupérer le premier PivotField de ligne
    PivotField rowField = pt.GetRowFields().Get(0);

    // Appliquer le filtre d'étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Actualiser et recalculer les données du tableau croisé dynamique pour que le filtre prenne effet
    pt.RefreshData();

    // Enregistrer le classeur sur le disque
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtre de date**

Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur les dates, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le trimestre prochain, ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement sur les champs stockant des informations de type date-heure.

{{% alert color="primary" %}}

Le filtre de date ne fonctionne que lorsque la zone de ligne ou de colonne contient uniquement des cellules de type date-heure ou des cellules vides. Si le champ sous-jacent contient d'autres types de données tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances valides de `DateTime` ou des cellules vides avant d'appliquer ce filtre.

{{% /alert %}}

Aspose.Cells expose le filtrage par date via la méthode `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, et `Between`. Selon le type de filtre choisi, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, vous transmettez les dates de début et de fin).

L'exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui restreint les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.

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
        // Classeur source introuvable.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Charger le classeur existant qui contient le tableau croisé dynamique
    Workbook workbook(U16String(inputPath.c_str()));

    // Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accéder au tableau croisé dynamique par index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Récupérer le PivotField de date depuis la zone des lignes
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Définir le critère de date pour le filtre Entre
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Appliquer le filtre de date sur le champ pivot
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
    pivotTable.RefreshData();

    // Enregistrer le classeur
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtre de valeur**

Les filtres de valeur opèrent sur les valeurs agrégées qu'un tableau croisé dynamique calcule dans sa zone de données. Au lieu de faire correspondre des étiquettes textuelles, ils comparent les totaux numériques à un seuil. Les cas d'utilisation typiques incluent l'affichage uniquement des produits dont la somme des ventes dépasse un montant cible, ou uniquement des régions dont le nombre de transactions se situe dans une plage donnée.

Aspose.Cells expose le filtrage par valeur via la méthode `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Le paramètre `filterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, et `ValueLessThanOrEqual`. Le paramètre `valueField` spécifie le champ de données à évaluer, et le ou les derniers arguments fournissent la ou les valeurs seuils.

L'exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

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

    pivotTable.RefreshData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtre des 10 premiers**

Le filtre des 10 premiers est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d'un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement tels que « les 10 meilleurs produits par chiffre d'affaires » ou « les 5 régions les moins performantes par nombre de ventes ».

{{% alert color="primary" %}}

Le filtre des 10 premiers n'est efficace que lorsque le tableau croisé dynamique possède un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n'y a aucune mesure agrégée sur laquelle classer les éléments, et le filtre ne peut pas être appliqué.

{{% /alert %}}

Aspose.Cells expose le filtrage des 10 premiers via la méthode `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Le paramètre `itemCount` définit le nombre d'éléments à conserver, `isTop` indique s'il faut conserver les éléments supérieurs (true) ou inférieurs (false), `valueField` fait référence au champ de données utilisé pour le classement, et `filterType` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`).

L'exemple suivant charge un classeur contenant un tableau croisé dynamique qui possède un champ de valeur, applique un filtre des 10 premiers pour ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.

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

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    pivotTable.RefreshData();

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrer en masquant ou en affichant des éléments dynamiques**

En plus des API de filtrage structurées, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément dynamique individuel. En parcourant la collection `PivotItems` d'un `PivotField` et en basculant la propriété `IsHidden`, vous pouvez supprimer sélectivement des éléments spécifiques sans appliquer un filtre basé sur une formule. Définir `IsHidden = true` masque l'élément dans le tableau croisé dynamique ; définir `IsHidden = false` l'affiche à nouveau.

Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, par exemple masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L'exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment l'afficher à nouveau, actualise le tableau croisé dynamique et enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Charger un classeur existant contenant un tableau croisé dynamique
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Récupérer le PivotField cible (le premier champ d'étiquette de ligne dans lequel nous masquerons/afficherons des éléments)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Parcourir la collection PivotItems du PivotField sélectionné
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Masquer les éléments du tableau croisé dynamique qui correspondent à un nom/critère spécifique
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Démontrer l'affichage : ré-afficher un élément précédemment masqué du tableau croisé dynamique
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
    pivotTable.CalculateData();

    // Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
    // mais sont exclus de l'affichage du tableau croisé dynamique
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Résumé**

Aspose.Cells for C++ fournit un ensemble complet de capacités de filtrage des tableaux croisés dynamiques qui correspondent à celles trouvées dans Microsoft Excel. Les filtres d'étiquettes, de dates et de valeurs couvrent les scénarios analytiques les plus courants, tandis que le filtre des 10 premiers gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.IsHidden` offre une alternative flexible au niveau de l'élément. La combinaison de ces stratégies — par exemple, appliquer un filtre d'étiquette puis masquer des éléments spécifiques — vous permet de construire des rapports de tableau croisé dynamique précisément ciblés entièrement à partir du code.
{{< app/cells/assistant language="cpp" >}}