---
title: Afficher les valeurs selon le type de calcul dans un tableau croisé dynamique avec Aspose.Cells for C++
linktitle: Afficher les valeurs selon le type de calcul dans un tableau croisé dynamique avec Aspose.Cells for C++
description: Affichez les valeurs des champs de données d'un tableau croisé dynamique sous forme de pourcentage du total, d'écart par rapport à un élément de base, de total cumulé, de rang, et plus encore avec Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tableau croisé dynamique, afficher les valeurs sous forme de, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /fr/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l'aide d'une fonction d'agrégation telle que `Sum` ou `Count`. La fonctionnalité **Afficher les valeurs sous forme de** d'Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, un écart par rapport à un élément de base choisi ou un rang — afin de permettre une analyse comparative sans formules auxiliaires ni colonnes calculées.
Les utilisations typiques comprennent l'analyse de la part de chaque valeur dans le total, notamment les pourcentages d'une ligne, d'une colonne ou du total général ; l'établissement de rapports cumulés à l'aide d'un total cumulé dans un champ de période ; l'analyse des écarts par rapport à un élément de référence, à l'aide de l'écart ou du pourcentage d'écart par rapport à un élément de base ; et le classement des valeurs de la plus petite à la plus grande ou de la plus grande à la plus petite.
Dans Aspose.Cells for C++, l'énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. La méthode `PivotField.GetShowValuesSetting()` retourne un objet `PivotShowValuesSetting`, dont les méthodes `SetShowValuesAs`, `SetBaseFieldIndex` et `SetBaseItemIndex` configurent le comportement ; la méthode `PivotField.ShowValuesAs(...)` permet d'appliquer les mêmes paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeurs obtenu à l'aide de `PivotTable.GetDataFields()`.

## **Membres de l'énumération `PivotShowValuesAsType`**
Le champ de données conserve sa fonction d'agrégation, telle que `Sum` ou `Count`, tandis que la fonctionnalité « Afficher les valeurs sous forme de » modifie uniquement la manière dont la valeur agrégée est affichée.
Outre la définition directe des valeurs de `PivotShowValuesSetting` (voir la dernière section), une méthode permet d'appliquer la même configuration en un seul appel. Elle propose deux formes : l'une qui désigne le champ de base et l'élément de base par indice, et l'autre par nom :

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `showValuesAsType` | Calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `baseField` | Indice démarrant à zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l'indice du champ de ligne auquel appartient l'élément de base) ou, dans la forme par nom, le nom du champ de base. | Les huit types de calcul liés à une base ci-dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) ; transmettez `0` (ou une `U16String` vide dans la forme par nom) pour tous les autres types de calcul. |
| `baseItem` | Indice démarrant à zéro de l'élément de base, avec deux valeurs sentinelles : -1 sélectionne l'élément précédent et -2 l'élément suivant (l'API C++ ne définit aucune constante nommée pour ces valeurs sentinelles — transmettez les valeurs littérales). La forme par nom utilise plutôt la légende de l'élément de base ; si le type de calcul sélectionné ne nécessite aucun élément de base, transmettez une `U16String` vide. | Seuls les trois types de calcul liés à l'élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) prennent en compte l'élément de base ; les cinq types de calcul liés au champ (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, les deux classements) l'ignorent — transmettez `0` ou une `U16String` vide. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DifferenceFrom` | Affiche l'écart entre la valeur et celle d'un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou une valeur sentinelle pour l'élément précédent/suivant) |
| `PercentageOf` | Affiche la valeur sous forme de pourcentage de la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou une valeur sentinelle pour l'élément précédent/suivant) |
| `PercentageDifferenceFrom` | Affiche le pourcentage d'écart entre la valeur et celle d'un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou une valeur sentinelle pour l'élément précédent/suivant) |
| `RunningTotalIn` | Affiche la valeur sous forme de total cumulé pour des éléments successifs d'un champ de base. | `baseField` (le champ dont l'ordre des éléments détermine l'accumulation) |
| `PercentageOfRow` | Affiche la valeur en pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur en pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur en pourcentage du total général. | — |
| `Index` | Affiche la valeur à l'aide de la formule d'index d'Excel ((valeur * total général) / (total de la ligne * total de la colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur en pourcentage du total de sa ligne parente (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur en pourcentage du total de sa colonne parente (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur en pourcentage du total de son champ parent. | `baseField` (le champ parent dont le total sert de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur en pourcentage d'un total cumulé dans un champ de base. | `baseField` (le champ d'accumulation) |
| `RankSmallestToLargest` | Classe les valeurs de la plus petite (1) à la plus grande. | `baseField` (le champ dont les éléments définissent la portée du classement) |
| `RankLargestToSmallest` | Classe les valeurs de la plus grande (1) à la plus petite. | `baseField` (le champ dont les éléments définissent la portée du classement) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` écrit les valeurs de `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex` et `BaseItemIndex`) — la méthode et l'objet de configuration sont deux moyens de configurer le même état, à l'instar des sélecteurs de champ de base et d'élément de base dans la boîte de dialogue « Afficher les valeurs sous forme de » d'Excel.
{{% /alert %}}

## **Afficher les valeurs sous forme de pourcentage du total**
Appelez la méthode `PivotField.ShowValuesAs` avec `PivotShowValuesAsType::PercentageOfTotal` pour convertir chaque cellule du champ de données, y compris le total général, en pourcentage du total général. Les valeurs affichées représentent donc la part de chaque résultat dans l'ensemble complet des résultats. Ce format ne compare chaque valeur qu'au total général ; il ne nécessite donc ni champ de base ni élément de base — les arguments finaux (`0`, `0`) sont des valeurs de remplacement que ce format ignore, comme l'indique le tableau des paramètres ci-dessus.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obtenir et configurer `PivotField.ShowValuesSetting`**
Lisez la configuration actuelle à l'aide de `PivotField.GetShowValuesSetting()` : cette méthode retourne l'objet `PivotShowValuesSetting` du champ, dont les méthodes de lecture décrivent le type de calcul actif sélectionné par la fonctionnalité « Afficher les valeurs sous forme de ». Pour modifier la configuration, appelez la méthode `PivotField.ShowValuesAs` : elle écrit tous les paramètres en un seul appel, si bien que vous n'avez jamais à les définir un par un.
L'objet `PivotShowValuesSetting` expose l'état écrit par `ShowValuesAs` :
- `GetShowValuesAs()` / `SetShowValuesAs()` permettent d'obtenir ou de définir le calcul secondaire `PivotShowValuesAsType`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` permettent d'obtenir ou de définir l'indice démarrant à zéro du champ de base parmi les champs du tableau croisé dynamique. Ces méthodes sont utilisées par les types de calcul liés à une base.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` permettent d'obtenir ou de définir l'élément de base : un indice démarrant à zéro d'un élément spécifique du tableau croisé dynamique, ou l'une des deux valeurs sentinelles — -1 pour l'élément précédent, -2 pour l'élément suivant (l'API C++ ne définit aucune constante nommée pour ces valeurs sentinelles). Ces méthodes sont utilisées par les types de calcul liés à l'élément de base.
- `GetBaseFieldName()` et `GetBaseItemCaption()` sont des méthodes en lecture seule qui fournissent respectivement le nom résolu du champ de base et la légende de l'élément de base ; par exemple, après avoir sélectionné la valeur sentinelle correspondant à l'élément précédent, `GetBaseItemCaption()` retourne `(previous)`.
Après avoir appelé `ShowValuesAs`, appelez à nouveau `PivotTable.CalculateData()` afin que le corps du tableau croisé dynamique soit recalculé et réaffiché avec la configuration mise à jour.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articles connexes**
- [Gérer les champs de valeurs dans un tableau croisé dynamique](/cells/fr/cpp/manage-value-fields/)
- [Actualiser un tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}