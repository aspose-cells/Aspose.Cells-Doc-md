---
title: Afficher les valeurs comme dans le tableau croisé dynamique avec Aspose.Cells pour C++
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique avec Aspose.Cells pour C++
description: Affichez les valeurs des champs de données du tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulés, de classements et plus encore avec Aspose.Cells pour C++.
keywords: Aspose.Cells, C++, tableau croisé dynamique, afficher les valeurs comme, format d'affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /fr/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l'aide d'une fonction d'agrégation telle que `Sum` ou `Count`. La fonction **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement — afin de pouvoir effectuer une analyse comparative sans formules auxiliaires ni colonnes calculées.  
Les utilisations typiques comprennent l’analyse de **la** part du total, y compris les pourcentages d’une ligne, d’une colonne ou du total général ; la production de rapports cumulatifs en utilisant un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence à l’aide de la différence ou de la différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for C++, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. L’accesseur `PivotField.GetShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` et `SetBaseItemIndex` configurent le comportement ; la méthode de commodité `PivotField.ShowValuesAs(...)` applique les mêmes quatre paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeurs obtenu via `PivotTable.GetDataFields()`.

## **Membres de l'énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d'agrégation, telle que Sum ou Count, tandis que Show Values As ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d'écrire les valeurs de `PivotShowValuesSetting` directement (voir la dernière section), une méthode de commodité en un seul appel applique la même configuration :

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `displayFormat` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `baseField` | Index basé sur zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l'index du champ de ligne auquel appartient l'élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`) ; ignoré par tout autre format. |
| `baseItemPositionType` | Mode de sélection de l’élément de base par rapport à l’élément actuel : `PivotItemPositionType::Previous`, `::Next` ou `::Custom`. | Uniquement pour les trois formats à élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) ; ignoré par tout autre format. |
| `baseItem` | Index basé sur zéro de l’élément de base. | Seulement lorsque `baseItemPositionType` vaut `Custom` (l’index indique l’élément exact) ; ignoré pour `Previous` / `Next` et pour tous les formats non‑base — passez `0`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DifferenceFrom` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageOf` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageDifferenceFrom` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `RunningTotalIn` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments détermine l’accumulation) |
| `PercentageOfRow` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur comme un pourcentage du total général. | — |
| `Index` | Affiche la valeur en utilisant la formule d’indice Excel ((valeur * total général) / (total de ligne * total de colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur comme un pourcentage du total de la ligne parente (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur comme un pourcentage du total de la colonne parente (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur comme un pourcentage du total parent. | `baseField` (le champ parent servant de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RankSmallestToLargest` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RankLargestToSmallest` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` écrit les valeurs de `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — la méthode et l’objet de paramètres sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs comme pourcentage du total**
Appelez la méthode `PivotField.ShowValuesAs` avec `PivotFieldDataDisplayFormat::PercentageOfTotal` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc lus comme des proportions de l’ensemble complet des résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni aucun élément de base — les arguments finaux (`0`, `PivotItemPositionType::Previous`, `0`) sont des espaces réservés que le format ignore, comme indiqué dans le tableau des paramètres ci‑dessous.

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
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obtenir et configurer PivotField.ShowValuesSetting**
Lisez la configuration actuelle via `PivotField.GetShowValuesSetting()` : l’accesseur renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre méthodes d’accès décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.ShowValuesAs` — elle écrit les quatre paramètres en un seul appel, vous n’avez donc jamais besoin d’assigner les valeurs individuellement.  
L’objet `PivotShowValuesSetting` expose les quatre valeurs écrites par `ShowValuesAs` :
- `GetCalculationType()` / `SetCalculationType()` sélectionnent le calcul secondaire `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` spécifient l'index basé sur zéro du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à une base.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` déterminent comment l’élément de base est positionné par rapport à l’élément actuel et acceptent `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` ou `PivotItemPositionType::Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` spécifient l'index basé sur zéro de l’élément de base et sont utilisés lorsque le type de position est `Custom`.
Après avoir appelé `ShowValuesAs`, appelez à nouveau `PivotTable.CalculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu à nouveau avec la configuration mise à jour.

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
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/cpp/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/)
- [Application de style au tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}