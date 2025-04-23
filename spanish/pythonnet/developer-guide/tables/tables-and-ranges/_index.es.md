---
title: Tablas y Rangos
type: docs
weight: 50
url: /es/python-net/tables-and-ranges/
---

## **Introducción**

A veces crea una tabla en Microsoft Excel y no desea seguir trabajando con la funcionalidad de la tabla con la que viene. En su lugar, desea algo que se vea como una tabla. Para mantener los datos en una tabla sin perder el formato, convierta la tabla a un rango normal de datos.
Aspose.Cells para Python via .NET sí soporta esta característica de Microsoft Excel para tablas y objetos de lista.

## **Usar Microsoft Excel**

Utiliza la función **Convertir en rango** para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:

1. Haz clic en cualquier lugar de la tabla para asegurarte de que la celda activa esté en una columna de la tabla.
1. En la pestaña **Diseño**, en el grupo **Herramientas**, haz clic en **Convertir en rango**.

## **Usando Aspose.Cells para Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

Las características de la tabla ya no están disponibles después de que la tabla ha sido convertida en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas para ordenar y filtrar, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celda regulares.

{{% /alert %}}

## **Convertir Tabla a Rango con Opciones**

Aspose.Cells para Python via .NET ofrece opciones adicionales al convertir Tabla a Rango a través de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions). La clase [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) ofrece la propiedad [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/) que permite establecer el último índice de la fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato será eliminado.

El código de ejemplo a continuación demuestra el uso de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

