---
title: Análisis de registros en caché del pivote al cargar archivos de Excel
type: docs
weight: 70
url: /es/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Cómo analizar los registros en caché de tabla dinámica al cargar un archivo de Excel con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca de Python de Excel, Cómo analizar los registros en caché de tabla dinámica al cargar un archivo de Excel usando la biblioteca de Excel Aspose.Cells para Python.
---

## **Escenarios de uso posibles**

Cuando creas una tabla dinámica, Microsoft Excel toma una copia de los datos fuente y los almacena en la Caché del pivote. La Caché del pivote se encuentra dentro de la memoria de Microsoft Excel. No puedes verla, pero esos son los datos a los que hace referencia la tabla dinámica cuando construyes tu tabla dinámica o cambias una selección de filtro o mueves filas/columnas. Esto permite a Microsoft Excel ser muy receptivo a los cambios en la tabla dinámica, pero también puede duplicar el tamaño de tu archivo. Después de todo, la Caché del pivote es solo un duplicado de tus datos fuente, así que tiene sentido que el tamaño de tu archivo potencialmente se duplique.

Cuando cargas tu archivo de Excel dentro del objeto Libro, puedes decidir si también deseas cargar los registros de la Caché de Pivot o no, usando la propiedad [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). El valor predeterminado de esta propiedad es **falso**. Si la Caché de Pivot es bastante grande, puede aumentar el rendimiento. Pero si también deseas cargar los registros de la Caché de Pivot, debes configurar esta propiedad como **verdadero**.

## **Cómo analizar los registros en caché de tabla dinámica al cargar un archivo de Excel**

El siguiente código de muestra explica el uso de la propiedad [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). Carga el [archivo de Excel de muestra](61767773.xlsx) mientras analiza los registros en caché de pivot. Luego actualiza la tabla dinámica y la guarda como el [archivo de Excel de salida](61767774.xlsx).

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
