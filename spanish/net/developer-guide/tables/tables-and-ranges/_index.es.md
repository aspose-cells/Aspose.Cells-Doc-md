---
title: Tablas y Rangos
type: docs
weight: 50
url: /es/net/tables-and-ranges/
---
## **Introducción**

A veces crea una tabla en Microsoft Excel y no quiere seguir trabajando con la funcionalidad de tabla que viene con ella. En cambio, quieres algo que parezca una mesa. Para mantener los datos en una tabla sin perder el formato, convierta la tabla a un rango regular de datos.
Aspose.Cells admite esta función de Microsoft Excel para tablas y objetos de lista.

## **Usando Microsoft Excel**

 Utilizar el**Convertir a rango** función para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:

1. Haga clic en cualquier parte de la tabla para asegurarse de que la celda activa esté en una columna de la tabla.
1.  Sobre el**Diseño** pestaña, en la**Instrumentos** grupo, haga clic**Convertir a rango**.

## **Usando Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Las características de la tabla ya no están disponibles después de que la tabla se haya convertido en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas de clasificación y filtro, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celdas normales.

{{% /alert %}}

## **Convertir tabla a rango con opciones**

Aspose.Cells proporciona opciones adicionales al convertir Tabla a Rango a través del[**TableToRangeOptionsTableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) clase. los[**TableToRangeOptionsTableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)clase proporciona[**Última fila**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)propiedad que le permite establecer el último índice de la fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.

El código de ejemplo que se proporciona a continuación demuestra el uso de[**TableToRangeOptionsTableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)clase.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
