---
title: Agrupación discreta de elementos de campos de tabla dinámica
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tabla dinámica en grupos personalizados con nombre, como grupos de frutas y verduras, mediante DiscreteGroupItem y PivotFieldGroupOptions.DiscreteGroupItems en Aspose.Cells for .NET.
keywords: Aspose.Cells, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de campos de tabla dinámica, grupos personalizados, PivotField.Group, C#, tabla dinámica de Excel
type: docs
weight: 90
url: /es/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- La agrupación automática agrupa los elementos según el tipo de datos; por ejemplo, agrupa las fechas por meses y trimestres o los números por rangos. La agrupación discreta resuelve el problema opuesto: agrupa elementos específicos y no relacionados en grupos personalizados con nombre; por ejemplo, productos en categorías de frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells ofrece este tipo de agrupación mediante la clase `DiscreteGroupItem` y la propiedad `PivotFieldGroupOptions.DiscreteGroupItems`.
- Un `DiscreteGroupItem` representa el nombre de un grupo y los elementos que pertenecen a él. Los elementos se pueden identificar de dos formas: por sus nombres (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) o por sus posiciones en base cero en los datos de origen (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo del área de filas o del área de columnas de una tabla dinámica; para aplicarla, se pasan las opciones a `PivotField.Group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tabla dinámica por los nombres de los elementos**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha e importe), genera una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos; a continuación, define dos grupos personalizados por nombres de elementos: fruit (grape y cherry) y vegetable (carrot y potato). El resultado muestra una estructura de filas de dos niveles, con el nombre del grupo como nivel superior y los elementos originales anidados en el nivel inferior, lo que permite analizar las tendencias por grupo personalizado y por elemento.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

Después de `CalculateData()`, el área de filas de la tabla dinámica muestra fruit (grape 50, cherry 80) y vegetable (carrot 60, potato 70), con un total general de 260, mientras que las etiquetas de columna conservan las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tabla dinámica por los índices de los elementos**
Cuando los nombres de los elementos son largos o están localizados, el segundo constructor de `DiscreteGroupItem` los identifica por su índice. Los índices son posiciones en base cero de los elementos, en el orden en que aparecen en los datos de origen, y no en orden alfabético. En los datos de ejemplo anteriores, grape es el elemento 0, carrot es el elemento 1, potato es el elemento 2 y cherry es el elemento 3; por lo tanto, el grupo fruit corresponde a `{ 0, 3 }` y el grupo vegetable a `{ 1, 2 }`. El resultado es idéntico al del ejemplo basado en nombres.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no se asignan a ningún grupo personalizado no se pierden. Permanecen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno de ellos como una entrada independiente de un solo elemento. En el ejemplo anterior, al definir solo el grupo fruit, carrot y potato permanecen en el área de filas como entradas independientes junto al grupo fruit.
- La propiedad `PivotFieldGroupOptions.NewPivotField` controla la estructura de la agrupación discreta. Su valor predeterminado es `true`; esto añade el campo agrupado como un nuevo campo de nivel superior junto al original y produce la estructura de dos niveles mostrada anteriormente (`RowFields` pasa a contener 2 campos). Si se establece en `false`, el campo original se sustituye y el área de filas muestra un único nivel con solo los nombres de los grupos y sus valores agregados: fruit 130 (50 + 80) y vegetable 130 (60 + 70).
- Los constructores de `DiscreteGroupItem` basados en nombres y en índices se pueden combinar dentro de la misma matriz `DiscreteGroupItems`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de tabla dinámica en la tabla dinámica](/cells/es/net/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de filas y columnas en una tabla dinámica](/cells/es/net/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/net/filter-by-label-or-value-of-pivot-table/)
- [Aplicar un estilo a una tabla dinámica](/cells/es/net/apply-style-to-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}