---
title: Agrupar campos dinámicos en la tabla dinámica
linktitle: Agrupar campos dinámicos en la tabla dinámica
description: Aprenda cómo agrupar campos dinámicos de filas y columnas en una tabla dinámica en períodos de fechas como meses y trimestres, y en rangos numéricos, usando PivotField.Group y PivotFieldGroupOptions en Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, tabla dinámica, agrupar campo dinámico, PivotField.Group, PivotFieldGroupOptions, agrupación por fechas, agrupación por números, meses, trimestres, rango numérico, JavaScript
type: docs
weight: 80
url: /es/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- Agrupar campos dinámicos resulta útil cuando un campo de fila o columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación contrae estos elementos en secciones significativas: las fechas en meses, trimestres y años, y los números en rangos como 0-1, 2-3, 4-5. Esto hace que una tabla dinámica grande sea compacta y más fácil de analizar. Aspose.Cells ofrece esta capacidad mediante el método `pivotField.group()` (agrupación automática por tipo de dato) y `pivotField.group(PivotFieldGroupOptions)` (opciones de agrupación personalizada).
- La agrupación por fechas acumula las fechas individuales en períodos más grandes, como días, meses, trimestres y años, y construye una jerarquía temporal (por ejemplo Años, Trimestres, Meses). Las tendencias a lo largo del tiempo se vuelven visibles de un vistazo, y cada nivel de período se convierte en su propio campo dinámico en el área de fila o columna de la tabla dinámica.
- La agrupación solo está disponible para los campos colocados en el área de FILA o COLUMNA de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo, primero debe agregarlo al área de fila o columna de la tabla dinámica.

## **Agrupar campos dinámicos automáticamente**
La sobrecarga sin parámetros `pivotField.group()` inspecciona el tipo de dato del campo y lo agrupa automáticamente. Un campo que solo contiene fechas (y espacios en blanco) se agrupa por meses. Un campo que solo contiene números (y espacios en blanco) se agrupa en rangos numéricos usando un intervalo automático.

```javascript
const AsposeCells = require("aspose.cells.node");
// Cargar el libro de trabajo de muestra
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de cálculo y su tabla dinámica
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Agrupar automáticamente el primer campo de fila.
// El campo contiene fechas, por lo que se agrupa por meses.
const field = pt.getRowFields().get(0);
field.group();
// Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Agrupar campos dinámicos con opciones personalizadas**
La clase `PivotFieldGroupOptions` ofrece una configuración de agrupación personalizada. Para los campos de fecha, configure `startDate`, `endDate` y `groupTypes`. Para los campos numéricos, configure `startNumber`, `endNumber` e `interval`. La propiedad `newPivotField` controla si la agrupación crea nuevos campos dinámicos junto al original (consulte la sección Nota al final de este artículo).

### **Agrupar un campo de fecha por meses y trimestres**
El siguiente ejemplo agrupa el campo de fila de fecha de la tabla dinámica de muestra por meses y trimestres entre una fecha de inicio y una fecha de fin. El código carga el [archivo Excel de muestra](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fila de fecha ahora está agrupado por trimestres y meses.
Tenga en cuenta que el orden de los valores en `options.groupTypes` se ignora. No importa en qué orden se enumeren los tipos de agrupación, los campos agrupados siempre se muestran desde el período más grande al más pequeño: años, trimestres, meses, días, horas, minutos, segundos. En este ejemplo, los meses se enumeran antes que los trimestres en `options.groupTypes`, sin embargo, los trimestres se muestran como el nivel externo y los meses como el nivel interno.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de cálculo y su tabla dinámica
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Agrupar el primer campo de fila (un campo de fecha) por meses y trimestres
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un campo numérico en rangos**
`FieldTwo` de la tabla dinámica de muestra es inicialmente un campo de datos (valor). Dado que solo los campos de fila o columna se pueden agrupar, el código primero llama a `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` para mover `FieldTwo` al área de filas, actualiza la tabla dinámica y luego agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 usando `startNumber = 0`, `endNumber = 5` e `interval = 2`.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de cálculo y su tabla dinámica
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo es un campo de datos: muévalo primero al área de filas,
// porque solo los campos de fila/columna se pueden agrupar
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Agrupar el campo numérico en los rangos 0-1, 2-3, 4-5
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Las sobrecargas del método `pivotField.groupBy()` están obsoletas y se han eliminado de la superficie de la API. `pivotField.group()` y `pivotField.group(PivotFieldGroupOptions)` son los reemplazos.
- En Microsoft Excel, al agrupar un campo numérico se REEMPLAZA el campo dinámico original con los rangos agrupados, mientras que al agrupar un campo de fecha se crean NUEVOS campos dinámicos (uno por cada nivel de agrupación, por ejemplo Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `pivotField.group()` siguen el mismo comportamiento que Excel. La propiedad `pivotFieldGroupOptions.newPivotField` existe por compatibilidad con versiones anteriores: su valor predeterminado es false para agrupación numérica y true para agrupación de fecha y hora; configúrela en false si desea que la agrupación por fechas reemplace el campo dinámico original en lugar de crear nuevos campos dinámicos.
- La propiedad `pivotFieldGroupOptions.interval` solo surte efecto para la agrupación numérica y para la agrupación de fechas por días (por ejemplo, agrupar fechas en períodos de 7 días); se ignora cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos relacionados**
- [Agregar campos de fila y columna en la tabla dinámica](/cells/es/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Agregar campo de página en la tabla dinámica](/cells/es/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aplicar estilo a la tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)
- [Actualizar tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}