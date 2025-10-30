---
title: Conversión entre el nombre de la celda y el índice de fila/columna
linktitle: Conversión entre Nombre de Celda e Índice
type: docs
weight: 10
url: /es/nodejs-cpp/names-and-indices/
description: Aprende cómo obtener la conversión entre el nombre de la celda y el índice de fila/columna a través de la API Aspose.Cells for Node.js via C++.
keywords: Obtener desde Node.js vía C++ el nombre de la celda a partir de los índices de fila y columna, obtener los índices de fila y columna desde el nombre de la celda, crear nombres seguros para hojas de trabajo, agregar nombres seguros a hojas de trabajo
---

## **Obtener el nombre de celda a partir de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells for Node.js via C++ proporciona el método CellsHelper.cellIndexToName que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

Microsoft Excel empieza a contar los índices de fila y columna desde 1. A diferencia de Microsoft Excel, Aspose.Cells for Node.js via C++ empieza a contar desde 0.

{{% /alert %}} 

 El código de ejemplo a continuación ilustra cómo usar CellsHelper.cellIndexToName para acceder al nombre de la celda dado un índice de fila y columna conocidos. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Obtener Índices de Fila y Columna a partir del Nombre de la Celda**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells for Node.js via C++ proporciona el método CellsHelper.cellNameToIndex que permite a los desarrolladores obtener un índice de fila y columna a partir del nombre de la celda.

{{% alert color="primary" %}} 

Microsoft Excel empieza a contar los índices de fila y columna desde 1. A diferencia de Microsoft Excel, Aspose.Cells for Node.js via C++ empieza a contar desde 0.

{{% /alert %}} 

 El código de ejemplo a continuación muestra cómo usar CellsHelper.cellNameToIndex para obtener el índice de fila y columna a partir del nombre de la celda. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Crear nombres seguros de hoja**
A veces es necesario asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hoja que contengan algunos caracteres adicionales como <>+(?”. Es necesario reemplazar cualquier carácter que no esté permitido como nombre de hoja con algún carácter predefinido proporcionado por el usuario. De manera similar, la longitud puede aumentar a más de 31 caracteres y necesita ser truncada. Apache POI ofrece ciertas funciones para crear nombres seguros, por lo que una función similar la proporciona Aspose.Cells for Node.js via C++ para manejar todos estos problemas. El siguiente código de ejemplo demuestra esta función:



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Salida:

este es el primer nombre que se creó

` <>(adj. Privado _ " Privado"
{{< app/cells/assistant language="nodejs-cpp" >}}
