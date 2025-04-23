---
title: Análisis de registros en caché del pivote al cargar archivos de Excel
type: docs
weight: 100
url: /es/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Escenarios de uso posibles**

Cuando creas una tabla dinámica, Microsoft Excel toma una copia de los datos fuente y los almacena en la Caché del pivote. La Caché del pivote se encuentra dentro de la memoria de Microsoft Excel. No puedes verla, pero esos son los datos a los que hace referencia la tabla dinámica cuando construyes tu tabla dinámica o cambias una selección de filtro o mueves filas/columnas. Esto permite a Microsoft Excel ser muy receptivo a los cambios en la tabla dinámica, pero también puede duplicar el tamaño de tu archivo. Después de todo, la Caché del pivote es solo un duplicado de tus datos fuente, así que tiene sentido que el tamaño de tu archivo potencialmente se duplique.

Cuando cargas tu archivo de Excel dentro del objeto Libro, puedes decidir si también quieres cargar los registros de la Caché del pivote o no, utilizando la propiedad [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). El valor predeterminado de esta propiedad es **falso**. Si la Caché del pivote es bastante grande, puede aumentar el rendimiento. Pero si también quieres cargar los registros de la Caché del pivote, debes establecer esta propiedad como **verdadero**.

## **Analizar registros en caché de la tabla dinámica al cargar el archivo de Excel**

El siguiente código de muestra explica el uso de la propiedad [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Carga el [archivo de Excel de ejemplo](61767786.xlsx) mientras analiza los registros en caché del pivote. Luego actualiza la tabla dinámica y la guarda como el [archivo de Excel de salida](61767785.xlsx).

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
