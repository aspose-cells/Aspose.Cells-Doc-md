---
title: Aplicar estilos a tablas dinámicas
linktitle: Aplicar estilos a tablas dinámicas
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for C++, que cubre autoformatos XLS heredados, estilos con nombre modernos de Excel 2007+, estilos personalizados de tabla dinámica y el atajo FormatAll.
keywords: Aspose.Cells C++ pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la aplicación tanto de autoformatos heredados para tablas dinámicas (diseñados para archivos `.xls`) como de estilos modernos con nombre o personalizados para tablas dinámicas (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro de trabajo, no del formato desde el que se cargó.

{{% /alert %}}

## **Introducción**

Aspose.Cells expone dos APIs de estilo paralelas para tablas dinámicas. La decisión entre ellas está determinada por el formato de archivo en el que se guarda el libro de trabajo, no por el formato desde el que se lee. Un libro de trabajo cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilo moderna en lugar de la heredada.

Para la salida heredada `.xls`, use la propiedad `PivotTable.AutoFormatType` junto con la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Esta API corresponde al selector de autoformato que el Excel clásico ofrecía para las tablas dinámicas.

Para la salida moderna `.xlsx`, `.xlsm` y `.xlsb`, hay dos variantes de API de estilo disponibles:

- `PivotTable.PivotTableStyleType` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que usted mismo define a través de `Worksheets.TableStyles.AddPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.

Además, `PivotTable.FormatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando lo que se haya establecido a través de cualquiera de las APIs de nombre de estilo anteriores. Esto es útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preajustado heredado de XLS**

`PivotTable.AutoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic`, y `Table1` a `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` solo se respeta cuando el libro de trabajo se guarda como `.xls`. Cuando el mismo libro de trabajo se guarda como `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora esta propiedad y recurre a la configuración de `PivotTableStyleType` y `PivotTableStyleName`.

{{% /alert %}}

El siguiente ejemplo carga un libro de trabajo nuevo, completa los datos de muestra de Fruit/Year/Amount, agrega una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}

**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas unidimensionales** con solo campos de fila y valores — no tienen estilo integrado para los encabezados de campos de columna. Si tu tabla dinámica necesita campos de columna, usa los preajustes modernos `PivotTableStyleType` del Escenario 2 a continuación, que están diseñados para el diseño bidimensional que usa el Excel moderno.

{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Crear un nuevo libro de trabajo
    Workbook workbook;

    // Obtener la primera hoja de trabajo
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Rellenar los datos fuente con una fila de encabezado (Fruta, Año, Cantidad)
    // y 9 filas de datos que cubren uva, arándano, kiwi, cereza a lo largo de 2020 y 2021
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // Agregar una tabla dinámica en la celda de destino E3, con nombre "Pivot1", usando el rango fuente A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // Asignar campos: Fruta -> Filas, Año -> Columnas, Cantidad -> Datos
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Aplicar el formato automático preestablecido heredado de XLS "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Guardar el libro de trabajo en formato heredado .xls
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Aplicar un estilo preajustado con nombre moderno de tabla dinámica**

`PivotTable.PivotTableStyleType` acepta un valor de la enumeración `Aspose.Cells.PivotTableStyleType`. La enumeración cubre temas claros `PivotTableStyleLight1` a `PivotTableStyleLight28` y temas oscuros `PivotTableStyleDark1` a `PivotTableStyleDark28`. Los estilos añadidos en Excel 2017 (la segunda oleada de temas claros y oscuros) se pueden acceder a través de la misma enumeración.

Esta es la API recomendada para cualquier formato de archivo moderno. A diferencia del autoformato heredado, el estilo seleccionado aquí se representa fielmente por Excel y sobrevive a las idas y vueltas a través de otras herramientas de Office.

El siguiente ejemplo utiliza los mismos datos de Fruit/Year/Amount, crea una tabla dinámica idéntica, aplica `PivotTableStyleDark1` y guarda el libro de trabajo como `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**

Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo personalizado de tabla dinámica. El flujo de trabajo tiene tres pasos:

1. Agregue un estilo personalizado a la colección `TableStyles` del libro de trabajo mediante `Worksheets.TableStyles.AddPivotTableStyle(string name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) a través de `TableStyle.TableStyleElements.Add(TableStyleElementType)`, luego asigne un `Style` a cada elemento mediante `TableStyleElement.SetElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica estableciendo `PivotTable.PivotTableStyleName` al nombre del estilo. No use `PivotTableStyleType` aquí, ya que esa propiedad selecciona preajustes integrados.

{{% alert color="primary" %}}

`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Use `PivotTableStyleType` para preajustes integrados, y `PivotTableStyleName` para estilos personalizados que haya definido mediante `AddPivotTableStyle`. Establecer ambos es inofensivo, pero solo se representa el que coincide con la fuente prevista.

{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.

El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `PivotTableStyleName` y lo guarda como `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // Poblar datos de origen: fila de encabezado + 9 filas de datos (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // Agregar tabla dinámica con origen en A1:C10, anclada en E3, llamada "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Paso 1: registrar un nuevo estilo de tabla dinámica personalizado y capturar su índice
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para preajustes integrados)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Aplicar un solo estilo a cada celda de la tabla dinámica con FormatAll**

`PivotTable.FormatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de fila y columna, y los totales. Cualquier configuración previamente establecida a través de `PivotTableStyleType` o `PivotTableStyleName` se anula.

{{% alert color="primary" %}}

`FormatAll` anula tanto `PivotTableStyleType` como `PivotTableStyleName`. Úselo solo cuando se requiera una apariencia uniforme, independiente del tema, en toda la tabla dinámica.

{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita, y bordes negros finos en todos los lados, luego lo aplica con `FormatAll` y lo guarda como `.xlsx`.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Fila de encabezado
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Filas de datos
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // Agregar tabla dinámica: rango de origen A1:C10, celda de destino E3, nombre "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Asignar campos de la tabla dinámica
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Crear un estilo que se aplicará a cada celda de la tabla dinámica
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // Aplicar FormatAll
    pivotTable.FormatAll(style);

    // Guardar el libro
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **¿Qué API de estilo debo usar?**

La elección de la API de estilo depende del formato de archivo en el que está guardando. Use la tabla siguiente como referencia rápida.

| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Úselo cuando los preajustes integrados no son suficientes. Configure mediante `TableStyleElement.SetElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.FormatAll(Style)` | Atajo que anula cualquier otra configuración de estilo en toda la tabla dinámica. |

En caso de duda, guarde como `.xlsx` y use `PivotTableStyleType` para temas integrados, o `PivotTableStyleName` para temas personalizados.

{{< app/cells/assistant language="cpp" >}}