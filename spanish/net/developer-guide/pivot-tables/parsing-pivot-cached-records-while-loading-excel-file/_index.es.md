---
title: Análisis de registros en caché de pivote al cargar un archivo de Excel
type: docs
weight: 70
url: /es/net/parsing-pivot-cached-records-while-loading-excel-file/
---
## **Posibles escenarios de uso**

Cuando crea una tabla dinámica, Microsoft Excel toma una copia de los datos de origen y la almacena en la memoria caché dinámica. El Pivot Cache se encuentra dentro de la memoria de Microsoft Excel. No puede verlo, pero esos son los datos a los que hace referencia la tabla dinámica cuando crea su tabla dinámica o cambia una selección de segmentación o mueve filas/columnas. Esto permite que Microsoft Excel responda muy bien a los cambios en la tabla dinámica, pero también puede duplicar el tamaño de su archivo. Después de todo, Pivot Cache es solo un duplicado de sus datos de origen, por lo que tiene sentido que el tamaño de su archivo sea potencialmente el doble.

Cuando carga su archivo de Excel dentro del objeto Workbook, puede decidir si también desea cargar los registros de Pivot Cache o no, utilizando el[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) propiedad. El valor predeterminado de esta propiedad es**falso** . Si Pivot Cache es bastante grande, puede aumentar el rendimiento. Pero si también desea cargar los registros de Pivot Cache, debe establecer esta propiedad como**verdadero**.

## **Análisis de registros en caché de pivote al cargar un archivo de Excel**

El siguiente código de ejemplo explica el uso de[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) propiedad. carga el[ejemplo de archivo de Excel](61767773.xlsx) mientras analiza los registros almacenados en caché de pivote. Luego actualiza la tabla dinámica y la guarda como el[archivo de salida de Excel](61767774.xlsx).

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
