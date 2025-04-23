---
title: Tablas y Rangos
type: docs
weight: 50
url: /es/net/tables-and-ranges/
---

## **Introducción**

A veces crea una tabla en Microsoft Excel y no desea seguir trabajando con la funcionalidad de la tabla con la que viene. En su lugar, desea algo que se vea como una tabla. Para mantener los datos en una tabla sin perder el formato, convierta la tabla a un rango normal de datos.
Aspose.Cells es compatible con esta función de Microsoft Excel para tablas y objetos de lista.

## **Usar Microsoft Excel**

Utiliza la función **Convertir en rango** para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:

1. Haz clic en cualquier lugar de la tabla para asegurarte de que la celda activa esté en una columna de la tabla.
1. En la pestaña **Diseño**, en el grupo **Herramientas**, haz clic en **Convertir en rango**.

## **Usar Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Las características de la tabla ya no están disponibles después de que la tabla ha sido convertida en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas para ordenar y filtrar, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celda regulares.

{{% /alert %}}

## **Convertir Tabla a Rango con Opciones**

Aspose.Cells proporciona opciones adicionales al convertir una Tabla en un Rango a través de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions). La clase [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) proporciona la propiedad [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) que le permite establecer el último índice de la fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.

El código de ejemplo a continuación demuestra el uso de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
