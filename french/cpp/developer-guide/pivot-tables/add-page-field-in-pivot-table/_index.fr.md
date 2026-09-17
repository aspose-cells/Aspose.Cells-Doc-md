---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for C++
description: Apprenez à ajouter et configurer des champs de filtre dans des tableaux croisés dynamiques en utilisant Aspose.Cells for C++, y compris l'ajout de champs de filtre, le filtrage à sélection unique et le filtrage à sélection multiple.
keywords: Aspose.Cells, C++, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Ajouter des champs de filtre
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API pratique de haut niveau ou via la collection de bas niveau `PageFields`, et vous pouvez piloter le filtre en mode sélection unique, le réinitialiser pour afficher tous les éléments du filtre, ou basculer le champ en sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de filtre en une fois grâce à l'interface à cases à cocher d'Excel.
{{% /alert %}}

## **Introduction**
Un champ de filtre est un champ croisé dynamique qui contrôle *quel sous-ensemble* des données source le corps du tableau croisé dynamique affiche. Les utilisateurs finaux le voient comme une liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et la sélection d'un des éléments de filtre disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de filtre soient synthétisés. Un champ croisé dynamique devient un champ de filtre lorsqu'il est enregistré comme `PivotFieldType.Page` plutôt que comme `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

## **Ajout d'un champ de filtre**

### Ajout d'un champ de filtre avec AddFieldToArea
L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone des lignes, `Montant` dans la zone des données, et `Année` dans la zone des filtres, actualise le tableau croisé dynamique, puis enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Créer un nouveau classeur
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    Cells cells = worksheet.GetCells();
    // Configurer la ligne d'en-tête
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // Remplir 9 lignes de données d'exemple : Fruit, Année, Montant
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };
    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Ajouter un tableau croisé dynamique ancré à la cellule E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Ajouter des champs à leurs zones : Fruit comme ligne, Montant comme données, Année comme champ de page
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // Actualiser et calculer les données du tableau croisé dynamique
    pivotTable.CalculateData();
    // Enregistrer le classeur
    workbook.Save(u"pageFieldSample.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### Ajout d'un champ de filtre avec PageFields.Add
Lorsque vous travaillez déjà avec une instance de `PivotField`, vous pouvez la transmettre directement à `PivotTable.PageFields.Add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final dans la zone des filtres est remplacé par l'appel à l'API de bas niveau.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // En-têtes
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // Données d'exemple (9 lignes)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);
    // Ajouter un tableau croisé dynamique à E3 couvrant A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    // Fruit -> Ligne, Montant -> Données
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    // Approche bas niveau : localiser le PivotField Year existant dans BaseFields
    // et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }
    // Actualiser pour que le nouveau champ de page soit reflété dans le classeur enregistré
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrage à sélection unique (affichage d'un seul élément de filtre)**
Dans le comportement par défaut de sélection unique, le champ de filtre s'affiche sous la forme d'une liste déroulante unique et l'entier `PivotField.CurrentPageItem` sélectionne quel élément de filtre pilote le corps du tableau croisé dynamique. L'assignation d'un index spécifique choisit cet élément unique ; l'assignation de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) réinitialise le filtre afin que tous les éléments de filtre soient synthétisés en une fois. La sélection unique est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments
Définir `CurrentPageItem` sur la valeur magique `0x7FFD` équivaut à réinitialiser le filtre : le corps du tableau croisé dynamique synthétise chaque élément de filtre comme si aucun filtre n'était appliqué.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};
    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    pivotTable.CalculateData();
    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### Affichage d'un élément spécifique
Définir `CurrentPageItem` sur un index réel ne sélectionne que cet élément de filtre unique. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de filtre. Par exemple, `1` sélectionne le deuxième élément après le tri.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));
    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));
    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));
    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));
    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrage à sélection multiple**
Le filtrage à sélection multiple transforme la liste déroulante de filtre en une liste à cases à cocher et permet à l'utilisateur final de sélectionner simultanément plusieurs éléments de filtre. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être défini sur `true` avant que l'interface de sélection multiple prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste à cases à cocher, ce qui vous permet soit d'afficher tous les éléments, soit de n'autoriser que des éléments spécifiques via une liste blanche.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // Données d'exemple : Fruit | Année | Montant
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");
    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };
    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }
    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // — Activer la sélection multiple sur le champ de page
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);
    // Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }
    // Partie B — sélectionner uniquement des éléments spécifiques par valeur source
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Remarque :** Lors de l'utilisation du filtrage à sélection multiple via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si tous les éléments sont masqués, Excel plante lors de l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste blanche de sélection multiple comprend au moins un élément provenant de vos données source.

## **Quelle API et quel mode dois-je utiliser ?**
Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans lire chaque scénario en détail.
| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (cas le plus courant) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "nomDuChamp")` | n/a | Haut niveau, une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous disposez déjà d'un objet `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | À utiliser lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de filtre (mode par défaut) | `PivotField.CurrentPageItem` | définir sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / réinitialiser le filtre | `PivotField.CurrentPageItem` | définir sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface de sélection multiple dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | définir sur `true` | Requis avant que tout appel à `IsHidden` ne prenne effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.IsHidden` | définir par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage à sélection multiple. Si tous les `PivotItem` d'un champ de filtre à sélection multiple sont masqués, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste blanche à partir de vos données source de sorte qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur toutes les machines.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}