---
title: Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de fila y columna
description: Aprenda cómo agregar campos base a las regiones de fila y columna de una tabla dinámica y cómo controlar los subtotales de los campos dinámicos usando PivotField.setSubtotals en Aspose.Cells for Java.
keywords: Aspose.Cells, Java, tabla dinámica, campo de fila, campo de columna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/java/pivot-table-add-row-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de fila o columna**

El método `PivotTable.addFieldToArea(int fieldType, String fieldName)` mueve un campo base desde los datos de origen a una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.

- `ROW` — campos colocados verticalmente a la izquierda
- `COLUMN` — campos colocados horizontalmente en la parte superior
- `DATA` — campos cuyos valores se agregan
- `PAGE` — campos utilizados como filtros de informes

Después de agregar los campos, puede acceder a ellos a través de las propiedades `PivotTable.getRowFields()` y `PivotTable.getColumnFields()`. Cada propiedad devuelve un `PivotFieldCollection`. El campo en el índice 0 de `RowFields` es el campo de fila más externo, y los índices siguientes representan campos anidados dentro de él. La misma convención de indexación se aplica a `ColumnFields`.

El orden de anidamiento de los campos es importante. Agregar `Category` a la región de fila primero y luego `Item` produce una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de campos dinámicos**

El método `PivotField.setSubtotals(int subtotalType, boolean shown)` controla qué filas de subtotales aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = true` muestra el subtotal, mientras que `shown = false` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotalType` crea un subconjunto personalizado de subtotales.

La enumeración `PivotFieldSubtotalType` define los tipos de subtotales disponibles.

- `AUTOMATIC` — Aspose.Cells elige la selección predeterminada (normalmente `SUM` para campos numéricos)
- `NONE` — suprime todas las filas de subtotales
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Los subtotales solo se representan cuando hay dos o más campos dinámicos en la región de fila (o en la región de columna). Un único campo no tiene nada significativo entre lo que calcular subtotales, por lo que las llamadas a `setSubtotals` no tienen ningún efecto visible en ese caso. Por lo tanto, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite de subtotal entre cada grupo de `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**

Cuando no se llama a `setSubtotals` en absoluto, Aspose.Cells aplica la selección `AUTOMATIC` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` en el campo de fila `Category` externo.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Escenario 2 — Suprimir todos los subtotales (Ninguno)**

Llamar a `setSubtotals(PivotFieldSubtotalType.NONE, true)` elimina todas las filas de subtotales de la tabla dinámica, dejando solo las filas de campo y el total general en la parte inferior. Esto resulta útil cuando se desean los datos agrupados sin procesar y sin filas de resumen.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Escenario 3 — Subconjunto personalizado de subtotales (Suma + Promedio)**

No se limita a un único tipo de subtotal. Cada llamada a `setSubtotals` opera de forma independiente en un tipo, por lo que llamar al método dos veces —una vez con `SUM` y otra con `AVERAGE`— produce un subconjunto personalizado de dos filas de subtotales para cada grupo de `Category`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

PivotTableCollection pivotTables = worksheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);

pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```

## **Resumen**

Los tres escenarios anteriores comparten el mismo conjunto de datos y la misma estructura de tabla dinámica. La única diferencia entre ellos es la llamada a `setSubtotals` aplicada al campo de fila `Category` externo. Recuerde la regla de los dos campos: un único campo en una región no tiene nada entre lo que calcular subtotales, así que coloque siempre al menos dos campos en la región de fila o columna cuando desee que `setSubtotals` tenga un efecto visible.

## **Artículos relacionados**

- [Campos de página en tablas dinámicas](/cells/es/java/add-page-field-in-pivot-table/)
- [Actualización de tablas dinámicas en Aspose.Cells for Java](/cells/es/java/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
