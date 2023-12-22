---
title: Análisis de registros en caché dinámicos mientras se carga un archivo de Excel
type: docs
weight: 70
url: /es/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Cómo analizar registros en caché dinámicos mientras se carga un archivo de Excel con Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Posibles escenarios de uso**

Cuando crea una tabla dinámica, Microsoft Excel toma una copia de los datos de origen y los almacena en la caché dinámica. El Pivot Cache se guarda dentro de la memoria de Microsoft Excel. No puede verlo, pero esos son los datos a los que hace referencia la tabla dinámica cuando crea su tabla dinámica o cambia una selección de segmentación de datos o mueve filas/columnas. Esto permite que Microsoft Excel responda muy bien a los cambios en la tabla dinámica, pero también puede duplicar el tamaño de su archivo. Después de todo, Pivot Cache es solo un duplicado de sus datos de origen, por lo que tiene sentido que el tamaño de su archivo sea potencialmente el doble.

Cuando carga su archivo de Excel dentro del objeto Libro de trabajo, puede decidir si también desea cargar los registros de Pivot Cache o no, usando el[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)propiedad. El valor por defecto de esta propiedad es "falso**. Si Pivot Cache es bastante grande, puede aumentar el rendimiento. Pero si también desea cargar los registros de Pivot Cache, debe establecer esta propiedad como *verdadera**.

##  **Análisis de registros en caché dinámicos mientras se carga un archivo de Excel**

El siguiente código de muestra explica el uso de[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)propiedad. Se carga el[archivo de Excel de muestra](61767773.xlsx) mientras analiza los registros en caché dinámicos. Luego actualiza la tabla dinámica y la guarda como[archivo de salida de Excel](61767774.xlsx).

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
