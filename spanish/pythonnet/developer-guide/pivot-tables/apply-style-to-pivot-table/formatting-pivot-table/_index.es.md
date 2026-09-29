---
title: Dar formato a la tabla dinámica
type: docs
weight: 10
url: /es/python-net/formatting-pivot-table/
description: Cómo formatear la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Formato de tabla dinámica
---

## **Apariencia de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica estableciendo diversas propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos de tabla dinámica
- Opciones de formato de campos de datos

### **Cómo establecer opciones de formato de tabla dinámica**

La clase [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) controla la tabla dinámica general y se puede formatear de varias maneras.

#### **Cómo establecer el tipo de autoformato**

Microsoft Excel ofrece una serie de formatos de informe preestablecidos diferentes. Aspose.Cells for Python via .NET también admite estas opciones de formato. Para acceder a ellos:

1. Establezca [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) en **verdadero**.
1. Asignar una opción de formato de la enumeración [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **Cómo establecer opciones de formato**

El ejemplo de código a continuación muestra cómo dar formato a la tabla dinámica para mostrar totales generales para filas y columnas, y cómo establecer el orden de los campos del informe. También muestra cómo establecer una cadena personalizada para los valores nulos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **Dar formato manualmente al aspecto visual**

Para formatear cómo se ve el informe de tabla dinámica manualmente, en lugar de usar formatos de informe preestablecidos, use los métodos [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) y [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/). Cree un objeto de estilo para su formato deseado, por ejemplo:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **Cómo establecer opciones de formato de campo de tabla dinámica**

La clase [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) representa un campo en una tabla dinámica y se puede formatear de varias formas. El ejemplo de código a continuación muestra cómo:

- Acceder a los campos de fila.
- Establecer subtotales.
- Establecer orden automático.
- Establecer autover.

#### **Cómo establecer el formato de campos de fila/columna/página.**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **Cómo establecer el formato de campos de datos.**

El ejemplo de código a continuación muestra cómo establecer formatos de visualización y formato numérico para los campos de datos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **Cómo limpiar los campos de filtro.**

La clase [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) tiene un método llamado [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) que te permite borrar campos de tabla dinámica. Úsalo cuando quieras borrar todos los campos de tabla dinámica en las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos de tabla dinámica en un área de datos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
