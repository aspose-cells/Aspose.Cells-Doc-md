---
title: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for C++
linktitle: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for C++
description: Apprenez à ajouter des champs de base aux régions de ligne et de colonne d'un tableau croisé dynamique et à contrôler les sous-totaux des champs du tableau croisé dynamique à l'aide de PivotField.SetSubtotals dans Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, SetSubtotals, PivotFieldSubtotalType, sous-totaux
type: docs
weight: 220
url: /fr/cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajout d'un champ à la région Ligne ou Colonne**
La méthode `PivotTable.AddFieldToArea(PivotFieldType fieldType, U16String fieldName)` déplace un champ de base des données source vers l'une des quatre régions du tableau croisé dynamique. L'argument `fieldType` accepte l'une des valeurs `PivotFieldType` suivantes.
- `Row` — champs placés verticalement à gauche
- `Column` — champs placés horizontalement en haut
- `Data` — champs dont les valeurs sont agrégées
- `Page` — champs utilisés comme filtres de rapport
L'ordre d'imbrication des champs est important. Ajouter `Category` à la région de ligne en premier, puis `Item`, produit un tableau croisé dynamique dont le regroupement externe est `Category` et le regroupement interne est `Item`. Inverser l'ordre inverse la hiérarchie.

## **Sous-totaux des champs du tableau croisé dynamique**
La méthode `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` contrôle les lignes de sous-total qui s'affichent pour un champ du tableau croisé dynamique. Chaque appel active ou désactive un seul type de sous-total indépendamment. Passer `shown = true` affiche le sous-total, tandis que `shown = false` le masque. Comme chaque appel n'affecte qu'un seul type, appeler la méthode plusieurs fois avec différentes valeurs de `subtotalType` permet de construire un sous-ensemble personnalisé de sous-totaux.
L'énumération `PivotFieldSubtotalType` définit les types de sous-totaux disponibles.
- `Automatic` — Aspose.Cells choisit la sélection par défaut (généralement `Sum` pour les champs numériques)
- `None` — supprime toutes les lignes de sous-total
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que lorsqu'il y a au moins deux champs du tableau croisé dynamique dans la région de ligne (ou dans la région de colonne). Un seul champ n'a rien de significatif à sous-totaliser entre les éléments, donc les appels à `SetSubtotals` n'ont aucun effet visible dans ce cas. Cet article place donc deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple afin que la limite de sous-total entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Lorsque vous n'appelez pas du tout `SetSubtotals`, Aspose.Cells applique la sélection `Automatic` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sur le champ de ligne externe `Category`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");
    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);
    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);
    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);
    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);
    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);
    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);
    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);
    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);
    pivotTable.CalculateData();
    workbook.Save(u"output_automatic.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scénario 2 — Suppression de tous les sous-totaux (None)**
Appeler `SetSubtotals(PivotFieldSubtotalType.None, true)` supprime toutes les lignes de sous-total du tableau croisé dynamique, ne laissant que les lignes de champ et le total général en bas. Ceci est utile lorsque vous souhaitez obtenir les données groupées brutes sans aucune ligne de synthèse.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");
    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }
    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };
    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.CalculateData();
    wb.Save(u"output_none.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scénario 3 — Sous-ensemble personnalisé de sous-totaux (Sum + Average)**
Vous n'êtes pas limité à un seul type de sous-total. Chaque appel à `SetSubtotals` agit indépendamment sur un seul type, donc appeler la méthode deux fois — une fois avec `Sum` et une fois avec `Average` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");
    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);
    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);
    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);
    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);
    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);
    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);
    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);
    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);
    pivotTable.CalculateData();
    workbook.Save(u"output_custom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Récapitulatif**

Les trois scénarios ne diffèrent que par un seul aspect : les appels à `SetSubtotals`. Tout le reste — le jeu de données, les champs et les zones auxquelles ils sont attribués — est identique, ce qui rend les dispositions directement comparables.
- **Placement des champs.** `PivotTable.AddFieldToArea(PivotFieldType::Row, fieldName)` déplace une colonne source vers une région. Dans une même région, l’ordre des appels correspond à l’ordre d’affichage, de sorte que le premier appel devient le groupe le plus externe. Les sous-totaux nécessitent deux champs ou plus dans la même région : avec un seul champ, il n’y a rien entre les groupes sur lequel calculer un sous-total.
- **Scénario 1 — sous-totaux automatiques.** Ne pas appeler `SetSubtotals` laisse le choix à Excel, qui applique son sous-total par défaut aux champs numériques. Appeler `SetSubtotals` avec `PivotFieldSubtotalType::Automatic` enregistre explicitement ce choix plutôt que de le laisser implicite.
- **Scénario 2 — pas de sous-totaux.** `SetSubtotals` avec `PivotFieldSubtotalType::None` désactive le sous-total par défaut, de sorte que le tableau croisé conserve les lignes de champ et le total général, mais supprime les lignes de sous-total qu’Excel insérerait autrement entre elles.
- **Scénario 3 — un sous-ensemble choisi.** Chaque appel active ou désactive exactement un type de sous-total, et les appels s’accumulent plutôt que de se réinitialiser les uns les autres. Appeler `SetSubtotals` une fois avec `PivotFieldSubtotalType::Sum` et une fois avec `PivotFieldSubtotalType::Average` active donc les deux types de sous-total, et le tableau croisé affiche un sous-total Somme, un sous-total Moyenne et un total général.

{{% alert color="primary" %}}
Aucun aspect des sous-totaux n’est spécifique à la région des lignes. Les mêmes appels à `SetSubtotals` sur un champ provenant de `PivotTable.ColumnFields` produisent les mêmes trois dispositions sur l’axe des colonnes, car le paramètre appartient au champ croisé et non à l’axe sur lequel il est placé.
{{% /alert %}}
## **Articles connexes**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/cpp/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for C++](/cells/fr/cpp/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}