---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Apprenez à contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique à l'aide d'Aspose.Cells for C++, y compris la définition de l'ordre d'affichage, du nombre de champs par ligne et de l'ordre des champs de page en haut du tableau croisé dynamique.
keywords: Aspose.Cells, bibliothèque C++, tableur, tableau croisé dynamique, champ de page, ordre des champs de page, nombre de champs de page par ligne, déplacer un champ de page
type: docs
weight: 191
url: /fr/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Cet article fait suite au sujet **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la bande de contrôles de filtre située en haut d'un tableau croisé dynamique — y compris l'ordre d'affichage, le nombre de champs par ligne et le réordonnancement des champs.
{{% /alert %}}
## **Introduction**
Un tableau croisé dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée qui se trouve au-dessus du corps ligne/colonne/données du tableau. Cette zone est rendue sous la forme d'une bande de contrôles déroulants de filtrage (un par champ de page) et c'est ce sur quoi les utilisateurs finaux cliquent pour découper le tableau croisé dynamique selon des critères tels que l'année ou la région. Aspose.Cells for C++ modélise cette zone via la collection `PivotTable.PageFields` et expose trois propriétés qui contrôlent la disposition visuelle de la bande :
- `PivotTable.PageFieldOrder` (une valeur `Aspose.Cells.PrintOrderType`) détermine si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous* de ceux-ci.
- `PivotTable.PageFieldWrapCount` définit combien de champs de page sont placés par ligne ou par colonne avant d'effectuer un retour à la ligne.
- `PivotTable.PageFields.Move(currIndex, destIndex)` réordonne les champs de page sans modifier le mode d'ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données partagé, afin que vous puissiez comparer les dispositions résultantes côte à côte.
## **Données sources**
Les trois exemples ci-dessous chargent ces huit lignes de données de ventes dans une feuille de calcul nommée `PivotData`. Les données contiennent deux candidats aux champs de page (`Year`, `Region`), un candidat au champ de ligne (`Fruit`) et une mesure (`Amount`), ce qui rend la bande des champs de page significative à inspecter.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Les huit lignes sont remplies dans chaque exemple de code, dans un ordre identique, de sorte que les données sources ne diffèrent jamais entre les scénarios — seules les propriétés de disposition des champs de page diffèrent.
## **Exemple 1 : De gauche à droite puis de haut en bas**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu'ils apparaissent **côte à côte sur une seule ligne** en haut du tableau croisé dynamique. Nous attribuons `Fruit` à l'axe des lignes, plaçons `Year` en premier et `Region` en second sur l'axe des pages (l'ordre des appels `AddFieldToArea` détermine l'indice de départ), ajoutons `Amount` (Sum) comme champ de données, puis définissons `PageFieldOrder` sur `PrintOrderType.OverThenDown` avec `PageFieldWrapCount = 2`. Avec `OverThenDown` et un nombre de champs par ligne égal à 2, les deux champs de page sont disposés horizontalement côte à côte sur une seule ligne en haut du tableau croisé dynamique, de sorte que la bande occupe une ligne d'une largeur de deux.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // En-têtes (ligne 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Ligne 1 : Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Ligne 2 : Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Ligne 3 : Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Ligne 4 : Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Ligne 5 : Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Ligne 6 : Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Ligne 7 : Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Ligne 8 : Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // Ajouter la feuille PivotTableReport
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Créer un tableau croisé dynamique à partir de PivotData!A1:D9 placé en A1 sur PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Ajouter les champs
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Année
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Région
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Montant
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Configurer la disposition de la zone des champs de page : placer les champs de page horizontalement d'abord, revenir à la ligne tous les 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Actualiser et calculer
    pivotTable.CalculateData();

    // Enregistrer
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Exemple 2 : De haut en bas puis de gauche à droite**
Dans cet exemple, nous plaçons `Fruit` sur l'axe des lignes, `Year` et `Region` sur l'axe des pages (avec `Year` en premier), et `Amount` (Sum) comme champ de données — exactement comme dans l'Exemple 1. Nous définissons ensuite `PageFieldOrder` sur `PrintOrderType.DownThenOver` et `PageFieldWrapCount` à `2`. Avec `DownThenOver` et un nombre de champs par ligne égal à 2, les deux champs de page sont empilés verticalement — `Year` en haut, `Region` directement en dessous — formant une seule colonne en haut du tableau croisé dynamique. La bande occupe donc deux lignes d'une largeur de un, contrairement à l'Exemple 1.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, nous conservons ce jeu de données et cette allocation de champs, définissons une disposition neutre (`OverThenDown` avec un nombre de champs par ligne `2`), puis démontrons l'opération `PageFields.Move`. L'appel `Move(0, 1)` déplace le champ de page à l'indice 0 (`Year`) à la position 1, et le champ de page qui était à la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le second. Le mode d'ordre et le nombre de champs par ligne restent inchangés, de sorte que la bande est toujours rendue horizontalement côte à côte — seul l'ordre des deux listes déroulantes a été inversé.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Articles connexes**
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/cpp/add-page-field-in-pivot-table/) — la page parente qui présente comment les champs de page sont ajoutés à un tableau croisé dynamique.
- [Champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/cpp/row-and-column-fields/) — couvre l'allocation des champs aux axes des lignes et des colonnes, en complément du travail sur l'axe des pages présenté ici.
- [Gérer les champs de valeur dans un tableau croisé dynamique](/cells/fr/cpp/manage-value-fields/) — décrit comment configurer la zone des données (valeurs), y compris l'agrégation `Sum` utilisée dans cet article.
- [Actualiser un tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/) — explique `RefreshData` et `CalculateData`, qui sont requis après le réordonnancement des champs de page.
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/) — montre comment formater le tableau croisé dynamique rendu après que la bande des champs de page a été disposée.
{{< app/cells/assistant language="" >}}