---
title: Champs de page dans les tableaux croisés dynamiques
linktitle: Champs de page dans les tableaux croisés dynamiques
description: Apprenez à ajouter et configurer des champs de page dans des tableaux croisés dynamiques à l'aide d'Aspose.Cells for C++, y compris l'ajout de champs de page, le filtrage à sélection unique et le filtrage multi-sélection.
keywords: Aspose.Cells, C++, tableau croisé dynamique, champ de page, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de page dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de page via une API pratique de haut niveau ou via la collection `PageFields` de bas niveau, et vous pouvez piloter le filtre de page en mode sélection unique, le réinitialiser pour afficher tous les éléments de page, ou basculer le champ en multi-sélection afin que les utilisateurs puissent choisir plusieurs éléments de page simultanément via l'interface à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**

Un champ de page est un champ de tableau croisé dynamique qui contrôle *quel sous-ensemble* des données sources est affiché dans le corps du tableau croisé dynamique. Les utilisateurs finaux le voient sous forme de liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et sélectionner l'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page soient résumés. Un champ de tableau croisé dynamique devient un champ de page lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt qu'en tant que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

Un champ de page peut fonctionner selon deux comportements. Dans le comportement par défaut **sélection unique**, un seul élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique résume exactement un sous-ensemble. Dans le comportement **multi-sélection**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique résume l'union de tous les éléments de page cochés. Le même champ source peut être basculé entre ces comportements en activant/désactivant une seule propriété.

Aspose.Cells for C++ expose deux façons équivalentes d'enregistrer un champ de page. L'API de haut niveau est `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `PivotTable.PageFields.Add(PivotField)`, qui est utilisée lorsque vous détenez déjà une référence `PivotField` et souhaitez ajouter la même instance de champ à la zone de page. Les deux APIs finissent par remplir la même collection `PageFields`, et le reste de cet article montre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de page**

Il existe deux façons d'enregistrer un champ de tableau croisé dynamique dans la zone de page. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et est pratique lorsque le même objet de champ doit être réutilisé dans plusieurs zones du tableau croisé dynamique. Les deux appels placent le champ dans `PivotTable.PageFields`, après quoi il apparaît comme liste déroulante de page en haut du tableau croisé dynamique rendu.

### Ajout d'un champ de page avec AddFieldToArea

L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone de ligne, `Amount` dans la zone de données et `Year` dans la zone de page, actualise le tableau croisé dynamique et enregistre le classeur.

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

    // Ajouter des champs à leurs zones : Fruit comme Ligne, Montant comme Données, Année comme champ Page
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // Actualiser et calculer les données du tableau croisé dynamique
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Enregistrer le classeur
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Ajout d'un champ de page avec PageFields.Add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la transmettre directement à `PivotTable.PageFields.Add`. Le tableau croisé dynamique et le champ de page sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final de la zone de page est remplacé par l'appel d'API de bas niveau.

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

    // Approche de bas niveau : localiser le PivotField Year existant dans BaseFields
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
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrage à sélection unique (affichage d'un élément de page)**

Dans le comportement par défaut de sélection unique, le champ de page est rendu sous forme de liste déroulante unique et l'entier `PivotField.CurrentPageItem` sélectionne quel élément de page pilote le corps du tableau croisé dynamique. L'attribution d'un index spécifique sélectionne cet élément ; l'attribution de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) efface le filtre afin que tous les éléments de page soient résumés simultanément. La sélection unique est la valeur par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Afficher tous les éléments

Définir `CurrentPageItem` sur la valeur magique `0x7FFD` équivaut à effacer le filtre de page : le corps du tableau croisé dynamique résume tous les éléments de page comme si aucun filtre n'était appliqué.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Afficher un élément spécifique

Définir `CurrentPageItem` sur un index réel sélectionne uniquement cet élément de page. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de page. Ainsi, par exemple, `1` sélectionne le deuxième élément après le tri.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrage multi-sélection**

Le filtrage multi-sélection transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner simultanément plusieurs éléments de page. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être défini sur `true` pour que l'interface multi-sélection prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, de sorte que vous pouvez soit afficher tous les éléments, soit n'autoriser que des éléments spécifiques.

Le code ci-dessous active la multi-sélection sur le même champ de page Year construit dans le scénario 1a, puis montre deux schémas : la Partie A révèle tous les éléments de page en laissant `IsHidden` défini sur `false` pour chaque entrée, tandis que la Partie B n'autorise que les valeurs sources que vous choisissez et masque tout le reste via un bloc `switch (pivotItems[i].GetStringValue())`.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Remarque :** Lors de l'utilisation du filtrage multi-sélection via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si tous les éléments sont masqués, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste autorisée de multi-sélection inclut au moins un élément de vos données sources.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans avoir à lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de page par nom de colonne source (le plus courant) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Haut niveau, une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de page lorsque vous avez déjà un objet `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | À utiliser lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer à un seul élément de page (mode par défaut) | `PivotField.CurrentPageItem` | définir sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / effacer le filtre de page | `PivotField.CurrentPageItem` | définir sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface multi-sélection dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | définir sur `true` | Requis avant que les appels à `IsHidden` ne prennent effet. |
| Masquer / afficher des éléments individuels dans une liste multi-sélection | `PivotItem.IsHidden` | définir par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage multi-sélection. Si tous les `PivotItem` d'un champ de page multi-sélection sont masqués, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste autorisée à partir de vos données sources afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur toutes les machines.
{{% /alert %}}



{{< app/cells/assistant language="cpp" >}}