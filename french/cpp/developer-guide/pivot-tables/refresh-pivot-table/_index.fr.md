---
title: Actualiser les tableaux croisés dynamiques et les caches de tableau croisé dynamique dans Aspose.Cells for C++
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for C++ en utilisant l'API d'actualisation des tableaux croisés dynamiques de la v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les tableaux croisés dynamiques
keywords: Aspose.Cells, C++, tableau croisé dynamique, actualiser, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents, du classeur entier à un seul tableau croisé dynamique. À partir de **Aspose.Cells for C++ v26.7**, la méthode héritée `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, prenant en charge le cache, décrites dans cet article.
{{% /alert %}}

## **Introduction**
Actualiser un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données source d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour chaque situation.
La chaîne de données à quatre couches est :
1. **Source de données** — les plages de la feuille de calcul d'origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données source. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont rassemblées et agrégées.
3. **Tableau croisé dynamique** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `Tableau croisé dynamique` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cellules** — les `Cellules` de la feuille de calcul dans lesquelles le `Tableau croisé dynamique` rend ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.Refresh()` ne prend en charge que les types de source **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans les plages de la feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API du cache.
{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un `Tableau croisé dynamique` à partir des données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données source de cellules de feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.

## **Démarrage Rapide**
Si vous avez seulement besoin du code le plus court possible qui actualise chaque tableau croisé dynamique dans le classeur, un seul appel suffit :

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

Tout le reste de cet article explique quand choisir une API plus restreinte à la place.

## **Directives Include Requises**
Tous les exemples C++ de cet article commencent par les directives d'inclusion d'en-tête et d'espace de noms suivantes car les types de tableau croisé dynamique se trouvent dans l'espace de noms `Aspose::Cells::Pivot` :
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## **Actualiser Tous les Tableaux Croisés Dynamiques du Classeur**
Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflète les dernières données source, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` à partir de sa source, puis recalculant chaque `Tableau croisé dynamique` dépendant. C'est l'approche recommandée pour les actualisations générales de document complet où la performance n'est pas une préoccupation.
L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs source, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

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

## **Actualiser Tous les Tableaux Croisés Dynamiques sur une Seule Feuille de Calcul**
Parfois, vous avez seulement besoin d'actualiser les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul sont connus pour ne pas être liés et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

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
    // Ajouter un tableau croisé dynamique nommé "Pivot1" placé dans la cellule de destination E3, à partir de la plage A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Assigner les champs : Fruit à Ligne, Année à Colonne, Montant à Données
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modifier une propriété d'affichage/mise en page — il s'agit d'une modification purement présentationnelle,
    // elle ne nécessite donc PAS de relire les données source via PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() restitue l'affichage de CE tableau croisé dynamique (données + style) à partir des
    // données déjà détenues dans le PivotCache. Étant donné que les données source n'ont pas changé,
    // aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
    // dans les cellules de la feuille de calcul.
    pivotTable.CalculateData();
    // Enregistrer le classeur sur le disque
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Actualiser un Seul Tableau Croisé Dynamique**
Lorsque vous voulez un contrôle précis sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données source sous-jacentes, ou simplement les paramètres de vue/mise en page du tableau croisé dynamique lui-même.

### **Les Données Source Ont Changé — Utilisez `PivotCache.Refresh()`**
Si les données source sous-jacentes ont changé, le bon point d'entrée est `pivotTable.GetPivotCache().Refresh()`. Cet appel relit les données source dans le cache, puis recalcule chaque `Tableau croisé dynamique` qui dépend de ce cache.

### **Seule la Vue/Mise en Page A Changé — Utilisez `CalculateData()`**
Si les données source n'ont *pas* changé mais que seuls les paramètres de vue ou de mise en page du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une zone différente, ou un paramètre d'actualisation à l'ouverture a été basculé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `Tableau croisé dynamique` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.
L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `CalculateData()` pour le rendre à nouveau à partir du cache existant.

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

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lots, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de chaque `Tableau croisé dynamique` qui dépend du cache donné.

## **Migrer depuis l'Obsolète `PivotTable.RefreshData()`**
Avant Aspose.Cells for C++ v26.7, la manière standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. À partir de la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API prenant en charge le cache décrites ci-dessus.
Il y a deux raisons pour lesquelles l'approche `RefreshData()` par tableau est problématique dans les classeurs réels :
- Elle récupère à nouveau les données depuis la source à *chaque* appel, même lorsque la source n'a pas changé.
Les remplacements recommandés sont :
L'exemple suivant démontre le nouveau modèle efficace pour les classeurs avec plusieurs tableaux croisés dynamiques partageant un seul cache.

## **Quelle API d'Actualisation Dois-je Utiliser ?**
Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune.
| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tous les tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques sur une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une feuille de calcul. |
| Les données source ont changé pour un cache | `pivotTable.GetPivotCache().Refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/mise en page ont changé | `pivotTable.CalculateData()` | Évite l'aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |
En pratique, préférez les API basées sur le cache à l'obsolète `RefreshData()` par tableau. Elles sont conscientes des caches partagés, elles évitent les récupérations redondantes de la source, et elles vous permettent de choisir la plus petite portée qui satisfait votre exigence d'actualisation.

## **Pièges Courants**
- **Oublier d'actualiser avant d'enregistrer.** Un tableau croisé dynamique n'écrit ses valeurs rendues dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez les cellules source, appelez `PivotCache.Refresh()` (ou `Workbook.RefreshAll()`) avant `Workbook.Save()`, sinon le fichier enregistré contient toujours les anciennes valeurs agrégées.
- **Appeler l'obsolète `RefreshData()` par tableau.** Dans la v26.7, `PivotTable.RefreshData()` est marquée comme obsolète et récupère à nouveau la source à chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela signifie N récupérations redondantes de la source. Remplacez par un seul `PivotCache.Refresh()` suivi de `CalculateData()` par tableau.
- **Actualiser lorsque seule la mise en page a changé.** Si vous avez uniquement modifié la vue d'un tableau croisé dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données source, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour rendre à nouveau à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d'une connexion externe (base de données, cube OLAP, etc.), `PivotCache.Refresh()` ne peut pas l'actualiser dans la v26.7 — elle ne prend actuellement en charge que les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="cpp" >}}