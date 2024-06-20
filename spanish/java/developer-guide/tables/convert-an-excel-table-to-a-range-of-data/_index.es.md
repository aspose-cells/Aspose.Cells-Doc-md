---
title: Convertir una Tabla de Excel a un Rango de Datos
type: docs
weight: 10
url: /es/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

A veces crea una tabla en Microsoft Excel y no desea seguir trabajando con la funcionalidad de la tabla con la que viene. En su lugar, desea algo que se vea como una tabla. Para mantener los datos en una tabla sin perder el formato, convierta la tabla a un rango normal de datos.

Aspose.Cells admite esta característica de Microsoft Excel para tablas y objetos de lista.

{{% /alert %}}

## **Usar Microsoft Excel**

Utiliza la función **Convertir en rango** para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:

1. Haz clic en cualquier lugar de la tabla para asegurarte de que la celda activa esté en una columna de la tabla.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. En la pestaña **Diseño**, en el grupo **Herramientas**, haz clic en **Convertir en rango**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Las características de la tabla ya no están disponibles después de que la tabla ha sido convertida en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas para ordenar y filtrar, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celda regulares.

{{% /alert %}}

## **Usar Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Convertir Tabla a Rango con Opciones**

Aspose.Cells proporciona opciones adicionales al convertir Tabla a Rango a través de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). La clase [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) proporciona la propiedad [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) que le permite establecer el último índice de fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.

El código de ejemplo a continuación demuestra el uso de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
