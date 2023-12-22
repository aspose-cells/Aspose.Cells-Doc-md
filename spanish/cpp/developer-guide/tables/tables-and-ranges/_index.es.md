---
title: Mesas y rangos
type: docs
weight: 30
url: /es/cpp/tables-and-ranges/
---
##  **Introducción**
veces creas una tabla en Microsoft Excel y no quieres seguir trabajando con la funcionalidad de tabla que viene con ella. En cambio, quieres algo que parezca una mesa. Para mantener los datos en una tabla sin perder formato, convierta la tabla a un rango normal de datos. Aspose.Cells admite esta característica de Microsoft Excel para tablas y objetos de lista.
##  **Usando Microsoft Excel**
 Utilizar el**Convertir a rango** Función para convertir rápidamente una tabla en un rango sin perder formato. En Microsoft Excel 2007/2010:

1. Haga clic en cualquier lugar de la tabla para asegurarse de que la celda activa esté en una columna de la tabla.
1.  Sobre el**Diseño** pestaña, en la**Herramientas** grupo, haga clic en *Convertir a rango**.

{{% alert color="primary" %}} 

Las funciones de la tabla ya no están disponibles después de que la tabla se haya convertido en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas para ordenar y filtrar, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en las fórmulas se convierten en referencias de celda normales.

{{% /alert %}} 
##  **Usando Aspose.Cells**
El siguiente fragmento de código demuestra la misma funcionalidad usando Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
