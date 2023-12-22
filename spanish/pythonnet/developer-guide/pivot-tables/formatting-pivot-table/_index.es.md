---
title: Formato de tabla dinámica
type: docs
weight: 10
url: /es/net/formatting-pivot-table/
description: Cómo formatear una tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **Apariencia de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica estableciendo varias propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos dinámicos
- Opciones de formato de campo de datos

###  **Configuración de opciones de formato de tabla dinámica**

 El[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)La clase controla la tabla dinámica general y se puede formatear de varias maneras.

####  **Configuración del tipo de formato automático**

Microsoft Excel ofrece varios formatos de informes preestablecidos diferentes. Aspose.Cells for Python via .NET también admiten estas opciones de formato. Para acceder a ellos:

1.  Colocar[**Tabla dinámica.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)a *verdadero**.
1.  Asigne una opción de formato desde el[**Tipo de formato automático de tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)enumeración.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Configuración de opciones de formato**

El siguiente ejemplo de código muestra cómo formatear la tabla dinámica para mostrar los totales generales de filas y columnas, y cómo configurar el orden de los campos del informe. También muestra cómo configurar una cadena de cliente para valores nulos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Formatear la apariencia manualmente**

Para formatear manualmente el aspecto del informe de la tabla dinámica, en lugar de utilizar formatos de informe preestablecidos, utilice el[**Tabla dinámica.format_all(estilo)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) y[**Tabla dinámica.formato (fila, columna, estilo)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)métodos. Cree un objeto de estilo para el formato que desee, por ejemplo:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Configuración de opciones de formato de campo dinámico**

 El[**Campo dinámico**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)La clase representa un campo en una tabla dinámica y se puede formatear de varias maneras. El siguiente ejemplo de código muestra cómo:

- Accede a los campos de fila.
- Configuración de subtotales.
- Configuración de clasificación automática.
- Configuración de presentación automática.

####  **Configuración del formato de campos de fila/columna/página**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Configuración del formato de los campos de datos**

El siguiente código de ejemplo muestra cómo configurar formatos de visualización y formato numérico para campos de datos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Borrar campos dinámicos**

 El[**Colección de campos dinámicos**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) tiene un método llamado[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)que le permite borrar campos dinámicos. Úselo cuando desee borrar todos los campos dinámicos en las áreas, por ejemplo, página, columna, fila o datos.
El siguiente código de ejemplo muestra cómo borrar todos los campos dinámicos en un área de datos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
