---
title: Agrupación discreta de elementos de campos de tabla dinámica
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tabla dinámica en grupos personalizados con nombre, como frutas y verduras, mediante DiscreteGroupItem y PivotFieldGroupOptions.DiscreteGroupItems en Aspose.Cells for Java.
keywords: Aspose.Cells for Java, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de tablas dinámicas, grupos personalizados, PivotField.group, Java, tabla dinámica de Excel
type: docs
weight: 90
url: /es/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles casos de uso**
- La agrupación automática recopila elementos según el tipo de datos; por ejemplo, agrupa las fechas por meses y trimestres o los números por rangos. La agrupación discreta resuelve el problema opuesto: reúne elementos específicos y no relacionados en grupos personalizados con nombre; por ejemplo, agrupa productos en frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells ofrece la agrupación discreta mediante la clase `DiscreteGroupItem` y la propiedad `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` se compone de un nombre de grupo y de los elementos que pertenecen a él. Los elementos pueden identificarse de dos maneras: por sus nombres (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) o por sus posiciones con base cero en los datos de origen (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo del área de filas o de columnas de una tabla dinámica al pasar las opciones a `PivotField.group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tabla dinámica por nombres de elementos**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha e importe), construye una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos; a continuación, define dos grupos personalizados en función de los nombres de los elementos: fruit (grape, cherry) y vegetable (carrot, potato). El resultado muestra una disposición de filas de dos niveles, con el nombre del grupo en el nivel exterior y los elementos originales anidados debajo, lo que permite analizar las tendencias por grupo personalizado y por elemento.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Después de `calculateData()`, el área de filas de la tabla dinámica muestra fruit (grape 50, cherry 80) y vegetable (carrot 60, potato 70), con un total general de 260, y las etiquetas de columna conservan las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tabla dinámica por índices de elementos**
Cuando los nombres de los elementos son largos o están localizados, el segundo constructor de `DiscreteGroupItem` los identifica por índice. Los índices son posiciones con base cero de los elementos en el orden en que aparecen en los datos de origen, no en orden alfabético. En los datos de ejemplo anteriores, grape es el elemento 0, carrot es el elemento 1, potato es el elemento 2 y cherry es el elemento 3; por lo tanto, fruit es `{ 0, 3 }` y vegetable es `{ 1, 2 }`. El resultado es idéntico al del ejemplo basado en nombres.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no se asignan a ningún grupo personalizado no se pierden. Permanecen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno como su propia entrada de un solo elemento. En el ejemplo anterior, al definir solo el grupo fruit, carrot y potato permanecen en el área de filas como entradas independientes junto al grupo fruit.
- La propiedad `PivotFieldGroupOptions.getNewPivotField()` controla la disposición de la agrupación discreta. Su valor predeterminado es `true`, lo que añade el campo agrupado como un nuevo campo exterior junto al original y produce la disposición de dos niveles mostrada anteriormente (`getRowFields()` aumenta a 2). Establézcala en `false` mediante `setNewPivotField(false)` para sustituir el campo original. A continuación, el área de filas muestra un único nivel que contiene solo los nombres de los grupos con sus valores agregados: fruit 130 (50 + 80) y vegetable 130 (60 + 70).
- Los constructores de `DiscreteGroupItem` basados en nombres y en índices pueden mezclarse dentro de la misma matriz `getDiscreteGroupItems()`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de tabla dinámica en la tabla dinámica](/cells/es/java/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de fila y columna a una tabla dinámica](/cells/es/java/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/java/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a una tabla dinámica](/cells/es/java/apply-style-to-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}