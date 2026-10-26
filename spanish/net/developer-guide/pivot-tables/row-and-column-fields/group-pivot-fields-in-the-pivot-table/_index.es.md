---
title: Agrupar campos dinámicos en la tabla dinámica
linktitle: Agrupar campos dinámicos en la tabla dinámica
description: Aprenda a agrupar campos dinámicos de filas y columnas en una tabla dinámica en períodos de fechas como meses y trimestres, y en rangos numéricos, usando PivotField.Group y PivotFieldGroupOptions en Aspose.Cells for .NET.
keywords: Aspose.Cells, tabla dinámica, agrupar campo dinámico, PivotField.Group, PivotFieldGroupOptions, agrupación por fechas, agrupación por números, meses, trimestres, rango numérico, C#
type: docs
weight: 80
url: /es/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- Agrupar campos dinámicos resulta útil cuando un campo de fila o columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación condensa estos elementos en secciones significativas: las fechas en meses, trimestres y años, y los números en rangos como 0-1, 2-3, 4-5. Esto hace que una tabla dinámica grande sea compacta y más fácil de analizar. Aspose.Cells ofrece esta capacidad a través del método `PivotField.Group()` (agrupación automática por tipo de dato) y `PivotField.Group(PivotFieldGroupOptions)` (opciones de agrupación personalizadas).
- La agrupación por fechas consolida las fechas individuales en períodos más grandes, como días, meses, trimestres y años, y construye una jerarquía temporal (por ejemplo, Años, Trimestres, Meses). Las tendencias a lo largo del tiempo se vuelven visibles de un vistazo, y cada nivel de período se convierte en su propio campo dinámico en el área de filas o columnas de la tabla dinámica.
- La agrupación solo está disponible para los campos colocados en el área de FILA o COLUMNA de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo, primero debe añadirlo al área de filas o columnas de la tabla dinámica.

## **Agrupar campos dinámicos automáticamente**
La sobrecarga sin parámetros `PivotField.Group()` inspecciona el tipo de dato del campo y lo agrupa automáticamente. Un campo que solo contiene fechas (y espacios en blanco) se agrupa por meses. Un campo que solo contiene números (y espacios en blanco) se agrupa en rangos numéricos usando un intervalo automático.

```csharp
using Aspose.Cells.Pivot;
// Cargar el libro de muestra
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de cálculo y a su tabla dinámica
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Agrupar automáticamente el primer campo de fila.
// El campo contiene fechas, por lo que se agrupa por meses.
PivotField field = pt.RowFields[0];
field.Group();
// Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **Agrupar campos dinámicos con opciones personalizadas**
La clase `PivotFieldGroupOptions` proporciona una configuración de agrupación personalizada. Para los campos de fecha, establezca `StartDate`, `EndDate` y `GroupTypes`. Para los campos numéricos, establezca `StartNumber`, `EndNumber` e `Interval`. La propiedad `NewPivotField` controla si la agrupación crea nuevos campos dinámicos junto al original (consulte la sección Nota al final de este artículo).

### **Agrupar un campo de fecha por meses y trimestres**
El siguiente ejemplo agrupa el campo de fila de fecha de la tabla dinámica de muestra por meses y trimestres entre una fecha de inicio y una fecha de fin. El código carga el [archivo Excel de muestra](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fila de fecha ahora está agrupado por trimestres y meses.
Tenga en cuenta que el orden de los valores en `options.GroupTypes` se ignora. Sin importar el orden en que se enumeren los tipos de grupo, los campos agrupados siempre se muestran del período más grande al más pequeño: años, trimestres, meses, días, horas, minutos, segundos. En este ejemplo los meses se enumeran antes que los trimestres en `options.GroupTypes`, sin embargo, los trimestres se muestran como el nivel externo y los meses como el nivel interno.

```csharp
using Aspose.Cells.Pivot;
// Cargar el libro de muestra
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de cálculo y su tabla dinámica
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Agrupar el primer campo de fila (un campo de fecha) por meses y trimestres
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un campo numérico en rangos**
`FieldTwo` de la tabla dinámica de muestra es inicialmente un campo de datos (valor). Como solo se pueden agrupar los campos de fila o columna, el código primero llama a `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` para mover `FieldTwo` al área de filas, actualiza la tabla dinámica y luego agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 usando `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```csharp
using Aspose.Cells.Pivot;
// Cargar el libro de muestra
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de cálculo y su tabla dinámica
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo es un campo de datos: muévalo al área de filas primero,
// porque solo los campos de fila/columna pueden agruparse
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// Agrupar el campo numérico en los rangos 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Las sobrecargas del método `PivotField.GroupBy()` están obsoletas y se han eliminado de la superficie de la API. `PivotField.Group()` y `PivotField.Group(PivotFieldGroupOptions)` son los reemplazos.
- En Microsoft Excel, al agrupar un campo numérico se REEMPLAZA el campo dinámico original por los rangos agrupados, mientras que al agrupar un campo de fecha se crean NUEVOS campos dinámicos (uno por nivel de grupo, por ejemplo, Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `PivotField.Group()` siguen el mismo comportamiento que Excel. La propiedad `PivotFieldGroupOptions.NewPivotField` existe por compatibilidad con versiones anteriores: su valor predeterminado es false para la agrupación numérica y true para la agrupación de fecha y hora; establézcala en false si desea que la agrupación por fechas reemplace el campo dinámico original en lugar de crear nuevos campos dinámicos.
- La propiedad `PivotFieldGroupOptions.Interval` solo tiene efecto para la agrupación numérica y para la agrupación de fechas por días (por ejemplo, agrupar fechas en períodos de 7 días); se ignora cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos relacionados**
- [Agregar campos de fila y columna en la tabla dinámica](/cells/es/net/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/net/filter-by-label-or-value-of-pivot-table/)
- [Agregar campo de página en la tabla dinámica](/cells/es/net/add-page-field-in-pivot-table/)
- [Aplicar estilo a la tabla dinámica](/cells/es/net/apply-style-to-pivot-table/)
- [Actualizar tabla dinámica](/cells/es/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}