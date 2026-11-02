---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con la clasificación más alta o más baja de un campo de tabla dinámica en Aspose.Cells for .Net. Este artículo cubre el método Top10AutoShow de Excel 97-2003, la lectura de las opciones con Top10AutoShowSettings y el filtro de los 10 principales de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, .NET, tabla dinámica, 10 principales, mostrar automáticamente, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /es/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede resultar difícil de leer cuando dicho campo contiene decenas de miembros. Un informe de los 10 principales conserva solo los elementos con la clasificación más alta o más baja, que es exactamente lo que necesitan los informes de clasificación, como «5 productos principales por ingresos» o «3 regiones con peor clasificación por número de ventas». Aspose.Cells admite dos mecanismos para esta operación, que corresponden a dos generaciones de Microsoft Excel.
- **AutoShow de Excel 97-2003** — el método `PivotField.Top10AutoShow()`. Esta es la opción clásica «Mostrar los N elementos superiores/inferiores», almacenada directamente en el campo de la tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como modernas, porque forma parte del formato original de las tablas dinámicas.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.FilterTop10()`. Este es el filtro moderno de los 10 principales por valor que se encuentra en «Filtros de valores, 10 principales...» del menú del campo. Se almacena como un objeto `PivotFilter` adjunto al campo y ofrece una clasificación basada en el número de elementos o en porcentajes.

## **Mostrar los 10 principales en Excel 97-2003 (Top10AutoShow)**
La opción clásica AutoShow se configura con una sola llamada a `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)`:
- `isAutoShow` — habilita o deshabilita la configuración AutoShow en el campo.
- `isTop` — `true` conserva los elementos con la clasificación más alta (Superior), mientras que `false` conserva los que tienen la clasificación más baja (Inferior).
- `count` — el número de elementos que se conservan; por ejemplo, 10 para un informe clásico de los 10 principales.
- `rankBy` — el índice basado en cero del **campo de datos** cuyos valores se utilizan para clasificar los elementos. Pase -1 para clasificar los elementos por el propio campo.
La clasificación puede basarse en un campo de valores o en el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar por un campo de valores**
Clasifique los elementos del campo de fila según un campo de valores habitual, como Suma de ventas. El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`) y, a continuación, muestra los 2 deportes con mayor clasificación según las ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos situado en el índice 0.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Mostrar los 2 elementos principales clasificados por "Suma de ventas" (índice del campo de datos 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Clasificar por el propio campo**
Un campo también puede clasificarse por sí mismo: pase -1 como `rankBy`. Esta variante no requiere ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con la clasificación más baja según el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `Top10AutoShowSettings.RankBy` devuelve -1 al leer sus valores.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Mostrar los 3 elementos inferiores clasificados por el propio campo (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Lectura de las opciones actuales (Top10AutoShowSettings)**
La propiedad `PivotField.Top10AutoShowSettings` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de AutoShow almacenadas actualmente en el campo. Utilícela para inspeccionar cómo se presentarían los elementos de un libro de trabajo existente o de una tabla dinámica que se acaba de configurar, incluidos los libros de trabajo cargados desde un archivo.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

Las cuatro propiedades se corresponden con los atributos clásicos de AutoShow escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores leídos son los que se aplicarán en todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Las propiedades directas de `PivotField` `IsAutoShow`, `IsAscendShow`, `AutoShowCount` y `AutoShowField` están marcadas como obsoletas. En su lugar, utilice el objeto `Top10AutoShowSettings`: `IsAutoShow` se sustituye por `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` se sustituye por `Top10AutoShowSettings.IsTop`, `AutoShowCount` se sustituye por `Top10AutoShowSettings.AutoShowCount` y `AutoShowField` se sustituye por `Top10AutoShowSettings.RankBy`. El propio método `Top10AutoShow()` es la forma admitida de modificar la configuración.
- `Top10AutoShow` funciona con campos de fila y de columna. Un campo que se encuentra únicamente en el área de página (filtro) no se puede clasificar de esta forma porque sus elementos no están distribuidos en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (FilterTop10)**
Las versiones modernas de Excel ofrecen la opción «10 principales» como filtro de valores en el menú del campo («Filtros de valores, 10 principales...»). Aspose.Cells lo implementa mediante el método `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, que devuelve el `PivotFilter` creado:
- `valueFieldIndex` — el índice basado en cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — el significado de `itemCount`. `PivotFilterType.Count` conserva un número fijo de elementos (la opción «Elementos» del cuadro de diálogo). `PivotFilterType.Percent` conserva un porcentaje de los elementos, de modo que `itemCount` es el propio porcentaje: 30 conserva el 30 % superior. `PivotFilterType.Sum` clasifica según la cobertura acumulada de los valores.
- `isTop` — `true` para Superior y `false` para Inferior.
- `itemCount` — el N de «N principales»; su unidad depende de `type`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Filtro de los 10 principales: conservar los 2 elementos principales por "Suma de Ventas" (índice del campo de datos 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// Para un filtro basado en porcentaje, conservar el 30 por ciento de los elementos principales:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` y `FilterTop10` son dos funcionalidades distintas. AutoShow escribe el atributo clásico `autoShow` en el campo de la tabla dinámica y se aplica en todas las versiones de Excel, desde Excel 97. `FilterTop10` escribe una entrada `PivotFilter` moderna, que requiere Excel 2007 o una versión posterior. Cuando se abre un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utiliza el filtro moderno deja de aplicar el filtro y muestra todos los elementos. Para los documentos que deban experimentar un ciclo de guardado y reapertura con herramientas heredadas, se recomienda `Top10AutoShow`; para los libros de trabajo modernos, se recomienda `FilterTop10` porque se integra con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/net/filter-by-label-or-value-of-pivot-table/)
- [Añadir campos de fila y de columna a una tabla dinámica](/cells/es/net/pivot-table-add-row-and-column-fields/)
- [Agrupar campos de una tabla dinámica](/cells/es/net/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/net/refresh-pivot-table/)
- [Añadir un campo de página a una tabla dinámica](/cells/es/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}