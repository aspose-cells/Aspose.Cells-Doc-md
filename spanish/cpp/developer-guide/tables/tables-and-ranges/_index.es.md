---
title: Tablas y Rangos
type: docs
weight: 30
url: /es/cpp/tables-and-ranges/
---

## **Introducción**
A veces creas una tabla en Microsoft Excel y no quieres seguir trabajando con la funcionalidad de tabla con la que viene. En su lugar, quieres algo que se parezca a una tabla. Para mantener los datos en una tabla sin perder el formato, convierte la tabla en un rango regular de datos. Aspose.Cells admite esta característica de Microsoft Excel para tablas y objetos de lista.
## **Usar Microsoft Excel**
Utiliza la función **Convertir en rango** para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:

1. Haz clic en cualquier lugar de la tabla para asegurarte de que la celda activa esté en una columna de la tabla.
1. En la pestaña **Diseño**, en el grupo **Herramientas**, haz clic en **Convertir en rango**.

{{% alert color="primary" %}} 

Las características de la tabla ya no están disponibles después de que la tabla ha sido convertida en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas para ordenar y filtrar, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celda regulares.

{{% /alert %}} 
## **Usar Aspose.Cells**
El siguiente fragmento de código demuestra la misma funcionalidad utilizando Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
