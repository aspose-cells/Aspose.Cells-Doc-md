---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con mayor o menor clasificación de un campo de tabla dinámica en Aspose.Cells for Java. Este artículo cubre el método Top10AutoShow de Excel 97-2003, la lectura de las opciones con Top10AutoShowSettings y el filtro de 10 principales de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, Java, tabla dinámica, 10 principales, AutoShow, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /es/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede resultar difícil de leer cuando el campo contiene decenas de miembros. Un informe de los 10 principales conserva únicamente los elementos con mayor o menor clasificación, que es exactamente lo que necesitan los informes de clasificación, como «los 5 productos con mayores ingresos» o «las 3 regiones con menor número de ventas». Aspose.Cells admite dos mecanismos para ello, que corresponden a dos generaciones de Microsoft Excel.
- **AutoShow de Excel 97-2003** — el método `PivotField.top10AutoShow()`. Esta es la configuración clásica «Mostrar los N elementos principales/inferiores» almacenada directamente en el campo de la tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como nuevas, porque forma parte del formato original de la tabla dinámica.
- **Filtro de 10 principales de Excel 2007-365** — el método `PivotField.filterTop10()`. Este es el filtro moderno de valores de 10 principales disponible en «Filtros de valores» del menú del campo. Se almacena como un objeto `PivotFilter` asociado al campo y ofrece una clasificación según el número de elementos o por porcentaje.

## **Mostrar los 10 principales en Excel 97-2003 (top10AutoShow)**
El AutoShow clásico se configura con una sola llamada a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — habilita o deshabilita la configuración de AutoShow en el campo.
- `isTop` — `true` conserva los elementos con mayor clasificación (Principales) y `false` conserva los de menor clasificación (Inferiores).
- `count` — cuántos elementos conservar; por ejemplo, 10 para un informe clásico de los 10 principales.
- `rankBy` — el índice que empieza en cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos por el propio campo.
La clasificación puede basarse en un campo de valor o en el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar por un campo de valor**
Clasifique los elementos del campo de fila en función de un campo de valor corriente, como Suma de ventas. El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y luego muestra los 2 deportes con mayores ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos situado en el índice 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Mostrar los 2 elementos principales clasificados por "Sum of Sales" (índice del campo de datos 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Clasificar por el propio campo**
Los elementos de un campo también pueden clasificarse por ese mismo campo: pase -1 como `rankBy`. Esta variante no necesita ningún campo de datos adicional; basta con que el campo esté en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con menor clasificación según el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `Top10AutoShowSettings.getRankBy()` devuelve -1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Mostrar los 3 elementos inferiores clasificados por el propio campo (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Leer las opciones actuales (Top10AutoShowSettings)**
El método `PivotField.getTop10AutoShowSettings()` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de AutoShow almacenadas actualmente en el campo. Utilícelo para inspeccionar cómo se presentarán los elementos de un libro de trabajo existente o de una tabla dinámica que se acaba de configurar. Este método también se aplica a los libros de trabajo cargados desde un archivo.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

Las cuatro propiedades se corresponden con los atributos clásicos de AutoShow escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores recuperados son los que respetarán todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Las propiedades directas de `PivotField`, expuestas mediante `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` y `getAutoShowField()`, están marcadas como obsoletas. Utilice en su lugar el objeto `Top10AutoShowSettings`: `Top10AutoShowSettings.isAutoShow()` sustituye a `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` sustituye a `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` sustituye a `PivotField.getAutoShowCount()` y `Top10AutoShowSettings.getRankBy()` sustituye a `PivotField.getAutoShowField()`. El propio método `PivotField.top10AutoShow()` es la forma admitida de modificar la configuración.
- `top10AutoShow` funciona con campos de fila y columna. Un campo que solo se encuentre en el área de página (filtro) no puede clasificarse de este modo, porque sus elementos no se presentan en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de 10 principales (filterTop10)**
Las versiones modernas de Excel ofrecen los 10 principales como filtro de valores en el menú del campo («Filtros de valores», «10 principales...»). Aspose.Cells representa esta función mediante el método `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, que devuelve el objeto `PivotFilter` creado:
- `valueFieldIndex` — el índice que empieza en cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — determina qué significa `itemCount`. `PivotFilterType.COUNT` conserva un número fijo de elementos (la opción «Elementos» del cuadro de diálogo). `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje: 30 conserva el 30 % de los elementos con mayor clasificación. `PivotFilterType.SUM` clasifica los elementos según la cobertura acumulada de los valores.
- `isTop` — `true` para Principales y `false` para Inferiores.
- `itemCount` — el valor N en «N principales»; su unidad depende de `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Filtro Top 10: conservar los 2 elementos principales por "Sum of Sales" (índice del campo de datos 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// Para usar en su lugar un filtro basado en porcentajes, conservar el 30 por ciento de los elementos:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` y `filterTop10` son dos funciones independientes. AutoShow escribe el conjunto clásico de atributos de `autoShow` en el campo de la tabla dinámica y se respeta en todas las versiones de Excel desde Excel 97. `filterTop10` escribe una entrada moderna de tipo `PivotFilter`, que requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utilice el filtro moderno vuelve a mostrar todos los elementos. Para los documentos que deban procesarse de ida y vuelta mediante herramientas heredadas, prefiera `top10AutoShow`; para los libros de trabajo modernos, prefiera `filterTop10`, ya que es compatible con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/java/filter-by-label-or-value-of-pivot-table/)
- [Agregar campos de fila y columna a una tabla dinámica](/cells/es/java/pivot-table-add-row-and-column-fields/)
- [Agrupar campos de tabla dinámica en una tabla dinámica](/cells/es/java/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/java/refresh-pivot-table/)
- [Agregar un campo de página a una tabla dinámica](/cells/es/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}