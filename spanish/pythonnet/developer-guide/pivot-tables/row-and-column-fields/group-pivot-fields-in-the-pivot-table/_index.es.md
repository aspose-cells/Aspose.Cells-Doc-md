---
title: Agrupar Campos de Tabla Dinámica en la Tabla Dinámica
linktitle: Agrupar Campos de Tabla Dinámica en la Tabla Dinámica
description: Aprenda a agrupar campos dinámicos de fila y columna en una tabla dinámica en períodos de fechas como meses y trimestres, y en rangos numéricos usando PivotField.Group y PivotFieldGroupOptions en Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, tabla dinámica, agrupar campo dinámico, PivotField.Group, PivotFieldGroupOptions, agrupación por fechas, agrupación por números, meses, trimestres, rango numérico, Python via .NET
type: docs
weight: 80
url: /es/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles Escenarios de Uso**
- La agrupación de campos dinámicos es útil cuando un campo de fila o columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación condensa estos elementos en secciones significativas: fechas en meses, trimestres y años, y números en rangos como 0-1, 2-3, 4-5. Esto hace que una tabla dinámica grande sea compacta y más fácil de analizar. Aspose.Cells for Python via .NET ofrece esta capacidad mediante el método `pivot_field.group()` (agrupación automática por tipo de datos) y `pivot_field.group(pivot_field_group_options)` (opciones de agrupación personalizadas).
- La agrupación por fechas agrupa las fechas individuales en períodos más grandes, como días, meses, trimestres y años, y construye una jerarquía temporal (por ejemplo Años, Trimestres, Meses). Las tendencias a lo largo del tiempo se vuelven visibles de un vistazo, y cada nivel de período se convierte en su propio campo dinámico en el área de fila o columna de la tabla dinámica.
- La agrupación sólo está disponible para campos colocados en el área de FILA o COLUMNA de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo primero debe agregarlo al área de fila o columna de la tabla dinámica.

## **Agrupar Campos Dinámicos Automáticamente**
La sobrecarga sin parámetros de `pivot_field.group()` inspecciona el tipo de datos del campo y lo agrupa automáticamente. Un campo que contiene sólo fechas (y blancos) se agrupa por meses. Un campo que contiene sólo números (y blancos) se agrupa en rangos numéricos usando un intervalo automático.

```python
import aspose.cells as ac
# Cargar el libro de muestra
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Acceder a la segunda hoja de cálculo y su tabla dinámica
pt = wb.worksheets[1].pivot_tables[0]
# Agrupar el primer campo de fila automáticamente.
# El campo contiene fechas, por lo que se agrupa por meses.
field = pt.row_fields[0]
field.group()
# Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Agrupar Campos Dinámicos con Opciones Personalizadas**
La clase `PivotFieldGroupOptions` proporciona configuración de agrupación personalizada. Para campos de fecha, establezca `start_date`, `end_date` y `group_types`. Para campos numéricos, establezca `start_number`, `end_number` y `interval`. La propiedad `new_pivot_field` controla si la agrupación crea nuevos campos dinámicos junto al original (consulte la sección Nota al final de este artículo).

### **Agrupar un Campo de Fecha por Meses y Trimestres**
El siguiente ejemplo agrupa el campo de fila de fecha de la tabla dinámica de muestra por meses y trimestres entre una fecha de inicio y una fecha de fin. El código carga el [archivo Excel de muestra](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fila de fecha ahora está agrupado por trimestres y meses.
Tenga en cuenta que el orden de los valores en `options.group_types` se ignora. Sin importar el orden en que se enumeren los tipos de grupo, los campos agrupados siempre se muestran del período más grande al más pequeño: años, trimestres, meses, días, horas, minutos, segundos. En este ejemplo, los meses se enumeran antes de los trimestres en `options.group_types`, sin embargo, los trimestres se muestran como el nivel externo y los meses como el nivel interno.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Cargar el libro de muestra
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Acceder a la segunda hoja de cálculo y su tabla dinámica
pt = wb.worksheets[1].pivot_tables[0]
# Agrupar el primer campo de fila (un campo de fecha) por meses y trimestres
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un Campo Numérico en Rangos**
`FieldTwo` de la tabla dinámica de muestra es inicialmente un campo de datos (valor). Dado que sólo los campos de fila o columna se pueden agrupar, el código primero llama a `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` para mover `FieldTwo` al área de fila, actualiza la tabla dinámica y luego agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 usando `start_number=0`, `end_number=5` e `interval=2`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Cargar el libro de muestra
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Acceder a la segunda hoja de cálculo y su tabla dinámica
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo es un campo de datos: muévalo al área de filas primero,
# porque solo los campos de fila/columna se pueden agrupar
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Agrupar el campo numérico en los rangos 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Nota**

{{% alert color="primary" %}}
- Las sobrecargas del método `pivot_field.group_by()` están obsoletas y se han eliminado de la superficie de la API. `pivot_field.group()` y `pivot_field.group(pivot_field_group_options)` son los reemplazos.
- En Microsoft Excel, agrupar un campo numérico REEMPLAZA el campo dinámico original con los rangos agrupados, mientras que agrupar un campo de fecha crea NUEVOS campos dinámicos (uno por nivel de grupo, por ejemplo Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `pivot_field.group()` siguen el mismo comportamiento que Excel. La propiedad `PivotFieldGroupOptions.new_pivot_field` existe por compatibilidad con versiones anteriores: por defecto es false para la agrupación numérica y true para la agrupación de fecha y hora; establézcala en false si desea que la agrupación de fechas reemplace el campo dinámico original en lugar de crear nuevos campos dinámicos.
- La propiedad `PivotFieldGroupOptions.interval` surte efecto sólo para la agrupación numérica y para la agrupación de fechas por días (por ejemplo, agrupar fechas en períodos de 7 días); se ignora cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos Relacionados**
- [Agregar Campos de Fila y Columna en la Tabla Dinámica](/cells/es/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrar Tablas Dinámicas por Etiqueta o por Valor](/cells/es/python-net/filter-by-label-or-value-of-pivot-table/)
- [Agregar Campo de Página en la Tabla Dinámica](/cells/es/python-net/add-page-field-in-pivot-table/)
- [Aplicar Estilo a la Tabla Dinámica](/cells/es/python-net/apply-style-to-pivot-table/)
- [Actualizar la Tabla Dinámica](/cells/es/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}