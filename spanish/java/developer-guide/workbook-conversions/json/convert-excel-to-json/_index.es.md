---
title: Convertir Excel a JSON
type: docs
weight: 20
url: /es/java/convert-excel-to-json/
description: Aprenda cómo convertir un archivo de Excel a JSON con Aspose.Cells for Java API.
keywords: Java Exportar Libro de trabajo a json, Convertir Excel a JSON usando Java, Guardar Excel a JSON en Java, Convertir Libro de trabajo a JSON usando Java, Guardar Libro de trabajo a JSON en Java, Exportar Excel a JSON via Java.
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de una hoja de cálculo a un archivo JSON (JavaScript Object Notation).

{{% /alert %}}

## **Cómo Convertir un Libro de Trabajo de Excel a JSON**

No es necesario preguntarse cómo convertir un Libro de Trabajo de Excel a JSON, porque la biblioteca Java de Aspose.Cells tiene la mejor solución. La API de Aspose.Cells Java proporciona soporte para la conversión de hojas de cálculo al formato JSON. Para exportar el libro de trabajo a JSON, pase [**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) como segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.lang.String-int-). También puede usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra la exportación de un libro de Excel a Json. Consulte el código para convertir [archivo de origen](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

El siguiente ejemplo de código, que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales, demuestra la exportación de una hoja de cálculo de Excel a JSON. Consulte el código para convertir el [archivo fuente](muestra.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
{{< app/cells/assistant language="java" >}}
