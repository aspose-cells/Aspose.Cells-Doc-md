---
title: Agrupar Campos Dinámicos en la Tabla Dinámica
linktitle: Agrupar Campos Dinámicos en la Tabla Dinámica
description: Aprenda a agrupar campos dinámicos de filas y columnas en una tabla dinámica en períodos de fechas como meses y trimestres, y en rangos numéricos usando PivotField.group y PivotFieldGroupOptions en Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tabla dinámica, agrupar campo dinámico, PivotField.group, PivotFieldGroupOptions, agrupación por fechas, agrupación por números, meses, trimestres, rango numérico, Python
type: docs
weight: 80
url: /es/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles Escenarios de Uso**
- Agrupar campos dinámicos es útil cuando un campo de fila o columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación colapsa estos elementos en secciones significativas: las fechas en meses, trimestres y años, y los números en rangos como 0-1, 2-3, 4-5. Esto hace que una tabla dinámica grande sea compacta y más fácil de analizar. Aspose.Cells ofrece esta capacidad a través del método `PivotField.group()` (agrupación automática por tipo de dato) y `PivotField.group(PivotFieldGroupOptions)` (opciones de agrupación personalizadas).
- La agrupación por fechas acumula las fechas individuales en períodos más grandes, como días, meses, trimestres y años, y construye una jerarquía temporal (por ejemplo, Años, Trimestres, Meses). Las tendencias a lo largo del tiempo se vuelven visibles de un vistazo, y cada nivel de período se convierte en su propio campo dinámico en el área de filas o columnas de la tabla dinámica.
- La agrupación solo está disponible para campos colocados en el área de FILAS o COLUMNAS de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo, primero debe agregarlo al área de filas o columnas de la tabla dinámica.

## **Agrupar Campos Dinámicos Automáticamente**
La sobrecarga sin parámetros `PivotField.group()` inspecciona el tipo de dato del campo y lo agrupa automáticamente. Un campo que contiene solo fechas (y espacios en blanco) se agrupa por meses. Un campo que contiene solo números (y espacios en blanco) se agrupa en rangos numéricos utilizando un intervalo automático.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Cargar el libro de muestra
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Acceder a la segunda hoja de cálculo y su tabla dinámica
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Agrupar el primer campo de fila automáticamente.
# El campo contiene fechas, por lo que se agrupa por meses.
field = pt.getRowFields().get(0)
field.group()
# Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Agrupar Campos Dinámicos con Opciones Personalizadas**
La clase `PivotFieldGroupOptions` proporciona configuración de agrupación personalizada. Para campos de fecha, establezca `StartDate`, `EndDate` y `GroupTypes`. Para campos numéricos, establezca `StartNumber`, `EndNumber` e `Interval`. La propiedad `NewPivotField` controla si la agrupación crea nuevos campos dinámicos junto al original (consulte la sección Nota al final de este artículo).

### **Agrupar un Campo de Fecha por Meses y Trimestres**
El siguiente ejemplo agrupa el campo de fila de fecha de la tabla dinámica de muestra por meses y trimestres entre una fecha de inicio y una fecha de fin. El código carga el [archivo de Excel de muestra](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fila de fecha ahora está agrupado por trimestres y meses.
Tenga en cuenta que el orden de los valores en `options.GroupTypes` se ignora. Sin importar en qué orden se enumeren los tipos de grupo, los campos agrupados siempre se muestran desde el período más grande al más pequeño: años, trimestres, meses, días, horas, minutos, segundos. En este ejemplo, los meses se enumeran antes que los trimestres en `options.GroupTypes`, sin embargo, los trimestres se muestran como el nivel externo y los meses como el nivel interno.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Cargar el libro de muestra
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Acceder a la segunda hoja de cálculo y su tabla dinámica
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Agrupar el primer campo de fila (un campo de fecha) por meses y trimestres
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un Campo Numérico en Rangos**
`FieldTwo` de la tabla dinámica de muestra es inicialmente un campo de datos (valor). Dado que solo se pueden agrupar campos de fila o columna, el código primero llama a `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` para mover `FieldTwo` al área de filas, actualiza la tabla dinámica y luego agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 usando `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Cargar el libro de muestra
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Acceder a la segunda hoja de cálculo y su tabla dinámica
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo es un campo de datos: muévalo al área de filas primero,
# porque solo los campos de fila/columna pueden agruparse
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Agrupar el campo numérico en los rangos 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Calcular los datos de la tabla dinámica y guardar el archivo de salida
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Nota**

{{% alert color="primary" %}}
- Las sobrecargas del método `PivotField.groupBy()` están obsoletas y se han eliminado de la superficie de la API. `PivotField.group()` y `PivotField.group(PivotFieldGroupOptions)` son los reemplazos.
- En Microsoft Excel, agrupar un campo numérico REEMPLAZA el campo dinámico original con los rangos agrupados, mientras que agrupar un campo de fecha crea NUEVOS campos dinámicos (uno por nivel de grupo, por ejemplo, Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `PivotField.group()` siguen el mismo comportamiento que Excel. La propiedad `PivotFieldGroupOptions.NewPivotField` existe por compatibilidad con versiones anteriores: por defecto es false para agrupación numérica y true para agrupación de fecha y hora; establézcala en false si desea que la agrupación por fechas reemplace el campo dinámico original en lugar de crear nuevos campos dinámicos.
- La propiedad `PivotFieldGroupOptions.Interval` solo surte efecto para la agrupación numérica y para la agrupación de fechas por días (por ejemplo, agrupar fechas en períodos de 7 días); se ignora cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos Relacionados**
- [Añadir Campos de Fila y Columna en Tabla Dinámica](/cells/es/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrar Tablas Dinámicas por Etiqueta o Valor](/cells/es/python-java/filter-by-label-or-value-of-pivot-table/)
- [Añadir Campo de Página en Tabla Dinámica](/cells/es/python-java/add-page-field-in-pivot-table/)
- [Aplicar Estilo a Tabla Dinámica](/cells/es/python-java/apply-style-to-pivot-table/)
- [Actualizar Tabla Dinámica](/cells/es/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}