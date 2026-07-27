---
title: Champs de valeur dans Aspose.Cells for C++
linktitle: Champs de valeur dans Aspose.Cells for C++
description: Découvrez comment ajouter des champs de base à la zone de données d'un tableau croisé dynamique, modifier la fonction de synthèse avec PivotField.Function, et tracer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /fr/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les champs de valeur constituent le cœur de chaque tableau croisé dynamique, ce sont les agrégats numériques qui résument les données sources. Dans Aspose.Cells for C++, la zone de données d'un tableau croisé dynamique est peuplée en y ajoutant des champs de base via `PivotTable.AddFieldToArea`, et chaque champ placé dans cette zone peut disposer de sa propre fonction de synthèse. Lorsque deux champs de données ou plus existent, Aspose.Cells expose un champ d'agrégat spécial, `PivotTable.ValuesField`, qui peut être tracé sur l'axe Ligne ou Colonne en tant que champ de base, vous offrant un contrôle plus fin sur l'affichage des champs de valeur dans la mise en page.

## Ajout d'un champ à la zone de données

L'ajout d'un champ de base à la zone de données (valeur) constitue la première étape pour façonner la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.AddFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.Data` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.DataFields`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est résumée avec `ConsolidationFunction.Sum`, tandis qu'une colonne non numérique utilise `Count` par défaut.

## Modification de la fonction de synthèse

Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `Function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `Function` vous permet de basculer entre les agrégats disponibles, notamment `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, et `Varp`.

{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
{{% /alert %}}

Vous pouvez donc conserver un champ de données en tant que `Sum` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `Count` ou `Average`, le tout dans un seul tableau croisé dynamique.

## Tracer les champs de valeur sur l'axe Ligne ou Colonne

Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.ValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données résidant dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ croisé dynamique de base, ce qui est utile pour disposer plusieurs mesures côte à côte.

{{% alert color="primary" %}}
`PivotTable.ValuesField` ne fonctionne pas s'il n'y a aucun ou un seul champ de valeur.
{{% /alert %}}

Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque capacité décrite ci-dessus sur la même structure de tableau croisé dynamique.

## Scénario 1 — Glisser un champ de base dans la zone de données

Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone de données d'un tableau croisé dynamique existant. La structure partagée du tableau croisé dynamique place `Category` et `Item` sur l'axe Ligne et `Year` sur l'axe Colonne. Après l'opération, `Amount` apparaît dans la zone de données et est calculé comme le `Sum` de `Amount` par défaut.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Aspose::Cells::Startup();

 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");

 Cells cells = worksheet.GetCells();

 // Headers in A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // Data rows A2:D9 using nested loops branching on j
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }

 // Add pivot table at F3 with name PivotTable1
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Pivot layout: Category and Item on Row, Year on Column, Amount as data field
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

 pivotTable.RefreshData();
 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");

 Aspose::Cells::Cleanup();
 return 0;
}
```

## Scénario 2 — Modification de la fonction de synthèse

Ce scénario démarre à partir de la même structure de tableau croisé dynamique que le Scénario 1, mais ajoute le champ `Amount` à la zone de données deux fois. Les deux champs de données référencent la même colonne source, toutefois le second champ est remplacé à l'aide du setter `PivotField.Function` afin qu'il devienne `Count` au lieu du `Sum` par défaut.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 intrusive_ptr<Workbook> workbook = new Workbook();
 intrusive_ptr<Worksheet> ws = workbook->GetWorksheets()->Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // Fill data ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 intrusive_ptr<PivotTable> pivotTable = ws->GetPivotTables()->Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType_Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 intrusive_ptr<PivotField> countField = pivotTable->GetDataFields()->Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->RefreshData();
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```

## Scénario 3 — Tracer les champs de valeur sur l'axe Ligne ou Colonne

Avec deux champs de données en place, `PivotTable.ValuesField` devient utilisable. Ce scénario fait glisser ce champ virtuel agrégé sur la zone Colonne afin que chaque mesure de la zone de données apparaisse comme son propre bloc de colonnes à côté de `Year`.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 intrusive_ptr<Workbook> workbook = new Workbook();
 intrusive_ptr<Worksheet> ws = workbook->GetWorksheets()->Get(0);
 ws->SetName("Data");
 // ... build data ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 intrusive_ptr<PivotTable> pivotTable = ws->GetPivotTables()->Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType_Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType_Column, pivotTable->GetValuesField()->GetName());
 pivotTable->RefreshData();
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```

Ensemble, ces trois scénarios couvrent chaque aspect de la manipulation des champs de valeur dans Aspose.Cells for C++, d'un seul champ de données avec le `Sum` par défaut jusqu'à un tableau croisé dynamique multi-mesures dans lequel le `ValuesField` virtuel contrôle la disposition sur l'axe Ligne ou Colonne.

## Articles connexes

- [Champs Ligne et Colonne du tableau croisé dynamique dans Aspose.Cells for C++](/cells/fr/cpp/row-and-column-fields/)
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/cpp/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for C++](/cells/fr/cpp/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}