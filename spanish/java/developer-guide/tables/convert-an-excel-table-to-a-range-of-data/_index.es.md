---
title: Convertir una tabla de Excel en un rango de datos
type: docs
weight: 10
url: /es/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

A veces crea una tabla en Microsoft Excel y no quiere seguir trabajando con la funcionalidad de tabla que viene con ella. En cambio, quieres algo que parezca una mesa. Para mantener los datos en una tabla sin perder el formato, convierta la tabla a un rango regular de datos.

Aspose.Cells admite esta característica de Microsoft Excel para tablas y objetos de lista.

{{% /alert %}}

## **Usando Microsoft Excel**

 Utilizar el**Convertir a rango** función para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:

1. Haga clic en cualquier parte de la tabla para asegurarse de que la celda activa esté en una columna de la tabla.

![todo:imagen_alternativa_texto](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  Sobre el**Diseño** pestaña, en la**Instrumentos** grupo, haga clic**Convertir a rango**.

![todo:imagen_alternativa_texto](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Las características de la tabla ya no están disponibles después de que la tabla se haya convertido en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas de clasificación y filtro, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celdas normales.

{{% /alert %}}

## **Usando Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Convertir tabla a rango con opciones**

Aspose.Cells proporciona opciones adicionales al convertir Tabla a Rango a través del[**TableToRangeOptionsTableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)clase. los[**TableToRangeOptionsTableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)clase proporciona[**Última fila**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)propiedad que le permite establecer el último índice de la fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.

El código de ejemplo que se proporciona a continuación demuestra el uso de[**TableToRangeOptionsTableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)clase.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
