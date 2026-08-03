---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells para .NET
linktitle: Agregar campos de filtro
description: Aprenda a agregar y configurar campos de filtro en tablas dinámicas con Aspose.Cells for C++, incluyendo cómo añadir campos de filtro, el filtrado de selección única y el filtrado de selección múltiple.
keywords: Aspose.Cells, C++, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en tablas dinámicas. Puede agregar un campo de filtro mediante una API conveniente de alto nivel o mediante la colección de bajo nivel `PageFields`, y puede controlar el filtro de página en modo de selección única, limpiarlo para mostrar todos los elementos de página, o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos de página a la vez a través de la interfaz de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**

Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como un menú desplegable en la parte superior de una tabla dinámica representada en Excel, y al seleccionar uno de los elementos de página disponibles se reconstruye el cuerpo de la tabla dinámica de modo que solo se resumen los registros pertenecientes a ese elemento de página. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.Page` en lugar de `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

Un campo de filtro puede operar con dos comportamientos. En el comportamiento predeterminado de **selección única**, solo un elemento de página es visible a la vez, por lo que el cuerpo de la tabla dinámica resume exactamente un subconjunto. En el comportamiento de **selección múltiple**, el campo expone una lista de casillas de verificación, y el cuerpo de la tabla dinámica resume la unión de cada elemento de página marcado. El mismo campo de origen se puede mover de un lado a otro entre estos comportamientos alternando una sola propiedad.

Aspose.Cells for C++ expone dos formas equivalentes para registrar un campo de filtro. La API de alto nivel es `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, que toma el nombre de la columna de origen y añade el campo en una sola llamada. La API de bajo nivel es `PivotTable.PageFields.Add(PivotField)`, que se usa cuando ya tiene una referencia a un `PivotField` y desea agregar la misma instancia de campo al área de filtro. Ambas APIs terminan poblando la misma colección `PageFields`, y el resto de este artículo demuestra cómo elegir entre ellas y cómo controlar cada modo de filtrado.

## **Agregar un campo de filtro**

Hay dos formas de registrar un campo dinámico en el área de filtro. La llamada de alto nivel toma el nombre de la columna de origen como una cadena y es la ruta más común. La llamada de bajo nivel acepta una instancia existente de `PivotField` y resulta conveniente cuando la misma instancia de campo debe reutilizarse en varias áreas dinámicas. Ambas llamadas colocan el campo en `PivotTable.PageFields`, tras lo cual aparece como el menú desplegable de página en la parte superior de la tabla dinámica representada.

### Agregar un campo de filtro con AddFieldToArea

El siguiente ejemplo construye un pequeño conjunto de datos de Fruta / Año / Cantidad, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // Crear un nuevo libro de trabajo
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();

    // Configurar la fila de encabezados
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Poblar 9 filas de datos de muestra: Fruta, Año, Cantidad
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // Agregar una tabla dinámica anclada en la celda E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Agregar campos a sus áreas: Fruta como Fila, Cantidad como Datos, Año como Campo de Página
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // Actualizar y calcular los datos de la tabla dinámica
    pivotTable.CalculateData();

    // Guardar el libro de trabajo
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Agregar un campo de filtro con PageFields.Add

Cuando ya trabaja con una instancia de `PivotField`, puede pasarla directamente a `PivotTable.PageFields.Add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo se reemplaza el registro final del área de filtro con la llamada a la API de bajo nivel.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Encabezados
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Datos de muestra (9 filas)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // Agregar tabla dinámica en E3 cubriendo A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Fruit -> Fila, Amount -> Dato
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // Enfoque de bajo nivel: localizar el PivotField existente de Year en BaseFields
    // y registrarlo en el área de Página mediante PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // Actualizar para que el nuevo campo de página se refleje en el libro guardado
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrado de selección única (mostrar un elemento de página)**

En el comportamiento predeterminado de selección única, el campo de filtro se representa como un único menú desplegable y el entero `PivotField.CurrentPageItem` selecciona qué elemento de página controla el cuerpo de la tabla dinámica. Asignar un índice específico elige ese único elemento; asignar el centinela especial `0x7FFD` (decimal 32765) limpia el filtro de modo que todos los elementos de página se resuman a la vez. La selección única es el valor predeterminado; no es necesario habilitarla explícitamente.

### Mostrar todos los elementos

Establecer `CurrentPageItem` en el valor mágico `0x7FFD` equivale a limpiar el filtro de página: el cuerpo de la tabla dinámica resume todos los elementos de página como si no se aplicara ningún filtro.

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

### Mostrar un elemento específico

Establecer `CurrentPageItem` en un índice real elige solo ese elemento de página. El índice es la posición del elemento en la lista ordenada de elementos del campo de filtro, por lo que, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

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

## **Filtrado de selección múltiple**

El filtrado de selección múltiple convierte el menú desplegable de página en una lista de casillas de verificación y permite al usuario final elegir varios elementos de página simultáneamente. Aspose.Cells expone dos propiedades que funcionan juntas. `PivotField.IsMultipleItemSelectionAllowed` debe establecerse en `true` antes de que la interfaz de selección múltiple surta efecto. Después de habilitarla, `PivotItem.IsHidden` controla qué elementos aparecen en la lista de casillas de verificación, de modo que puede mostrar todos los elementos o permitir solo elementos específicos en una lista permitida.

El código siguiente habilita la selección múltiple en el mismo campo de filtro Year construido en el escenario 1a, y luego muestra dos patrones: la Parte A revela cada elemento de página dejando `IsHidden` establecido en `false` para cada entrada, mientras que la Parte B solo permite los valores de origen que usted elija y oculta todo lo demás mediante un bloque `switch (pivotItems[i].GetStringValue())`.

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

    // Datos de muestra: Fruta | Año | Cantidad
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

    // — Habilitar selección múltiple en el campo de página
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // Parte A — seleccionar TODOS los elementos (hacer visible cada elemento)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // Parte B — seleccionar solo elementos específicos por valor de origen
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

> **Nota:** Al usar el filtrado de selección múltiple a través de `PivotItem.IsHidden`, **al menos un `PivotItem` debe permanecer visible** (`IsHidden == false`). Si todos los elementos están ocultos, Excel se bloquea al abrir el archivo o muestra una tabla dinámica en blanco. Verifique siempre que su lista permitida de selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y qué modo debo usar?**

La tabla siguiente resume cuándo usar cada API y modo para que pueda elegir la combinación correcta sin leer cada escenario en detalle.

| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por nombre de columna de origen (lo más común) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Alto nivel, en una sola línea. Use esta opción a menos que necesite una referencia a `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | Úselo cuando el objeto de campo se haya obtenido en otro lugar o necesite reutilizarse. |
| Filtrar a un único elemento de página (modo predeterminado) | `PivotField.CurrentPageItem` | establecer en un índice específico | Por ejemplo, `1` muestra el segundo elemento de la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro de página | `PivotField.CurrentPageItem` | establecer en `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela para "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.IsMultipleItemSelectionAllowed` | establecer en `true` | Requerido antes de que cualquier llamada a `IsHidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.IsHidden` | establecer por elemento | Al menos un elemento debe permanecer visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si todos los `PivotItem` de un campo de filtro de selección múltiple están ocultos, Excel se bloquea al abrirlo o muestra una tabla dinámica en blanco. Construya su lista permitida contra sus datos de origen para que al menos un elemento permanezca visible, y sus libros de trabajo guardados se abrirán de forma fiable en cualquier máquina.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
