---
title: Agrupación discreta de elementos de campos de tabla dinámica
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tabla dinámica en grupos personalizados con nombre, como los grupos de frutas y verduras, mediante DiscreteGroupItem y PivotFieldGroupOptions.DiscreteGroupItems en Aspose.Cells for C++.
keywords: Aspose.Cells for C++, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de campos de tabla dinámica, grupos personalizados, PivotField.Group, C++, tabla dinámica de Excel
type: docs
weight: 90
url: /es/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- La agrupación automática agrupa elementos según su tipo de datos; por ejemplo, las fechas por meses y trimestres o los números por intervalos. La agrupación discreta resuelve el problema contrario: reúne elementos específicos no relacionados en grupos personalizados con nombre; por ejemplo, agrupa productos en grupos de frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells permite la agrupación discreta mediante la clase `DiscreteGroupItem` y la propiedad `PivotFieldGroupOptions.DiscreteGroupItems`.
- Un `DiscreteGroupItem` representa un nombre de grupo y los elementos que pertenecen a él. Los elementos se pueden identificar de dos maneras: por sus nombres (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) o por sus posiciones en los datos de origen, numeradas desde cero (`DiscreteGroupItem("fruit", { 0, 3 })`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo del área de filas o de columnas de una tabla dinámica al pasar las opciones a `PivotField.Group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tabla dinámica por nombres de elementos**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha e importe), genera una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos; a continuación, define dos grupos personalizados por nombres de elementos: `fruit` (`grape`, `cherry`) y `vegetables` (`carrot`, `potato`). El resultado muestra una estructura de filas de dos niveles, con el nombre del grupo como nivel exterior y los elementos originales anidados debajo, lo que permite analizar las tendencias por grupo personalizado y por elemento.

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

Después de `CalculateData()`, el área de filas de la tabla dinámica muestra `fruit` (`grape` 50, `cherry` 80) y `vegetable` (`carrot` 60, `potato` 70), con un total general de 260, mientras que las etiquetas de columna conservan las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tabla dinámica por índices de elementos**
Cuando los nombres de los elementos son largos o están adaptados al idioma, el segundo constructor de `DiscreteGroupItem` identifica los elementos por índice. Los índices representan las posiciones de los elementos, numeradas desde cero, según el orden en que aparecen en los datos de origen, no en orden alfabético. En los datos de ejemplo anteriores, `grape` es el elemento 0, `carrot` es el elemento 1, `potato` es el elemento 2 y `cherry` es el elemento 3; por lo tanto, `fruit` es `{ 0, 3 }` y `vegetable` es `{ 1, 2 }`. El resultado es idéntico al del ejemplo basado en nombres.

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

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no están asignados a ningún grupo personalizado no se pierden. Se mantienen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno como una entrada independiente de un solo elemento. En el ejemplo anterior, al definir únicamente el grupo `fruit`, `carrot` y `potato` permanecen en el área de filas como entradas independientes junto al grupo `fruit`.
- La propiedad `PivotFieldGroupOptions.NewPivotField` controla la estructura de la agrupación discreta. Su valor predeterminado es `true`, lo que añade el campo agrupado como un nuevo campo exterior junto al original y produce la estructura de dos niveles mostrada anteriormente (`RowFields` aumenta a 2). Si se establece en `false`, el campo original se sustituye y el área de filas muestra un único nivel que contiene únicamente los nombres de los grupos y sus valores agregados: `fruit` 130 (50 + 80) y `vegetable` 130 (60 + 70).
- Se pueden combinar instancias creadas mediante los constructores de `DiscreteGroupItem` basados en nombres e índices dentro de la misma colección `DiscreteGroupItems`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de tabla dinámica en la tabla dinámica](/cells/es/cpp/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de fila y de columna en una tabla dinámica](/cells/es/cpp/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/cpp/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a una tabla dinámica](/cells/es/cpp/apply-style-to-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}