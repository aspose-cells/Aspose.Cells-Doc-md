---
title: Champs de valeur dans Aspose.Cells for C++
description: Découvrez comment ajouter des champs de base à la zone de données d'un tableau croisé dynamique, modifier la fonction de synthèse avec PivotField.Function, et tracer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for C++.
linktitle: Champs de valeur dans Aspose.Cells for C++
keywords: Aspose.Cells, C++, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /fr/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeur) constitue la première étape pour façonner la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.AddFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.Data` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.DataFields`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est résumée avec `ConsolidationFunction.Sum`, tandis qu'une colonne non numérique utilise `Count` par défaut.

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
 PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);
 // Pivot layout: Category and Item on Row, Year on Column, Amount as data field
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");
 Aspose::Cells::Cleanup();
 return 0;
}
```

## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `Function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `Function` vous permet de basculer entre les agrégats disponibles, notamment `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, et `Varp`.

{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
Vous pouvez donc conserver un champ de données en tant que `Sum` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `Count` ou `Average`, le tout dans un seul tableau croisé dynamique.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana", u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) {
                worksheet.GetCells().Get(i, j).PutValue(i <= 4 ? u"Fruit" : u"Vegetable");
            } else if (j == 1) {
                worksheet.GetCells().Get(i, j).PutValue(items[i - 1]);
            } else if (j == 2) {
                worksheet.GetCells().Get(i, j).PutValue(years[i - 1]);
            } else {
                worksheet.GetCells().Get(i, j).PutValue(amounts[i - 1]);
            }
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField countField = pivotTable.GetDataFields().Get(1);
    countField.SetFunction(ConsolidationFunction::Count);

    pivotTable.CalculateData();

    wb.Save(u"output_function.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Tracer les champs de valeur sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.ValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données résidant dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ croisé dynamique de base, ce qui est utile pour disposer plusieurs mesures côte à côte.

{{% alert color="primary" %}}
`PivotTable.ValuesField` ne fonctionne pas s'il n'y a aucun ou un seul champ de valeur.
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque capacité décrite ci-dessus sur la même structure de tableau croisé dynamique.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Category"));
    cells.Get(0, 1).PutValue(U16String("Item"));
    cells.Get(0, 2).PutValue(U16String("Year"));
    cells.Get(0, 3).PutValue(U16String("Amount"));

    std::vector<U16String> categories = {
        U16String("Fruit"), U16String("Fruit"), U16String("Fruit"), U16String("Fruit"),
        U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable")
    };
    std::vector<U16String> items = {
        U16String("Apple"), U16String("Apple"), U16String("Banana"), U16String("Banana"),
        U16String("Carrot"), U16String("Carrot"), U16String("Daikon"), U16String("Daikon")
    };
    int years[8] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[8] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) cells.Get(i, j).PutValue(categories[i - 1]);
            else if (j == 1) cells.Get(i, j).PutValue(items[i - 1]);
            else if (j == 2) cells.Get(i, j).PutValue(years[i - 1]);
            else cells.Get(i, j).PutValue(amounts[i - 1]);
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::Count);

    pivotTable.AddFieldToArea(PivotFieldType::Column, pivotTable.GetValuesField().GetName());

    pivotTable.CalculateData();
    workbook.Save(u"output_plot.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}