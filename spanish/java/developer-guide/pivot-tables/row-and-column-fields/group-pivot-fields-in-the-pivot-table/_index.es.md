---
title: Agrupar Campos Dinámicos en la Tabla Dinámica
linktitle: Agrupar Campos Dinámicos en la Tabla Dinámica
description: "Aprenda a agrupar campos dinámicos de filas y columnas en una tabla dinámica en períodos de fechas como meses y trimestres y en rangos numéricos usando PivotField.group y PivotFieldGroupOptions en Aspose.Cells for Java."
keywords: Aspose.Cells, tabla dinámica, agrupar campo dinámico, PivotField.group, PivotFieldGroupOptions, agrupación por fechas, agrupación por números, meses, trimestres, rango numérico, Java
type: docs
weight: 80
url: /es/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles Escenarios de Uso**
- Agrupar campos dinámicos resulta útil cuando un campo de fila o columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación colapsa estos elementos en secciones significativas: las fechas en meses, trimestres y años, y los números en rangos como 0-1, 2-3, 4-5. Esto hace que una tabla dinámica grande sea compacta y más fácil de analizar. Aspose.Cells ofrece esta capacidad a través del método `PivotField.group()` (agrupación automática por tipo de dato) y `PivotField.group(PivotFieldGroupOptions)` (opciones de agrupación personalizadas).
- La agrupación por fechas acumula las fechas individuales en períodos más grandes, como días, meses, trimestres y años, y construye una jerarquía temporal (por ejemplo Años, Trimestres, Meses). Las tendencias a lo largo del tiempo se vuelven visibles de un vistazo, y cada nivel de período se convierte en su propio campo dinámico en el área de fila o columna de la tabla dinámica.
- La agrupación solo está disponible para los campos colocados en el área de FILA o COLUMNA de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo primero debe agregarlo al área de fila o columna de la tabla dinámica.

## **Agrupar Campos Dinámicos Automáticamente**
La sobrecarga `PivotField.group()` sin parámetros inspecciona el tipo de dato del campo y lo agrupa automáticamente. Un campo que contiene solo fechas (y espacios en blanco) se agrupa por meses. Un campo que contiene solo números (y espacios en blanco) se agrupa en rangos numéricos usando un intervalo automático.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Agrupar Campos Dinámicos con Opciones Personalizadas**
La clase `PivotFieldGroupOptions` proporciona una configuración de agrupación personalizada. Para campos de fecha, establezca `startDate`, `endDate` y `groupTypes`. Para campos numéricos, establezca `startNumber`, `endNumber` y `interval`. La propiedad `newPivotField` controla si la agrupación crea nuevos campos dinámicos junto al original (consulte la sección Nota al final de este artículo).

### **Agrupar un Campo de Fecha por Meses y Trimestres**
El siguiente ejemplo agrupa el campo de fila de fecha de la tabla dinámica de muestra por meses y trimestres entre una fecha de inicio y una fecha de fin. El código carga el [archivo Excel de muestra](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fila de fecha ahora está agrupado por trimestres y meses.
Tenga en cuenta que el orden de los valores en `options.groupTypes` se ignora. Sin importar en qué orden se listen los tipos de grupo, los campos agrupados siempre se muestran desde el período más grande al más pequeño: años, trimestres, meses, días, horas, minutos, segundos. En este ejemplo los meses se listan antes que los trimestres en `options.groupTypes`, sin embargo, los trimestres se muestran como el nivel externo y los meses como el nivel interno.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un Campo Numérico en Rangos**
`FieldTwo` de la tabla dinámica de muestra es inicialmente un campo de datos (valor). Dado que solo los campos de fila o columna se pueden agrupar, el código primero llama a `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` para mover `FieldTwo` al área de fila, actualiza la tabla dinámica y luego agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 usando `startNumber = 0`, `endNumber = 5` y `interval = 2`.

```java
import com.aspose.cells.*;
// Cargar el libro de trabajo de muestra
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Acceder a la segunda hoja de trabajo y su tabla dinámica
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo es un campo de datos: muévelo al área de filas primero,
// porque solo los campos de fila/columna se pueden agrupar
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Agrupar el campo numérico en los rangos 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
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
- Las sobrecargas del método `PivotField.groupBy()` están obsoletas y se han eliminado de la superficie de la API. `PivotField.group()` y `PivotField.group(PivotFieldGroupOptions)` son los reemplazos.
- En Microsoft Excel, agrupar un campo numérico REEMPLAZA el campo dinámico original con los rangos agrupados, mientras que agrupar un campo de fecha crea NUEVOS campos dinámicos (uno por nivel de grupo, por ejemplo Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `PivotField.group()` siguen el mismo comportamiento que Excel. La propiedad `PivotFieldGroupOptions.newPivotField` existe por compatibilidad con versiones anteriores: su valor predeterminado es false para agrupación numérica y true para agrupación de fecha-hora; establézcala en false si desea que la agrupación de fechas reemplace al campo dinámico original en lugar de crear nuevos campos dinámicos.
- La propiedad `PivotFieldGroupOptions.interval` solo tiene efecto para agrupación numérica y para agrupación de fechas por días (por ejemplo, agrupar fechas en períodos de 7 días); se ignora cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos Relacionados**
- [Agregar Campos de Fila y Columna en la Tabla Dinámica](/cells/es/java/pivot-table-add-row-and-column-fields/)
- [Filtrar Tablas Dinámicas por Etiqueta o Valor](/cells/es/java/filter-by-label-or-value-of-pivot-table/)
- [Agregar Campo de Página en la Tabla Dinámica](/cells/es/java/add-page-field-in-pivot-table/)
- [Aplicar Estilo a la Tabla Dinámica](/cells/es/java/apply-style-to-pivot-table/)
- [Actualizar la Tabla Dinámica](/cells/es/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}