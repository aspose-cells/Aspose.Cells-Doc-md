---
title: Regroupement discret des éléments d’un champ de tableau croisé dynamique
linktitle: Regroupement discret
description: Découvrez comment regrouper les éléments d’un champ de tableau croisé dynamique dans des groupes personnalisés nommés, tels que les fruits et les légumes, à l’aide de DiscreteGroupItem et de la propriété PivotFieldGroupOptions.DiscreteGroupItems dans Aspose.Cells for C++.
keywords: Aspose.Cells for C++, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regroupement des éléments d’un champ de tableau croisé dynamique, groupes personnalisés, PivotField.Group, C++, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique collecte les éléments selon leur type de données, par exemple les dates par mois et par trimestre ou les nombres par plages. Le regroupement discret résout le problème inverse : regrouper des éléments spécifiques et non liés dans des groupes personnalisés nommés, par exemple des produits sous les catégories fruits et légumes, des magasins par région ou des comptes par zone. Aspose.Cells fournit le regroupement discret au moyen de la classe `DiscreteGroupItem` et de la propriété `PivotFieldGroupOptions.DiscreteGroupItems`.
- Un `DiscreteGroupItem` représente un nom de groupe accompagné des éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux façons : par leur nom (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) ou par leur position dans les données source, avec une indexation à partir de zéro (`DiscreteGroupItem("fruit", { 0, 3 })`). Les deux formes produisent le même résultat.
- Pour appliquer le regroupement discret à un champ situé dans la zone des lignes ou des colonnes du tableau croisé dynamique, transmettez les options à `PivotField.Group(PivotFieldGroupOptions)`.

## **Regrouper les éléments d’un champ de tableau croisé dynamique par nom d’élément**
L’exemple suivant construit une petite liste de ventes (produit, date et montant), crée un tableau croisé dynamique à partir de cette liste avec `product` dans la zone des lignes, `date` dans la zone des colonnes et `amount` dans la zone des données, puis définit deux groupes personnalisés d’après les noms des éléments : le groupe fruit (grape, cherry) et le groupe vegetable (carrot, potato). Le résultat présente une disposition à deux niveaux dans la zone des lignes, avec le nom du groupe au niveau extérieur et les éléments d’origine imbriqués en dessous, afin de permettre l’analyse des tendances par groupe personnalisé et par élément.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Après l’appel à `CalculateData()`, la zone des lignes du tableau croisé dynamique affiche les groupes fruit (grape 50, cherry 80) et vegetable (carrot 60, potato 70), avec un total général de 260, tandis que les libellés de colonne conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments d’un champ de tableau croisé dynamique par indice d’élément**
Lorsque les noms des éléments sont longs ou localisés, le second constructeur de `DiscreteGroupItem` identifie les éléments par leur indice. Les indices indiquent les positions des éléments dans l’ordre d’apparition dans les données source, la numérotation commençant à zéro ; ils ne correspondent pas à l’ordre alphabétique. Dans les données d’exemple ci-dessus, grape correspond à l’élément 0, carrot à l’élément 1, potato à l’élément 2 et cherry à l’élément 3 ; les groupes fruit et vegetable correspondent donc respectivement à `{ 0, 3 }` et `{ 1, 2 }`. Le résultat est identique à celui de l’exemple fondé sur les noms.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le tableau croisé dynamique, au même niveau que les groupes personnalisés, sous la forme d’entrées autonomes, chacune contenant un seul élément. Dans l’exemple ci-dessus, la définition du seul groupe fruit laisse les éléments carrot et potato dans la zone des lignes sous forme d’entrées autonomes à côté du groupe fruit.
- La propriété `PivotFieldGroupOptions.NewPivotField` contrôle la disposition du regroupement discret. Par défaut, sa valeur est `true`, ce qui ajoute le champ regroupé comme nouveau champ extérieur à côté du champ d’origine et produit la disposition à deux niveaux illustrée ci-dessus (`RowFields` contient alors 2 champs). Pour remplacer le champ d’origine, définissez cette propriété sur `false` ; la zone des lignes affiche alors un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées, à savoir fruit 130 (50 + 80) et vegetable 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` fondés respectivement sur les noms et sur les indices peuvent être utilisés conjointement dans la même collection `DiscreteGroupItems`.
{{% /alert %}}

## **Articles associés**
- [Regrouper les champs du tableau croisé dynamique](/cells/fr/cpp/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne dans le tableau croisé dynamique](/cells/fr/cpp/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/cpp/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}