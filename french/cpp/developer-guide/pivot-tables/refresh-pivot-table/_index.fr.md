---
title: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for C++
linktitle: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for C++
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for C++ à l'aide de l'API d'actualisation des tableaux croisés dynamiques v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, C++, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose une API d'actualisation en couches qui vous permet de recharger les données de tableau croisé dynamique à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir de **Aspose.Cells for C++ v26.7**, la méthode héritée `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, conscientes du cache, décrites dans cet article.
{{% /alert %}}
## Introduction
L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells gère une chaîne de données en couches qui relie vos données sources d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour chaque situation.
La chaîne de données à quatre couches est la suivante :
1. **Source de données** — les plages de feuille de calcul d'origine, la requête de base de données ou la plage de consolidation où vivent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cells** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` restitue ses valeurs calculées et ses styles.
Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques dans un classeur font référence à la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise tous les `PivotTable` dépendants en une seule fois.
{{% alert color="primary" %}}
`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.Refresh()` ne prend en charge que les types de sources **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans des plages de feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API de cache.
{{% /alert %}}
En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :
- **`PivotCache.Refresh()`** — recharge les données source vers le cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un seul `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources de cellules de feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.
## Directives Include requises
Tous les exemples C++ de cet article commencent par les directives d'inclusion d'en-tête et d'espace de noms suivantes car les types de tableau croisé dynamique se trouvent dans l'espace de noms `Aspose::Cells::Pivot` :
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`
## Actualiser tous les tableaux croisés dynamiques du classeur
Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflètent les dernières données sources, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt le classeur entier — actualisant chaque `PivotCache` à partir de sa source puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes de documents lorsque la performance n'est pas un problème.
L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.
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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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
## Actualiser tous les tableaux croisés dynamiques d'une seule feuille de calcul
Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul sont connus pour être sans rapport et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.
C'est plus sélectif que `Workbook.RefreshAll()` : seuls les tableaux croisés dynamiques de la feuille de calcul ciblée sont actualisés, laissant intacts les tableaux croisés dynamiques des autres feuilles de calcul.
L'exemple suivant remplit les mêmes données sources Fruit/Année/Montant, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs sources, puis actualise uniquement les tableaux croisés dynamiques de cette feuille de calcul.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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
## Actualiser un seul tableau croisé dynamique
Lorsque vous souhaitez un contrôle fin sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres de vue/mise en page du tableau croisé dynamique lui-même.
### Données sources modifiées — Utilisez `PivotCache.Refresh()`
Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivotTable.GetPivotCache().Refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.
{{% alert color="primary" %}}
Étant donné que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel de `PivotCache.Refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un cache actualise les deux.
{{% /alert %}}
L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs sources, puis actualise via une référence de cache.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Ligne d'en-tête : Fruit / Année / Montant
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Lignes de données
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Ajouter le premier tableau croisé dynamique "Pivot1" ancré à la cellule E3, plage source A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Attribuer les champs pour Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Ajouter un SECOND tableau croisé dynamique "Pivot2" ancré à E15 en utilisant la MÊME plage source A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Attribuer les mêmes champs pour Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modifier plusieurs valeurs de cellules Montant dans les données sources pour simuler un changement de données
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Actualiser le PivotCache partagé en actualisant les données du tableau croisé dynamique
    pivotTable1.RefreshData();

    // Enregistrer le classeur
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
### Seule la vue/mise en page modifiée — Utilisez `CalculateData()`
Si les données sources n'ont *pas* changé mais que seuls les paramètres de vue ou de mise en page du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une zone différente, ou un paramètre d'actualisation à l'ouverture a été activé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.
Cela évite la récupération source inutile et est nettement plus rapide lorsque de nombreux tableaux croisés dynamiques partagent le même cache.
L'exemple suivant modifie une propriété non-source du tableau croisé dynamique, puis appelle `CalculateData()` pour le restituer à partir du cache existant.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Écrire la ligne d'en-tête Fruit / Année / Montant
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

    // Ajouter un tableau croisé dynamique nommé "Pivot1" placé dans la cellule de destination E3, à partir de A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Assigner les champs : Fruit à Ligne, Année à Colonne, Montant à Données
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modifier une propriété d'affichage/de disposition — il s'agit d'une modification purement visuelle,
    // elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() restitue l'affichage DE CE tableau croisé dynamique (données + style) à partir des
    // données déjà présentes dans le PivotCache. Comme les données source n'ont pas changé,
    // aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
    // dans les cellules de la feuille de calcul.
    pivotTable.CalculateData();

    // Enregistrer le classeur sur le disque
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache
Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lots, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.
C'est également le moyen le plus direct de confirmer que deux tableaux croisés dynamiques partagent bien la même instance de `PivotCache` : vous pouvez comparer les références du cache, ou simplement parcourir la collection renvoyée par `GetPivotTables()` et observer quels tableaux croisés dynamiques y apparaissent.
L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.

## Migration depuis l'obsolète `PivotTable.RefreshData()`
Avant Aspose.Cells for C++ v26.7, la méthode standard pour actualiser un tableau croisé dynamique consistait à appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API conscientes du cache décrites ci-dessus.
L'approche par table `RefreshData()` pose problème dans les classeurs réels pour deux raisons :
- Elle récupère les données à partir de la source *à chaque* appel, même lorsque la source n'a pas changé.
- Chaque appel actualise le cache partagé entier. Lorsque de nombreux tableaux croisés dynamiques partagent un cache, l'appel répété de `RefreshData()` par tableau croisé dynamique provoque la re-récupération du même cache encore et encore, ce qui est très lent.
Les remplacements recommandés sont :
- **Actualiser TOUS les tableaux croisés dynamiques du classeur** → utilisez `workbook.RefreshAll();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivotTable.GetPivotCache().Refresh();` pour un cache. Étant donné que le cache est partagé, cet appel unique met à jour chaque tableau croisé dynamique construit au-dessus de ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seule la vue/mise en page du tableau croisé dynamique a changé** → utilisez `pivotTable.CalculateData();` pour restituer à partir du cache existant sans aucun aller-retour vers la source.
L'exemple suivant démontre le nouveau modèle efficace pour les classeurs avec plusieurs tableaux croisés dynamiques partageant un seul cache.
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

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
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
## Quelle API d'actualisation dois-je utiliser ?
Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.
| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tables. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une seule feuille de calcul. |
| Données sources modifiées pour un cache | `pivotTable.GetPivotCache().Refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/mise en page ont changé | `pivotTable.CalculateData()` | Évite l'aller-retour source inutile. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |
En pratique, préférez les API basées sur le cache par rapport à l'obsolète `RefreshData()` par table. Elles sont conscientes des caches partagés, elles évitent les récupérations source redondantes et elles vous permettent de choisir la plus petite portée qui satisfait votre besoin d'actualisation.{{< app/cells/assistant language="cpp" >}}
