---
title: Campos de valor en Aspose.Cells for C++
linktitle: Campos de valor en Aspose.Cells for C++
description: Aprenda a añadir campos base a la región de datos de una tabla dinámica, cambiar la función de resumen con PivotField.Function y trazar el campo de valor en el eje de fila o columna en Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /es/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Añadir un campo a la región de datos

Añadir un campo base a la región de datos (valores) es el primer paso para definir cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.AddFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.Data` y el nombre de la columna de origen. Una vez que un campo se añade a la región de datos, la API lo expone a través de la colección `PivotTable.DataFields`, en el orden en que se añadieron los campos. Por defecto, una columna de origen numérica se resume con `ConsolidationFunction.Sum`, mientras que una columna no numérica toma `Count` por defecto.

## Cambiar la función de resumen

Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `Function` devuelve un valor del enumerado `ConsolidationFunction`. El mismo setter de `Function` le permite alternar entre los agregados disponibles, incluyendo `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` y `Varp`.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado, la columna de origen no cambia.
{{% /alert %}}

Por lo tanto, puede dejar un campo de datos como `Sum` mientras añade un segundo campo de datos que apunte a la misma columna de origen pero use `Count` o `Average`, todo en una sola tabla dinámica.

## Trazar campos de valor en el eje de fila o columna

Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.ValuesField`. Este campo virtual representa el agregado de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región de fila o columna como un campo dinámico base, lo cual resulta útil para disponer varias medidas en paralelo.

{{% alert color="primary" %}}
`PivotTable.ValuesField` no funciona si no hay ningún campo de valor o si hay solo uno.
{{% /alert %}}

Los escenarios siguientes recorren tres ejemplos de extremo a extremo que demuestran cada capacidad descrita anteriormente sobre la misma estructura de tabla dinámica.

## Escenario 1: arrastrar un campo base a la región de valores

Este escenario muestra cómo colocar un único campo base (`Amount`) en la región de datos de una tabla dinámica existente. La estructura compartida de la tabla dinámica coloca `Category` e `Item` en el eje de fila y `Year` en el eje de columna. Tras la operación, `Amount` aparece en la región de datos y se calcula como la `Sum` de `Amount` por defecto.

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

 // Encabezados en A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // Filas de datos A2:D9 usando bucles anidados ramificando en j
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

 // Agregar tabla dinámica en F3 con el nombre PivotTable1
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Diseño de la tabla dinámica: Categoría e Ítem en Fila, Año en Columna, Cantidad como campo de datos
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

## Escenario 2: cambiar la función de resumen

Este escenario parte de la misma estructura de tabla dinámica que el Escenario 1, pero añade el campo `Amount` a la región de datos dos veces. Ambos campos de datos hacen referencia a la misma columna de origen; sin embargo, el segundo campo se sobrescribe mediante el setter `PivotField.Function` para que pase a ser `Count` en lugar del `Sum` por defecto.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // Llenar datos ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 PivotField countField = pivotTable.GetDataFields().Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```

## Escenario 3: trazar campos de valor en el eje de fila o columna

Con dos campos de datos en su lugar, `PivotTable.ValuesField` pasa a estar disponible. Este escenario arrastra dicho campo virtual agregado a la región de columna de modo que cada medida presente en la región de datos aparezca como su propio bloque de columnas junto a `Year`.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    ws->SetName("Data");
    // ... construir datos ...
    int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
    PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
    pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
    pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
    pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
    pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
    pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
    pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
    pivotTable->AddFieldToArea(PivotFieldType::Column, pivotTable->GetValuesField()->GetName());
    pivotTable->CalculateData();
    workbook->Save("output_plot.xlsx");
}
```

En conjunto, estos tres escenarios abarcan todos los aspectos de la manipulación de campos de valor en Aspose.Cells for C++, desde un único campo de datos con el `Sum` por defecto hasta una tabla dinámica con múltiples medidas en la que el `ValuesField` virtual controla el diseño en el eje de fila o columna.

{{< app/cells/assistant language="cpp" >}}
