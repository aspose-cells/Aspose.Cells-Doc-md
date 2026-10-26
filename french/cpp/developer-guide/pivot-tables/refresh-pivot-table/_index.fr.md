---
title: Actualiser les tableaux croisés dynamiques dans Aspose.Cells for C++
linktitle: Actualiser les tableaux croisés dynamiques dans Aspose.Cells for C++
description: "Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for C++ à l’aide de l’API d’actualisation des pivots v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques."
keywords: Aspose.Cells, C++, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d’actualisation à plusieurs niveaux qui permet de recharger les données du tableau croisé dynamique à quatre portées différentes, du classeur entier jusqu’à un seul tableau croisé dynamique. À partir de **Aspose.Cells for C++ v26.7**, l’ancienne méthode `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces qui tiennent compte du cache et décrites dans cet article.
{{% /alert %}}

## Introduction
L’actualisation d’un tableau croisé dynamique relève rarement d’une seule opération. En arrière-plan, Aspose.Cells gère une chaîne de données hiérarchisée qui relie les données source d’origine aux valeurs affichées dans la feuille de calcul. Comprendre cette chaîne est essentiel pour choisir l’API d’actualisation adaptée à chaque situation.
La chaîne de données à quatre niveaux est la suivante :
1. **Source de données** — les plages de la feuille de calcul d’origine, la requête de base de données ou la plage de consolidation dans lesquelles les valeurs brutes sont stockées.
2. **PivotCache** — l’instantané en mémoire des données source. Chaque tableau croisé dynamique est construit au-dessus d’un `PivotCache` ; c’est là que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l’objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* les données de son `PivotCache`, jamais directement celles de la source.
4. **Cells** — la collection `Cells` de la feuille de calcul dans laquelle le `PivotTable` rend les valeurs calculées et les styles.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indique l’origine des données du cache. À partir de v26.7, `PivotCache.Refresh()` prend en charge uniquement les types de source **`Sheet`** et **`Consolidation`**, c’est-à-dire les données stockées dans des plages de feuilles de calcul. Les sources externes, telles que les bases de données et les connexions externes, ne peuvent pas encore être actualisées via l’API du cache.
En raison de cette chaîne, Aspose.Cells propose deux chemins d’actualisation fondamentaux :
- **`PivotTable.CalculateData()`** — recalcule l’affichage d’un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données source stockées dans des cellules d’une feuille de calcul. Le type de source est donc `Sheet` et les opérations d’actualisation se comportent comme décrit.
{{% /alert %}}

## Quick Start
Si vous avez uniquement besoin du code le plus court possible pour actualiser tous les tableaux croisés dynamiques du classeur, un seul appel suffit :

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Tout le reste de cet article explique quand choisir une API plus ciblée.

## Required Include Directives
Tous les exemples C++ de cet article commencent par les directives d’inclusion d’en-tête et de namespace suivantes, car les types de pivot résident dans le namespace `Aspose::Cells::Pivot` :
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
Lorsque vous devez garantir que chaque cache de pivot et chaque tableau croisé dynamique du classeur reflète les dernières données source, l’API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt tout le classeur, actualise chaque `PivotCache` depuis sa source, puis recalcule chaque `PivotTable` dépendant. C’est l’approche recommandée pour les actualisations générales de l’ensemble du document lorsque les performances ne sont pas un facteur déterminant.
L’exemple suivant construit un classeur avec une plage source Fruit/Year/Amount, crée un tableau croisé dynamique, modifie certaines valeurs source, puis utilise `RefreshAll()` pour tout actualiser en un seul appel.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh All Pivot Tables on a Single Worksheet
Parfois, vous ne souhaitez actualiser que les tableaux croisés dynamiques résidant sur une feuille de calcul donnée, par exemple lorsque vous savez que ceux des autres feuilles de calcul ne sont pas liés et ne doivent pas être modifiés. Dans ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limitée à une seule instance de `Worksheet`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh a Single Pivot Table
Lorsque vous souhaitez contrôler finement un seul tableau croisé dynamique, l’API basée sur le cache vous offre deux options. Le choix dépend de ce qui a réellement changé : les données source sous-jacentes ou uniquement les paramètres d’affichage et de disposition du tableau croisé dynamique lui-même.

### Source Data Changed — Use `PivotCache.Refresh()`
Si les données source sous-jacentes ont changé, le point d’entrée approprié est `pivotTable.GetPivotCache().Refresh()`. Cet appel relit les données source dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Only View/Layout Changed — Use `CalculateData()`
Si les données source n’ont *pas* changé et que seuls les paramètres d’affichage ou de disposition du tableau croisé dynamique ont été modifiés, par exemple si un champ a été déplacé vers une autre zone ou si un paramètre d’actualisation à l’ouverture a été modifié, il est inutile de retourner à la source de données. Le cache contient déjà les données correctes ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.
L’exemple suivant modifie une propriété non liée à la source du tableau croisé dynamique, puis appelle `CalculateData()` pour effectuer un nouveau rendu à partir du cache existant.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Écrire la ligne d’en-tête Fruit / Year / Amount
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Écrire 8 lignes de données (lignes 2-9, correspondant à la plage source A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
 // Ajouter un tableau croisé dynamique nommé, placé dans la cellule de destination E3 et utilisant A1:C9 comme source
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    // Affecter les champs : Fruit à Ligne, Year à Colonne, Amount à Données
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modifier une propriété d’affichage/disposition — il s’agit uniquement d’une modification de présentation,
    // elle ne nécessite donc PAS de relire les données source via PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() régénère l’affichage de CE tableau croisé dynamique (données + style) à partir des
    // données déjà conservées dans le PivotCache. Comme les données source n’ont pas changé,
    // aucun aller-retour vers la source n’est effectué — seules les valeurs mises en cache sont recalculées
    // dans les cellules de la feuille de calcul.
    pivotTable.CalculateData();
    // Enregistrer le classeur sur le disque
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un même cache. Pour les énumérer, par exemple avant d’effectuer une actualisation par lot ou de diagnostiquer l’impact d’un cache partagé, utilisez `PivotCache.GetPivotTables()`. Cette méthode retourne la collection de tous les `PivotTable` qui dépendent du cache spécifié.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Avant Aspose.Cells for C++ v26.7, la méthode standard consistait à appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique. À partir de v26.7, cette méthode est marquée **obsolète** et doit être remplacée par les API basées sur le cache décrites ci-dessus.
Dans les classeurs réels, l’approche par table avec `RefreshData()` présente deux problèmes :
- Elle récupère à nouveau les données depuis la source *à chaque appel*, même si la source n’a pas changé.
Les remplacements recommandés sont les suivants :
L’exemple suivant illustre le nouveau modèle efficace pour les classeurs contenant plusieurs tableaux croisés dynamiques qui partagent un même cache.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    PivotTable pivotTable1 = sheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotTable pivotTable2 = sheet.GetPivotTables().Add(u"A1:C9", 14, 4);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Which Refresh API Should I Use?
Le tableau ci-dessous récapitule les API d’actualisation disponibles et le moment où choisir chacune d’elles.
| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser tout le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tous les tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d’une seule feuille | `Worksheet.RefreshPivotTables()` | Limitée à une seule feuille de calcul. |
| Les données source d’un cache ont changé | `pivotTable.GetPivotCache().Refresh()` | Actualise TOUS les tableaux croisés dynamiques qui utilisent ce cache partagé. |
| Seuls les paramètres d’affichage et de disposition ont changé | `pivotTable.CalculateData()` | Évite un aller-retour inutile vers la source. |
| Répertorier tous les tableaux croisés dynamiques d’un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour les énumérer avant une actualisation groupée. |
En pratique, préférez les API basées sur le cache à la méthode obsolète `RefreshData()` par table. Elles tiennent compte des caches partagés, évitent les récupérations redondantes de la source et permettent de choisir la plus petite portée qui répond au besoin d’actualisation.

## Common Pitfalls
- **Oublier d’actualiser avant d’enregistrer.** Un tableau croisé dynamique n’écrit ses valeurs affichées dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules source, appelez `PivotCache.Refresh()` ou `Workbook.RefreshAll()` avant `Workbook.Save()`, sinon le fichier enregistré contient toujours les anciennes valeurs agrégées.
- **Appeler la méthode obsolète `RefreshData()` pour chaque table.** Dans v26.7, `PivotTable.RefreshData()` est marquée obsolète et récupère à nouveau la source à chaque appel. Lorsque plusieurs tableaux croisés dynamiques partagent un cache, cela entraîne N récupérations redondantes de la source. Remplacez cet appel par un seul `PivotCache.Refresh()`, suivi de `CalculateData()` pour chaque table.
- **Actualiser lorsque seule la disposition a changé.** Si vous ne modifiez que l’affichage d’un tableau croisé dynamique, par exemple l’ordre des colonnes ou `ConsolidationFunction`, sans toucher aux données source, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour effectuer un nouveau rendu à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d’une connexion externe, telle qu’une base de données ou un cube OLAP, `PivotCache.Refresh()` ne peut pas l’actualiser dans v26.7. Cette méthode prend actuellement en charge uniquement les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

{{< app/cells/assistant language="cpp" >}}